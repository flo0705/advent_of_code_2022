
input = [line.replace('\n', '').strip() for line in  open("aoc_25/input.txt").readlines()]

print(input)

values_dict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "-": -1,
    "=": -2
}

reversed_values_dict = {
    0 : "00",
    1 : "01",
    2 : "02",
    3 : "1=",
    4 : "1-",
}

def snafu_to_decimal(snafu):
    number = 0
    for idx, digit in enumerate(reversed(snafu)):
        number += values_dict[digit] * pow(5, idx)

    return number

def decimal_to_snafu(decimal):
    number = []

    while True:
        q = decimal // 5
        r = decimal % 5
        number.append(reversed_values_dict[r])
        decimal = q

        if q == 0:
            break

    snafu = ""
    add = "0"

    rv = {value: key for key, value in values_dict.items()}

    i = 0
    while i < len(number):
        digit = number[i]
        sum = values_dict[digit[1]] + values_dict[add]

        if sum > 2:
            number[i] = reversed_values_dict[sum]
            add = "0"
            continue

        snafu = rv[sum] + snafu
        add = digit[0]
        i += 1

    if add != "0":
        return add + snafu

    return snafu

print("Aoc 24.1")
print(decimal_to_snafu(sum([snafu_to_decimal(snafu) for snafu in input])))
print("Aoc 24.2")