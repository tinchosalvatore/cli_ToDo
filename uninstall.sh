#!/bin/bash

# ==========================================
# CONFIGURATION
# ==========================================
APP_DIR="$HOME/.todo_cli_app"
BIN_FILE="$HOME/.local/bin/todo"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

# ==========================================
# LANGUAGE SELECTION
# ==========================================
clear
echo "-----------------------------------------------------"
echo "Select Language / Seleccione Idioma"
echo "-----------------------------------------------------"
read -p "Type 'en' for English or 'es' for Spanish: " LANG_CHOICE

if [[ "$LANG_CHOICE" == "es" ]]; then
    TXT_START=">>> Desinstalando CLI ToDo..."
    TXT_RM_DIR="Eliminado directorio de aplicación:"
    TXT_NO_DIR="El directorio de aplicación no existía (o ya fue borrado)."
    TXT_RM_BIN="Eliminado ejecutable:"
    TXT_NO_BIN="El ejecutable no se encontró en"
    TXT_DONE=">>> Desinstalación completada."
    TXT_NOTE="NOTA: Tu archivo de tareas (tasks.json) en '~/.config/cli_ToDo' se ha mantenido a salvo."
    TXT_RM_DATA="Si quieres borrar tus datos también, ejecuta: rm -rf ~/.config/cli_ToDo"
elif [[ "$LANG_CHOICE" == "en" ]]; then
    TXT_START=">>> Uninstalling CLI ToDo..."
    TXT_RM_DIR="Removed application directory:"
    TXT_NO_DIR="Application directory did not exist (or was already removed)."
    TXT_RM_BIN="Removed executable:"
    TXT_NO_BIN="Executable not found at"
    TXT_DONE=">>> Uninstallation complete."
    TXT_NOTE="NOTE: Your tasks file (tasks.json) in '~/.config/cli_ToDo' has been preserved."
    TXT_RM_DATA="If you want to delete your data too, run: rm -rf ~/.config/cli_ToDo"
else
    echo -e "${RED}Invalid language / Idioma inválido.${NC}"
    exit 1
fi

# ==========================================
# UNINSTALL LOGIC (UNCHANGED)
# ==========================================

echo -e "${YELLOW}${TXT_START}${NC}"

# 1. Remove App Dir
if [ -d "$APP_DIR" ]; then
    rm -rf "$APP_DIR"
    echo -e "${TXT_RM_DIR} ${APP_DIR}"
else
    echo -e "${TXT_NO_DIR}"
fi

# 2. Remove Binary
if [ -f "$BIN_FILE" ]; then
    rm "$BIN_FILE"
    echo -e "${TXT_RM_BIN} ${BIN_FILE}"
else
    echo -e "${TXT_NO_BIN} ${BIN_FILE}."
fi

echo -e "-----------------------------------------------------"
echo -e "${GREEN}${TXT_DONE}${NC}"
echo -e "${YELLOW}${TXT_NOTE}${NC}"
echo -e "${TXT_RM_DATA}"
