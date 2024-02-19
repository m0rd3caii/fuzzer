# Importar las librerías necesarias
import argparse  # Para parsear los argumentos de la línea de comandos
import requests  # Para hacer peticiones HTTP
from tqdm import tqdm  # Para mostrar una barra de progreso
from rich.console import Console  # Para manejar la salida en la consola de forma enriquecida
from rich.panel import Panel  # Para crear un panel de texto enriquecido

# Crear un banner de bienvenida con Rich
console = Console()  # Crear un objeto Console para manejar la salida
banner = Panel.fit("[bold green]Script de fuzzing de directorios web[/bold green]", title="Bienvenido")  # Crear un panel de texto enriquecido con el título "Bienvenido"
console.print(banner)  # Imprimir el banner en la consola

# Parsing de los argumentos de la línea de comandos
parser = argparse.ArgumentParser(description="Script de fuzzing de directorios web")  # Crear un objeto ArgumentParser con una descripción
parser.add_argument("url", help="URL base para el fuzzing")  # Definir un argumento para la URL base
parser.add_argument("diccionario", help="Archivo de diccionario")  # Definir un argumento para el archivo de diccionario
args = parser.parse_args()  # Analizar los argumentos de la línea de comandos y almacenarlos en la variable args

# Leer el diccionario de palabras desde el archivo proporcionado
with open(args.diccionario) as file:
    wordlist = file.read().splitlines()  # Leer el contenido del archivo y dividirlo en líneas

try:
    # Configurar la barra de progreso con tqdm
    barrita = tqdm(total=len(wordlist), desc="Progreso", unit="urls", dynamic_ncols=True)  # Crear una barra de progreso con el tamaño total de palabras del diccionario

    # Iterar sobre cada palabra en el diccionario
    for linea in wordlist:
        url_completa = args.url + linea  # Construir la URL completa concatenando la URL base con la palabra actual del diccionario
        response = requests.get(url_completa)  # Realizar una petición GET a la URL completa
        if response.status_code == 200:  # Si la respuesta es exitosa (código 200)
            tqdm.write(f"Directiorio encontrado: {url_completa}")  # Escribir en la consola que se ha encontrado un directorio
        barrita.update(1)  # Actualizar la barra de progreso

except KeyboardInterrupt:  # Capturar la excepción si el usuario interrumpe el script con Ctrl+C
    print("\nScript interrumpido por el usuario al pulsar control +C")

finally:
    barrita.close()  # Cerrar la barra de progreso al finalizar el script
