from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):

        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        pokemons_data = '\n'.join(f"- {p.pokemon_details()}" for p in self.pokemons)
        final_print = [f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"]
        final_print.append(pokemons_data)
        return '\n'.join(final_print)