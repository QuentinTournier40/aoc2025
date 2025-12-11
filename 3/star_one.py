def main():
    with open("./input.txt", "r") as file:
        banks = [line.strip() for line in file]

    total_joltage = 0

    for bank in banks:
        max_joltage = 0
        batteries = list(map(int, bank))
        for i in range(len(batteries)):
            for j in range(i + 1, len(batteries)):
                if int(str(batteries[i]) + str(batteries[j])) > max_joltage:
                    max_joltage = int(str(batteries[i]) + str(batteries[j]))
        total_joltage += max_joltage

    print(total_joltage)


if __name__ == "__main__":
    main()
