# implement theoretical iris scan comparison

def compare(x, y):
    c = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            c += 1
    return c

def convert(code):
    return str(bin(int(code, 16))[2:].zfill(64))

def main():
    Alice = "BE439AD598EF5147"
    Bob = "9C8B7A1425369584"
    Charlie = "885522336699CCBB"
    U = "C975A2132E89CEAF"
    V = "DB9A8675342FEC15"
    W = "A6039AD5F8CFD965"
    X = "1DCA7A54273497CC"
    Y = "AF8B6C7D5E3F0F9A"

    reg = [Alice, Bob, Charlie]
    regnames = ["Alice", "Bob", "Charlie"]
    rec = [U, V, W, X, Y]
    recnames = ['U', 'V', 'W', 'X', 'Y']

    for i in range(3):
        reg[i] = convert(reg[i])

    for i in range(5):
        rec[i] = convert(rec[i])

    for i in range(3):
        for j in range(5):
            r = compare(reg[i],rec[j])
            if i == 0:
                s = "  "
            elif i == 1:
                s = "    "
            else:
                s = ""
            print(f"{regnames[i]} and {s} {recnames[j]} = {r} / 64 = {r / 64}")

if __name__ == "__main__":
    main()
