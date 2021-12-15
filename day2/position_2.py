FILE_NAME = 'input.txt'


def get_position(directions: list[str]) -> tuple:
    """Gets x and y position of submarine"""
    hor = 0
    depth = 0
    aim = 0

    for direction in directions:
        # either + smth for hor
        # or +- smth for depth
        command, amount = direction.split(' ')
        amount = int(amount)
        # print(amount)

        if command == 'forward':
            # It increases your horizontal position by X units.
            # It increases your depth by your aim multiplied by X.
            hor += amount
            depth += aim * amount
        elif command == 'down':
            # down X increases your aim by X units.
            aim += amount
        elif command == 'up':
            # decreases your aim by X units.
            aim -= amount

    print(hor, depth, sep=' - ')

    return (hor, depth)


def get_final_position(data: list[str]) -> int:
    """Multiplies x and y position of submarine"""
    pos = get_position(data)
    multiplied_pos = pos[0] * pos[1]

    return multiplied_pos


with open(FILE_NAME, 'r') as input:
    input_lines = input.readlines()
    res = get_final_position(input_lines)
    print(f'The result is: {res}')
