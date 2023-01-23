for n in range(1, 100):
    result = ""
    # print(f"[{n}]")

    if n % 3 == 0:
        result += "fizz"
    if n % 5 == 0:
        result += "buzz"
    if n % 3 != 0 and n % 5 != 0:
        print(n)

    if result != "":
        print(result)
