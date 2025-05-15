# to create a tuple of numbers and print one item.
def create_tuple():
    numbers = (1, 2, 3, 4, 5)
    print(numbers[1])

# to unpack a tuple into several variables.
def unpack_tuple():
    numbers = (1, 2, 3, 4, 5)
    a, b, c, d, e = numbers
    print(a)

# to add an item to a tuple.
def add_item():
    numbers = (1, 2, 3, 4, 5)
    item = (6,)
    numbers += item
    print(numbers)

# to find the index of an item in a tuple.
def find_index():
    numbers = (1, 2, 3, 4, 5)
    print(numbers.index(3))

# to find the repeated items of a tuple
def find_repeated():
    numbers = (1, 2, 3, 4, 5, 1, 2, 3)
    seen = set()
    repeated = set()

    for item in numbers:
        if item in seen:
            repeated.add(item)
        else:
            seen.add(item)

    for item in repeated:
        print(item)

# Write a Python program to find the maximum and minimum values in a set.
def max_min():
    numbers = {1, 2, 3, 4, 5, 1, 2, 3}
    print(max(numbers))
    print(min(numbers))

# Write a Python program to check if a given value is present in a set or not.
def check_value():
    numbers = {1, 2, 3, 4, 5, 1, 2, 3}
    given_value = 0

    for number in numbers:
        if number == given_value:
            print("The value is present in the set")
            break

# Write a Python program to check if two given sets have no elements in common.
def have_no_common_elements():
    set_1 = {1, 2, 3, 4, 5, 1, 2, 3}
    set_2 = {1, 9, 3, 9, 5, 0, 3, 11}

    common = set_1.intersection(set_2)

    if len(common) == 0:
        print("No common elements")
    else:
        print("There are common elements")

# Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
def find_unique_and_count_occurrences():
    given_str = ["apple", "banana", "orange", "pie", "toy", "banana", "toy", "video"]
    updated_str = set(given_str)

    for word in updated_str:
        count = given_str.count(word)
        print(f"{word}: {count}")

# Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
def find_missing():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}

    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1

    print("Các phần tử có trong set1 nhưng không có trong set2:", missing_in_set2)
    print("Các phần tử có trong set2 nhưng không có trong set1:", missing_in_set1)

# Convert two lists into a dictionary
def lists_to_dict():
    keys = ['Vietnam', 'Thailand', 'England']
    values = ['Hanoi', 'Bangkok', 'London']

    result_dict = dict(zip(keys, values))

    print(result_dict)
# Merge two Python dictionaries into one
def two_dicts_to_one():
    dict1 = {'VietNam': 'Hanoi', 'Thailand': 'Bangkok'}
    dict2 = {'England': 'London', 'America': 'Washington'}

    dict1.update(dict2)
    print("Merged dictionary:", dict1)

# Initialize dictionary with default values
def default_value_dict():
    keys = ['Vietnam', 'Thailand', 'England']
    default_value = 0

    new_dict = dict.fromkeys(keys, default_value)

    print(new_dict)

# Create a dictionary by extracting the keys from a given dictionary
def extracted_dict():
    dict1 = {'Vietnam': 'Hanoi', 'Thailand': 'Bangkok'}
    keys_to_extract = ['Vietnam', 'Thailand']
    new_dict = {key: dict1[key] for key in keys_to_extract if key in dict1}

    print(new_dict)

# Delete a list of keys from a dictionary
def del_keys():
    dict1 = {'Vietnam': 'Hanoi', 'Thailand': 'Bangkok', 'England': 'London', 'America': 'Washington'}
    keys_to_remove = ['Vietnam', 'Thailand']

    for key in keys_to_remove:
        if key in dict1:
            del dict1[key]

    print(dict1)

# Check if a value exists in a dictionary
def check_value():
    dict1 = {'Vietnam': 'Hanoi', 'Thailand': 'Bangkok', 'England': 'London', 'America': 'Washington'}

    if 'Hanoi' in dict1.values():
        print("The value is present in the set")
    else:
        print("The value is not present in the set")

# Rename key of a dictionary
def rename_key():
    dict1 = {'old_key': 123, 'b': 456}

    dict1['new_key'] = dict1.pop('old_key')

    print(dict1)

# Get the key of a minimum value from the following dictionary
def get_min_value():
    dict1 = {'a': 10, 'b': 5, 'c': 8}
    min_key = min(dict1, key=dict1.get)

    print(min_key)

# Change value of a key in a nested dictionary
def change_value_in_nested():
    my_dict = {
        'person1': {'name': 'Alice', 'age': 25},
        'person2': {'name': 'Bob', 'age': 30}
    }

    my_dict['person1']['age'] = 28

    print(my_dict)

# Counts the number of times characters appear in a text paragraph.
def count_char():
    text = "Hello world!"

    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count)

# Using a dictionary containing keys starting from 1 and values containing prime numbers less than a value N.
def get_prime_dict():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    prime_dict = {}
    count = 1
    for num in range(2, N):
        if is_prime(num):
            prime_dict[count] = num
            count += 1
    return prime_dict


def restructure_by_department(employees):
    dept_employees = {}

    for emp_id, info in employees.items():
        dept = info["department"]

        emp_data = {"name": info["name"], "salary": info["salary"]}

        if dept not in dept_employees:
            dept_employees[dept] = {}

        dept_employees[dept][emp_id] = emp_data

    return dept_employees

if __name__ == '__main__':
    #N = 30
    #result = get_prime_dict()
    #print(result)

    employees = {
        1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
        1002: {"name": "Bob", "department": "Sales", "salary": 50000},
        1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
        1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
        1005: {"name": "Eve", "department": "Sales", "salary": 55000}
    }

    result = restructure_by_department(employees)

    from pprint import pprint

    pprint(result)
