import statistics


def get_input(filepath):
    with open(filepath) as f:
        i = [int(num) for num in f.read().strip().split(',')]

    return i


def cost_fuel(start, end):
    return abs(start - end)


def main():
    horizontal_positions = get_input('input.txt')
    median = round(statistics.median(horizontal_positions))
    total_fuel = 0
    for pos in horizontal_positions:
        total_fuel += cost_fuel(pos, median)

    print(f"Optimal horizontal position: {median}")
    print(f"Total used fuel: {total_fuel}")


if __name__ == "__main__":
    main()
