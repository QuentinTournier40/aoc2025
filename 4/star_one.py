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

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != "@":
                continue

            neighbors = get_neighbors(lines, i, j)
            if neighbors.count("@") < 4:
                cpt += 1

    print(cpt)


if __name__ == "__main__":
    main()
