import easygui
max_sensors = 4
limit_temp = 38.0
failed_sensors_count = 0
report_log = "-------------- Sensor Report -------------\n"

gui_title = "Monitor v1.0"

easygui.msgbox(f'Iniciando a checagem de {max_sensors} sensores de temperatura...', title=gui_title)

for i in range(1, max_sensors + 1):
    input_value = easygui.enterbox(f'Informe a temperatura do sensor {i}:', title=gui_title)
    
    if input_value is None:
        break
    temp = float(input_value)
    if temp > limit_temp:
        report_log += f'Sensor {i}: Falha - Temperatura {temp}°C excede o limite de {limit_temp}°C\n'
        failed_sensors_count += 1
    else:
        report_log += f'Sensor {i}: OK - Temperatura {temp}°C dentro do limite\n'