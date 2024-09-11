import asyncio
import httpx

async def fetch_pokemon(client, url):
    response = await client.get(url)
    return response.json()

async def get_pokemons():
    url = "https://pokeapi.co/api/v2/ability/battle-armor/"
    async with httpx.AsyncClient() as client:
        # Retrieve the initial list of Pokémon
        data = await fetch_pokemon(client, url)
        pokemon_urls = [data['results'][i]['url'] for i in range(10)]  # Get URLs for 10 Pokémon
        
        tasks = [fetch_pokemon(client, url) for url in pokemon_urls]
        pokemons = await asyncio.gather(*tasks)
        return pokemons

async def main():
    pokemons = await get_pokemons()
    for pokemon in pokemons:
        print(pokemon['name'])

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
