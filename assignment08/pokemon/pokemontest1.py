import aiofiles
import asyncio
import json

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    # Read the contents of the json file 
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode='r') as f:
        contents = await f.read()

    # Load it into a dicrectory and create a list of move
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move ['move']['name'] for move in pokemon['moves']]
    
    # Open a new file to write the list of move into.
    async with aiofiles.open(f"{pokemonmove_directory}/{name}_move.txt", mode='w') as f:
        await f.write('\n'.join(moves))
    
asyncio.run(main())