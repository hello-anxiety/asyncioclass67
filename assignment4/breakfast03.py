# Asynchronous breakfast
import asyncio
from time import sleep, time


async def make_coffee():
    print("coffee:prapare ingridients")
    sleep(1)
    print("coffee: waiting.....")
    await asyncio.sleep(5)
    print("coffee: ready")

async def fry_egg():
    print("egg: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)
    print("eggs: ready")

async def main():
    start = time()
    coffee_task = asyncio.create_task(make_coffee())
    eggs_task = asyncio.create_task(fry_egg())
    await coffee_task
    await eggs_task
    print(f"breakfast is ready in {time()-start} min")


asyncio.run(main())
