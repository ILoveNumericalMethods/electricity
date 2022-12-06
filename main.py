import grid


def main():

    grid = grid.Grid(100, 50, -1, 1, 1, 1, 0.001)

    while True:
        grid.modeling()
        grid.print_data("output.txt")


if __name__ == "__main__":
    main()
