import locale
from datetime import datetime, timedelta

# Configuración de los Drivers y URL de Trivago

# Página Trivago
url = "https://www.trivago.com.mx/es-MX"

# Seleccionar destino
hotel = "Ocean Coral & Turquesa"

# Establecer la fecha de check in

# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES')

# PARA PRUEBAS CON ASSERTS

# Establecer la fecha de check in / Obtener la fecha actual
today = datetime.today()

check_in = {
    "day_ci": today.day,
    # Aquí utilizamos el método strftime para obtener el nombre del mes en formato de texto
    "month_ci": today.strftime("%B"),
    "month_number_ci": today.strftime("%m"),
    "year_ci": str(today.year)
}
# Agregando un nuevo elemento al diccionario check_in (concatenando mes y año)
check_in["month_year_ci"] = check_in["month_ci"] + " " + check_in["year_ci"]
print(check_in["day_ci"], check_in["month_ci"], check_in["month_number_ci"], check_in["year_ci"])

# Establecer la fecha de check in ayer / Obtener la fecha de ayer
yesterday = today - timedelta(days=1)

check_in_1 = {
    "day_ci_1": yesterday.day,
    # Aquí utilizamos el método strftime para obtener el nombre del mes en formato de texto
    "month_ci_1": yesterday.strftime("%B"),
    "month_number_ci_1": yesterday.strftime("%m"),
    "year_ci_1": str(yesterday.year)
}

# Agregando un nuevo elemento al diccionario check_in (concatenando mes y año)
check_in_1["month_year_ci_1"] = check_in_1["month_ci_1"] + " " + check_in_1["year_ci_1"]
print(check_in_1["day_ci_1"], check_in_1["month_ci_1"], check_in_1["month_number_ci_1"], check_in_1["year_ci_1"])

# Establecer la fecha de check in mañana / Obtener la fecha de mañana
tomorrow = today + timedelta(days=1)

check_in_2 = {
    "day_ci_2": tomorrow.day,
    # Aquí utilizamos el método strftime para obtener el nombre del mes en formato de texto
    "month_ci_2": tomorrow.strftime("%B"),
    "month_number_ci_2": tomorrow.strftime("%m"),
    "year_ci_2": str(tomorrow.year)
}

# Agregando un nuevo elemento al diccionario check_in (concatenando mes y año)
check_in_2["month_year_ci_2"] = check_in_2["month_ci_2"] + " " + check_in_2["year_ci_2"]
print(check_in_2["day_ci_2"], check_in_2["month_ci_2"], check_in_2["month_number_ci_2"], check_in_2["year_ci_2"])


# Agregando/quitando huéspedes adultos
adults_to_add = 5
adults_to_remove = 2

# Agregando/quitando huéspedes niños
kids_to_add = 3
kids_to_remove = 1

# Configurar edades de los niños
kids_ages = {
    1: "6",
    2: "0"
    #    3: "4",
    #    4: "15"
}

# Agregando/quitando cuartos
rooms_to_add = 2
rooms_to_remove = 1


# Establecer la fecha de check out
check_out = {
    "day_co": '28',
    "month_co": 'Julio',
    "month_number_co": '07',
    "year_co": '2024',
}
# Agregando un nuevo elemento al diccionario check_out (concatenando mes y año)
check_out["month_year_co"] = check_out["month_co"] + " " + check_out["year_co"]
