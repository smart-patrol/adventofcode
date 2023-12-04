from typing import List
from collections import Counter


def process_card(data_point: List[str]) -> set:
    card, entries = data_point.split(":")
    want, have = entries.strip().split("|")
    want_set = set(want.rstrip().split(" "))
    have_set = set(have.strip().split(" "))
    both = want_set.intersection(have_set)
    return both



def problem2(data:List[str]) -> int:
    # Create our starting cards, one for each id
    cards = [1 for _ in range(len(data))]
    i : int = 0

    while len(data) > i:
        winning_number = len(process_card(data[i]))

        # If the winning numbers is 4, and we are on card 2
        # add one to card 3, 4, 5, 6
        for x in range(i + 1, winning_number + i + 1):
            cards[x] += cards[i]
        i+=1

    return sum(cards)




def problem1(data: List[str]) -> int:

        total_points = 0

        for data_point in data:
            both = process_card(data_point)

            points = 0
            i = 0
            ln = len(both)
            while ln > i:
                if i == 0:
                    points = 1
                else:
                    points *= 2
                i+=1
            total_points += points
        
        return total_points




if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    clean_lines = [line.strip() for line in lines if line.strip()]
    clean_lines = [' '.join(line.split()) for line in clean_lines]
    data = [line for line in clean_lines if line]


    print(problem1(data))
    print(problem2(data)) 
