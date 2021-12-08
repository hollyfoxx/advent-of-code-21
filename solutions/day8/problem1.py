# num segments: digit
num_segments: {
    2: 1,
    3: 7,
    4: 4,
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: 8,
}

unique_lengths = [2, 3, 4, 7]


def get_input(filepath):
    entries = []
    with open(filepath) as f:
        for line in f:
            wiring, output = line.strip().split(' | ')
            entries.append((wiring.split(' '), output.split(' ')))

    return entries


def main():
    entries = get_input('input.txt')

    unique_digits = 0
    for wiring, output in entries:
        for digit_representation in output:
            if len(digit_representation) in unique_lengths:
                unique_digits += 1

    print(f"There are {unique_digits} unique digits in the output values.")


if __name__ == "__main__":
    main()
