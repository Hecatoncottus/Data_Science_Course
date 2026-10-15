
input_list = input("Введите числа через пробел: ")

raw_numbers = []

for text_numbers in input_list.split():
    raw_numbers.append(int(text_numbers))

def process_numbers(lst):
    Processed_numbers = []
    for number in lst:
        if number % 2 == 0:
            if number not in Processed_numbers:
                Processed_numbers.append(number)
    Processed_numbers.sort(reverse=True)
    return Processed_numbers

final_list = process_numbers(raw_numbers)

print(final_list)