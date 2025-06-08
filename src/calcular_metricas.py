import subprocess
import csv


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


# main
if __name__ == "__main__":
    commits = registrar_git_log()
    escribir_csv(commits)
