# decrypts in.txt

import subprocess

def main():

    file = open("ciphers.txt", "r")
    ciphers = (file.read()).split()
    file.close()

    file2 = open("password.txt", "r")
    password = (file2.read()).split()
    file2.close()

    cmd = []

    for i in range(14):
        num = str(i)
        subprocess.call(["touch", "pass" + num + ".txt"])
        f = open("pass" + num + ".txt", "w")
        f.write(password[i])
        for j in range(7):
            numb = str(j)
            input = "openssl " + "enc " + "-d" + " -a " + ciphers[j] + " -in" + " in.txt " + "-out " + "empty.txt" + " -pass file:" + "pass" + num + ".txt"
            cmd.append(input)
        f.close()

    x = len(cmd)

    for c in range(x):
        status = subprocess.call([cmd[c]], shell=True)
        if (status == 0):
            print(cmd[c])


if __name__ == "__main__":
    main()

#
