# num segments: digit
num_segments = {
    2: 1,
    3: 7,
    4: 4,
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: 8,
}

unique_lengths = [2, 3, 4, 7]

base_key = {
    0: None,
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
}


def get_input(filepath):
    entries = []
    with open(filepath) as f:
        for line in f:
            wiring, output = line.strip().split(' | ')
            entries.append((wiring.split(' '), output.split(' ')))

    return entries


def main():
    entries = get_input('input.txt')

    all_output_values = []
    for wiring, output in entries:
        num_to_letters = base_key
        letters_to_num = {}
        five_digits = []
        six_digits = []
        for digit_representation in wiring:
            if len(digit_representation) in unique_lengths:
                num_to_letters[num_segments[len(digit_representation)]] = digit_representation
                letters_to_num[digit_representation] = num_segments[len(digit_representation)]
            elif len(digit_representation) == 5:
                five_digits.append(digit_representation)
            elif len(digit_representation) == 6:
                six_digits.append(digit_representation)

        five_digits = set(five_digits)
        # Find the 'three'
        for five in five_digits:
            if set(five).intersection(set(num_to_letters[1])) == set(num_to_letters[1]):
                num_to_letters[3] = five
                letters_to_num[five] = 3
        five_digits.remove(num_to_letters[3])
        # Find the 'five'
        for five in five_digits:
            if len(set(five).intersection(set(num_to_letters[4]))) == 3:
                num_to_letters[5] = five
                letters_to_num[five] = 5
        five_digits.remove(num_to_letters[5])
        five_digits = list(five_digits)
        # The 'two' is leftover
        num_to_letters[2] = five_digits[0]
        letters_to_num[five_digits[0]] = 2

        six_digits = set(six_digits)
        # Find the 'nine'
        for six in six_digits:
            if set(six).intersection(set(num_to_letters[4])) == set(num_to_letters[4]):
                num_to_letters[9] = six
                letters_to_num[six] = 9
        six_digits.remove(num_to_letters[9])
        # Find the 'zero'
        for six in six_digits:
            if set(six).intersection(set(num_to_letters[1])) == set(num_to_letters[1]):
                num_to_letters[0] = six
                letters_to_num[six] = 0
        six_digits.remove(num_to_letters[0])
        six_digits = list(six_digits)
        # The 'six' is leftover
        num_to_letters[6] = six_digits[0]
        letters_to_num[six_digits[0]] = 6

        output_string = ''
        for value in output:
            scrambled_key = None
            for key in letters_to_num.keys():
                if set(key) == set(value):
                    scrambled_key = key
            output_string += str(letters_to_num[scrambled_key])

        print(f"{' '.join(wiring)}: {output_string}")
        all_output_values.append(int(output_string))

    print(f"\nSum of all output values: {sum(all_output_values)}")


if __name__ == "__main__":
    main()
