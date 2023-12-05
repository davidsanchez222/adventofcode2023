with open("input.txt", "r") as file:
    LINES = file.read().splitlines()


def part1():
    calibration_sum = 0
    # i = 1
    for line in LINES:
        first_digit = None
        last_digit = None
        for index, char in enumerate(line): 
            eol = index == len(line) - 1 # bool to check if char is at the end of line
            if char.isdigit() and not first_digit:
                if eol:
                    first_digit = char
                    last_digit = char
                else:    
                    first_digit = char
            elif char.isdigit():
                last_digit = char

            elif eol and not last_digit:
                last_digit = first_digit
            

        calibration_sum += int(first_digit+last_digit)
        # print(f"{i} Line: {line} -> First: {first_digit} Last: {last_digit}")
        # i += 1

    print("Part 1: ", calibration_sum)
    # 53651


def part2():
    digit_map = {
        "one": "on1e",
        "two": "tw2o",
        "three": "thr3ee",
        "four": "fo4ur",
        "five": "fi5ve",
        "six": "si6x",
        "seven": "sev7en",
        "eight": "eig8ht",
        "nine": "ni9ne"
    }

    calibration_sum = 0
    # i = 1
    for line in LINES:
        for key, value in digit_map.items():
            line = line.replace(key, value)

        first_digit = None
        last_digit = None
        for index, char in enumerate(line): 
            eol = index == len(line) - 1 # bool to check if char is at the end of line
            if char.isdigit() and not first_digit:
                if eol:
                    first_digit = char
                    last_digit = char
                else:    
                    first_digit = char
            elif char.isdigit():
                last_digit = char

            elif eol and not last_digit:
                last_digit = first_digit
            

        calibration_sum += int(first_digit+last_digit)
        # print(f"{i} Line: {line} -> First: {first_digit} Last: {last_digit}")
        # i += 1

    print("Part 2: ", calibration_sum)
    # 53894





