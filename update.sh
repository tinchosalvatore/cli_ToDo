#!/bin/bash

# CLI ToDo Updater
# Author: tinchosalvatore
# Description: Reinstalación limpia conservando datos, gestionando el idioma automáticamente.

# 1. Preguntar idioma UNA sola vez
echo "------------------------------------------------"
echo "Select Language for Update / Seleccione Idioma"
echo "------------------------------------------------"
PS3="Choose/Elija (1-2): "
options=("English" "Español")
select opt in "${options[@]}"
do
    case $opt in
        "English")
            LANG_INPUT="1"
            break
            ;;
        "Español")
            LANG_INPUT="2"
            break
            ;;
        *) echo "Invalid option / Opción inválida $REPLY";;
    esac
done

echo ""
echo "🔄 Update sequence initiated..."

# 2. Ejecutar Uninstall
# Le enviamos:
#   - $LANG_INPUT (1 o 2) + enter (\n) -> Para el selector de idioma.
#   - "n" -> Para decirle NO a borrar los datos.
# Usamos printf para asegurar que los saltos de línea sean precisos.
printf "$LANG_INPUT\nn" | ./uninstall.sh

# 3. Ejecutar Setup
# Le enviamos:
#   - $LANG_INPUT (1 o 2) + enter (\n) -> Para el selector de idioma.
printf "$LANG_INPUT\n" | ./setup.sh

echo ""
echo "✨ Update finished! You are on the latest version."