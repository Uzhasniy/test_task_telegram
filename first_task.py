sequence_of_numbers = int(input('Введите первое число '))
desired_number = int(input('Введите второе число '))

list_of_numbers = list(range(1,sequence_of_numbers+1))
merging_with_plus = "+".join(map(str,list_of_numbers))
sum_of_all_numbers = sum(map(int,list_of_numbers))
if sum_of_all_numbers == desired_number:
    print(f'{merging_with_plus} = {sum_of_all_numbers}')

def main(list_of_numbers):
    sum_of_some_numbers = str(list_of_numbers[number])+ str(list_of_numbers[number+1])
    list_of_numbers.pop(number)
    list_of_numbers[number] = sum_of_some_numbers
    merging_with_plus = "+".join(map(str,list_of_numbers))
    sum_of_all_numbers = sum(map(int,list_of_numbers))
    return list_of_numbers, merging_with_plus, sum_of_all_numbers

for number in range(sequence_of_numbers-1):
    list_of_numbers = list(range(1,sequence_of_numbers+1))
    list_of_numbers, merging_with_plus, sum_of_all_numbers = main(list_of_numbers)
    if sum_of_all_numbers == desired_number:
        print(f'{merging_with_plus} = {sum_of_all_numbers}')
    for second_level_numbers in range(len(list_of_numbers)-number-1):
        local_list_of_numbers = list_of_numbers
        list_of_numbers, merging_with_plus, sum_of_all_numbers = main(local_list_of_numbers)
        if sum_of_all_numbers == desired_number:
            print(f'{merging_with_plus} = {sum_of_all_numbers}')

merging = "".join(map(str,list_of_numbers))
for sum_of_all_numbers in range(1,sequence_of_numbers):
    addition_of_halves = int(merging[:sum_of_all_numbers]) + int(merging[sum_of_all_numbers:])
    if addition_of_halves == desired_number:
        print(f'{int(merging[:sum_of_all_numbers])} + {int(merging[sum_of_all_numbers:])} = {addition_of_halves}')