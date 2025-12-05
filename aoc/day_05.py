import fileinput
from itertools import dropwhile, takewhile
from operator import attrgetter


def main():
    puzzle_input: list[str] = list(filter(None, map(str.rstrip, fileinput.input())))
    fresh_ranges: list[range] = list(map(parse_fresh_range, takewhile(lambda s: '-' in s, puzzle_input)))
    ingredient_ids: list[int] = list(map(int, dropwhile(lambda s: '-' in s, puzzle_input)))

    print(part_1(fresh_ranges, ingredient_ids))
    print(part_2(fresh_ranges))


def parse_fresh_range(raw_range: str) -> range:
    start, stop = raw_range.split('-')

    return range(int(start), int(stop) + 1)


def part_1(fresh_ranges: list[range], ingredient_ids: list[int]) -> int:
    return sum(any(ingredient_id in fresh_range for fresh_range in fresh_ranges)
               for ingredient_id in ingredient_ids)


def part_2(fresh_ranges: list[range]) -> int:
    fresh_ranges = sorted(fresh_ranges, key=attrgetter('start'), reverse=True)
    fresh_ingredients = 0

    while fresh_ranges:
        fresh_range = fresh_ranges.pop()

        while fresh_ranges and fresh_ranges[-1].start in fresh_range:
            fresh_range = range(fresh_range.start, max(fresh_range.stop, fresh_ranges[-1].stop))
            del fresh_ranges[-1]

        fresh_ingredients += len(fresh_range)

    return fresh_ingredients


if __name__ == '__main__':
    main()
