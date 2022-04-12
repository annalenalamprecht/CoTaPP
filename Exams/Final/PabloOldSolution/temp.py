def get_three_smallest(elements):
    return sorted(elements)[:3]

my_grades = [1, 6, 4, 9.5, 7]

def getHighest(elements):
    return max(elements)

print(f'My highest grade: {getHighest(my_grades)}')

print('My worst grades are', get_three_smallest(my_grades))
