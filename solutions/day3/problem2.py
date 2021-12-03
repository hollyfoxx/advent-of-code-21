from statistics import multimode


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


def filter_columns_by_common_bits(binary_strings, columns, keep_mode, fallback_digit):
    for i in range(0, len(columns)):
        if len(binary_strings) == 1:
            return binary_strings[0]

        columns = columnize(binary_strings)
        most_common_digit = multimode(columns[i])

        if len(most_common_digit) == 1:
            most_common_digit = most_common_digit[0]
        else:
            binary_strings = list(filter(lambda binary_string: binary_string[i] == fallback_digit, binary_strings))
            continue

        if keep_mode:
            binary_strings = list(filter(lambda binary_string: binary_string[i] == most_common_digit, binary_strings))
        else:
            binary_strings = list(filter(lambda binary_string: binary_string[i] != most_common_digit, binary_strings))


def main():
    binary_strings = get_input('input1.txt')
    columns = columnize(binary_strings)

    oxygen_generator_rating = filter_columns_by_common_bits(binary_strings, columns, True, '1')
    co2_scrubber_rating = filter_columns_by_common_bits(binary_strings, columns, False, '0')

    print(f"oxygen_generator_rating binary: {oxygen_generator_rating}")
    print(f"oxygen_generator_rating rate decimal: {int(oxygen_generator_rating, 2)}")
    print(f"co2_scrubber_rating binary: {co2_scrubber_rating}")
    print(f"co2_scrubber_rating rate decimal: {int(co2_scrubber_rating, 2)}")

    print(
        f"life support rating (oxygen_generator_rating * co2_scrubber_rating) = {int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)}")


if __name__ == "__main__":
    main()
