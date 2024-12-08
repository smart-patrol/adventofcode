from typing import Set, Tuple, List
from collections import deque
from pathlib import Path


def parse_input(input_file: str) -> Tuple[complex, Set[complex], int]:
    """Parse input file and return start position, obstacles, and grid dimension."""
    grid = Path(input_file).read_text().splitlines()
    dim = len(grid)
    obstacles = set()
    start = None
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':
                start = complex(x, y)
            elif cell == '#':
                obstacles.add(complex(x, y))
                
    return start, obstacles, dim


def get_initial_path(
    start: complex, obstacles: Set[complex], dim: int
) -> List[Tuple[complex, complex]]:
    """
    Get the initial path of the guard with positions and directions.
    
    Args:
        start: Starting position
        obstacles: Set of obstacle positions
        dim: Grid dimension
        
    Returns:
        List of (position, direction) tuples representing first visits
    """
    # Directions as complex numbers
    UP = -1j
    RIGHT = 1
    DOWN = 1j
    LEFT = -1
    
    dirs = deque([UP, RIGHT, DOWN, LEFT])
    
    # Create boundary set
    boundary = set()
    for i in range(-1, dim + 1):
        boundary.add(complex(-1, i))    # Left boundary
        boundary.add(complex(dim, i))   # Right boundary
        boundary.add(complex(i, -1))    # Top boundary
        boundary.add(complex(i, dim))   # Bottom boundary
    
    position = start
    seen = {position}
    path = [(position, dirs[0])]
    
    while True:
        new_pos = position + dirs[0]
        
        # If we hit an obstacle, rotate direction right
        while new_pos in obstacles:
            dirs.rotate(-1)
            new_pos = position + dirs[0]
        
        # Check if we've hit the boundary
        if new_pos in boundary:
            break
            
        position = new_pos
        if position not in seen:
            path.append((position, dirs[0]))
        seen.add(position)
    
    return path


def is_loop(
    path: List[Tuple[complex, complex]], obstacles: Set[complex], dim: int
) -> bool:
    """
    Check if adding an obstacle at the end of the path creates a loop.
    
    Args:
        path: List of (position, direction) tuples
        obstacles: Set of existing obstacles
        dim: Grid dimension
        
    Returns:
        True if path creates a loop, False otherwise
    """
    obstacle_pos, direction = path[-1]
    seen = set(path[:-1])
    new_obstacles = obstacles | {obstacle_pos}
    
    # Start from position before obstacle
    position = obstacle_pos - direction
    
    # Initialize directions
    dirs = deque([-1j, 1, 1j, -1])  # UP, RIGHT, DOWN, LEFT
    while dirs[0] != direction:
        dirs.rotate(-1)
    
    # Create boundary set
    boundary = set()
    for i in range(-1, dim + 1):
        boundary.add(complex(-1, i))
        boundary.add(complex(dim, i))
        boundary.add(complex(i, -1))
        boundary.add(complex(i, dim))
    
    while True:
        new_pos = position + dirs[0]
        while new_pos in new_obstacles:
            dirs.rotate(-1)
            new_pos = position + dirs[0]
            
        if new_pos in boundary:
            return False
            
        position = new_pos
        current_state = (position, dirs[0])
        if current_state in seen:
            return True
        seen.add(current_state)

def solve_part1(input_file: str) -> int:
    """Solve part 1 of the puzzle."""
    start, obstacles, dim = parse_input(input_file)
    path = get_initial_path(start, obstacles, dim)
    return len({pos for pos, _ in path})


def solve_part2(input_file: str) -> int:
    """
    Solve part 2 of the puzzle.
    
    Args:
        input_file: Path to the input file
        
    Returns:
        Number of possible positions for new obstacle that create loops
    """
    start, obstacles, dim = parse_input(input_file)
    path = get_initial_path(start, obstacles, dim)
    
    total = 0
    for i in range(len(path)):
        subpath = path[: i + 1]
        if subpath[-1][0] == start:
            continue
        if is_loop(subpath, obstacles, dim):
            total += 1
    
    return total


def main() -> None:
    """Main function to run the solution."""
    # Parse input once for both parts
    test_input = "test_input.txt"
    start_test, obstacles_test, dim_test = parse_input(test_input)
    path_test = get_initial_path(start_test, obstacles_test, dim_test)
    
    # Test part 1
    test_result = len({pos for pos, _ in path_test})
    print(f"Test result part 1: {test_result}")
    assert test_result == 41, f"Test failed: expected 41, got {test_result}"
    
    # Solve part 1
    input_file = "input.txt"
    start, obstacles, dim = parse_input(input_file)
    path = get_initial_path(start, obstacles, dim)
    result = len({pos for pos, _ in path})
    print(f"Part 1 result: {result}")
    
    # Test part 2
    total_test = 0
    for i in range(len(path_test)):
        subpath = path_test[: i + 1]
        if subpath[-1][0] == start_test:
            continue
        if is_loop(subpath, obstacles_test, dim_test):
            total_test += 1
    test_result2 = total_test
    print(f"Test result part 2: {test_result2}")
    assert test_result2 == 6, f"Test failed: expected 6, got {test_result2}"
    
    # Solve part 2
    total = 0
    for i in range(len(path)):
        subpath = path[: i + 1]
        if subpath[-1][0] == start:
            continue
        if is_loop(subpath, obstacles, dim):
            total += 1
    result2 = total
    print(f"Part 2 result: {result2}")


if __name__ == "__main__":
    main()
