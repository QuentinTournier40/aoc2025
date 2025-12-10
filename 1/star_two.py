def main():
    with open("./input.txt", "r") as file:
        rotations = [line.strip() for line in file]

    dial_position = 50
    left_on_zero = 0

    for rotation in rotations:
        direction = rotation[0]
        tick = int(rotation[1::])

        for _ in range(tick):
            if direction == "R":
                dial_position = (dial_position + 1) % 100
            elif direction == "L":
                dial_position = (dial_position - 1) % 100

            if dial_position == 0:
                left_on_zero += 1

    print(left_on_zero)


if __name__ == "__main__":
    main()
