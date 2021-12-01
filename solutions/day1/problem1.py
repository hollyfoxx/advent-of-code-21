def get_input(filepath):
    problem_input = []
    with open(filepath) as f:
        for line in f:
            number = int(line.strip())
            problem_input.append(number)

    return problem_input


def main():
    depth_readings = get_input('input1.txt')
    increases = 0
    decreases = 0

    for index, current_reading in enumerate(depth_readings):
        if index == 0:
            continue

        if current_reading > depth_readings[index - 1]:
            increases += 1
            print(f"{current_reading} (increased)")

        elif current_reading < depth_readings[index - 1]:
            decreases += 1
            print(f"{current_reading} (decreased)")

        else:
            print(f"{current_reading} (no change)")

    print(f"Increased {increases} times")
    print(f"Decreased {decreases} times")


if __name__ == "__main__":
    main()
