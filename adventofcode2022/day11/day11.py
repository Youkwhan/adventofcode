# darn monkeys playing with my missing items!
# we need to predict where the monkeys will throw.
# They opeerate based on how worried I am of each item

# MONKEY FUNCTION:
# starting items: is my worry level
# Operation: is how my worry level changes as the monkey inspects
# (BEFORE TEST): relief => int(worrylevel / 3) nearest integer
# Test: is how the monkey decides based on my worry level

# Rounds: Each monkey taks a single turn
# Signle turn: each monkey throws all their items one at a time before the next monkey continues

# Recieveing:
# items goes to the end of the recipient list.
# if monkey has no items end turn.

# RETURN
# OVER 20 ROUNDS
# count the number of times each monkey inspects items
# FIND THE total monkey business = two most active monkeys count (multiplied)

# SOlution:
# class: Monkey(var:starting_items, var:inspection, func:operation, func:test)
# ds:

# we are going to parse by monkey and create a list of monkeys
# where the list = single round of monkyes
from __future__ import annotations
from typing import List
from math import floor


class Item:
    def __init__(self, worry_level) -> None:
        self.worry_level = worry_level

    def __repr__(self):
        return f"{self.worry_level}"

    def __str__(self):
        return f"{self.worry_level}"

    def adjust_item_worry_level(self) -> None:
        self.worry_level = floor(self.worry_level / 3)

    def adjust_item_worryless(self, monkeys_input_multiple) -> None:
        self.worry_level %= monkeys_input_multiple


class Monkey:
    def __init__(
        self,
        starting_items: list[int],
        operations: tuple[str, str],
        test_value: int,
        true_throw_target: int,
        false_throw_target: int,
        is_worryless: bool = False,
    ) -> None:
        self.items = [Item(worry_level) for worry_level in starting_items]
        self.operator = operations[0]
        self.operator_input_value = operations[1]
        self.test_value = test_value
        self.true_throw_target = true_throw_target
        self.false_throw_target = false_throw_target
        self.inspection_count = 0
        self.is_worryless = is_worryless

    def __repr__(self):
        return f"{self.__class__.__name__} items={self.items} inspection_count={self.inspection_count}"

    def __str__(self):
        return f"items={self.items} inspection_count={self.inspection_count}"

    def __lt__(self, other: Monkey) -> bool:
        return self.inspection_count < other.inspection_count

    def inspect_items(self) -> None:
        for item in self.items:
            self.perform_item_inspection_operation(item)
            if not self.is_worryless:
                item.adjust_item_worry_level()
            self.inspection_count += 1

    def adjust_worry_with_multiples(self, monkeys_input_multiple: int) -> None:
        if self.is_worryless:
           for item in self.items:
                item.adjust_item_worryless(monkeys_input_multiple)

    def perform_item_inspection_operation(self, item: Item) -> None:
        operator_input_value = (
            self.operator_input_value
            if self.operator_input_value != "old"
            else str(item.worry_level)
        )
        item.worry_level = eval(
            str(item.worry_level) + self.operator + operator_input_value
        )

    def perform_item_test_and_toss(self) -> list[tuple(int, list[Item])]:
        true_tossed_items = []
        false_tossed_items = []
        for item in self.items:
            if item.worry_level % self.test_value == 0:
                true_tossed_items.append(item)
            else:
                false_tossed_items.append(item)
        self.items = []
        return [
            (self.true_throw_target, true_tossed_items),
            (self.false_throw_target, false_tossed_items),
        ]

    def recieve_items(self, items: list[Item]):
        self.items.extend(items)


class MonkeySimulator:
    def __init__(self, monkeys: List(Monkey), monkeys_input_multiple:int = 1) -> None:
        self.monkeys = monkeys
        self.monkeys_input_multiple = monkeys_input_multiple

    def simulate_round(self, num_rounds: int) -> None:
        for _ in range(num_rounds):
            for monkey in self.monkeys:
                monkey.inspect_items()
                #adjust the item level for part 2
                monkey.adjust_worry_with_multiples(self.monkeys_input_multiple)

                tossed_items = monkey.perform_item_test_and_toss()
                true_toss_monkey_idx, true_tossed_items = tossed_items[0]
                false_toss_monkey_idx, false_tossed_items = tossed_items[1]
                self.monkeys[true_toss_monkey_idx].recieve_items(true_tossed_items)
                self.monkeys[false_toss_monkey_idx].recieve_items(false_tossed_items)

    def get_product_of_most_active_monkeys(self) -> int:
        self.monkeys.sort(reverse=True)
        monkey1_inspection_count = self.monkeys[0].inspection_count
        monkey2_inpsection_count = self.monkeys[1].inspection_count
        return monkey1_inspection_count * monkey2_inpsection_count


class MonkeyListGenerator:
    @staticmethod
    def generate_monkey_list(
        input: str, is_worryless: bool = False
    ) -> tuple(list[Monkey], int):
        with open(input) as data:
            monkey_list = []
            monkey_common_multiple = 1
            parsed_input = data.read().split("\n\n")
            for monkey in parsed_input:
                genereated_monkey = MonkeyListGenerator.parse_monkey(
                    monkey, is_worryless
                )
                monkey_common_multiple *= genereated_monkey.test_value
                monkey_list.append(genereated_monkey)
            return (monkey_list, monkey_common_multiple)

    @staticmethod
    def parse_monkey(monkey: str, is_worryless: bool = False) -> Monkey:
        monkey = monkey.split("\n")
        starting_item = [
            int(item) for item in monkey[1].strip().split(":")[1].split(",")
        ]
        operation_parsed = monkey[2].strip().split(":")[1].split(" ")
        operation = (operation_parsed[-2], operation_parsed[-1])
        test_value = int(monkey[3].strip().split(":")[1].split(" ")[-1])
        true_throw_target = int(monkey[4].strip().split(":")[1].split(" ")[-1])
        false_throw_target = int(monkey[5].strip().split(":")[1].split(" ")[-1])
        return Monkey(
            starting_item,
            operation,
            test_value,
            true_throw_target,
            false_throw_target,
            is_worryless,
        )


def part_one(monkey_list: list[Monkey]) -> None:
    monkey_sim = MonkeySimulator(monkey_list)
    monkey_sim.simulate_round(20)
    print(monkey_sim.get_product_of_most_active_monkeys())


def part_two(monkey_list: list[Monkey], input_monkey_multiple: int) -> None:
    monkey_sim = MonkeySimulator(monkey_list, input_monkey_multiple)
    monkey_sim.simulate_round(10000)
    print(monkey_sim.get_product_of_most_active_monkeys())


if __name__ == "__main__":
    worried_monkey_list, worried_monkey_multiple = MonkeyListGenerator.generate_monkey_list(
        "input.txt"
    )
    worryless_monkey_list, worryless_monkey_multiple = MonkeyListGenerator.generate_monkey_list(
        "input.txt", True
    )
    part_one(worried_monkey_list)
    part_two(worryless_monkey_list, worryless_monkey_multiple)