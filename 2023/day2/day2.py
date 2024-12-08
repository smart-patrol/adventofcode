from collections import Counter
from typing import List, Dict, Tuple
import math


def count_games(game_list: List[str]) -> List[Tuple[int, Dict[str, int]]]:
    result = []

    for game in game_list:
        game_num, color_counts_str = game.split(':')
        game_num = int(game_num.split()[1])
        color_counts_str = color_counts_str.split(';')

        game_valid = True

        for color_count_str in color_counts_str:
            color_counts = {}

            for count_color_str in color_count_str.strip().split(','):
                count, color = count_color_str.strip().split()
                count = int(count)

                if color in color_counts:
                    color_counts[color] += count
                else:
                    color_counts[color] = count

            for color, count in color_counts.items():
                if count > total_cubes[color]:
                    game_valid = False
                    break

            if not game_valid:
                break

        if game_valid:
            result.append(game_num)

    return result


def  calculate_min_cubes(game_list):
    _sum = 0
    for line in game_list:
        counts = {"red": 0, "green": 0, "blue": 0}
        _, sets = line.split(": ")
        sets = sets.split("; ")
        for _set in sets:
            _set = {k: int(v) for v, k in map(str.split, _set.split(", "))}
            counts = {k: max(v, _set.get(k, 0)) for k, v in counts.items()}
        _sum += math.prod(counts.values())

    return _sum



if __name__ == "__main__":
    total_cubes = {"red": 12, "green": 13, "blue": 14}

    with open('input.txt') as f:
        game_list = f.readlines()

    result = count_games(game_list)

    total_ids : int = sum(result)

    print(total_ids)

    result = calculate_min_cubes(game_list)

    total_power : int = 0
    for r in result:
        game_id, cubes = r[0], r[1]
        power = cubes["red"] * cubes["green"] * cubes["blue"]
        total_power += power
    print(total_power)
