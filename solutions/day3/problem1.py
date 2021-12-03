from statistics import mode


def get_input(filepath):
    with open(filepath) as f:
        problem_input = f.read().splitlines()

    return problem_input


def columnize(string_list):
    columns = []

    for index, string in enumerate(string_list):
        for i in range(0, len(string)):
            if index == 0:
                columns.append([string[i]])
            else:
                columns[i].append(string[i])

    return columns


def main():
    binary_strings = get_input('input1.txt')
    columns = columnize(binary_strings)

    gamma_digits = []
    epsilon_digits = []

    for i in range(0, len(columns)):
        gamma_digit = mode(columns[i])
        epsilon_digit = "0" if gamma_digit == "1" else "1"

        gamma_digits.append(gamma_digit)
        epsilon_digits.append(epsilon_digit)

    gamma_string = "".join(gamma_digits)
    epsilon_string = "".join(epsilon_digits)

    print(f"gamma rate binary: {gamma_string}")
    print(f"gamma rate decimal: {int(gamma_string, 2)}")
    print(f"epsilon rate binary: {epsilon_string}")
    print(f"epsilon rate decimal: {int(epsilon_string, 2)}")

    print(f"power consumption (gamma * epsilon) = {int(gamma_string, 2) * int(epsilon_string, 2)}")


if __name__ == "__main__":
    main()
