import pytest
import os
import builtins
import json
import csv
from unittest import mock
from src.notificar_retrasos import notificar_retrasos

# --- Datos simulados ---
ISSUES = [
    {"id": 1, "owner": "junal"},
    {"id": 2, "owner": "janio"},
    {"id": 3, "owner": "andres"},
    {"id": 4, "owner": "desconocido"}
]

LEAD_TIME_CONTENT = """issue_id,lead_time_hours
1,1.2
2,2.2
3,80.5
4,100.1
"""

@pytest.fixture
def fake_files(tmp_path):
    # Crear archivos temporales
    issues_path = tmp_path / "issues.json"
    lead_time_path = tmp_path / "lead_time.csv"
    with open(issues_path, "w") as f:
        json.dump(ISSUES, f)
    with open(lead_time_path, "w") as f:
        f.write(LEAD_TIME_CONTENT)
    return str(issues_path), str(lead_time_path)


def test_archivo_csv_no_existe(capsys):
    notificar_retrasos(archivo_lead_time="inexistente.csv", archivo_issues="issues.json")
    salida = capsys.readouterr().out
    assert "error: inexistente.csv no encontrado" in salida


def test_archivo_issues_no_existe(tmp_path, capsys):
    lead_path = tmp_path / "lead_time.csv"
    lead_path.write_text(LEAD_TIME_CONTENT)
    notificar_retrasos(archivo_lead_time=str(lead_path), archivo_issues="falso.json")
    salida = capsys.readouterr().out
    assert "error: falso.json no encontrado" in salida


def test_formato_csv_erroneo(tmp_path, capsys):
    issues_path = tmp_path / "issues.json"
    csv_path = tmp_path / "bad.csv"
    issues_path.write_text(json.dumps(ISSUES))
    csv_path.write_text("no_tiene_cabeceras\nx,y,z")
    notificar_retrasos(archivo_lead_time=str(csv_path), archivo_issues=str(issues_path))
    salida = capsys.readouterr().out
    assert "error: formato csv erroneo" in salida


@mock.patch("os.makedirs")
@mock.patch("os.path.exists", side_effect=lambda p: False if "delay" in p else True)
def test_generacion_emails(mock_exists, mock_makedirs, tmp_path, capsys):
    # Rutas válidas
    issues_path = tmp_path / "issues.json"
    lead_path = tmp_path / "lead_time.csv"
    with open(issues_path, "w") as f:
        json.dump(ISSUES, f)
    with open(lead_path, "w") as f:
        f.write(LEAD_TIME_CONTENT)

    notificar_retrasos(
        archivo_lead_time=str(lead_path),
        archivo_issues=str(issues_path),
        umbral_horas=72
    )

    salida = capsys.readouterr().out
    assert "email generado: reports/emails/issue_3_delay.txt" in salida
    assert "email generado: reports/emails/issue_4_delay.txt" in salida

