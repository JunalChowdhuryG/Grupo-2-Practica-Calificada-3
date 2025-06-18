import csv
import os
import json


def notificar_retrasos(archivo_lead_time='metricas/lead_time.csv', archivo_issues='issues.json', umbral_horas=72):
    # detectar problemas con el tiempo de entrega mayor al umbral y generar email
    if not os.path.exists(archivo_lead_time):
        print(f"error: {archivo_lead_time} no encontrado")
        return
    if not os.path.exists(archivo_issues):
        print(f"error: {archivo_issues} no encontrado")
        return
    try:
        # cargar issues
        with open(archivo_issues, 'r') as f:
            issues = json.load(f)
        # leer lead times
        with open(archivo_lead_time, 'r') as f:
            lector = csv.DictReader(f)
            if not lector.fieldnames or 'issue_id' not in lector.fieldnames or 'lead_time_hours' not in lector.fieldnames:
                print(f"error: formato csv erroneo en {archivo_lead_time}")
                return
            issues_retrasados = []
            total_issues = 0
            for row in lector:
                try:
                    issue_id = row['issue_id']
                    lead_time = float(row['lead_time_hours'])
                    total_issues += 1
                    print(f"Issue #{issue_id}: {lead_time: .1f} horas", end="")
                    if lead_time > umbral_horas:
                        issues_retrasados.append((issue_id, lead_time))
                        owner = get_owner(issue_id, issues)
                        if owner == "unknown":
                            print(f"owner no encontrado en el issue #{issue_id}")
                            continue
                        directorio_email_issue = f"reports/emails/issue_{issue_id}_delay.txt"
                        # Crear directorio si no existe
                        directorio_email = 'reports/emails'
                        os.makedirs(directorio_email, exist_ok=True)
                        if os.path.exists(directorio_email_issue):
                            print(f"\nemail para issue #{issue_id} ya existe")
                            continue
                        # genera email
                        contenido_email = f"""From: devops@local
To: {owner}@local
Subject: Retraso en issue #{issue_id}

Hola {owner}, \nEl issue #{issue_id} lleva un lead time de {round(lead_time, 2)} horas, superior al umbral de {umbral_horas} horas. Por favor, revisar estado.
"""
                        with open(directorio_email_issue, 'w') as f:
                            f.write(contenido_email)
                        print(f"\nemail generado: {directorio_email_issue}")
                    else:
                        print("\nOK")
                except (ValueError, KeyError) as e:
                    print(f"\nerror al procesar issue {row.get('issue_id', 'unknown')}: {e}")
    except (IOError, csv.Error, json.JSONDecodeError) as e:
        print(f"\nerror al leer los archivos: {e}")


def get_owner(issue_id, issues):
    # buscar el owner del issue de la lista de issues
    for issue in issues:
        if str(issue['id']) == str(issue_id):
            return issue['owner']
    return "unknown"


if __name__ == "__main__":
    umbral = 72
    notificar_retrasos(umbral_horas=umbral)
