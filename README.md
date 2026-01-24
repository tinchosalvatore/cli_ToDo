# 👾 CLI ToDo Tool by tinchosalvatore

### *A KISS philosophy task manager for the terminal*

Una herramienta de línea de comandos (CLI) ultraligera, rápida y estética, diseñada para informáticos que viven en la terminal. Basada en la simplicidad, utiliza **JSON** para persistencia, **Rich** para una UI moderna y **Nerd Fonts** para una experiencia visual superior.

---

## 📚 Características

Esta herramienta sigue el principio **KISS** (*Keep It Simple, Stupid*):

* **Sin sobrecarga**: Sin bases de datos pesadas; solo un archivo JSON.
* **IDs Dinámicos**: Los números de tarea se recalculan automáticamente para evitar huecos al borrar.
* **Velocidad**: Comandos cortos y directos para no interrumpir el flujo de trabajo.

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


3. Ejecuta el setup y elige tu idioma (**en/es**):
```bash
./setup.sh

```


4. **Reinicia tu terminal** o recarga tu configuración (`source ~/.zshrc` o `.bashrc`).

---

## ⌨️ Uso de Comandos

El comando base es `todo`. Aquí tienes la lista de argumentos disponibles:

| Comando | Descripción | Ejemplo |
| --- | --- | --- |
| `todo` | Muestra la lista completa y el progreso. | `todo` |
| `todo -a <tarea>` | Añade una nueva tarea (no requiere comillas). | `todo -a Estudiar Física` |
| `todo -t <id>` | **Toggle**: Marca o desmarca una tarea como hecha. | `todo -t 1` |
| `todo -d <id>` | **Delete**: Elimina la tarea y reajusta los IDs. | `todo -d 2` |
| `todo -u` | Muestra solo las tareas **pendientes**. | `todo -u` |
| `todo -r` | **Reset**: Reinicia todas las tareas a pendientes. | `todo -r` |

---

## ⚙️ Desinstalación

Si deseas eliminar la herramienta pero **mantener tus datos** (tareas guardadas):

1. Ejecuta el script de desinstalación:
```bash
chmod +x uninstall.sh && ./uninstall.sh

```



> **Nota:** Tus tareas se guardan en `~/.config/cli_ToDo/tasks.json`. Si también quieres borrar tus datos, elimina esa carpeta manualmente con `rm -rf ~/.config/cli_ToDo`.

---

## 👨‍💻 Créditos

Desarrollado por **tinchosalvatore**.