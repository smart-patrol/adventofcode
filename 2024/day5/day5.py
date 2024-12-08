from collections import defaultdict

def read_data(file_path: str) -> tuple[defaultdict[int, set], list]:
    with open(file_path, 'r') as file:
        data = file.readlines()

    rules = defaultdict(set) 
    start = 0
    for i in range(len(data)):
        if data[i] == '\n':
            break
        page1, page2 = map(int, data[i].strip().split("|"))
        rules[page1].add(page2)
        start = i
    
    pages = []
    for i in range(start+1, len(data)):
        if data[i].strip():
            pages.append([int(n) for n in data[i].strip().split(",")])

    return rules, pages

def find_valid_pages(pages: list, rules: defaultdict[int, set]) -> list:
    valid_pages = list()
    invalid_pages = list()
    
    for p in pages:
        valid = True
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                # For each pair of pages (i,j) where i comes before j in the sequence
                # Check if there's a rule saying j should come before i
                # If such a rule exists, the sequence is invalid
                if p[i] in rules[p[j]]:  # if j->i exists, it's invalid
                    valid = False
                    break
            if not valid:
                invalid_pages.append(p)
                break
        if valid:
            valid_pages.append(p)
    return valid_pages, invalid_pages

def get_totals(valid_pages:list) -> int:
    total = 0
    for p in valid_pages:
        ln = len(p)
        mid = len(p) // 2
        if ln % 2 == 0:
            total += (p[mid]+ p[mid+1])/2
        else:
            total += p[mid]
    return total


def get_invalid_totals(invalid_pages: list, rules: defaultdict[int, set]) -> int:
    """
    For each invalid page sequence, reorders the pages according to the rules
    and returns the sum of middle page numbers from the corrected sequences.
    
    Args:
        invalid_pages: List of page sequences that violate the ordering rules
        rules: Dictionary mapping pages to the pages that should come after them
        
    Returns:
        Sum of middle page numbers from correctly ordered sequences
    """
    total = 0
    for pages in invalid_pages:
        # Create directed graph of page ordering rules
        graph = defaultdict(set)
        for i in range(len(pages)):
            for j in range(len(pages)):
                if i != j and pages[j] in rules[pages[i]]:
                    graph[pages[i]].add(pages[j])
        
        # Topologically sort pages based on rules
        ordered = []
        visited = set()
        temp = set()
        
        def dfs(node):
            if node in temp:
                return  # Skip if cycle detected
            if node in visited:
                return
            temp.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            temp.remove(node)
            visited.add(node)
            ordered.append(node)
            
        for page in pages:
            if page not in visited:
                dfs(page)
                
        ordered = ordered[::-1]  # Reverse to get correct order
        
        # Get middle value(s)
        mid = len(ordered) // 2
        if len(ordered) % 2 == 0:
            total += (ordered[mid - 1] + ordered[mid]) / 2
        else:
            total += ordered[mid]
            
    return int(total)


def calculate_pages(file_path:str) -> None:
    rules, pages =read_data(file_path)
    valid_pages, invalid_pages  = find_valid_pages(pages, rules)
    valid_totals = get_totals(valid_pages)
    print("Valid Total is :",valid_totals)
    invalid_totals = get_invalid_totals(invalid_pages, rules)
    print("Invalid Total is :",invalid_totals)

def main():
    calculate_pages("test_input.txt")
    calculate_pages("input.txt")

if __name__ == "__main__":
    main()



