def is_valid_id(id):
    size = len(str(id))
    if size % 2 == 1:
        return True

    beginning = str(id)[:size//2]
    end = str(id)[size//2:]
    return beginning != end

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
