from typing import Tuple,List
from collections import Counter



def read_data(file_path:str) -> Tuple[List, List]:
    data = list()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            points = [int(s) for s in line.split(" ")]
            data.append(points)
    return data


def check_adjacent_differences(levels):
    """Check if adjacent differences are between 1 and 3 inclusive."""
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_safe_report(levels):
    """Check if a report is safe."""
    # Check if strictly increasing
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    # Check if strictly decreasing
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    # Must be either increasing or decreasing (not both)
    if not (increasing or decreasing):
        return False

    # Check adjacent differences
    return check_adjacent_differences(levels)

def count_safe_reports(reports):
    """Count how many reports are safe."""
    safe_count = 0
    for levels in reports:
        if is_safe_report(levels):
            safe_count += 1
    return safe_count

def is_safe_with_dampener(levels):
    """Check if a report is safe or can be made safe by removing one element."""
    # First check if it's already safe
    if is_safe_report(levels):
        return True

    # Try removing each element one at a time
    for i in range(len(levels)):
        # Create new list without element at index i
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe_report(dampened_levels):
            return True

    return False

def count_safe_reports_with_dampener(reports):
    """Count how many reports are safe with the Problem Dampener."""
    return sum(is_safe_with_dampener(levels) for levels in reports)

def main(file_path):
    data = read_data(file_path)
    safe_count = count_safe_reports(data)
    print("Safe reports", safe_count)
    safe_count = count_safe_reports_with_dampener(data)
    print("Number of safe reports with Problem Dampener:", safe_count)

if __name__ == "__main__":
    main("test_input.txt")
    main("input.txt")
