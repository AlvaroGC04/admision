"""
Code Challenge #1
Having a list of n numbers with digits in range [0, S], where n <= 100, switch all list positions in O(n)
time. If the input number contains a digit greater or equal than S, you will delete the digit from the
number, for example with S=6, 61 becomes 1, and 6 will be deleted from the array. The result
should be printed in console/terminal. Please, don’t use built-in sort of your language.

Examples with S=6:
> [1, 2, 3, 4, 5, 6] -> [5, 4, 3, 2, 1]
> [10, 20, 30, 40] -> [40, 30, 20, 10]
> [6] -> []
> [66] -> []
> [65] -> [5]
> [6, 2, 1] -> [1 , 2]
> [60, 6, 5, 4, 3, 2, 7, 7, 29, 1] -> [1, 2, 2, 3, 4, 5, 0]

"""

def reverse_remove(s, number_list):
    new_number_list =[]
    for number in number_list:
        new_number = [digit for digit in str(number) if int(digit) < s]#["1", "5"]
        if new_number:
            new_number_list.append(int("".join(new_number)))#15

    print(f"La lista resultante de procesar {number_list} sin {s} --> {new_number_list[::-1]}")





