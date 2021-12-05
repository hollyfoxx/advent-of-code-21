def get_input(filepath):
    with open(filepath) as f:
        problem_input = f.read().splitlines()

    return problem_input


def parse_bingo_card_colums(rows):
    cols = []

    for index, row in enumerate(rows):
        if index == 0:
            for num in row:
                cols.append([num])
        else:
            for index_2, num in enumerate(row):
                cols[index_2].append(num)

    return rows, cols


def parse_bingo_cards(input):
    bingo_cards = []

    rows = []
    for i in range(2, len(input)):
        if input[i] == '' or i == len(input) - 1:
            if input[i]:
                rows.append(input[i].split())
            bingo_cards.append(parse_bingo_card_colums(rows))
            rows = []
            continue

        rows.append(input[i].split())

    return bingo_cards


def main():
    problem_input = get_input('input1.txt')
    bingo_numbers = problem_input[0].split(",")
    bingo_cards = parse_bingo_cards(problem_input)

    bingo = False
    winning_card = None
    winning_number = None

    for number in bingo_numbers:
        for index, card in enumerate(bingo_cards):
            for row_index, row in enumerate(card[0]):
                if number in row:
                    row.remove(number)
                    if not row:
                        print("bingo!!!")
                        bingo = True
                        winning_card = index
                        winning_number = number

            for col_index, col in enumerate(card[1]):
                if number in col:
                    col.remove(number)
                    if not col:
                        print("bingo!!!")
                        bingo = True
                        winning_card = index
                        winning_number = number

            if bingo:
                break

        if bingo:
            break

    print(f"Winning card index: {winning_card}")
    print(f"Winning number: {winning_number}")
    unmarked_number_strings = sum(bingo_cards[winning_card][0], [])
    unmarked_numbers = list(map(lambda x: int(x), unmarked_number_strings))
    unmarked_sum = sum(unmarked_numbers)

    print(f"Sum of unmarked numbers on card {winning_card}: {unmarked_sum}")
    print(f"Final score (unmarked sum * winning number): {int(winning_number) * unmarked_sum}")

if __name__ == "__main__":
    main()
