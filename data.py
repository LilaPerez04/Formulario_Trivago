# Configuración de los Drivers y URL de Trivago

# Página Trivago
url = "https://www.trivago.com.mx/es-MX"

# Seleccionar destino
hotel = "Ocean Coral & Turquesa"

# Establecer la fecha de check in
check_in = {
    "day_ci": '10',
    "month_ci": 'Mayo',
    "month_number_ci": '05',
    "year_ci": '2024',
}
# Agregando un nuevo elemento al diccionario check_in (concatenando mes y año)
check_in["month_year_ci"] = check_in["month_ci"] + " " + check_in["year_ci"]

# Establecer la fecha de check out
check_out = {
    "day_co": '28',
    "month_co": 'Julio',
    "month_number_co": '07',
    "year_co": '2024',
}
# Agregando un nuevo elemento al diccionario check_out (concatenando mes y año)
check_out["month_year_co"] = check_out["month_co"] + " " + check_out["year_co"]


#2345