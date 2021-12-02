def get_input(filepath):
    problem_input = []
    with open(filepath) as f:
        for line in f:
            problem_input.append(line.strip().split(' '))

    return problem_input


def main():
    commands = get_input('input1.txt')
    depth = 0
    horizontal_position = 0

    for command in commands:
        match command:
            case ["forward", units]:
                horizontal_position += int(units)
            case ["down", units]:
                depth += int(units)
            case ["up", units]:
                depth -= int(units)

        print(horizontal_position)
        print(depth)
        print("\n")

    print(f"Final horizontal position: {horizontal_position}")
    print(f"Final depth: {depth}")
    print(f"Position product (horizontal position * depth): {horizontal_position * depth}")


if __name__ == "__main__":
    main()
