def max_gap(numbers):
    numbers.sort()

    max = -99999999
    for i in range(1, len(numbers)):
        if max < numbers[i] - numbers[i - 1]:
            max = numbers[i] - numbers[i - 1]
    return max


def main():
    print(max_gap([13, 10, 2, 9, 5]),4)
    print(max_gap([13, 3, 5]), 8)
    print(max_gap([24, 299, 131, 14, 26, 25]), 168)
    print(max_gap([-3, -27, -4, -2]), 23)
    print(max_gap([-7, -42, -809, -14, -12]), 767)
    print(max_gap([12, -5, -7, 0, 290]), 278)
    print(max_gap([-54, 37, 0, 64, -15, 640, 0]), 576)
    print(max_gap([130, 30, 50]), 80)
    print(max_gap([1, 1, 1]), 0)
    print(max_gap([-1, -1, -1]), 0)


if __name__ == "__main__":
    main()
