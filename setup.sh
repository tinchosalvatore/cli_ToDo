#!/bin/bash

# CLI ToDo V2 Installer
# Author: Martin Salvatore

# --- Language Selector ---
echo "------------------------------------------------"
echo "Select Language / Seleccione Idioma"
echo "------------------------------------------------"
PS3="Choose/Elija (1-2): "
options=("English" "Español")
select opt in "${options[@]}"
do
    case $opt in
        "English")
            L_START="🚀 Starting CLI ToDo V2 installation (Nexus Update)..."
            L_ERR_PY="❌ Error: Python 3 is not installed or not found."
            L_CLEAN="📦 Cleaning previous installations..."
            L_VENV="📦 Creating virtual environment in"
            L_DEPS="📥 Installing dependencies (Rich)..."
            L_LINK="🔗 Creating symlink in"
            L_SUCCESS="✅ Installation completed successfully!"
            L_TEST="Try your new tool:"
            L_TIP1="  $ todo          (Show tasks for current directory)"
            L_TIP2="  $ todo -o       (Show tasks for ALL projects)"
            L_PATH_NOTE="NOTE: Ensure this path is in your PATH:"
            break
            ;;
        "Español")
            L_START="🚀 Iniciando instalación de CLI ToDo V2 (Nexus Update)..."
            L_ERR_PY="❌ Error: Python 3 no está instalado o no se encuentra."
            L_CLEAN="📦 Limpiando instalaciones previas..."
            L_VENV="📦 Creando entorno virtual en"
            L_DEPS="📥 Instalando librerías (Rich)..."
            L_LINK="🔗 Creando enlace simbólico en"
            L_SUCCESS="✅ ¡Instalación completada con éxito!"
            L_TEST="Prueba tu nueva tool:"
            L_TIP1="  $ todo          (Ver tareas de este directorio)"
            L_TIP2="  $ todo -o       (Ver tareas de TODOS los proyectos)"
            L_PATH_NOTE="NOTA: Asegúrate de que esta ruta está en tu PATH:"
            break
            ;;
        *) echo "Invalid option / Opción inválida $REPLY";;
    esac
done

APP_DIR="$HOME/.todo_cli_app"
BIN_DIR="$HOME/.local/bin"
EXECUTABLE_NAME="todo"

echo ""
echo "$L_START"

# 1. Verificar Python 3.10+
if ! command -v python3 &> /dev/null; then
    echo "$L_ERR_PY"
    exit 1
fi

# 2. Crear Entorno Virtual Limpio
echo "$L_CLEAN"
rm -rf "$APP_DIR"
echo "$L_VENV $APP_DIR..."
python3 -m venv "$APP_DIR"

# 3. Instalar Dependencias
echo "$L_DEPS"
"$APP_DIR/bin/pip" install -r requirements.txt --upgrade --quiet

# 4. Crear el Shim (Ejecutable)
echo "$L_LINK $BIN_DIR..."
mkdir -p "$BIN_DIR"

cat > "$BIN_DIR/$EXECUTABLE_NAME" <<EOF
#!/bin/bash
"$APP_DIR/bin/python" "$(pwd)/todo.py" "\$@"
EOF

chmod +x "$BIN_DIR/$EXECUTABLE_NAME"

# 5. Finalización
echo ""
echo "$L_SUCCESS"
echo "------------------------------------------------"
echo "$L_TEST"
echo "$L_TIP1"
echo "$L_TIP2"
echo "------------------------------------------------"
echo "$L_PATH_NOTE $BIN_DIR"