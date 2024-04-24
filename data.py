from datetime import datetime
from dateutil.relativedelta import relativedelta
# Prueba
# Configuración de los Drivers y URL de Trivago

# Página Trivago
url = "https://www.trivago.com.mx/es-MX"

# Seleccionar destino
hotel = "Ocean Coral & Turquesa"

# Establecer la fecha de hoy, ayer y mañana
today = datetime.today()
yesterday = datetime.now().date() - relativedelta(days=1)
tomorrow = datetime.now().date() + relativedelta(days=1)


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