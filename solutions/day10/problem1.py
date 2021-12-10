def get_input(filepath):
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append([char for char in line.strip()])

    return lines


opening_chars = ['(', '<', '[', '{']
closing_chars = [')', '>', ']', '}']
char_pairs = {
    '(': ')',
    '{': '}',
    '<': '>',
    '[': ']',
}
illegal_char_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def main():
    lines = get_input('input.txt')
    illegal_chars = []
    for line in lines:
        start_chars = []

        for index, char in enumerate(line):
            # print(char)
            if char in opening_chars:
                start_chars.append(char)
            else:
                if char != char_pairs[start_chars[-1]]:
                    illegal_chars.append(char)
                    break
                else:
                    start_chars.pop()



    points = [illegal_char_points[char] for char in illegal_chars]
    total_points = sum(points)
    print(f"Total points: {total_points}")


if __name__ == "__main__":
    main()
