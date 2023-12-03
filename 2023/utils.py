import os
import requests

def save_input(day, year=2022):
    if not os.path.exists(f"day_{day}input.txt"):
        input_url = f"https://adventofcode.com/2022/{year}/{day}/input"
    with open("input.txt", "w") as f:
        f.write(requests.get(input_url, cookies={"session": os.environ["AOC_SESSION"]}).text)
        