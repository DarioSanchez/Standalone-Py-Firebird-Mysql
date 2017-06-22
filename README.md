# Standalone Python - Firebird - Mysql

Es un proyecto para crear conexión entre dos bases de datos y realizar múltiples consultas entre un software de escritorio que utilize Interbase-Firebird y Mysql en un servidor web.

Se esta utilizando python, también varias interfaces que ayudan a trabajar con tecnologías de base de datos y gráficos para desarrollar la aplicación de escritorio.

# Tecnologías:

Wx (Grafica)



Kinterbasdb (Firebird 1.X)



MySQLdb (Mysql)



Cx_Freeze



Kinterbasdb fue reemplazado por FDB, por que este dejo de recibir soporte y además FDB solo se puede utilizar si estas utilizando una versión de Firebird 2.X o superior.

Cx_Freeze es un conjunto de scripts que ayudan a convertir una aplicación de Python en un ejecutable .exe.

Esta aplicación solo realiza la prueba de conexión y también la posibilidad de crear un proceso secundario que pueda ejecutar peticiones al servidor en la nube o al servidor local y viceversa para editar,insertar y eliminar datos, comprar y entregar resultados.

El archivo que contiene el proceso para intercambiar información tiene que desarrollarlo el usuario ya que el que tengo yo es para una aplicación que no serviría compartir.

# Archivos .bat

Esta aplicación contiene archivos .bat que se utilizan para ejecutar los procesos que la comandan, como por ejemplo iniciar una vez que el sistema operativo encienda o hasta crear un archivo que se ejecute en segundo plano para no interrumpir la labor del usuario.

config.bat

Este archivo tiene el deber de copiar el acceso directo de la aplicación connect-crm.exe (ejecuta una serie de consultas SQL para comprar datos) al inicio de windows.

run.bat

Este archivo tiene el deber de ejecutar proceso principal de aplicación connect-crm.exe y cargarla en segundo plano. Cabe aclarar que este archivo no está cargado en github ya que no sería lógico compartir porque contiene consultas específicas y no pueden volcarse como ejemplo. 

stop.bat

Cierra el proceso que está ejecutando connect-crm.exe

stop-config.bat

Cierra el proceso que se está ejecutando el nombre config-connect.bat

# Como iniciar la prueba

Completar los datos correspondientes los archivos de texto, y luego ir a la raíz de la aplicación mediante la consola, ejecutar el comando "python confi-connect.py".
