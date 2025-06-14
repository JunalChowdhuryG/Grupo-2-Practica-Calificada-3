from datetime import datetime, timedelta
import json

def generar_burn_down(issues='issues.json', output='reports/burn_down.txt'):
    try:
        # Cargar los issues desde el JSON
        with open(issues, 'r') as f:
            issues = json.load(f)
        issues_totales = len(issues)
        # Verificando que hayan issues
        if issues_totales == 0:
            return
        # Extrae las fechas de creacion y cierre de los issues
        fechas = [datetime.fromisoformat(issue['created_at']) for issue in issues]
        # El start date sera la menor fecha
        fecha_inicial = min(fechas)
        # El end date sera la mayor fecha de cierre. Sino esta cerrado, la fecha actual 
        fecha_final = max(datetime.fromisoformat(issue['closed_at']) if issue['closed_at'] else datetime.now() for issue in issues)
        # La cantidad de dias entre el inicio y el fin
        dias = (fecha_final - fecha_inicial).days + 1
        # Generar el grafico de burndown
        # Por cada dia contar los issues abiertos y cerrados
        # Issue abierto: █ Issue cerrado: -
        with open(output, 'w') as f:
            for dia in range(dias):
                fecha_actual = fecha_inicial + timedelta(days=dia)
                #Usar el final del dia para las comparaciones
                final_del_dia = fecha_actual.replace(hour=23, minute=59, second=59)
                # Contar issues creados hasta el final de este dia (acumulativo)
                issues_creadas = sum(1 for issue in issues if 
                                          datetime.fromisoformat(issue['created_at']) <= final_del_dia)
                # De esos issues creados cuantos estan abiertos al final del dia
                issues_abiertas = sum(1 for issue in issues if 
                                datetime.fromisoformat(issue['created_at']) <= final_del_dia and
                                (issue['state'] == 'open' or 
                                 (issue['closed_at'] and datetime.fromisoformat(issue['closed_at']) > final_del_dia)))
                # Barra proporcional al total acumulado
                bars = '█' * issues_abiertas + '─' * (issues_creadas - issues_abiertas)
                f.write(f"[{fecha_actual.strftime('%d-%m-%Y')}] {bars} ({issues_abiertas}/{issues_creadas})\n")
    except (IOError, json.JSONDecodeError, ValueError) as e:
        print(f"Error generando burn-down : {e}")

generar_burn_down()