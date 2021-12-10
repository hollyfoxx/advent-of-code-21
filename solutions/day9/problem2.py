def get_input(filepath):
    rows = []
    with open(filepath) as f:
        for line in f:
            rows.append([int(char) for char in line.strip()])

    return rows


seen_points = []


def get_basin_size(height_map, starting_point):
    start_x, start_y = starting_point
    num = height_map[start_y][start_x]
    seen_points.append(starting_point)
    new_points = [starting_point]

    # get ups
    if not start_y == 0:
        if height_map[start_y - 1][start_x] > num and height_map[start_y - 1][start_x] != 9 and (
                start_x, start_y - 1) not in seen_points:
            seen_points.append((start_x, start_y - 1))
            new_points.append((start_x, start_y - 1))
            new_points.extend(get_basin_size(height_map, (start_x, start_y - 1)))

    # get downs
    if not start_y == len(height_map) - 1:
        if height_map[start_y + 1][start_x] > num and height_map[start_y + 1][start_x] != 9 and (
                start_x, start_y + 1) not in seen_points:
            seen_points.append((start_x, start_y + 1))
            new_points.append((start_x, start_y + 1))
            new_points.extend(get_basin_size(height_map, (start_x, start_y + 1)))

    # get lefts
    if not start_x == 0:
        if height_map[start_y][start_x - 1] > num and height_map[start_y][start_x - 1] != 9 and (
                start_x - 1, start_y) not in seen_points:
            seen_points.append((start_x - 1, start_y))
            new_points.append((start_x - 1, start_y))
            new_points.extend(get_basin_size(height_map, (start_x - 1, start_y)))

    # get rights
    if not start_x == len(height_map[0]) - 1:
        if height_map[start_y][start_x + 1] > num and height_map[start_y][start_x + 1] != 9 and (
                start_x + 1, start_y) not in seen_points:
            seen_points.append((start_x + 1, start_y))
            new_points.append((start_x + 1, start_y))
            new_points.extend(get_basin_size(height_map, (start_x + 1, start_y)))

    return set(new_points)


def main():
    height_map = get_input('input.txt')

    basins = []
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
                basins.append(get_basin_size(height_map, (col_index, row_index)))

    basin_sizes = sorted([len(basin) for basin in basins], reverse=True)

    print(f"Top three basin sizes = {basin_sizes[:3]}")
    print(f"Top three sizes multiplied = {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}")


if __name__ == "__main__":
    main()
