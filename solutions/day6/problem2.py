def get_input(filepath):
    with open(filepath) as f:
        current_fish = f.read().strip().split(',')

    return current_fish


def main():
    starting_fish = get_input('input.txt')
    days = {}
    for i in range(0, 256):
        days[i] = 0

    for fish in starting_fish:
        fish_age = int(fish)
        for i in range(fish_age, len(days), 7):
            days[i] += 1

    for day in days:
        if day + 9 in days:
            days[day + 9] += days[day]
            for i in range(day + 16, len(days), 7):
                if i in days:
                    days[i] += days[day]

    print(f"Total fish: {sum(days.values()) + len(starting_fish)}")


if __name__ == "__main__":
    main()
