array_initial = input('Введите массив чисел одной строкой ').split(', ')
monotonous_segment = []
monotonous_segment_max = []

for slice_number in range(len(array_initial)-1):
    monotonous_segment = []
    array_sliced = array_initial[slice_number:]
    for sequence_number in range(len(array_sliced)):   
        if sequence_number == len(array_sliced)-1:
            if array_sliced[sequence_number] > array_sliced[sequence_number-1]:
                monotonous_segment.append(array_sliced[sequence_number])
        elif array_sliced[sequence_number] < array_sliced[sequence_number+1]: 
            monotonous_segment.append(array_sliced[sequence_number])   
        else:
            monotonous_segment.append(array_sliced[sequence_number+1]) 
            break
    
    if monotonous_segment_max != 0:
        if len(monotonous_segment_max) < len(monotonous_segment):
            monotonous_segment_max = monotonous_segment
            beginning_of_cut = slice_number
    else:
        monotonous_segment_max = monotonous_segment

first_index = array_initial.index(monotonous_segment_max[0])
second_index = array_initial.index(monotonous_segment_max[-1])

if (array_initial.count(monotonous_segment_max[0]) == 1) or (len(monotonous_segment_max) == 1):
    print(f'{first_index}, {second_index}')
elif array_initial.count(monotonous_segment_max[0]) > 1 and (array_initial.count(monotonous_segment_max[-1]) == 1):
    print(f'{beginning_of_cut}, {second_index}')
elif array_initial.count(monotonous_segment_max[-1]) > 1 and (array_initial.count(monotonous_segment_max[-1]) == 1):
    print(f'{first_index}, {beginning_of_cut+len(monotonous_segment_max)}')
elif (array_initial.count(monotonous_segment_max[0]) > 1) and (array_initial.count(monotonous_segment_max[-1]) > 1):
    print(f'{beginning_of_cut}, {beginning_of_cut+len(monotonous_segment_max)}')
