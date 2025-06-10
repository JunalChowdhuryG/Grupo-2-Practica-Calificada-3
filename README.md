# **Proyecto 8 - Grupo 2: "Integración de métricas ágiles: Burn-Down y lead time con scripts personalizados"**

## **Integrantes:**

| Integrante                         | Codigo    | Repositorio Personal del Proyecto                                                 |
| ---------------------------------- | --------- | --------------------------------------------------------------------------------- |
| Chowdhury Gomez, Junal Johir       | 20200092K | [JunalChowdhuryG](https://github.com/JunalChowdhuryG/Proyecto-8-Personal-Grupo-2) |
| La Torre Vasquez, Andres Sebastian | 20212100C | [Jun1el](https://github.com/Jun1el/Proyecto-8-Personal-Grupo-2)                   |
| Zapata Inga, Janio Adolfo          | 20212636K | [Janiopi](https://github.com/Janiopi/Proyecto-8-Personal-Grupo-2)                 |

## Descripcion

El **Proyecto 8 - Grupo 2**, está enfocado en desarrollar scripts personalizados para calcular metricas agiles como _burn-down_ y _lead time_  
El avance se divide en 3 Sprints.

## Sprint 1

El **Sprint 1**, ejecutado del 7 al 9 de junio de 2025, se compone de los siguientes issues:

- [#1](#1-inicializar-repositorio-y-estructura) La infraestructura inicial del proyecto mediante la configuracion del repositorio
- [#2](#2-implementar-hook-commit-msg) Un hook de Git para asegurar una correcta estructura en los mensajes de los commits
- [#3](#3-crear-script-generar_kanbansh-inicial-y-su-test) Un script que genere un tablero Kanban en md a partir de un json
- [#4](#4-desarrollar-esqueleto-de-calcular_metricaspy) El esqueleto del script Python para metricas
- [#5](#5-crear-datos-iniciales-en-issuesjson) Datos iniciales de los issues en JSON.

## Demostracion en video

[Sprint 1 (Dia 3: 8/06/2025) Grupo 2 Proyecto 8 ](https://www.youtube.com/watch?v=iJIAYbbfaYw)

## Issues del Sprint 1

### [1] Inicializar repositorio y estructura

- **Historia de Usuario**:
  - **Como** desarrollador
  - **Necesito** configurar un repositorio con estructura de carpetas y archivos base
  - **Para** que el equipo pueda desarrollar scripts de metricas agiles de forma organizada
- **Responsable**: Junal
- **Objetivo**: Establecer la arquitectura base del proyecto, creando directorios para scripts, codigo, metricas, informes, documentacion, y pruebas, junto con archivos de configuracion iniciales.

### [2] Implementar hook commit-msg

- **Historia de Usuario**:
  - **Como** desarrollador
  - **Necesito** un hook que valide mensajes de commit con el patron feat[#n], fix[#n], docs[#n]
  - **Para** que los commits sean trazables en el calculo de metricas
- **Responsable**: Janio
- **Objetivo**: Desarrollar un hook Bash que se instale en `.git/hooks/` para validar mensajes de commit, asegurando que sigan el formato requerido.

### [3] Crear script generar_kanban.sh inicial y su test

- **Historia de Usuario**:
  - **Como** desarrollador
  - **Necesito** un script que genere un tablero Kanban en Markdown desde `issues.json`
  - **Para** visualizar el progreso del proyecto.
- **Responsable**: Andres
- **Objetivo**: Implementar `generar_kanban.sh` para generar `docs/kanban.md` con columnas To Do, En Progreso, y Done, acompañado de un test para validar su funcionalidad.

### [4] Desarrollar esqueleto de calcular_metricas.py

- **Historia de Proyecto**:
  - **Como** desarrollador
  - **Necesito** un script Python que formatee el historial Git y genere un CSV
  - **Para** que se puedan calcular metricas agiles como lead time
- **Responsable**: Junal
- **Objetivo**: Crear un esqueleto de `calcular_metricas.py` con funciones para parsear commits y escribir resultados, preparando la base para calculos avanzados en futuros sprints.

### [5] Crear datos iniciales en issues.json

- **Historia de Proyecto**:
  - **Como** desarrollador
  - **Necesito** un archivo issues.json con issues iniciales
  - **Para** que los scripts de Kanban y métricas funcionen correctamente
- **Responsable**: Janio
- **Objetivo**: Poblar `issues.json` con los 5 issues del Sprint 1, asegurando compatibilidad con `generar_kanban.sh` y futuros calculos de metricas.

## Distribución

- **Junal**: Issues [#1](#1-inicializar-repositorio-y-estructura), [#4](#4-desarrollar-esqueleto-de-calcular_metricaspy).
- **Janio**: Issues [#2](#2-implementar-hook-commit-msg), [#5](#5-crear-datos-iniciales-en-issuesjson).
- **Andres**: [#3](#3-crear-script-generar_kanbansh-inicial-y-su-test).

## Flujo de Trabajo

- **Ramas**: Cada issue se desarrollo en una rama `feature/*`, fusionada a `develop` tras revisar y aceptar un pull request.
- **Commits**: Atomicos (<200 lineas), con mensajes en el formato `feat[#ID]: descripcion` o `docs[#ID]: descripcion`.
- **Pull Requests**: PRs #1, #2, #5 cerrados; #3, #4 abiertos, todos revisados por otro miembro del equipo.
- **Tablero Kanban**: Generado por `generar_kanban.sh` en `docs/kanban.md`, refleja el estado de los issues.

## Ejecucion del Proyecto

1. Instalar dependencias(requirements.txt)
2. Generar el tablero Kanban:
   ```bash
   bash scripts/generar_kanban.sh
   ```
3. Ejecutar tests:
   ```bash
   bash tests/test_generar_kanban.sh
   ```
4. Parsear historial de Git:
   ```bash
   python src/calcular_metricas.py
   ```
5. Inspeccionar resultados:
   - `docs/kanban.md`: Tablero Kanban.
   - `metricas/commits.csv`: Datos de commits.

Nota: No olvidar darle permisos a los scripts

```bash
 chmod +x scripts/generar_kanban.sh test/test_generar_kanban.sh
```
