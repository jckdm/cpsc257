# implements TEA encryption / decryption
#! /usr/bin/env python3

from operator import xor

# unsigned 32 bit integers

from ctypes import c_uint32

MASK32 = 0xffffffff
delta = c_uint32(0x9e3779b9).value
ROUNDS = 32


def add(x,y):
    return c_uint32(x + y).value

def subtract(x,y):
    return c_uint32(x - y).value

def leftshift4add(x,k):
    return add(c_uint32(x << 4).value, c_uint32(k).value)

def rightshift5add(x,k):
    return add(c_uint32(x >> 5).value, c_uint32(k).value)


class TEA:

    def __init__(self, p,k):
        self.P = p
        self.K = [c_uint32(((MASK32 << x) & k) >> x).value for x in range(96,-1,-32)]
        for x in self.K: print (hex(x))

    def encrypt(self):
        L = (self.P & (MASK32 << 32)) >> 32
        R = c_uint32(self.P).value
        summ = 0

        for _ in range(ROUNDS):
            summ = add(summ, delta)
            L = add(L,(((leftshift4add(R,self.K[0])) ^ add(R,summ)) ^ rightshift5add(R,self.K[1])))
            R = add(R,(((leftshift4add(L,self.K[2])) ^ add(L,summ)) ^ rightshift5add(L,self.K[3])))

        c = ((L << 32) + R)
        return c

    def decrypt(self, C):
        L = (C & (MASK32 << 32)) >> 32
        R = c_uint32(C).value
        summ = delta << 5

        for _ in range(ROUNDS):
            R = subtract(R,(((leftshift4add(L,self.K[2])) ^ add(L,summ)) ^ rightshift5add(L,self.K[3])))
            L = subtract(L,(((leftshift4add(R,self.K[0])) ^ add(R,summ)) ^ rightshift5add(R,self.K[1])))
            summ = subtract(summ, delta)

        p = ((L << 32) + R)
        return p

"""
Output answers
"""


if __name__ == '__main__':


    # TEA ALGORITHM
    K = 0xA56BABCD00000000FFFFFFFFABCDEF01
    # this is 2 32 bit quantities
    P = 0x0123456789ABCDEF

    T = TEA(P, K)
    C = T.encrypt()
    P2 = T.decrypt(C)
    print("Original plaintext: " + str(hex(P)))
    print("Ciphertext: " + str(hex(C)))
    print("Decrypted plaintext: " + str(hex(P2)))
