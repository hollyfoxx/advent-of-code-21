def get_input(filepath):
    problem_input = []
    with open(filepath) as f:
        for line in f:
            number = int(line.strip())
            problem_input.append(number)

    return problem_input


def consolidate_ints(original_list):
    consolidated_list = []
    for i in range(0, len(original_list)):
        if i == len(original_list) - 2:
            return consolidated_list

        group_sum = original_list[i] + original_list[i + 1] + original_list[i + 2]
        consolidated_list.append(group_sum)

    return consolidated_list


def main():
    depth_readings = get_input('input1.txt')
    consolidated_depth_readings = consolidate_ints(depth_readings)

    increases = 0
    decreases = 0

    for index, current_reading in enumerate(consolidated_depth_readings):
        if index == 0:
            continue

        if current_reading > consolidated_depth_readings[index - 1]:
            increases += 1
            print(f"{current_reading} (increased)")

        elif current_reading < consolidated_depth_readings[index - 1]:
            decreases += 1
            print(f"{current_reading} (decreased)")

        else:
            print(f"{current_reading} (no change)")

    print(f"Increased {increases} times")
    print(f"Decreased {decreases} times")


if __name__ == "__main__":
    main()
