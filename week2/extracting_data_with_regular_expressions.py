import re


with open('input.txt', 'r') as input_data:
    numbers = [int(x) for x in re.findall('[0-9]+', input_data.read())]
    print(sum(numbers))
