def bouncingBall(h, bounce, window):
    bounceCnt = 1

    while True:
        if h * bounce > window:
            bounceCnt += 2
            h *= bounce
        else:
            break

    if bounceCnt > 1:
        return bounceCnt
    return -1


def main():
    print(bouncingBall(3, 0.66, 1.5))
    print(bouncingBall(30, 0.66, 1.5))
    print(bouncingBall(1000000, 0.99, 1.5))
    print(bouncingBall(30, 0.9999999999, 1))    # 망했다.


if __name__ == "__main__":
    main()
