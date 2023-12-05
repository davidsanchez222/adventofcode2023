import re

with open("input.txt", "r") as file:
    LINES = file.read().splitlines()


def part1():
    sum = 0
    color_map = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    color_pattern = 'blue|red|green'
    for line in LINES:
        game_possible = None
        break_game_loop = None
        game_id = int(re.findall(r"Game (\d+):", line)[0])
        rounds = line.split(": ")[1].split("; ")
        for round in rounds:
            if break_game_loop:
                break
            else:
                color_divs = round.split(", ")
                for color_div in color_divs:
                    count = int(re.findall(r"(\d+) ", color_div)[0])
                    color = re.findall(color_pattern, color_div)[0]
                    if count > color_map[color]:
                        game_possible = False
                        break_game_loop = True
                        break
                    else:
                        game_possible = True

        if game_possible:
            sum += game_id

    print(sum) 
    # 1734


def part2():
    power_sum = 0
    color_pattern = 'blue|red|green'
    for line in LINES:
        color_map = {
        "red": 0,
        "green": 0,
        "blue": 0
        }
        game_possible = None
        break_game_loop = None
        game_id = int(re.findall(r"Game (\d+):", line)[0])
        rounds = line.split(": ")[1].split("; ")
        for round in rounds:
            color_divs = round.split(", ")
            for color_div in color_divs:
                count = int(re.findall(r"(\d+) ", color_div)[0])
                color = re.findall(color_pattern, color_div)[0]
                if count > color_map[color]:
                    color_map[color] = count

        game_power = 1
        for value in color_map.values():
            game_power *= value

        power_sum += game_power

    print(power_sum)
    # 70387


part2()
