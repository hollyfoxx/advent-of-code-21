def get_input(filepath):
    rows = []
    with open(filepath) as f:
        for line in f:
            rows.append([int(char) for char in line.strip()])

    return rows


def main():
    height_map = get_input('input.txt')

    risk_level = 0
    for row_index, row in enumerate(height_map):
        for col_index, num in enumerate(row):
            low_point = True
            # check up
            if not row_index == 0:
                if height_map[row_index - 1][col_index] <= num:
                    low_point = False
            # check left
            if not col_index == 0:
                if row[col_index - 1] <= num:
                    low_point = False
            # check down
            if not row_index == len(height_map) - 1:
                if height_map[row_index + 1][col_index] <= num:
                    low_point = False
            # check right
            if not col_index == len(row) - 1:
                if row[col_index + 1] <= num:
                    low_point = False

            if low_point:
                risk_level += num + 1

    print(f"Overall risk level: {risk_level}")


if __name__ == "__main__":
    main()
