from code_challenge_one import reverse_remove
from code_challenge_three import minimum_change
from code_challenge_two import square_result


def main():
    print("***Primer ejercicio***")
    reverse_remove(6,[60, 6, 5, 4, 3, 2, 7, 7, 29, 1])
    print("-------------------------------------------")
    print("***Segundo ejercicio***")
    square_result(3, [-6, -5, 0, 5, 6])
    print("-------------------------------------------")
    print("***Tercer ejercicio***")
    minimum_change([])

if __name__ == '__main__':
    main()