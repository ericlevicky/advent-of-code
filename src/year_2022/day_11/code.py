import os

COMFORT_LEVEL = 3


class Monkey:
    def __init__(
        self,
        monkey_index: int,
        starting_items: list[int],
        operation: str,
        test_int: int,
        true_monkey: int,
        false_monkey: int,
    ):
        self.monkey_index = monkey_index
        self.starting_items = starting_items
        self.operation = operation.replace("/", "//")
        self.test = test_int
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def take_turn(self, part_two: bool = False):
        for i in range(0, len(self.starting_items)):
            item = self.starting_items.pop(0)

            # inspect
            temp_item = self.__perform_operation(item)
            ACTIVITIES[self.monkey_index] += 1
            # relief
            if part_two is False:
                temp_item = temp_item // COMFORT_LEVEL
            else:
                temp_item %= DIVISOR

            # test
            if self.__perform_test(temp_item):
                MONKIES[self.true_monkey].starting_items.append(temp_item)
            else:
                MONKIES[self.false_monkey].starting_items.append(temp_item)

        MONKIES[self.monkey_index].starting_items = []

    def __perform_test(self, item: int) -> bool:
        if item % self.test == 0:
            return True
        return False

    def __perform_operation(self, item: int) -> int:
        old = item
        new = eval(self.operation)
        return new


MONKIES: dict[int, Monkey] = {}
ACTIVITIES: list[int] = []
DIVISOR: int = 1


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    rounds = 20 if part_two is False else 10000

    global ACTIVITIES
    global DIVISOR

    curr_monkey: int = -1
    for i, line in enumerate(all_lines):
        values_only = line.strip("\n")

        if values_only.startswith("Monkey "):
            curr_monkey = int(values_only.strip(":").replace("Monkey ", ""))
        elif values_only.startswith("  Starting items: "):
            starting_items = [
                int(i)
                for i in values_only.replace("  Starting items: ", "").split(", ")
            ]
        elif values_only.startswith("  Operation: new = "):
            operation = values_only.replace("  Operation: new = ", "")
        elif values_only.startswith("  Test: divisible by "):
            test = int(values_only.replace("  Test: divisible by ", ""))
        elif values_only.startswith("    If true: throw to monkey "):
            true_monkey = int(values_only.replace("    If true: throw to monkey ", ""))
        elif values_only.startswith("    If false: throw to monkey "):
            false_monkey = int(
                values_only.replace("    If false: throw to monkey ", "")
            )
            MONKIES[curr_monkey] = Monkey(monkey_index=curr_monkey, starting_items=starting_items, operation=operation, test_int=test, true_monkey=true_monkey, false_monkey=false_monkey)  # type: ignore

    ACTIVITIES = [0 for _ in MONKIES]
    DIVISOR = 1
    for monkey in MONKIES:
        DIVISOR *= MONKIES[monkey].test

    for r in range(0, rounds):
        for monkey in range(0, len(MONKIES)):
            MONKIES[monkey].take_turn(part_two=part_two)  # type: ignore

    ACTIVITIES.sort()

    return ACTIVITIES[-1] * ACTIVITIES[-2]
