def maj(x, y, z):
    sum = (x + y + z)
    if (sum == 0) or (sum == 1):
        return 0
    if (sum == 2) or (sum == 3):
        return 1

def XOR(a, b):
    if ((a + b) == 1):
        return 1
    else:
        return 0

def xstep(x):
    tx = XOR(XOR(x[13],x[16]), XOR(x[17], x[18]))
    for i in range(18, 0, -1):
        x[i] = x[i-1]
        x[0] = tx
    return x

def ystep(y):
    ty = XOR(y[20], y[21])
    for i in range(21, 0, -1):
        y[i] = y[i-1]
        y[0] = ty
    return y

def zstep(z):
    tz = XOR(XOR(z[7], z[20]), XOR(z[21], z[22]))
    for i in range(22, 0, -1):
        z[i] = z[i-1]
        z[0] = tz
    return z

def main():
    keys = []

    x = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    y = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    z = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]

    for i in range(32):
        nx = x[8]
        ny = y[10]
        nz = z[10]

        m = maj(nx, ny, nz)

        if (nx == m):
            x = xstep(x)
        if (ny == m):
            y = ystep(y)
        if (nz == m):
            z = zstep(z)

        bit = XOR(XOR(x[18], y[21]), z[22])
        keys.append(bit)

    print(keys)
    print("X: ", end="")
    print(x)
    print("Y: ", end="")
    print(y)
    print("Z: ", end="")
    print(z)

if __name__ == "__main__":
    main()
