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