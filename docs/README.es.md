# 👾 CLI ToDo Tool by tinchosalvatore (V2 Nexus)

### *A KISS philosophy task manager for the terminal*

Una herramienta de línea de comandos (CLI) ultraligera, rápida y estética, diseñada para informáticos que viven en la terminal. Basada en la simplicidad, utiliza **JSON** para persistencia, **Rich** para una UI moderna y **Nerd Fonts** para una experiencia visual superior.

**Novedad V2:** Ahora es **Context Aware**. Las tareas se guardan vinculadas al directorio donde te encuentras.

---

## 📚 Características

Esta herramienta sigue el principio **KISS** (*Keep It Simple, Stupid*):

* **Contextual (Multitenancy)**: Gestiona listas de tareas independientes por proyecto/directorio.
* **Omni View**: Un modo "Dios" para ver todas tus tareas de todos los proyectos en una sola lista.
* **Sin sobrecarga**: Sin bases de datos pesadas; solo un archivo JSON estructurado.
* **IDs Dinámicos**: Los números de tarea se recalculan automáticamente para evitar huecos al borrar.

---

## 🧰 Instalación

### Requisitos previos

* **Python 3.10+**
* **Nerd Fonts** (Recomendado: *JetBrainsMono Nerd Font*) para ver los iconos correctamente.

### Pasos

1. Clona este repositorio o descarga los archivos.
2. Dale permisos de ejecución al instalador:
```bash
chmod +x setup.sh

```

3. Ejecuta el setup (creará el entorno virtual y el enlace simbólico):

```bash
./setup.sh

```

4. **Reinicia tu terminal** o recarga tu configuración (`source ~/.zshrc` o `.bashrc`).

---

## ⌨️ Uso de Comandos

El comando base es `todo`. Recuerda que ahora **las tareas dependen del directorio** donde estés.

| Comando | Descripción | Ejemplo |
| --- | --- | --- |
| `todo` | Muestra las tareas del **directorio actual**. | `todo` |
| `todo -a <tarea>` | Añade una tarea al directorio actual. | `todo -a Deploy a producción` |
| `todo -t <id>` | **Toggle**: Marca/Desmarca una tarea como hecha. | `todo -t 1` |
| `todo -d <id>` | **Delete**: Elimina la tarea y reajusta los IDs. | `todo -d 2` |
| `todo -u` | Muestra solo las tareas **pendientes** (si está vacío, ¡celebra!). | `todo -u` |
| `todo -r` | **Wipeout**: ELIMINA todas las tareas de este directorio (limpieza total). | `todo -r` |
| `todo -o` | **Omni View**: Muestra TODAS las tareas de TODOS los directorios. | `todo -o` |

---

## ⚙️ Desinstalación

El nuevo desinstalador es inteligente y protege tus datos:

1. Ejecuta el script de desinstalación:

```bash
chmod +x uninstall.sh && ./uninstall.sh

```

> **Nota:** El script te preguntará interactivamente si deseas borrar la configuración y las tareas guardadas en `~/.config/cli_ToDo/tasks.json` o si prefieres conservarlas para el futuro.

---

## 👨‍💻 Créditos

Desarrollado por **tinchosalvatore**.