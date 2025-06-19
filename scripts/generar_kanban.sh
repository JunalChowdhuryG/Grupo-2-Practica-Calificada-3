#!/bin/bash

# Generar kanban.md desde issues.json con transiciones de estado
OUTPUT_ARCHIVO="docs/kanban.md"
ISSUES_ARCHIVO="issues.json"

# Verificamos si el archivo de issues existe
if [ ! -f "$ISSUES_ARCHIVO" ]; then
    echo "Error: $ISSUES_ARCHIVO not found"
    exit 1
fi

# Revisar si jq esta instalado
if ! command -v jq >/dev/null 2>&1; then
    echo "Error: jq es necesario para analizar JSON"
    exit 1
fi

# Inicializar kanban.md
{
    echo "# Kanban Board"
    echo

    for section in "To Do" "In Progress" "Done"; do
        echo "## $section"

        case $section in
            "To Do")
                jq -r '.[] | select(.state == "open") | "- Issue #\(.id): \(.title) (Owner: \(.owner), Created: \(.created_at))"' "$ISSUES_ARCHIVO"
                ;;
            "In Progress")
                jq -r '.[] | select(.state == "in_progress") | "- Issue #\(.id): \(.title) (Owner: \(.owner), Created: \(.created_at))"' "$ISSUES_ARCHIVO"
                ;;
            "Done")
                jq -r '.[] | select(.state == "closed") | "- Issue #\(.id): \(.title) (Owner: \(.owner), Closed: \(.closed_at))"' "$ISSUES_ARCHIVO"
                ;;
        esac

        echo 
    done
} > "$OUTPUT_ARCHIVO"

if [ $? -eq 0 ]; then
    echo "Generado $OUTPUT_ARCHIVO"
else
    echo "Error generando $OUTPUT_ARCHIVO"
    exit 1
fi