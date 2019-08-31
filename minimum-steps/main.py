def minimum_steps(numbers, value):
    numbers.sort()

    added_value = 0
    num = 0
    for val in numbers:
        if added_value + val < value:
            num += 1
            added_value += val
    return num


def main():
    print(minimum_steps([4, 6, 3], 7), 1)
    print(minimum_steps([10, 9, 9, 8], 17), 1)
    print(minimum_steps([8, 9, 10, 4, 2], 23), 3)
    print(minimum_steps([19, 98, 69, 28, 75, 45, 17, 98, 67], 464), 8)
    print(minimum_steps([4, 6, 3], 2), 0)


if __name__ == "__main__":
    main()
