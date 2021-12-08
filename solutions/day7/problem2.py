import statistics


def get_input(filepath):
    with open(filepath) as f:
        i = [int(num) for num in f.read().strip().split(',')]

    return i


def cost_fuel(start, end):
    fuel = 0
    for i in range(1, abs(start - end) + 1):
        fuel += i
    return fuel


def main():
    horizontal_positions = get_input('input.txt')
    optimal_position = 0

    # I am aware this is an extremely slow implementation
    min_total_fuel = None
    for i in range(0, max(horizontal_positions)):
        fuel = 0
        for pos in horizontal_positions:
            fuel += cost_fuel(pos, i)
        if min_total_fuel is None:
            optimal_position = i
            min_total_fuel = fuel
        elif fuel < min_total_fuel:
            optimal_position = i
            min_total_fuel = fuel

    print(f"Optimal horizontal position: {optimal_position}")
    print(f"Total used fuel: {min_total_fuel}")


if __name__ == "__main__":
    main()
