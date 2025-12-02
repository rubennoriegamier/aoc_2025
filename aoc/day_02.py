from collections.abc import Generator, Iterable
from itertools import count


def main():
    ranges: list[range] = list(map(parse_range, input().rstrip().split(',')))

    print(invalid_ids_sum(ranges, part_1_invalid_ids()))
    print(invalid_ids_sum(ranges, part_2_invalid_ids()))


def parse_range(raw_range: str) -> range:
    raw_start, raw_stop = raw_range.split('-')

    return range(int(raw_start), int(raw_stop) + 1)


def part_1_invalid_ids() -> Generator[int]:
    for n in count(1, 2):
        yield from range(10 ** n + 10 ** (n // 2), 10 ** (n + 1), 10 ** (n // 2 + 1) + 1)


def part_2_invalid_ids() -> Generator[int]:
    for digits in count(2):
        invalid_ids = set()

        for chunk_size in range(1, digits // 2 + 1):
            if digits % chunk_size == 0:
                chunks = digits // chunk_size
                fst_invalid_id = int(str(10 ** (chunk_size - 1)) * chunks)
                snd_invalid_id = int(str(10 ** (chunk_size - 1) + 1) * chunks)

                invalid_ids.update(range(fst_invalid_id, 10 ** digits, snd_invalid_id - fst_invalid_id))

        yield from sorted(invalid_ids)


def invalid_ids_sum(ranges: list[range], invalid_ids: Iterable[int]) -> int:
    ranges = sorted(ranges, key=lambda r: r.start, reverse=True)
    sum_ = 0

    for invalid_id in invalid_ids:
        while ranges[-1][-1] < invalid_id:
            del ranges[-1]
            if not ranges:
                return sum_

        if invalid_id in ranges[-1]:
            sum_ += invalid_id

    return sum_


if __name__ == '__main__':
    main()
