import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response =requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = input("Enter the pokemon name: ").lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"Types: {', '.join([t['type']['name'] for t in pokemon_info['types']])}")
else:
    print("Pokemon not found")

        



