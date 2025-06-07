#!/bin/bash

# Generar kanban.md desde issues.json
OUTPUT_ARCHIVO="docs/kanban.md"
ISSUES_ARCHIVO="issues.json"

# Revisar si jq esta instalado
if ! command -v jq >/dev/null 2>&1; then
    echo "Error: jq es necesario para analizar JSON"
    exit 1
fi

# Inicializar kanban.md
cat > "$OUTPUT_ARCHIVO" << 'EOF'
# Tablero Kanban 

## To Do
EOF

# Agregar issues abiertos a To Do
jq -r '.[] | select(.state == "open") | "- Issue #\(.id): \(.title) (Owner: \(.owner))"' "$ISSUES_ARCHIVO" >> "$OUTPUT_ARCHIVO"

# Agregar sección In Progress
echo -e "\n## In Progress" >> "$OUTPUT_ARCHIVO"
jq -r '.[] | select(.state == "in_progress") | "- Issue #\(.id): \(.title) (Owner: \(.owner))"' "$ISSUES_ARCHIVO" >> "$OUTPUT_ARCHIVO"

# Agregar sección Done
echo -e "\n## Done" >> "$OUTPUT_ARCHIVO"
jq -r '.[] | select(.state == "closed") | "- Issue #\(.id): \(.title) (Owner: \(.owner))"' "$ISSUES_ARCHIVO" >> "$OUTPUT_ARCHIVO"

echo "Generado $OUTPUT_ARCHIVO"