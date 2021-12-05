def get_input(filepath):
    with open(filepath) as f:
        problem_input = f.read().splitlines()

    return problem_input


def parse_bingo_card_columns_and_rows(rows):
    cols = []

    for index, row in enumerate(rows):
        # add a new list for each column using ea. digit in the first row
        if index == 0:
            for num in row:
                cols.append([num])

        # build out column lists for remaining rows
        else:
            for index_2, num in enumerate(row):
                cols[index_2].append(num)

    # return bingo card
    # ex. ([[row1], [row2], [[col1], [col2]])
    return rows, cols


def parse_bingo_cards(input):
    bingo_cards = []

    rows = []

    # start at first line of first card
    for i in range(2, len(input)):

        # if the line is a break between cards, or is the last line in input
        if input[i] == '' or i == len(input) - 1:
            # if its the last line of the input, then add the parsed rows
            if input[i]:
                rows.append(input[i].split())

            # generate and add the full bingo card (w/ columns) for the card using the parsed rows
            bingo_cards.append(parse_bingo_card_columns_and_rows(rows))

            # reset the rows and continue
            rows = []
            continue

        # if not the last line of the card/file, add the current row to list of rows
        rows.append(input[i].split())

    return bingo_cards


def main():
    problem_input = get_input('input1.txt')
    bingo_numbers = problem_input[0].split(",")
    bingo_cards = parse_bingo_cards(problem_input)

    winning_cards = []
    winning_card = None
    winning_number = None

    for number in bingo_numbers:
        for index, card in enumerate(bingo_cards):
            if index in winning_cards:
                continue

            # check each row of the card
            for row_index, row in enumerate(card[0]):
                if number in row:
                    row.remove(number)
                    if not row and index not in winning_cards:
                        print(f"bingo!!! on card {index}")
                        winning_cards.append(index)

            # check each column of the card
            for col_index, col in enumerate(card[1]):
                if number in col:
                    col.remove(number)
                    if not col and index not in winning_cards:
                        print(f"bingo!!! on card {index}")
                        winning_cards.append(index)

            if len(winning_cards) == len(bingo_cards):
                winning_card = index
                winning_number = number
                break

        if len(winning_cards) == len(bingo_cards):
            break

    print(f"LAST Winning card index: {winning_card}")
    print(f"LAST Winning number: {winning_number}")
    unmarked_number_strings = sum(bingo_cards[winning_card][0], [])
    unmarked_numbers = list(map(lambda x: int(x), unmarked_number_strings))
    unmarked_sum = sum(unmarked_numbers)

    print(f"Sum of unmarked numbers on card {winning_card}: {unmarked_sum}")
    print(f"Final score (unmarked sum * winning number): {int(winning_number) * unmarked_sum}")

if __name__ == "__main__":
    main()
