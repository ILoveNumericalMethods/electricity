from grid import Grid


def main():

    grid = Grid(10, 10, -1, 1, 1, 1, 0.001)
    output_file = open("output.txt", 'w')

    while True:
        grid.modeling(output_file)
        print("modeling")
        grid.print_data(output_file)
        print("printing")

if __name__ == "__main__":
    main()

