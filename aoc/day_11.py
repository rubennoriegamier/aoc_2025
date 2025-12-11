import fileinput
from collections.abc import Iterable
from functools import cache

type Devices = dict[str, list[str]]


def main():
    devices: Devices = parse_devices(map(str.rstrip, fileinput.input()))

    print(part_1(devices))
    print(part_2(devices))


def parse_devices(raw_value: Iterable[str]) -> Devices:
    return {source[:-1]: targets for source, *targets in map(str.split, raw_value)}


def part_1(devices: Devices) -> int:
    @cache
    def find_paths(device_from: str) -> int:
        return 1 if device_from == 'out' else sum(map(find_paths, devices[device_from]))

    return find_paths('you')


def part_2(devices: Devices) -> int:
    @cache
    def find_paths(device_from: str, dac: bool, fft: bool) -> int:
        if device_from == "out":
            return int(dac and fft)

        return sum(find_paths(device_to, dac or device_from == 'dac', fft or device_from == 'fft')
                   for device_to in devices[device_from])

    return find_paths('svr', False, False)


if __name__ == '__main__':
    main()
