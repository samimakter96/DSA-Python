"""
There are N students in a classroom , The students which are present are in the array present [] , one student absent
for the class. Find and return the number of that student who is absent .

Example:
Input: present = [3,0,1]
Output: 2

Explanation: N = 3 since there are 3 students, so all numbers are in the range [0,3]. 2 is the absent student in the
range since it does not appear in present.
"""

present = [3, 0, 1]
n = len(present)
max_value = max(present)
total_student = n * (n + 1) // 2    # including absent student
actual_student = sum(present)       # actual present student
absent_student = total_student - actual_student

if absent_student > max_value + 1:  # edge cases
    print(-1)
else:
    print(absent_student)