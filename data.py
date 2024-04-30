import datetime
import locale
# Prueba
# Configuración de los Drivers y URL de Trivago

# Página Trivago
url = "https://www.trivago.com.mx/es-MX"

# Seleccionar destino
hotel = "Ocean Coral & Turquesa"

# Las fechas ahora estaran en formato español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Establecer la fecha de hoy, ayer y mañana
today = datetime.date.today()
past = today - datetime.timedelta(days=1)
future = today + datetime.timedelta(days=1)

spanish_months = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}


# Agregando/quitando huéspedes adultos
adults_to_add = 0
adults_to_remove = 0
total_adults = adults_to_add - adults_to_remove - 2

# Agregando/quitando huéspedes niños
kids_to_add = 4
kids_to_remove = 1
total_kids = kids_to_add - kids_to_remove

# Configurar edades de los niños
kids_ages = {
    1: "4",
    2: "2",
    3: "4",
    4: "15"
}

# Agregando/quitando cuartos
rooms_to_add = 0
rooms_to_remove = 0
total_rooms = rooms_to_add - rooms_to_remove
#