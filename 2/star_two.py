def is_valid_id(id):
    size = len(str(id))
    for i in range(1, size // 2 + 1):
        if size % i != 0:
            continue

        split_id = list(map(''.join, zip(*[iter(str(id))] * i)))
        if split_id.count(split_id[0]) == len(split_id):
            return False
    return True


def main():
    with open("./input.txt", "r") as file:
        id_ranges = file.readline().split(",")

    id_sum = 0

    for id_range in id_ranges:
        lower = int(id_range.split("-")[0])
        higher = int(id_range.split("-")[1])

        for i in range(lower, higher + 1):
            if not is_valid_id(i):
                id_sum += i

    print(id_sum)


if __name__ == "__main__":
    main()
