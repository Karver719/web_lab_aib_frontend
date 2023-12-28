def count_horse_paths(board_width: int, board_height: int):
    field = [[0 for _ in range(0, width)] for _ in range(0, height)]
    field[0][0] = 1
    for i in range(0, board_height):
        for j in range(0, board_width):
            for move_x, move_y in [(-1, -2), (-2, -1)]:
                field[i][j] += field[i + move_y][j + move_x] if (0 <= i + move_y < board_height) and (0 <= j + move_x < board_width) else 0
    return field[board_height - 1][board_width - 1]

if __name__ == '__main__':
    width, height = map(int, input().split())
    print(count_horse_paths(width, height))