from time import perf_counter


def timeit(func):
    def inner(*args, **kwargs):
        marker = perf_counter()
        r = func(*args, **kwargs)
        elapsed = perf_counter() - marker
        print(f"[{func.__name__}] {elapsed * 1000:.3f}ms")
        return r

    return inner


MAGIC_NUMBER = 391
to_decode = "FPDGXANT"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = [4 / 23, -3 / 23, -7 / 23, 11 / 23]


@timeit
def chunks(word):
    if len(word) % 2:
        print("Error odd word length")
        quit()

    return tuple(word[i: i + 2] for i in range(0, len(word), 2))


@timeit
def decode(ciphered_pairs):
    deciphered_pairs = ""
    a, b, c, d = key
    for left, right in ciphered_pairs:
        left = alphabet.index(left)
        right = alphabet.index(right)
        deciphered_pairs += (
            alphabet[round((MAGIC_NUMBER * ((a * left) + (b * right))) % len(alphabet))]
        ) + (alphabet[round((MAGIC_NUMBER * (c * left + d * right)) % len(alphabet))])
    return deciphered_pairs


@timeit
def main():
    is_running = True
    while is_running:
        action = input(
            "WELCOME TO HILL \n"
            "- Encode (e) \n"
            "- Decode (d) \n"
            "- View Key (v) \n"
            "- Change key (c) \n"
            "- Quit (q) \n"
            ">>> "
        )

        if action == "e":
            print("Not implemented xD")
        elif action == "d":
            print(decode(chunks(to_decode)))
        elif action == "v":
            print(key)
        elif action == "c":
            print("Not implemented xD")
        elif action == "q":
            is_running = False


if __name__ == "__main__":
    main()
