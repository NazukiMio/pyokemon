# Documentación del código: Búsqueda de Pokémon

## Resumen

Este proyecto contiene dos versiones de una aplicación que obtiene información sobre un Pokémon usando la API pública de PokéAPI. La primera versión es una aplicación de línea de comandos, y la segunda es una aplicación con interfaz gráfica de usuario (GUI) utilizando Tkinter.

---

## 1. Versión de Línea de Comandos (CLI)

### Descripción

Esta versión permite al usuario ingresar el nombre de un Pokémon a través de la consola. Si el nombre es válido, el programa hace una solicitud HTTP a la PokéAPI y muestra información sobre el Pokémon como su nombre, ID, altura, peso y tipos.

### Requisitos

- Python 3.x
- Biblioteca `requests` (Instalar con `pip install requests`)

### Código

```python
import requests
# Llama al modulo de requests, es para hacer peticiones HTTP

def pokemon_info(pokemon_name):
# Definir la funcion de buscar informacion de pokemon con el nombre de pokemon como parametro
    pokemon_name = pokemon_name.lower()
    # Convierte el nombre del pokemon en minusculas

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    # La enlace para obtener la informacion del pokemon, un ejemplo: "https://pokeapi.co/api/v2/pokemon/pikachu"
    try:
        # "try" es un metodo de python para manejar errores, si ocurre un error, 
        # se ejecuta el "except" en lugar de parar la ejecucion del programa
        response = requests.get(url)
        # Hace una peticion GET a la url
        if response.status_code == 200:
        # "status_code 200" significa que la solicitud fue exitosa, entonces si la solicitación fue exitosa,
        # sigue ejecutando el codigo ensequida
            data = response.json()
            # Reproduce la resulta de resspuesta en formato json

            # Rellenar informacion del Pokémon
            name = data['name'].capitalize()
            pokemon_id = data['id']
            height = data['height'] / 10
            weight = data['weight'] / 10
            types = [t['type']['name'] for t in data['types']]

            print(f"Información de {pokemon_name}:")
            print(f"Nombre: {name}")
            print(f"ID: {pokemon_id}")
            print(f"Altura: {height}m")
            print(f"Peso: {weight}kg")
            print(f"Tipo(s): {', '.join(types)}")

            input("Presione Enter para continuar...")

            return data

        else:
            print(f"No se pudo encontrar información sobre {pokemon_name}.")
            # Si la solicitud no fue exitosa, imprime un mensaje de error
            return None
            # Retorna None para indicar que no se encontro informacion del pokemon

    except requests.exceptions.RequestException as e:
    # Si ocurre un error al hacer la solicitud, imprime un mensaje de error
        print(f"Error al obtener información sobre {pokemon_name}: {e}")
        return None

def main():
    while True:
        pokemon_name = input("Ingrese el nombre de un Pokémon (Ingrese 'salir' para terminar): ")
        # Pide al usuario que ingrese el nombre de un pokemon, si el usuario ingresa "salir", el programa se detiene

        # Condición de salida
        if pokemon_name.lower() == 'salir':
            break
        
        # Ejecutar la función "pokemon_info" 
        pokemon_info(pokemon_name)

if __name__ == "__main__":
# Revisa si el archivo se está ejecutando directamente o se está importando como un módulo
    main()
```

### Instrucciones de uso:

1. Ejecuta el script.
2. Ingresa el nombre de un Pokémon cuando se te pida (escribe "salir" para terminar).
3. El programa devolverá la información del Pokémon o un mensaje de error si no se encuentra.

---

## 2. Versión GUI (Interfaz Gráfica de Usuario)

### Descripción

Esta versión utiliza Tkinter para crear una interfaz gráfica en la que el usuario puede ingresar el nombre de un Pokémon en un cuadro de texto y, al presionar un botón, ver la información del Pokémon junto con su imagen.

### Requisitos

- Python 3.x
- Bibliotecas `requests`, `tkinter`, `PIL` (Instalar con `pip install requests pillow`)

```python
import tkinter as tk
# Llamar al modulo tkinter, y renombrarlo como tk, es el modulo GUI por defecto de python
from tkinter import ttk, messagebox
# Desde biblioteca tkinter, llamar a ttk y messagebox, ttk proporciona elementos 
# de interfaz de usuario más avanzados, y messagebox proporciona ventanas de mensaje
import requests
# Llamar a modulo requests, la biblioteca para hacer peticiones HTTP
from PIL import Image, ImageTk
# Llamar a modulo PIL, la biblioteca para manejar imagenes, image para manejar imagenes y imageTk para 
# convertir imagenes en objetos que tkinter puede manejar
from io import BytesIO
# Transformar datos binarios en datos de texto, en ese caso, para convertir imagenes, 
# es que requests devuelve imagenes en formato binario, y tkinter no puede manejar eso.
import webbrowser
# Llamar a modulo webbrowser, para abrir enlaces en el navegador

class InfoPokemon:
# Crear un clase llamada InfoPokemon, que contiene todas las funciones que se usaran en la app
    def __init__(self, root):
    # Define el metodo __init__, el raiz de todo lo que se va a mostrar en la app, es parecido a "body" de html 
        self.root = root
        # Define la variable root, que es igual a root, es decir, el raiz de la app
        self.root.title("Bunscador de Pokemon")
        # Define el titulo de la app
        self.root.geometry("400x600")
        # Define el tamaño de la app
        # self.root.resizable(False, False)
        # Si no quieres que la app se pueda redimensionar, puedes descomentar esta linea

        self.logo_frame = ttk.Frame(root)
        # Crear un contenedor para el logo, es parecido a un div en html
        self.logo_frame.pack(pady=20, padx=20)
        # Su ubicacion

        self.logo_url = "https://pngimg.com/uploads/pokemon_logo/pokemon_logo_PNG5.png"
        # URL de la imagen del logo, es parecido a un src en html
        self.logo_image = Image.open(BytesIO(requests.get(self.logo_url).content))
        # Consigue la imagen del logo y convertirla de binario a texto
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        # Convertir la imagen en un objeto que tkinter puede manejar

        # Configurar el logo
        width = 200
        aspect_ratio = self.logo_image.height / self.logo_image.width
        # Define el ancho de la imagen, y el aspect ratio, es el ratio de alto a ancho de la imagen
        height = int(width * aspect_ratio)
        # Define el alto de la imagen, es el ancho multiplicado por el aspect ratio
        self.logo_image = self.logo_image.resize((width, height))
        # Redimensiona la imagen, es el objeto imagen, y el tamaño que se quiere
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        # Convertir la imagen en un objeto que tkinter puede manejar
        
        self.logo_label = ttk.Label(self.logo_frame, image=self.logo_photo)
        # Mostrar la imagen del logo en la app
        self.logo_label.pack()
        # Su ubicacion

        self.logo_label.bind("<Button-1>", self.open_pokemon_website)
        # Funcion para abrir la pagina web de pokemon cuando se haga click en el logo

        # PARTE DE LA BUSQUEDA
        self.search_frame = ttk.Frame(root)
        # Crear el contenedor de la busqueda
        self.search_frame.pack(pady=20, padx=20)
        # Ubicar el contenedor de la busqueda en la app, es parecido a "position: absolute;" y "margin: 20px 20px;" en css
        
        self.search_entry = ttk.Entry(self.search_frame, width=30)
        # Crear una entrada de texto para buscar el pokemon, es parecido a un input en html con css de width 30
        self.search_entry.pack(side=tk.LEFT, padx=5)
        # Ubicar la entrada de texto en el contenedor de la busqueda, es parecido a "position: absolute;" y "padding-left: 5px;" en css

        self.search_button = ttk.Button(self.search_frame, text="¡Getto daze!", command=self.search_pokemon)
        # Crear un boton para buscar el pokemon, es parecido a un button en html con value "¡Getto daze!" 
        # y un evento "command" que llama a la funcion search_pokemon, parecerse a "onclick" 
        # a llamar a una funcion de javascript en html
        self.search_button.pack(side=tk.LEFT, padx=5)
        # Su ubicacion

        # PARTE DE LA INFORMACION
        self.info_frame = ttk.Frame(root)
        # Crear el contenedor de la informacion
        self.info_frame.pack(pady=10, padx=20)
        # Su ubicacion
        self.image_label = ttk.Label(self.info_frame)
        # Crear una etiqueta para mostrar la imagen del pokemon
        self.image_label.pack()
        # Su ubicacion, aqui no se ha aplicado nada

        self.info_label = ttk.Label(self.info_frame, text="Por favor introduce un nombre de pokemon",wraplength=350,justify=tk.LEFT)
        # Crear una etiqueta para mostrar la informacion del pokemon, con un texto por defecto, como el usuario no ha 
        # introducido nada, y con un wraplength de 350, para que el texto no se salga de la pantalla, y con un justify
        # de left, para que el texto se alinee a la izquierda, 
        # parecerse a "max-width" o "white-space" y "text-align: left;" en css
        self.info_label.pack(pady=10)

    #Funcion para abrir la pagina web de pokemon
    def open_pokemon_website(self, event):
        webbrowser.open("https://www.pokemon.com/es")
        # Abre la pagina web de pokemon en el navegador predeterminado del sistema

    # Definir la funcion de buscar el pokemon
    def search_pokemon(self):
        pokemon_name = self.search_entry.get().lower()
        # Obtener el nombre del pokemon que el usuario ha introducido y convertirlo a minusculas
        if not pokemon_name:
        # Si no se ha introducido el nombre del pokemon, 
            messagebox.showwarning("¡Por favor, introduce el nombre del Pokémon!")
            # muestra una ventana de advertencia 
            return
            # y devuelve
            
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        # La enlace para obtener la informacion del pokemon, un ejemplo: "https://pokeapi.co/api/v2/pokemon/pikachu"
        
        try:
        # "try" es un metodo de python para manejar errores, si ocurre un error, 
        # se ejecuta el "except" en lugar de parar la ejecucion del programa
            response = requests.get(url)
            # Enviar una solicitud GET a la URL para obtener los datos del Pokémon por el modulo "requests"
            if response.status_code == 200:
            # "status_code 200" significa que la solicitud fue exitosa, entonces si la solicitación fue exitosa,
            # sigue ejecutando el codigo ensequida
                data = response.json()
                # Reproduce la resulta de resspuesta en formato json

                # Mostrar la imagen del Pokémon
                sprite_url = data['sprites']['front_default']
                # Conseguir la URL de la imagen del Pokémon por buscar las palabras clave 
                image_response = requests.get(sprite_url)
                # Conseguir la imagen del Pokémon por enviar una solicitud GET a la URL de la imagen
                # Debido a requests.get() devuelve imagen en binario,
                image = Image.open(BytesIO(image_response.content))
                # tiene que convertirlo en una imagen de python por el modulo "BytesIO" e "Image"
                photo = ImageTk.PhotoImage(image)
                # Convertir la imagen en un objeto de imagen de tkinter por el modulo "ImageTk"
                self.image_label.configure(image=photo)
                # Pasar la imagen al label
                self.image_label.image = photo
                # Denuciar la imagen esta siendo usada,
                # porque solamente hemos pasado la imagen al label, 
                # pero no ha sido llamada en ningun parte de python para que sepa que la imagen esta siendo usada,
                # y python elimina automaticamente los objetos que no estan siendo usados para ahorar memoria.
                
                # Rellenar informacion del Pokémon
                name = data['name'].capitalize()
                pokemon_id = data['id']
                height = data['height'] / 10
                weight = data['weight'] / 10
                types = [t['type']['name'] for t in data['types']]
                
                info_text = f"Nombre: {name}\n"
                info_text += f"ID: {pokemon_id}\n"
                info_text += f"Altura: {height}m\n"
                info_text += f"Peso: {weight}kg\n"
                info_text += f"Tipo(s): {', '.join(types)}"
                
                self.info_label.configure(text=info_text)
                # Rellenar la informacion del Pokémon en el label
                
            else:
                messagebox.showerror("error", f"No ha encontrado el Pokémon  '{pokemon_name}'")
                # Si no se ha podido encontrar ningun registro correspondiente, devuelve un mensaje de error
                
        except requests.exceptions.RequestException as e:
            messagebox.showerror("error", f"Ocurrio un error a obtener datos: {e}")
            # Si hay un error al enviar la solicitud, por ejemplo fatal de conexion, devuelve un mensaje de error

# Definir una funcion para ejecutar la app InfoPokemon
def main():
    root = tk.Tk()
    app = InfoPokemon(root)
    root.mainloop()
    # root.mainloop() es para que la ventana se mantenga abierta hasta que el usuario la cierre

if __name__ == "__main__":
    main()
# El bloque 'if __name__ == "__main__":' asegura que el programa solo se ejecute cuando se ejecuta directamente,
# permitiendo que se importe como un módulo sin que se ejecute automáticamente. Esto mejora la modularidad y 
# escalabilidad del código.
# Por ejemplo:
# Si se añade un botón en otra aplicación para acceder a esta función de consulta de Pokémon, 
# el programa solo se ejecutará cuando el usuario haga clic, garantizando que no se ejecute automáticamente.


```

### Instrucciones de uso:

1. Ejecuta el script.
2. Ingresa el nombre del Pokémon en el cuadro de texto.
3. Haz clic en el botón "¡Getto daze!".
4. Verás la imagen y la información del Pokémon en la interfaz gráfica.
5. Puede acceder al sitio web oficial (Español) haciendo clic en el logo de Pokémon.

---

## Conclusión

Este programa es un sencillo buscador de Pokémon que utiliza la API de Pokémon para obtener información en tiempo real sobre cualquier Pokémon que se busque. Ofrece una interfaz gráfica fácil de usar y proporciona detalles como el nombre, ID, altura, peso, tipo y la imagen del Pokémon.

## Referencias

- [API de Pokémon](https://pokeapi.co/)
- [Documentación de Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Documentación de Requests](https://docs.python-requests.org/en/latest/index.html)
- [Documentación de Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)




