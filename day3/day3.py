import collections as c
import itertools
import re

def get_input_data(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    schema = [["."] + [char for char in line.strip()] + ["."] for line in lines]
    schema.insert(0, ["."] * len(schema[0]))
    schema.append(["."] * len(schema[0]))
    return schema

def find_positions(num, schema_str, schema):
    positions = [pos.start() for pos in re.finditer(f"[^0-9]{num}[^0-9]", schema_str)]
    iss = [pos % len(schema[0]) + 1 for pos in positions]
    jss = [pos // len(schema[0]) for pos in positions]
    return iss, jss

def calculate_gears_and_score(schema, schema_str):
    gears = c.defaultdict(list)
    score = 0
    for num in set(re.findall(r"\d+", schema_str)):
        iss, jss = find_positions(num, schema_str, schema)
        for i, j in zip(iss, jss):
            idx = [(m, n) for m in [j - 1, j + 1] for n in range(i - 1, i + len(num) + 1)]
            idx += [(j, i - 1), (j, i + len(num))]
            neighbours = [schema[k][l] for k, l in idx]
            if "*" in neighbours:
                gears[",".join(map(str, idx[neighbours.index("*")]))].append(int(num))
            score += int(num) * (not all(n == "." for n in neighbours))
    return gears, score

def main():
    schema = get_input_data("input.txt")
    schema_str = "".join(list(itertools.chain(*schema)))
    gears, score = calculate_gears_and_score(schema, schema_str)
    print(score)
    print(sum(v[0] * v[1] for _, v in gears.items() if len(v) == 2))

if __name__ == "__main__":
    main()
