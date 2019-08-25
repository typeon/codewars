def iq_test(numbers):
    nums = numbers.split(" ")
    nums = map(lambda x: int(x), nums)

    odd = []
    even = []
    i = 1

    for num in nums:
        if num % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        i += 1
    if len(even) == 1:
        return even[0]
    return odd[0]


if __name__ == "__main__":
    assert iq_test("2 4 7 8 10") == 3
    assert iq_test("1 2 1 1") == 2
