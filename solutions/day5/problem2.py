def get_input(filepath):
    problem_input = []
    with open(filepath) as f:
        for line in f:
            points = line.strip().split(' -> ')
            problem_input.append((points[0].split(','), points[1].split(',')))

    return problem_input


def build_graph(points, lines):
    for line in lines:
        match line:
            case ([x1, y1], [x2, y2]) if int(x1) == int(x2) and int(y2) > int(y1):
                for y in range(int(y1), int(y2) + 1):
                    point = (int(x1), y)
                    points[point] += 1
            case ([x1, y1], [x2, y2]) if int(x1) == int(x2) and int(y1) > int(y2):
                for y in range(int(y2), int(y1) + 1):
                    point = (int(x1), y)
                    points[point] += 1
            case ([x1, y1], [x2, y2]) if int(y1) == int(y2) and int(x2) > int(x1):
                for x in range(int(x1), int(x2) + 1):
                    point = (x, int(y1))
                    points[point] += 1
            case ([x1, y1], [x2, y2]) if int(y1) == int(y2) and int(x1) > int(x2):
                for x in range(int(x2), int(x1) + 1):
                    point = (x, int(y1))
                    points[point] += 1
            case ([x1, y1], [x2, y2]) if int(x2) > int(x1) and int(y2) > int(y1):
                difference = int(x2) - int(x1)
                for i in range(0, difference + 1):
                    point = (int(x1) + i, int(y1) + i)
                    points[point] += 1
            case ([x1, y1], [x2, y2]) if int(x2) < int(x1) and int(y2) > int(y1):
                difference = int(x1) - int(x2)
                for i in range(0, difference + 1):
                    point = (int(x1) - i, int(y1) + i)
                    points[point] += 1
            case ([x1, y1], [x2, y2]) if int(x2) > int(x1) and int(y2) < int(y1):
                difference = int(x2) - int(x1)
                for i in range(0, difference + 1):
                    point = (int(x1) + i, int(y1) - i)
                    points[point] += 1
            case ([x1, y1], [x2, y2]) if int(x2) < int(x1) and int(y2) < int(y1):
                difference = int(x1) - int(x2)
                for i in range(0, difference + 1):
                    point = (int(x1) - i, int(y1) - i)
                    points[point] += 1
            case _:
                continue

    return points


def print_graph(points):
    for i in range(0, 1000):
        row = ''
        for j in range(0, 1000):
            match points[(j, i)]:
                case 0:
                    row += '.'
                case x:
                    row += f"{x}"

        print(f'{row}\n')


def count_hotspots(points):
    hotspots = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if points[(i, j)] > 1:
                hotspots += 1

    return hotspots


def main():
    vent_lines = get_input('input1.txt')

    points = {}
    for i in range(0, 1000):
        for j in range(0, 1000):
            points[(i, j)] = 0

    points = build_graph(points, vent_lines)

    # print_graph(points)
    hotspots = count_hotspots(points)
    print(f"Number of hotspots (points with # overlapping lines >= 2): {hotspots}")


if __name__ == "__main__":
    main()
