def move_left(row: list) -> list:
    number_of_1 = row.count('1')
    number_of_0 = row.count('0')
    result = list()
    for i in range(0, number_of_1):
        result.append('1')
    for i in range(0, number_of_0):
        result.append('0')
    return result


def move_right(row: list) -> list:
    number_of_1 = row.count('1')
    number_of_0 = row.count('0')
    result = list()
    for i in range(0, number_of_0):
        result.append('0')
    for i in range(0, number_of_1):
        result.append('1')
    return result


def print_grid(grid: list):
    for row in grid:
        for item in row:
            print(item, end="")
        print()


def main():
    test_cases = int(input())
    while test_cases > 0:
        rows, columns = map(int, input().split())
        grid = list()
        for i in range(0, rows):
            grid.append(list(input()))
        operations = list(input())
        for item in operations:
            if item == 'L':
                for row_number in range(0, rows):
                    grid[row_number] = move_left(grid[row_number])
            elif item == 'R':
                for row_number in range(0, rows):
                    grid[row_number] = move_right(grid[row_number])
            elif item == 'D':
                for j in range(0, columns):
                    temp_list  = list()
                    for i in range(0, rows):
                        temp_list.append(grid[i][j])
                    temp_list = move_right(temp_list)

                    for i in range(0, rows):
                        grid[i][j] = temp_list[i]
            else:
                for j in range(0, columns):
                    temp_list = list()
                    for i in range(0, rows):
                        temp_list.append(grid[i][j])
                    temp_list = move_left(temp_list)

                    for i in range(0, rows):
                        grid[i][j] = temp_list[i]

        print_grid(grid)
        test_cases -= 1


if __name__ == '__main__':
    main()