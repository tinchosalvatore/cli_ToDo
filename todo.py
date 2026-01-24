#!/usr/bin/env python3
"""
CLI ToDo App - KISS Philosophy
Author: tinchosalvatore
Description: Una herramienta de línea de comandos minimalista para gestión de tareas.
             Utiliza almacenamiento JSON y estilizado con Rich/Nerd Fonts.
"""

import argparse
import json
import sys
from pathlib import Path
from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.panel import Panel

# Configuración de temas para Rich (Colores estilo UI moderna)
custom_theme = Theme({
    "success": "green",
    "warning": "yellow",
    "danger": "red",
    "dim": "dim white",
    "header_bg": "bold black on #E6DB74",
    "id_col": "cyan",
})

console = Console(theme=custom_theme)

# Configuración de rutas
CONFIG_DIR = Path.home() / ".config" / "cli_ToDo"
DATA_FILE = CONFIG_DIR / "tasks.json"

def load_tasks():
    """
    Carga las tareas desde el archivo JSON.
    Si el archivo o directorio no existe, los crea.
    """
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    if not DATA_FILE.exists():
        return []
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # Si el archivo está corrupto, retornamos lista vacía
        return []

def save_tasks(tasks):
    """
    Guarda la lista de tareas en el archivo JSON.
    """
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)

def get_progress_bar(completed, total):
    """
    Genera una barra de progreso visual usando caracteres de bloque.
    """
    if total == 0:
        percent = 0
    else:
        percent = (completed / total) * 100
    
    # Renderizado manual simple para mantener el control del estilo
    width = 40
    filled = int(width * (percent / 100))
    bar = "━" * filled + "─" * (width - filled)
    
    color = "success" if percent == 100 else "#b8bb26"
    return Text(f"{bar} {int(percent)}% Done", style=color)

def print_tasks(tasks, show_only_uncompleted=False):
    """
    Renderiza la lista de tareas en la consola con estilos Rich.
    """
    if not tasks:
        console.print(Panel("  No hay tareas pendientes. ¡Dia libre!", style="dim", expand=False), justify="center")
        return

    # Cabecera estilo 'Ribbon' (cinta)
    console.print()
    console.print(Text("   ToDo List ", style="header_bg"), justify="left")
    console.print()

    completed_count = 0
    
    for index, task in enumerate(tasks):
        is_done = task['completed']
        if is_done:
            completed_count += 1
        
        if show_only_uncompleted and is_done:
            continue

        # ID Dinámico: Siempre es index + 1. No se guarda en DB, se genera al vuelo.
        task_id = index + 1
        
        # Selección de iconos Nerd Font y estilos
        if is_done:
            icon = " " # Checkbox lleno
            style = "dim strike"
            id_style = "dim"
        else:
            icon = " " # Checkbox vacío
            style = "white"
            id_style = "id_col"

        # Construcción de la línea visual
        line = Text()
        line.append(f"{task_id:2} ", style=id_style) # ID alineado
        line.append(icon, style="success" if is_done else "warning")
        line.append(task['content'], style=style)
        
        console.print(line)

    console.print()
    
    # Barra de progreso al final
    progress_render = get_progress_bar(completed_count, len(tasks))
    console.print(progress_render)

    # signature
    console.print("by tinchosalvatore", style="dim italic", justify="right")

    console.print()

def add_task(content):
    """Añade una nueva tarea al final de la lista."""
    tasks = load_tasks()
    tasks.append({"content": content, "completed": False})
    save_tasks(tasks)
    print_tasks(tasks)

def toggle_task(task_id):
    """Marca o desmarca una tarea usando su ID visual (base 1)."""
    tasks = load_tasks()
    index = task_id - 1
    
    if 0 <= index < len(tasks):
        # Toggle: si estaba true pasa a false y viceversa
        tasks[index]['completed'] = not tasks[index]['completed']
        save_tasks(tasks)
        print_tasks(tasks)
    else:
        console.print(f"[danger]Error:[/danger] ID {task_id} no encontrado.")

def delete_task(task_id):
    """Elimina una tarea por su ID. Los IDs restantes se desplazan."""
    tasks = load_tasks()
    index = task_id - 1
    
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        console.print(f"[warning]Eliminado:[/warning] {removed['content']}")
        print_tasks(tasks)
    else:
        console.print(f"[danger]Error:[/danger] ID {task_id} no encontrado.")

def reset_tasks():
    """Reinicia el estado de todas las tareas a 'no completado'."""
    tasks = load_tasks()
    for task in tasks:
        task['completed'] = False
    save_tasks(tasks)
    console.print("[warning]Todas las tareas han sido reiniciadas.[/warning]")
    print_tasks(tasks)

def main():
    parser = argparse.ArgumentParser(description="CLI ToDo App Minimalista by tinchsalvatore")
    
    # Argumentos
    parser.add_argument("-a", "--add", nargs="+", help="Añadir tarea (permite espacios)")
    parser.add_argument("-t", "--toggle", type=int, help="Completar/Desmarcar tarea por ID")
    parser.add_argument("-d", "--delete", type=int, help="Eliminar tarea por ID")
    parser.add_argument("-r", "--reset", action="store_true", help="Reiniciar todas las tareas")
    parser.add_argument("-u", "--uncompleted", action="store_true", help="Mostrar solo tareas pendientes")
    
    args = parser.parse_args()

    # Lógica de enrutamiento de comandos
    if args.add:
        # ' '.join permite que escribas: todo -a Comprar pan (sin comillas)
        add_task(" ".join(args.add))
    elif args.toggle:
        toggle_task(args.toggle)
    elif args.delete:
        delete_task(args.delete)
    elif args.reset:
        reset_tasks()
    elif args.uncompleted:
        tasks = load_tasks()
        print_tasks(tasks, show_only_uncompleted=True)
    else:
        # Si no hay argumentos, simplemente mostramos la lista
        tasks = load_tasks()
        print_tasks(tasks)

if __name__ == "__main__":
    main()
