import os
import csv
import json
import pytest
from unittest.mock import patch, mock_open
from src.calcular_metricas import registrar_git_log, escribir_csv, calcular_lead_time


# Test 1: Mock de simulacion de git log 
@patch("subprocess.run")
def test_registrar_git_log_mock(mock_run):
    # Fecha valida con zona horaria
    mock_run.return_value.stdout = "abc123|2025-06-12T10:00:00+00:00|feat[#1]: mensaje de prueba"
    mock_run.return_value.returncode = 0

    commits = registrar_git_log()
    assert len(commits) == 1
    assert commits[0][0] == "abc123"
    assert commits[0][2] == "feat[#1]" 
    assert commits[0][3] == 0

# Test 2: Probar escribir_csv con datos simulados
def test_escribir_csv(tmp_path):
    # datos simulados de commits
    dummy_commits = [
        ("abc123", "2025-06-12T10:00:00+00:00", "fix[#2]: error corregido", 0),
        ("def456", "2025-06-13T11:00:00+00:00", "feat[#3]: nueva funcionalidad", 1)
    ]
    output_file = tmp_path / "commits.csv"
    escribir_csv(dummy_commits, output_file)

    # validamos el contenido del archivo generado
    with open(output_file, newline='') as f:
        reader = list(csv.reader(f))
        assert reader[0] == ['commit_hash', 'fecha', 'tipo_de_issue', 'dia_desde_inicio']
        assert reader[1] == [str(x) for x in dummy_commits[0]]
        assert reader[2] == [str(x) for x in dummy_commits[1]]


# Test 3: calcular_lead_time con un issue cerrado
def test_calcular_lead_time_closed(tmp_path):
    issues_data = [
        {
            "id": 1,
            "state": "closed",
            "created_at": "2025-06-07T12:00:00",
            "closed_at": "2025-06-07T15:00:00"
        }
    ]
    issues_path = tmp_path / "issues.json"
    output_path = tmp_path / "lead_time.csv"

    with open(issues_path, 'w') as f:
        json.dump(issues_data, f)

    result = calcular_lead_time(str(issues_path), str(output_path))
    # validamos que el resultado contenga un solo issue con lead time de 3 horas
    assert len(result) == 1
    assert result[0][0] == 1
    assert round(result[0][1], 2) == 3.0  # 3 horas exactas

    # verificamos el csv creado
    with open(output_path, newline='') as f:
        rows = list(csv.reader(f))
        assert rows[0] == ["issue_id", "lead_time_hours"]
        assert int(rows[1][0]) == 1
        assert abs(float(rows[1][1]) - 3.0) < 0.01


# Test 4: calcular_lead_time ignora issue abierto
def test_calcular_lead_time_abierto(tmp_path):
    issues_data = [
        {
            "id": 2,
            "state": "open",
            "created_at": "2025-06-07T12:00:00Z",
            "closed_at": None
        }
    ]
    # escribimos el archivo simulado
    issues_path = tmp_path / "issues.json"
    output_path = tmp_path / "lead_time.csv"

    with open(issues_path, 'w') as f:
        json.dump(issues_data, f)

    result = calcular_lead_time(str(issues_path), str(output_path))
    # la lista debe estar vacia ya que el issue esta abierto
    assert result == []


# Test 5: calcular_lead_time con JSON malformado
def test_calcular_lead_time_json_invalido(tmp_path):
    bad_json_path = tmp_path / "bad_issues.json"
    
    bad_json_path.write_text("{malformed_json")
    
    # ejecutamos y verificamos que devuelva una lista vacia sin lanzar excepcion
    result = calcular_lead_time(str(bad_json_path))
    assert result == []
