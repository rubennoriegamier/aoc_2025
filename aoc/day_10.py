import fileinput
from collections import deque
from operator import methodcaller, xor
from typing import Self

import pulp


def main():
    machines: list[Machine] = list(map(Machine.parse, map(str.rstrip, fileinput.input())))

    print(part_1(machines))
    print(part_2(machines))


class Machine:
    def __init__(self, lights: tuple[bool, ...], buttons: list[tuple[int, ...]], joltages: tuple[int, ...]):
        self._lights = lights
        self._buttons = buttons.copy()
        self._joltages = joltages

    @classmethod
    def parse(cls, raw_value: str) -> Self:
        raw_lights, *raw_buttons, raw_joltages = raw_value.split()
        lights = tuple(char == '#' for char in raw_lights[1:-1])
        buttons = [tuple(map(int, raw_button[1:-1].split(','))) for raw_button in raw_buttons]
        joltages = tuple(map(int, raw_joltages[1:-1].split(',')))

        return cls(lights, buttons, joltages)

    def part_1(self) -> int:
        buttons = [tuple(i in button for i in range(len(self._lights))) for button in self._buttons]
        nodes = deque([(0, (False,) * len(self._lights))])
        min_presses = float('inf')
        visited = set()

        while nodes:
            presses, lights = nodes.popleft()

            if presses < min_presses:
                if lights == self._lights:
                    min_presses = presses
                else:
                    for button in buttons:
                        if (lights_ := tuple(map(xor, lights, button))) not in visited:
                            visited.add(lights_)
                            nodes.append((presses + 1, lights_))

        return int(min_presses)

    def part_2(self) -> int:
        model = pulp.LpProblem()
        buttons = []
        buttons_by_joltage = [[] for _ in range(len(self._joltages))]

        for button in self._buttons:
            buttons.append(pulp.LpVariable(f'button_{len(buttons)}', lowBound=0, cat=pulp.LpInteger))
            for joltage_idx in button:
                buttons_by_joltage[joltage_idx].append(buttons[-1])

        for joltage_idx, joltage_buttons in enumerate(buttons_by_joltage):
            model += pulp.lpSum(joltage_buttons) == self._joltages[joltage_idx]
        model += pulp.lpSum(buttons)
        model.solve(pulp.GLPK(msg=False))

        return round(model.objective.value())


def part_1(machines: list[Machine]) -> int:
    return sum(map(methodcaller('part_1'), machines))


def part_2(machines: list[Machine]) -> int:
    return sum(map(methodcaller('part_2'), machines))


if __name__ == '__main__':
    main()
