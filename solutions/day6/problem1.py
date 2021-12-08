class Fish:
    def __init__(self, current_timer, cycle_length=8, first_cycle=True):
        self.current_timer = current_timer
        self.cycle_length = cycle_length
        self.first_cycle = first_cycle

    def age_one_day(self, school_of_fish):
        if self.current_timer == 0:
            school_of_fish.append(Fish(8))
            if self.first_cycle:
                self.cycle_length = 6
                self.first_cycle = False
            self.current_timer = self.cycle_length
        else:
            self.current_timer -= 1

    @property
    def timer(self):
        return self.current_timer


def get_input(filepath):
    problem_input = []
    with open(filepath) as f:
        current_fish = f.read().strip().split(',')

    for fish in current_fish:
        problem_input.append(Fish(int(fish), 6, False))

    return problem_input


def main():
    starting_fish = get_input('input.txt')

    print(f"Initial state: {','.join(str(fish.timer) for fish in starting_fish)}")

    for i in range(0, 80):
        starting_fish_copy = starting_fish.copy()
        for fish in starting_fish_copy:
            Fish.age_one_day(fish, starting_fish)
        # print(f"After {i + 1} Day: {','.join(str(fish.timer) for fish in starting_fish)}")

    print(f"Total fish: {len(starting_fish)}")


if __name__ == "__main__":
    main()
