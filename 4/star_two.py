def get_neighbors(tab, x, y):
    neighbors = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue

            ni, nj = x + i, y + j

            if 0 <= ni < len(tab) and 0 <= nj < len(tab[x]):
                neighbors.append(tab[ni][nj])
    return neighbors


def main():
    with open("./input.txt") as file:
        lines = [list(line.strip()) for line in file]

    cpt = 0
    old_cpt = 0

    while True:
        indexes = []
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] != "@":
                    continue

                neighbors = get_neighbors(lines, i, j)
                if neighbors.count("@") < 4:
                    indexes.append((i, j))
                    cpt += 1

        for i, j in indexes:
            lines[i][j] = "x"

        if cpt == old_cpt:
            break

        old_cpt = cpt

    print(cpt)


if __name__ == "__main__":
    main()
