class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


def sort_array(arr, length):
    # Using Bubble Sort
    for i in range(length-1):
        for j in range(length-1-i):
            if arr[j].salary > arr[j + 1].salary:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():
    n = int(input("Enter range:"))
    arr = []
    for i in range(0, n):
        name = input("Enter your name:")
        salary = int(input("Enter your salary:"))
        arr.append(Employee(name, salary))

    output = sort_array(arr, n)
    for i in range(0, n):
        print(output[i].name+" "+str(output[i].salary))


main()