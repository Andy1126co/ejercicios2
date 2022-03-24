def convert_decimal(number):
    binary = []
    while number != 0:
        if number % 2 != 1:
            binary.append(str(0))
        else:
            binary.append(str(1))
        number = int(number / 2)
    binary.reverse()
    binary = "".join(binary)
    return int(binary)


def convert_binary(number):
    con = 0
    end = 0
    for i in str(number)[::-1]:
        if i == "1":
            end = end + 2**con
        con = con + 1
    return end


def run():
    print(convert_decimal(97))
    print(convert_binary(1100001))


if __name__ == "__main__":
    run()
