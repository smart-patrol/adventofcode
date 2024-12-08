from typing import Tuple,List
from collections import Counter


def read_data(file_path:str) -> Tuple[List, List]:
    left = list()
    right = list()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            a,b = line.split("   ")
            left.append(int(a))
            right.append(int(b))
    return left,right

def calculate_total_distance(left:list, right:list) -> int:
    left_sorted = sorted(list(enumerate(left)), key=lambda x : x[1])
    right_sorted = sorted(list(enumerate(right)), key=lambda x : x[1])

    total_distance:int = 0
    for (_, left_value), (_, right_value) in zip(left_sorted, right_sorted):
          total_distance += abs(left_value - right_value)
    return total_distance

def calculate_similary_score(left:list, right:list) -> int:
    counts = Counter(right)
    total_score:int = 0
    for _, val in enumerate(left):
        if val in counts:
            total_score += counts[val]*val
    return total_score



def main(file_path):
    left, right = read_data(file_path)
    total_distance = calculate_total_distance(left,right)
    print("Total Distance:", total_distance)
    total_score: int = calculate_similary_score(left,right)
    print("Total Similairy Score:", total_score)

if __name__ == "__main__":
    main("test_input.txt")
    main("input.txt")
