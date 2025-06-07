#!/bin/bash
#Hook para asegurar un correcto mensaje de commit usando prefijos estandar

# leer el mensaje del commit
MSJ_COMMIT=$1
MENSAJE=$(cat "$MSJ_COMMIT")

# solo se permiten tipos feat, fix, refactor, docs, test
PATRON="^(feat|fix|refactor|docs|test)\[#([0-9]+)\]: .+"

if ! echo "$MENSAJE" | grep -Eq "$PATRON"; then
    echo " Error: El mensaje del commit debe seguir el patron '<tipo>[#n]: mensaje'"
    echo " Tipos permitidos: feat, fix, refactor, docs, test"
    echo " Ejemplo valido: feat[#1]: Inicializar repositorio y estructura"
    exit 1
fi

exit