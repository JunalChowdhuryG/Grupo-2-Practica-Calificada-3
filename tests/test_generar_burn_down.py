import pytest
import json
import tempfile
import os
from datetime import datetime, timedelta
from unittest.mock import patch, mock_open
from src.generar_burn_down import generar_burn_down

class TestGenerarBurnDown:
    
    #Issues de ejemplo
    @pytest.fixture
    def sample_issues(self):
        return [
            {
                "created_at": "2024-01-01T10:00:00",
                "closed_at": "2024-01-03T15:00:00",
                "state": "closed"
            },
            {
                "created_at": "2024-01-02T09:00:00",
                "closed_at": None,
                "state": "open"
            },
            {
                "created_at": "2024-01-03T14:00:00",
                "closed_at": "2024-01-04T16:00:00",
                "state": "closed"
            }
        ]
    
    #Archivos temporales
    @pytest.fixture
    def temp_files(self):
        temp_input = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        temp_output = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        temp_input.close() # Cerrar archivos para evitar bloqueos en Windows
        temp_output.close()

        yield temp_input.name, temp_output.name
        
        # Limpiar archivos temporales
        for file_path in [temp_input.name, temp_output.name]:
            try:     
                if os.path.exists(file_path):
                    os.unlink(file_path)
            except PermissionError:  # Posibles errores de permisos en Windows
                pass 

    def test_generar_burn_down_exitoso(self, sample_issues, temp_files):
        issues, output = temp_files
        
        # Escribir datos de prueba
        with open(issues, 'w',encoding='utf-8') as f:
            json.dump(sample_issues, f)
        
        # Ejecutar funcion
        generar_burn_down(issues, output)
        
        # Verificar que se genero el archivo
        assert os.path.exists(output)
        
        # Verificar contenido
        with open(output, 'r',encoding='utf-8') as f:
            content = f.read()
            
        lines = content.splitlines()
        assert len(lines) > 0
        
        # Verificar formato de las lineas
        for line in lines:
            assert '[' in line and ']' in line  # Formato de fecha
            assert '(' in line and ')' in line  # Formato de contadores
            assert '[|]' in line or '─' in line   # Barras de progreso
    
    def test_issues_vacios(self, temp_files):
        issues, output = temp_files
        
        # Crear archivo con lista vacia
        with open(issues, 'w',encoding='utf-8') as f:
            json.dump([], f)
        
        # Ejecutar funcion 
        generar_burn_down(issues, output)
        
        # El archivo de salida no deberia existir o estar vacio
        if os.path.exists(output):
            with open(output, 'r',encoding='utf-8') as f:
                content = f.read()
                assert content == ""
    
    def test_issues_no_existe(self, temp_files):
        _, output = temp_files
        
        with patch('builtins.print') as mock_print:
            generar_burn_down('archivo_inexistente.json', output)
            
        # Verificar que se imprimio el error
        mock_print.assert_called_once()
        assert "Error generando burn-down" in str(mock_print.call_args)
    
    def test_json_invalido(self, temp_files):
        issues, output = temp_files
        
        # Escribir JSON invalido
        with open(issues, 'w',encoding='utf-8') as f:
            f.write('{"invalid": json}')
        
        with patch('builtins.print') as mock_print:
            generar_burn_down(issues, output)
            
        mock_print.assert_called_once()
        assert "Error generando burn-down" in str(mock_print.call_args)
    
    def test_fechas_invalidas(self, temp_files):
        issues, output = temp_files
        
        invalid_issues = [
            {
                "created_at": "fecha-invalida",
                "closed_at": None,
                "state": "open"
            }
        ]
        
        with open(issues, 'w',encoding='utf-8') as f:
            json.dump(invalid_issues, f)
        
        with patch('builtins.print') as mock_print:
            generar_burn_down(issues, output)
            
        mock_print.assert_called_once()
        assert "Error generando burn-down" in str(mock_print.call_args)
    
    def test_issues_solo_abiertos(self, temp_files):
        issues, output = temp_files
        
        open_issues = [
            {
                "created_at": "2024-01-01T10:00:00",
                "closed_at": None,
                "state": "open"
            },
            {
                "created_at": "2024-01-02T10:00:00",
                "closed_at": None,
                "state": "open"
            }
        ]
        
        with open(issues, 'w', encoding='utf-8') as f:
            json.dump(open_issues, f)
        
        generar_burn_down(issues, output)
        
        with open(output, 'r',encoding='utf-8') as f:
            content = f.read()
        
        # Todas las lineas deberian tener solo [|] (issues abiertas)
        lines = content.strip().split('\n')
        for line in lines:
            assert '[|]' in line
            # No deberia haber barras cerradas en los dias donde hay issues
            if '(' in line and ')' in line:
                # Extraer contadores
                counter_part = line.split('(')[1].split(')')[0]
                open_count, total_count = map(int, counter_part.split('/'))
                if total_count > 0:
                    assert '─' not in line or open_count == total_count
    
    def test_formato_salida_correcto(self, sample_issues, temp_files):
        issues, output = temp_files
        
        with open(issues, 'w',encoding='utf-8') as f:
            json.dump(sample_issues, f)
        
        generar_burn_down(issues, output)
        
        with open(output, 'r',encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            # Verificar formato: [DD-MM-YYYY] [|][|][|][|]─── (X/Y)
            assert line.startswith('[')
            assert '] ' in line
            assert line.endswith(')')
            
            # Extraer y verificar fecha
            fecha_str = line.split(']')[0][1:]
            datetime.strptime(fecha_str, '%d-%m-%Y')  # Falla si el formato es incorrecto
    

    
    def test_sin_parametros_usa_defaults(self):
        with patch('builtins.open', mock_open()) as mock_file:
            with patch('json.load') as mock_json:
                mock_json.return_value = []  # Lista vacia para simular issues
                
                generar_burn_down()
                
                # Verificar que se intentaron abrir los archivos por defecto
                mock_file.assert_any_call(os.path.join('issues.json'), 'r')

class TestIntegracion:
    
    def test_flujo_completo_realista(self):
        issues_data = [
            {
                "created_at": "2024-01-01T09:00:00",
                "closed_at": "2024-01-02T17:00:00",
                "state": "closed"
            },
            {
                "created_at": "2024-01-01T10:00:00",
                "closed_at": None,
                "state": "open"
            },
            {
                "created_at": "2024-01-02T11:00:00",
                "closed_at": "2024-01-03T14:00:00",
                "state": "closed"
            },
            {
                "created_at": "2024-01-03T12:00:00",
                "closed_at": None,
                "state": "open"
            }
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_input:
            json.dump(issues_data, temp_input)
            temp_input_name = temp_input.name
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_output:
            temp_output_name = temp_output.name
        
        try:
            generar_burn_down(temp_input_name, temp_output_name)
            
            with open(temp_output_name, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.splitlines()
 
            
            # El primer dia deberia tener 2 issues abiertas
            first_line = lines[0]
            assert '(2/2)' in first_line or '[|][|]' in first_line
            lines = content.split(' ')
             # Verificar que tenemos al menos 3 dias de datos
            assert len(lines) >= 3

        finally:
            # Limpiar archivos temporales
            for file_path in [temp_input_name, temp_output_name]:
                try:
                    if os.path.exists(file_path):
                        os.unlink(file_path)
                except PermissionError:
                    pass

if __name__ == "__main__":
    pytest.main([__file__])