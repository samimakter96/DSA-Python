# sort () = This method sort the list by ascending by default

# Example : sort Ascending order
# syntax: list.sort()

my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]
my_numbers.sort()
print(my_numbers)

# Example 2: sort in Desending order
# syntax : list.sort(reverse=True)

my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]
my_numbers.sort(reverse=True)
print(my_numbers)

# Example : Sort list item using the key parameter

program_languages = ["python", "swift", "java", "c++", "Go"]
program_languages.sort(key=len)
print(program_languages)

# Example: sort the list items based on their length but in desending order

program_languages = ["python", "swift", "java", "c++", "Go"]
program_languages.sort(key=len, reverse=True)
print(program_languages)