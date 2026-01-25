#!/usr/bin/env python3
"""
CLI ToDo App - V2.0.1
Author: tinchosalvatore
Description: Herramienta CLI minimalista con gestión de tareas contextual (por directorio).
             Incluye modo 'Omni' para vista global y persistencia JSON estructurada.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.panel import Panel
from rich.rule import Rule

# ==========================================
# CONFIGURACIÓN & TEMA
# ==========================================

custom_theme = Theme({
    "success": "bold green",
    "warning": "yellow",
    "danger": "red",
    "dim": "dim white",
    "header_bg": "bold black on #E6DB74",
    "id_col": "cyan",
})

console = Console(theme=custom_theme)

CONFIG_DIR = Path.home() / ".config" / "cli_ToDo"
DATA_FILE = CONFIG_DIR / "tasks.json"

# ==========================================
# GESTIÓN DE DATOS (PERSISTENCIA V2)
# ==========================================

def get_context_path():
    """Retorna la ruta absoluta del directorio actual como clave única."""
    return str(Path.cwd())

def load_db():
    """
    Carga la base de datos completa.
    Maneja la migración automática de V1 (lista) a V2 (diccionario de contextos).
    """
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    if not DATA_FILE.exists():
        return {}
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # --- AUTO MIGRACIÓN V1 -> V2 ---
            # Si el JSON es una lista, viene de la V1. Lo guardamos bajo una key 'Legacy'.
            if isinstance(data, list):
                return {"[Legacy V1]": data}
            return data
            
    except (json.JSONDecodeError, IOError):
        return {}

def save_db(db):
    """Guarda la estructura completa en el JSON."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=4)

def get_tasks(context=None):
    """Obtiene las tareas del contexto actual (o uno específico)."""
    if context is None:
        context = get_context_path()
    db = load_db()
    return db.get(context, [])

def save_tasks(tasks, context=None):
    """Guarda las tareas en el contexto actual."""
    if context is None:
        context = get_context_path()
    db = load_db()
    
    if not tasks:
        # Si la lista está vacía, podríamos borrar la key para limpiar el JSON,
        # pero mantenerla vacía es inofensivo.
        if context in db:
            db[context] = []
    else:
        db[context] = tasks
        
    save_db(db)

# ==========================================
# LÓGICA DE UI
# ==========================================

def get_progress_bar(completed, total):
    """Genera barra de progreso visual."""
    if total == 0:
        percent = 0
    else:
        percent = (completed / total) * 100
    
    width = 30
    filled = int(width * (percent / 100))
    bar = "━" * filled + "─" * (width - filled)
    
    color = "success" if percent == 100 else "#b8bb26"
    return Text(f"{bar} {int(percent)}%", style=color)

def print_tasks(tasks, context_name=None, show_only_uncompleted=False, is_omni=False):
    """
    Renderiza la lista de tareas.
    Args:
        tasks: Lista de tareas.
        context_name: Nombre del directorio (para modo Omni).
        show_only_uncompleted: Flag -u.
        is_omni: Si es True, simplifica un poco la UI para listas masivas.
    """
    
    # Filtrado previo para verificar si "realmente" está vacío bajo los criterios actuales
    visible_tasks = tasks
    if show_only_uncompleted:
        visible_tasks = [t for t in tasks if not t['completed']]

    # Caso 1: No hay tareas en absoluto (o todas filtradas)
    if not visible_tasks:
        # Si venimos de un filtrado (-u) y está vacío, es que todo está hecho -> CELEBRAR
        if show_only_uncompleted and tasks: 
             msg = "  ¡Todo limpio! Tareas al día."
        elif not tasks:
             msg = "  Sin tareas aquí."
        else:
            # Caso raro: hay tareas, no filtra uncompleted, pero visible es 0 (no debería pasar)
             msg = "  Nada que mostrar."

        # Solo mostramos el panel de "Vacio" si NO estamos en modo Omni (para no spammear)
        if not is_omni:
            console.print(Panel(msg, style="dim", expand=False), justify="center")
        return

    # Cabecera
    if context_name:
        # Modo Omni: Muestra la ruta del proyecto
        console.print(Rule(style="dim"))
        console.print(Text(f" 📂 {context_name} ", style="path_header"), justify="left")
    elif not is_omni:
        # Modo Normal: Cabecera estándar
        console.print()
        console.print(Text("   ToDo List ", style="header_bg"), justify="left")
        console.print()

    completed_count = 0
    total_count = len(tasks) # Total real del contexto, no del filtrado

    for index, task in enumerate(tasks):
        is_done = task['completed']
        if is_done:
            completed_count += 1
        
        if show_only_uncompleted and is_done:
            continue

        # ID Dinámico
        task_id = index + 1
        
        if is_done:
            icon = " "
            style = "dim strike"
            id_style = "dim"
        else:
            icon = " "
            style = "white"
            id_style = "id_col"

        line = Text()
        line.append(f"{task_id:2} ", style=id_style)
        line.append(icon, style="success" if is_done else "warning")
        line.append(task['content'], style=style)
        
        console.print(line)

    if not is_omni:
        console.print()
        progress_render = get_progress_bar(completed_count, total_count)
        console.print(progress_render)
        console.print("v2.0.1 by tinchosalvatore", style="dim italic", justify="right")
        console.print()

# ==========================================
# COMANDOS
# ==========================================

def add_task(content):
    tasks = get_tasks()
    tasks.append({"content": content, "completed": False})
    save_tasks(tasks)
    print_tasks(tasks)

def toggle_task(task_id):
    tasks = get_tasks()
    index = task_id - 1
    
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = not tasks[index]['completed']
        save_tasks(tasks)
        print_tasks(tasks)
    else:
        console.print(f"[danger]Error:[/danger] ID {task_id} no existe en este contexto.")

def delete_task(task_id):
    tasks = get_tasks()
    index = task_id - 1
    
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        console.print(f"[warning]Eliminado:[/warning] {removed['content']}")
        print_tasks(tasks)
    else:
        console.print(f"[danger]Error:[/danger] ID {task_id} no existe.")

def reset_context():
    """Borra TODAS las tareas del contexto actual (Wipeout)."""
    # Feature 2: Borrado total del directorio, no reinicio.
    save_tasks([]) # Guardar lista vacía
    console.print(Panel(f"[danger]☢️  Contexto purgado:[/danger]\n{get_context_path()}", expand=False))

def show_omni_view(show_uncompleted=False):
    """Feature 4: Muestra tareas de TODOS los directorios registrados."""
    db = load_db()
    if not db:
        console.print(Panel("🪐 El universo está vacío 🪐. No hay tareas por aquí.", style="warning"))
        return

    console.print(Text(" 🪐 OMNI VIEW - GLOBAL STATUS 🪐 ", style="bold black on #fe8019"), justify="center")
    console.print()

    # Ordenamos paths alfabéticamente para que se vea ordenado
    total_projects = 0
    for path, tasks in sorted(db.items()):
        if not tasks: continue # Saltamos directorios vacíos
        
        # Si filtramos por uncompleted y este proyecto lo tiene todo hecho, checkeamos
        if show_uncompleted:
             pendientes = [t for t in tasks if not t['completed']]
             if not pendientes: continue

        print_tasks(tasks, context_name=path, show_only_uncompleted=show_uncompleted, is_omni=True)
        total_projects += 1
    
    if total_projects == 0:
         console.print("Nada pendiente en ningún sistema. ¡Impresionante!", justify="center", style="success")

def main():
    parser = argparse.ArgumentParser(description="CLI ToDo App V2 - Context Aware")
    
    parser.add_argument("-a", "--add", nargs="+", help="Añadir tarea")
    parser.add_argument("-t", "--toggle", type=int, help="Toggle tarea ID")
    parser.add_argument("-d", "--delete", type=int, help="Eliminar tarea ID")
    parser.add_argument("-r", "--reset", action="store_true", help="BORRAR todas las tareas de este dir")
    parser.add_argument("-u", "--uncompleted", action="store_true", help="Filtrar pendientes")
    parser.add_argument("-o", "--omni", action="store_true", help="Vista Global (Todos los directorios)")
    
    args = parser.parse_args()

    if args.omni:
        # Modo Dios: Ver todo
        show_omni_view(show_uncompleted=args.uncompleted)
    elif args.add:
        add_task(" ".join(args.add))
    elif args.toggle:
        toggle_task(args.toggle)
    elif args.delete:
        delete_task(args.delete)
    elif args.reset:
        reset_context()
    elif args.uncompleted:
        tasks = get_tasks()
        print_tasks(tasks, show_only_uncompleted=True)
    else:
        # Default view
        tasks = get_tasks()
        print_tasks(tasks)

if __name__ == "__main__":
    main()