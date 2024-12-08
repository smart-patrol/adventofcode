import re



def read_data(file_path:str) -> list:
    data = list()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            data.append(line)
    return data

def extract_mul_patterns(input_string):
    # Define the regex pattern
    pattern = r'mul\((\d+),(\d+)\)'

    # Find all matches in the input string
    matches = re.findall(pattern, input_string)

    return matches

def process_instructions(data:list) -> int:
    results = 0
    for d in data:
        pairs = extract_mul_patterns(d)
        results  += sum(int(v[0])*int(v[1]) for v in pairs)
    return results



def new_instructions(data:list) -> int:
    pattern = r"(don't\(\)|do\(\))"
    results = 0

    instructions = list()
    for d in data:
        split_string  = re.split(pattern, d)
        instructions = [part for part in split_string if part]
        # now go through and start stop calc based on do/dont
        skip = False
        for v in instructions:
            if v ==  "don't()":
                skip= True
            elif v ==  "do()":
                skip = False
            elif skip != True:
                pairs = extract_mul_patterns(v)
                results  += sum(int(v[0])*int(v[1]) for v in pairs)
            else:
                continue
    return results

def part2(data):
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    instructions = re.findall(pattern, "".join(data))

    enabled = True
    result = 0

    for inst in instructions:
        match inst[0]:
             case "do()":
                enabled = True
             case "don't()":
                enabled = False
             case _ if enabled:
                result += int(inst[1]) * int(inst[2])

    return result

def main(file_path):
    data = read_data(file_path)
    processed_results = process_instructions(data)
    print("Results are:", processed_results)
    new_processed_results = part2(data)
    print("New Results are:",new_processed_results)


if __name__ == "__main__":
    main("test_input.txt")
    main("input.txt")

