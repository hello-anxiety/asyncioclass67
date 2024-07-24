import time
import asyncio

my_computer_time = 0.1
opponent_computer_time = 0.5
opponents = 24
move_pairs = 30

async def game(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_computer_time)
        print(f"BOARD-{x+1} {i+1} Judit mode a move.")
        await asyncio.sleep(opponent_computer_time)
        print(f"BOARD-{x+1} {i+1} Opponent made move.")
    board_time = round(time.perf_counter() - board_start_time)
    print(f"BOAED-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {board_time,} sec\n")
    return board_time 
  
async def main():
    start_time = time.perf_counter()
    tasks = [game(board) for board in range(opponents)]
    board_time = await asyncio.gather(*tasks)
    total_board_time = sum(board_time)
 
    print(f"Board exhibition finished in {total_board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)}")

if __name__ == "__main__":
    asyncio.run(main())