#!/bin/bash
# salir al primer error
set -e
KANBAN_SCRIPT="./scripts/generar_kanban.sh"
KANBAN_ARCHIVO="./docs/kanban.md"
ISSUES_ARCHIVO="./issues.json"

# ejecutar script
bash "$KANBAN_SCRIPT"

# verificar que se genero el archivo kanban.md
if [[ -f "$KANBAN_ARCHIVO" ]]; then
    echo "kanban.md generado"
else
    echo "error: no se genero docs/kanban.md"
    exit 1
fi

# verificar existencia de 3 secciones basicas
for seccion in "## To Do" "## In Progress" "## Done"; do
    if grep -q "$seccion" "$KANBAN_ARCHIVO"; then
        echo "se encontro seccion: $seccion"
    else
        echo "error: falta seccion: $seccion"
        exit 1
    fi
done

# verificar que el archivo issues.json no esta vacio
if [[ $(jq length "$ISSUES_ARCHIVO") -gt 0 ]]; then
    echo "issues.json contiene al menos un issue"
else
    echo "error: issues.json esta vacio"
    exit 1
fi

echo "el test paso correctamente"