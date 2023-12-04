def sum_calibration_values(file_path):
    # Initialize sum to 0
    total_sum = 0

    # Open the file
    with open(file_path, 'r') as file:
        # Read each line
        for line in file:
            # Remove newline character and any leading/trailing whitespaces
            line = line.strip()

            # Find the first digit
            first_digit = next((char for char in line if char.isdigit()), None)

            # Find the last digit
            last_digit = next((char for char in reversed(line) if char.isdigit()), None)

            # If a first and last digit are found, add them to the total sum
            if first_digit and last_digit:
                total_sum += int(first_digit + last_digit)

    return total_sum


import re

digit_words = {
   "one": "1",
   "two": "2",
   "three": "3",
   "four": "4",
   "five": "5",
   "six": "6",
   "seven": "7",
   "eight": "8",
   "nine": "9",
}

def sum_calibration_values(file_path):
   total_sum = 0

   with open(file_path, 'r') as file:
       for line in file:
           line = line.strip()

           # Replace digit words with digits
           line = re.sub(r'\b(?:' + '|'.join(digit_words.keys()) + r')\b', 
                        lambda m: digit_words[m.group(0)], line)

           # Find the first and last numeric value
           first_numeric_value = re.search(r'\d+', line)
           last_numeric_value = re.search(r'\d+', line[::-1])

           # If a first and last numeric value are found, add them to the total sum
           if first_numeric_value and last_numeric_value:
               total_sum += int(first_numeric_value.group(0)) + int(last_numeric_value.group(0))

   return total_sum



class Trebuchet:
   def __init__(self, inputs):
       self.inputs = inputs
       self.number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
       self.number_digits = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]

   def solveA(self):
       return sum(self.lineValue(line) for line in self.inputs)

   def solveB(self):
       return sum(self.lineValue(self.replaceWordsWithNumber(line)) for line in self.inputs)

   def lineValue(self, line):
       result = [c for c in line if c.isdigit()]
       first = result[0]
       last = result[-1]
       number = int(first + last)
       return number

   def replaceWordsWithNumber(self, line):
       replaceLine = line
       for i in range(len(self.number_words)):
           replaceLine = replaceLine.replace(self.number_words[i], self.number_digits[i])
       return replaceLine

trebuchet = Trebuchet(["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"])
print(trebuchet.solveB()) # Output: 281


if __name__ == "__main__":
    total_sum = sum_calibration_values('input.txt')
    print(total_sum)

    trebuchet = Trebuchet(data)
    print(trebuchet.solveB()) 