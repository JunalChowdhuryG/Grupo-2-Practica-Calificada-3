import subprocess
import csv
import json
from datetime import datetime


# funcion que captura el historial de commits de un repositorio git
def registrar_git_log():
    # captura la salida del comando git log
    try:
        historial = subprocess.run(
            ['git', 'log', '--pretty=format:%H|%ad|%s', '--date=iso'],
            capture_output=True, text=True, check=True
        )
        commits = []
        for line in historial.stdout.splitlines():
            commit_hash, date, message = line.split('|', 2)
            commits.append((commit_hash, date, message))
        return commits
    except subprocess.CalledProcessError as e:
        print(f"error al ejecutar el comando git log: {e}")
        return []


# funcion que escribe los datos de los commits en un archivo CSV
def escribir_csv(commits, output_file='metricas/commits.csv'):
    # escribe los datos en un archivo CSV
    try:
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['commit_hash', 'fecha', 'tipo_de_issue'])
            for commit in commits:
                writer.writerow(commit)
    except IOError as e:
        print(f"error al escribir en el CSV: {e}")


# funcion que calcula el lead time de los issues cerrados
def calcular_lead_time(issues_file='issues.json', output_file='metricas/lead_time.csv'):
    try:
        # se lee el archivo JSON con los issues
        with open(issues_file, 'r') as f:
            issues = json.load(f)
        lead_times = []
        for issue in issues:
            # se calcula el lead time solo para issues cerrados
            if issue['state'] == 'closed' and issue['closed_at']:
                # se convierte las fechas de creación y cierre a objetos datetime
                f_creado = datetime.fromisoformat(issue['created_at'].replace('Z', '+00:00'))
                f_cerrado = datetime.fromisoformat(issue['closed_at'].replace('Z', '+00:00'))
                # se calcula el lead time en horas
                lead_time_horas = (f_cerrado - f_creado).total_seconds() / 3600
                # se guarda
                lead_times.append((issue['id'], lead_time_horas))
        # se escribe  resultado en un archivo CSV
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['issue_id', 'lead_time_hours'])
            for lead_time in lead_times:
                writer.writerow(lead_time)
        return lead_times
    except (IOError, json.JSONDecodeError, ValueError) as e:
        print(f"error al callcular lead time: {e}")
        return []


# main
if __name__ == "__main__":
    # se registra los commits
    commits = registrar_git_log()
    # se escribe los commits en un archivo CSV
    escribir_csv(commits)
    # se calcula el lead time de los issues cerrados
    calcular_lead_time()
