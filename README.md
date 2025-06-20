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

## Flujo de Trabajo

- **Ramas**: Cada issue se desarrollo en una rama `feature/*`, fusionada a `develop` tras revisar y aceptar un pull request.
- **Commits**: Atomicos (<300 lineas), con mensajes en el formato `feat[#ID]: descripcion` o `docs[#ID]: descripcion`.
- **Pull Requests**: Cuandos se quiere implementar un nuevo `feature|update|fix..` al proyecto, se realiza un PR hacia la rama `develop`. Es obligatorio que 2 colaboradores lo aprueben para que se proceda con el merge.
- **Tablero Kanban**: Muestra el estado de los issues (`Backlog, Ready,In Progress, QA, ... `). También agrupa issues en Sprints (epics)

## Documentación en video

- Sprint1:
  [Sprint 1 (8/06/2025) Grupo 2 Proyecto 8 ](https://www.youtube.com/watch?v=iJIAYbbfaYw)
- Sprint2: [Sprint 2 (17/06/2025) Grupo 2 Proyecto 8 ](https://youtu.be/cEHDw_kIgWw)
- Sprint3: [Sprint 3 (19/06/2025) Grupo 2 Proyecto 8 ](https://www.youtube.com/watch?v=V2qRnOWsgNE)

## Sprint 1

El **Sprint 1**, ejecutado del 7 al 9 de junio de 2025, se compone de los siguientes issues:

- [#1](#1-inicializar-repositorio-y-estructura) La infraestructura inicial del proyecto mediante la configuracion del repositorio
- [#2](#2-implementar-hook-commit-msg) Un hook de Git para asegurar una correcta estructura en los mensajes de los commits
- [#3](#3-crear-script-generar_kanbansh-inicial-y-su-test) Un script que genere un tablero Kanban en md a partir de un json
- [#4](#4-desarrollar-esqueleto-de-calcular_metricaspy) El esqueleto del script Python para metricas
- [#5](#5-crear-datos-iniciales-en-issuesjson) Datos iniciales de los issues en JSON.

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

## Sprint 2

El **Sprint 2**, ejecutado del 11 al 16 de junio de 2025, se compone de los siguientes issues:

- [#6](#6-implementar-calculo-de-lead-time-en-calcular_metricaspy) Un script que calcule el Lead Time
- [#7](#7-generar-gráfico-burn-down-en-ascii) Generar gráfico Burn-Down ASCII para visualizar el progreso de los issues
- [#8](#8-mejorar-generar_kanbansh-para-transiciones-de-estado) Mostrar transiciones de estado de tareas
- [#9](#9-agregar-pruebas-unitarias-para-calcular_metricaspy) Verificar la confiabilidad del script calcular_metricas.py

## Issues del sprint 2

### [6] Implementar calculo de Lead Time en calcular_metricas.py

- **Historia de Usuario**
  - **Como** desarrollador
  - **Necesito** extender `calcular_metricas.py` para calcular el _lead time_ de los issues
  - **Para que** el dashboard agil pueda mostrar cuanto tiempo toma completar tareas
  - **Responsable**: Junal
  - **objetivo**: Usar `metricas/commits.csv` [#4](#4-desarrollar-esqueleto-de-calcular_metricaspy) y `issues.json [#5](#5-crear-datos-iniciales-en-issuesjson) para correlacionar fechas de creacion y finalizacion de issues

### [7] Generar gráfico Burn-Down en ASCII

- **Historia de Usuario**

  - **Como** desarrollador
  - **Necesito** crear un script que genere un gráfico _burn-down_ en formato ASCII
  - **Para que** el equipo pueda visualizar el progreso del proyecto.
  - **Responsable**: Janio
  - **objetivo**: Usar `metricas/commits.csv`[#4](#4-desarrollar-esqueleto-de-calcular_metricaspy) y `issues.json`[#5](#5-crear-datos-iniciales-en-issuesjson) para contar tareas completadas por día.

### [8] Mejorar generar_kanban.sh para transiciones de estado

- **Historia de Usuario**

  - **Como** desarrollador
  - **Necesito** mejorar `generar_kanban.sh` [#3] para mostrar transiciones de estado de tareas
  - **Para que** el dashboard refleje el flujo de trabajo del Sprint 2
  - **Responsable**: Andres
  - **objetivo**: Mejorar generar_kanban.sh [#3](#3-crear-script-generar_kanbansh-inicial-y-su-test) para que muestre estados de los issues.

### [9] Agregar pruebas unitarias para calcular_metricas.py

- **Historia de Usuario**
  - **Como** desarrollador
  - **Necesito** escribir pruebas unitarias para `calcular_metricas.py`
  - **Para que** el codigo sea robusto y mantenible
  - **Responsable**: Andres
  - **objetivo**: Cubrir las pruebas de las funciones `registrar_git_log()`, `escribir_csv()`y la nueva `calcular_lead_time()`

## Sprint 3

El **Sprint 3**, ejecutado del 16 al 19 de junio de 2025, se compone de los siguientes issues:

-[#10](#10-implementar-deteccion-de-retrasos-en-notificar_retrasospy) Implementar detección de retrasos en notificar_retrasos.py -[#11](#11-agregar-pruebas-unitarias-para-notificar_retrasospy) Agregar pruebas unitarias para notificar_retrasos.py -[#12](#12-optimizar-calcular_metricaspy) Optimizar calcular_metricas.py -[#13](#13-optimizar-generar_kanbansh-para-rendimiento) Optimizar generar_kanban.sh para rendimiento -[#14](#14-agregar-pruebas-unitarias-para-generar_burn_downpy) Agregar pruebas unitarias para generar_burn_down.py

## Issues del sprint 3

### [10] Implementar deteccion de retrasos en notificar_retrasos.py

- **Historia de Usuario**:
  - **Como** desarrollador
  - **Necesito** crear un script que detecte retrasos en los issues
  - **Para que** notifique al equipo sobre tareas atrasadas
  - **Responsable**: Junal
  - **Objetivo**: Usa `issues.json` para comparar fechas de vencimiento con el estado actual,y en caso haya un retraso genera un `delay.txt`

### [11] Agregar pruebas unitarias para notificar_retrasos.py

- **Historia de Usuario**: -**Como** desarrollador
  - **Necesito** escribir pruebas unitarias para `notificar_retrasos.py`
  - **Para que** la deteccion de retrasos sea confiable
- **Responsable**: Andres
- **Objetivo**: Probar `notificar_retrasos.py` con al menos 4 escenarios.

### [12] Optimizar calcular_metricas.py

- **Historia de Usuario**:
  - **Como** desarrollador
  - **Necesito** optimizar `calcular_metricas.py` para reducir tiempos
  - **Para que** se reduzcan tiempos
- **Responsable**: Andres
- **Objetivo**: Refactorizar `calcular_metricas.py` para reducir tiempo de parseo de los git logs y generación de `commits.csv` y `lead_time.csv`

### [13] Optimizar generar_kanban.sh para rendimiento

- **Historia de Usuario**:
  - **Como** desarrollador
  - **Necesito** configurar un repositorio con estructura de carpetas y archivos base
  - **Para** que el equipo pueda desarrollar scripts de metricas agiles de forma organizada
- **Responsable**: Junal
- **Objetivo**: Establecer la arquitectura base del proyecto, creando directorios para scripts, codigo, metricas, informes, documentacion, y pruebas, junto con archivos de configuracion iniciales.

### [14] Agregar pruebas unitarias para generar_burn_down.py

- **Historia de Usuario**:
  - **Como** desarrollador
  - **Necesito** configurar un repositorio con estructura de carpetas y archivos base
  - **Para** que el equipo pueda desarrollar scripts de metricas agiles de forma organizada
- **Responsable**: Janio
- **Objetivo**: Establecer la arquitectura base del proyecto, creando directorios para scripts, codigo, metricas, informes, documentacion, y pruebas, junto con archivos de configuracion iniciales.

## Ejecucion del Proyecto

1. Clonar el repositorio del proyecto

```bash
  git clone < url-de-este-repo >
```

2. Se recomienda trabajar en un entorno virtual

```bash
  python3 -m venv venv
```

Activando el entorno

```bash
  source venv/bin/activate
```

    En caso se quiera desactivar

```bash
  deactivate
```

3. Instalar dependencias(requirements.txt)

```bash
  pip install -r requirements.txt
```

2. Generar el tablero Kanban:
   ```bash
   bash scripts/generar_kanban.sh
   ```
   Nota: No olvidar darle permisos a los scripts

```bash
chmod +x scripts/generar_kanban.sh test/test_generar_kanban.sh
```

3. Probar los scripts

- Calcular métricas:
  - _Lead Time_: Tiempo transcurrido entre el `open`y `closed`de un issue

```bash
python3 src/calcular_metricas.py
```

Archivos generados
`metricas/commits.csv`y `metricas/lead_time.csv`

- Generar burn down
  - _Burn down_: Gráfica que nos permite observar el estado de los issues de acuerdo al día.

```bash
python3 src/generar_burn_down.py
```

Archivo generado
`reports/burn_down.txt`

- Notificar retrasos
  - Si el `lead_time` de un issue excede un umbral establecido, se generará una notificación de retraso.

```bash
python3 src/notificar_retrasos.py
```

Archivo(s) generado(s)
`reports/emails/issue_x_delay`

4. Ejecutar tests:

   ```bash
   bash tests/test_generar_kanban.sh
   ```

   ```bash
   pytest --cov=src --cov-report=term-missing
   ```
