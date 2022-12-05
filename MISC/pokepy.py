#https://github.com/PokeDevs/pokedex.py/wiki

from pokedex import pokedex as p

def poke_api(pokedex):
    chosen_pokemon = input('Enter a pokemon: ')

    pokedex = pokedex.Pokedex()
    pokemon = pokedex.get_pokemon_by_name(chosen_pokemon)

    try:
        a = pokemon[0]
        my_dict = dict(a)

        type = my_dict["types"]
        abilities = my_dict["abilities"]["normal"]

        print(f'Pokemon: {my_dict["name"]}')
        print(f'Species: {my_dict["species"]}')
        print(f'Type: {type[0]}')
        print(f'Abilities: {abilities[0]}')

    except KeyError:
        print('Invalid pokemon!')
        poke_api()

poke_api(p)