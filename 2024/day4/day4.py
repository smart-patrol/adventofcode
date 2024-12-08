import re

def read_data(file_path:str) -> list:
    data = list()
    with open(file_path, 'r') as file:
        for line in file:
            line:str = line.strip()
            data.append([l for l in line])
    return data

def search_word(matrix, word):
    def is_valid(x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

    def search_from_position(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i*dx, y + i*dy
            if not is_valid(nx, ny) or matrix[nx][ny] != word[i]:
                return False
        return True

    directions = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]
    results = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == word[0]:
                for dx, dy in directions:
                    if search_from_position(i, j, dx, dy):
                        results.append((i, j))

    return results

def find_crosses(data:list):
    rows, cols = len(data), len(data[0])
    count = 0

    _set = {"M", "S"}

    # find A as center of the cross, then check the diagonals
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == "A":
                if {data[r - 1][c - 1], data[r + 1][c + 1]} == _set and {data[r - 1][c + 1], data[r + 1][c - 1]} == _set:
                    count += 1
    return count



def main(file_path):
    data = read_data(file_path)
    search_results = search_word(data,'XMAS')
    print("Results are:", len(search_results))
    total = find_crosses(data)
    print("Results are for part2 are:", total)


if __name__ == "__main__":
    main("test_input.txt")
    main("input.txt")

