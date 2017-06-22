# Standalone Python - Firebird - Mysql

Es un proyecto para crear conexión entre dos bases de datos y realizar múltiples consultas entre un software de escritorio que utilize Interbase-Firebird y Mysql en un servidor web.

Se esta utilizando python, también varias interfaces que ayudan a trabajar con tecnologías de base de datos y gráficos para desarrollar la aplicación de escritorio.

# Tecnologías:
<ul>
  <li><strong><a href="https://wxpython.org/">Wxpython (UI)</a></strong></li>
</ul>
<ul>
  <li><strong><a href="https://www.firebirdsql.org/en/python-driver/">Kinterbasdb  (Firebird 1.X)</a></strong></li>
</ul>
<ul>
  <li><strong><a href="https://pypi.python.org/pypi/MySQL-python">MySQLdb  (Mysql)</a></strong></li>
</ul>
<ul>
  <li><strong><a href="https://anthony-tuininga.github.io/cx_Freeze/">Cx_Freeze</a></strong></li>
</ul>


Kinterbasdb fue reemplazado por <a href='https://firebirdsql.org/file/documentation/drivers_documentation/python/fdb/getting-started.html'>FDB</a>, por que este dejo de recibir soporte y además FDB solo se puede utilizar si estas utilizando una versión de Firebird 2.X o superior.

Cx_Freeze es un conjunto de scripts que ayudan a convertir una aplicación de Python en un ejecutable .exe.

Esta aplicación solo realiza la prueba de conexión y también la posibilidad de crear un proceso secundario que pueda ejecutar peticiones al servidor en la nube o al servidor local y viceversa para editar,insertar y eliminar datos, comprar y entregar resultados.

El archivo que contiene el proceso para intercambiar información tiene que desarrollarlo el usuario ya que el que tengo yo es para una aplicación que no serviría compartir.

# Archivos .bat

Esta aplicación contiene archivos .bat que se utilizan para ejecutar los procesos que la comandan, como por ejemplo iniciar una vez que el sistema operativo encienda o hasta crear un archivo que se ejecute en segundo plano para no interrumpir la labor del usuario.

<p><strong>config.bat</strong></p>

Este archivo tiene el deber de copiar el acceso directo de la aplicación connect-crm.exe (ejecuta una serie de consultas SQL para comprar datos) al inicio de windows.

<p><strong>run.bat</strong></p>

Este archivo tiene el deber de ejecutar proceso principal de aplicación connect-crm.exe y cargarla en segundo plano. Cabe aclarar que este archivo no está cargado en github,ya que no sería lógico compartir porque contiene consultas específicas y no pueden volcarse como ejemplo. 

<p><strong>stop.bat</strong></p>

Cierra el proceso que está ejecutando connect-crm.exe

<p><strong>stop-config.bat</strong></p>

Cierra el proceso que se está ejecutando el nombre config-connect.bat

# Como iniciar la prueba

Completar los datos correspondientes los archivos de texto, y luego ir a la raíz de la aplicación mediante la consola, ejecutar el comando <strong>"python confi-connect.py"</strong>.
