import statistics


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
char_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def main():
    lines = get_input('input.txt')
    all_line_points = []
    for line in lines:
        start_chars = []
        illegal_char = None

        for index, char in enumerate(line):
            # print(char)
            if char in opening_chars:
                start_chars.append(char)
            else:
                if char != char_pairs[start_chars[-1]]:
                    illegal_char = char
                    break
                else:
                    start_chars.pop()

        if not illegal_char:
            line_points = 0
            for leftover_char in reversed(start_chars):
                line_points *= 5
                line_points += char_points[char_pairs[leftover_char]]
            all_line_points.append(line_points)

    winner = statistics.median(all_line_points)
    print(f"The winning score is {winner}")


if __name__ == "__main__":
    main()
