#!/bin/bash

# ==========================================
# CONFIGURATION & LOGIC
# ==========================================
APP_NAME="todo"
INSTALL_DIR="$HOME/.todo_cli_app"
BIN_DIR="$HOME/.local/bin"
SCRIPT_SOURCE="./todo.py" # Asume que todo.py está aquí

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# ==========================================
# LANGUAGE SELECTION
# ==========================================
clear
echo "-----------------------------------------------------"
echo "Select Language / Seleccione Idioma"
echo "-----------------------------------------------------"
read -p "Type 'en' for English or 'es' for Spanish: " LANG_CHOICE

if [[ "$LANG_CHOICE" == "es" ]]; then
    # Spanish Strings
    TXT_START=">>> Iniciando instalación de CLI ToDo (KISS edition)..."
    ERR_PYTHON="Error: python3 no está instalado."
    ERR_SOURCE="Error: No encuentro $SCRIPT_SOURCE en este directorio."
    TXT_CREATE_DIR="Creando directorio de instalación en"
    TXT_VENV="Creando entorno virtual (esto puede tardar unos segundos)..."
    TXT_RICH="Instalando librería 'rich' en el entorno aislado..."
    TXT_SHIM="Creando ejecutable en"
    TXT_SUCCESS=">>> ¡Instalación completada con éxito!"
    TXT_LOCATION="El comando '$APP_NAME' ha sido instalado en:"
    WARN_PATH="ATENCIÓN: Tu \$PATH no incluye"
    TXT_FIX="Para que funcione, agrega esto a tu .bashrc o .zshrc:"
    TXT_GOOD="Tu PATH parece correcto. Ya puedes ejecutar:"
elif [[ "$LANG_CHOICE" == "en" ]]; then
    # English Strings
    TXT_START=">>> Starting CLI ToDo installation (KISS edition)..."
    ERR_PYTHON="Error: python3 is not installed."
    ERR_SOURCE="Error: Could not find $SCRIPT_SOURCE in the current directory."
    TXT_CREATE_DIR="Creating installation directory at"
    TXT_VENV="Creating virtual environment (this might take a few seconds)..."
    TXT_RICH="Installing 'rich' library in isolated environment..."
    TXT_SHIM="Creating executable at"
    TXT_SUCCESS=">>> Installation completed successfully!"
    TXT_LOCATION="The command '$APP_NAME' has been installed to:"
    WARN_PATH="WARNING: Your \$PATH does not include"
    TXT_FIX="To fix this, add the following line to your .bashrc or .zshrc:"
    TXT_GOOD="Your PATH looks good. You can now run:"
else
    echo -e "${RED}Invalid language / Idioma inválido.${NC}"
    exit 1
fi

# ==========================================
# INSTALLATION PROCESS (UNCHANGED LOGIC)
# ==========================================

echo -e "${BLUE}${TXT_START}${NC}"

# 1. Check dependencies
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}${ERR_PYTHON}${NC}"
    exit 1
fi

if [ ! -f "$SCRIPT_SOURCE" ]; then
    echo -e "${RED}${ERR_SOURCE}${NC}"
    exit 1
fi

# 2. Create directory structure
echo -e "${TXT_CREATE_DIR} ${INSTALL_DIR}..."
rm -rf "$INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

# 3. Copy source
cp "$SCRIPT_SOURCE" "$INSTALL_DIR/main.py"

# 4. Create VENV
echo -e "${TXT_VENV}"
python3 -m venv "$INSTALL_DIR/venv"

# 5. Install requirements
echo -e "${TXT_RICH}"
"$INSTALL_DIR/venv/bin/pip" install rich --quiet --upgrade

# 6. Create Shim
echo -e "${TXT_SHIM} ${BIN_DIR}..."
mkdir -p "$BIN_DIR"

cat << EOF > "$BIN_DIR/$APP_NAME"
#!/bin/bash
exec "$INSTALL_DIR/venv/bin/python" "$INSTALL_DIR/main.py" "\$@"
EOF

chmod +x "$BIN_DIR/$APP_NAME"

echo -e "${GREEN}${TXT_SUCCESS}${NC}"
echo -e "-----------------------------------------------------"
echo -e "${TXT_LOCATION} ${BIN_DIR}/$APP_NAME"

# 7. Path Check
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo -e "${RED}${WARN_PATH} ${BIN_DIR}.${NC}"
    echo "${TXT_FIX}"
    echo -e "${BLUE}export PATH=\"\$HOME/.local/bin:\$PATH\"${NC}"
else
    echo -e "${TXT_GOOD} ${GREEN}${APP_NAME}${NC}"
fi
