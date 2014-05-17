Termometro
==========

Termometro Parlamentario
-------------------------

La aplicación quedó corriendo en http://megafono.herokuapp.com/


Instalación
--------------------------------

Para instalar todo en sus computadores realizar los siguientes pasos:

1. Instalar postgresql y crear una base de datos para la aplicación.

2. Instalar python y virtualenv.

3. Clonar el repositorio 
`git clone git@github.com:GonzaloAfa/Termometro.git`

3. Crear un entorno virtual para nuestra app 
`virtual --no-site-packages venv`

4. Activar el entorno virtual 
`source venv/bin/activate`

5. Instalar paquetes necesarios  
`pip install requirements.txt`

6. Crear un archivo llamado .env en el directorio root de la aplicacion, que contenga la url de la base de datos local que crearon antes, siguiendo el siguiente formato: 
`DATABASE_URL=postgres://usuario:password@localhost:5432/basededatos`

7. Luego de eso, utilicen foreman para ejecutar los comandos ya que setea esa variable de ambiente siempre antes de iniciar cualquier proceso. Ejemplos:

`foreman start`    -> inicia la aplicación
`foreman run python manage.py syncdb`   -> sincroniza la base de datos
`foreman run python manage.py migrate`  -> ejecuta las migraciones
