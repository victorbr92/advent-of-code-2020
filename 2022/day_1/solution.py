from utils import save_input

def main():
    save_input(year=2022, day=1)
    with open("input.txt") as f:
        input = f.read()

if __name__ == "__main__":
    main()
