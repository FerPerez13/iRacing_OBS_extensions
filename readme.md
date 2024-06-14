# iRacing OBS Extensions

## Información sobre el software
Este es un programa creado principalmente para Streamers de iRacing que quieren mostrar sus estadísticas en directo (actualizadas cada minuto).

## Requisitos previos

Para el correcto funcionamiento de este programa tienes que tener instalado en tu ordenador [Python](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe)

## Instalación
Para instalar el programa tienes que descargarte este repositorio en formato .zip y descomprimirlo en una carpeta de tu sistema (que no requiera de permisos de administrador) o clonarte el repositorio utilizando el comando 

    git clone https://github.com/FerPerez13/iRacing_OBS_extensions

Hecho esto, tienes que abrir la carpeta que has descargado o descomprimido y ejecutar el archivo

    install-dependencies.bat

Una vez hecho esto ya podrás ejecutar correctamente el archivo 

    iRacing-OBS-extensions.bat

## Configuración

Cuando se ejecuta el programa, aparece un formulario en el que tienes que meter tus credenciales de iRacing (esto es necesario para poder recoger tus estadisticas)

![img.png](/ReadmeImages/Login.png)

Si marcas el check de **Save Login** este te guardará en un archivo de la carpeta de tu ordenador los credenciales para facilitar los futuros acceos a la aplicación.

Hecho esto, y si tus credenciales son correctos, tendrás la siguiente ventana: 

![img.png](/ReadmeImages/Process.png)

Aqui tenemos las **Estadisticas de Piloto** y **Ultima Carrera**. Dentro de cada una de estas filas, tenemos unos interruptores que activan/desactivan cada uno de los procesos.
Estos tienes que activarlos para que se actualice de forma automatica las estadisticas. 

Se ha añadido una barra que muestra que el proceso esta en ejecución. 

Pero por si acaso este proceso no funciona correctamente, hay un boton de **Force Update** en el que se puede forzar la actualización de los archivos.

Hecho esto solo nos falta importar los datos en OBS. Para esto nos iremos a la carpeta del programa. Aqui tenemos una carpeta llamada

    /results

Aqui tendremos los archivos ``html`` que tenemos que importar en el OBS como **fuente de navegador** y **archivo local**

![img.png](/ReadmeImages/folder.png)

Esto quedará de la siguiente forma (dependiendo de la posición en la que lo coloques en el OBS)

![img.png](/ReadmeImages/resultado en directo.png)

## Conclusión

Espero que te sirva y que puedas usarlo en tu directo de forma correcta

Gracias por usarlo y se agradecen los comentarios y los créditos en tu directo 😊

> Estoy trabajando pra mejorar toda la experiencia de instalación y de funcionamiento. Revisa de vez en cuando este repositorio en busca de mas información o de actualizaciones