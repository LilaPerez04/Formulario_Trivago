# Formulario_Trivago
Proyecto 7: Liliana Pérez
Descripción del Proyecto: Pruebas para comprobar la funcionalidad de Urban Routes.
Escribe pruebas automatizadas que cubran el proceso completo de pedir un taxi. A través de definir los localizadores y métodos necesarios en la clase UrbanRoutesPage y las pruebas en la clase TestUrbanRoutes. Las pruebas deben cubrir estas acciones:

Configurar la dirección

Seleccionar la tarifa Comfort

Rellenar el número de teléfono

Agregar una tarjeta de crédito. (Consejo: el botón 'link' (enlace) no se activa hasta que el campo CVV de la tarjeta en el modal 'Agregar una tarjeta', id="code" class="card-input", pierde el enfoque. Para cambiar el enfoque, puedes simular que el usuario o usuaria presiona TAB o hace clic en otro lugar de la pantalla). El repositorio tiene preparada la función retrieve_phone_code() que intercepta el código de confirmación requerido para agregar una tarjeta

Escribir un mensaje para el controlador

Pedir una manta y pañuelos

Pedir 2 helados

Aparece el modal para buscar un taxi

Esperar a que aparezca la información del conductor en el modal (opcional). Además de los pasos anteriores, hay un paso opcional que puedes comprobar; este es un poco más complicado que los demás, pero es una buena práctica, ya que es probable que en tu trayectoria profesional encuentres tareas más difíciles

Servidor utilizado:
servidor utilizado

Configuración del proyecto y ejecución de las pruebas:
Inicie un nuevo servidor para la aplicación Urban.Routes iniciar servidor
Escriba la URL del nuevo servidor en el archivo data.py, asignándola en la variable urban_routes_url
Para ejecutar las pruebas escriba el código: pytest main.py, en la terminal de Pycharm
Técnicas y tecnologías utilizadas
En el proyecto se utilizan diversas tecnologías y técnicas, incluyendo PyCharm, Pytest, Pytest en la terminal para ejecutar las pruebas, Github, Github Desktop, funciones en Python y Selenium. Aquí hay una breve descripción de cada una:

PyCharm:

PyCharm es un entorno de desarrollo integrado (IDE) para Python que proporciona herramientas para escribir, editar, depurar y ejecutar código Python. Se puede configurar para ejecutar pruebas de Pytest.
Pytest:

Pytest es un framework de pruebas para Python que permite escribir pruebas de manera sencilla y efectiva. Ofrece funcionalidades avanzadas, como la ejecución de pruebas a diferentes escalas y la personalización a través de plugins.
Pytest en la Terminal:

Pytest se puede ejecutar desde la terminal utilizando comandos específicos, como buscar y ejecutar todos los tests, ejecutar tests de archivos indicados, ejecutar tests en una carpeta específica, entre otros.
Github y Github Desktop:

Github es una plataforma de desarrollo colaborativo que permite alojar proyectos utilizando el sistema de control de versiones Git. Github Desktop es una aplicación que facilita la interacción con repositorios Github a través de una interfaz gráfica.
Funciones en Python:

El proyecto hace uso de funciones en Python para modularizar y organizar el código, lo que permite reutilizar y mantener el código de manera eficiente.
Selenium:

Suite de herramientas de automatización de pruebas. Proporciona un conjunto de bibliotecas y APIs que permiten interactuar con los elementos de una página web y realizar acciones como hacer clic en botones, ingresar texto, obtener datos, etc.
