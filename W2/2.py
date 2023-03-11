import hashlib
import os
import time
import random

def Extended_Uclidean(n, b):
    r1, r2 = n, b
    t1, t2 = 0, 1
    while r2:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r
        t = t1 - q * t2
        t1 = t2
        t2 = t

    if r1 != 1:
        return 0
    if t1 < 0:
        t1 = n + t1
    return t1



def Double_And_Add_Operation(Gx, Gy, key, dp):
    tmp = int(key, 16)
    Binary_String = bin(tmp)
    Binary_String = Binary_String[3:len(Binary_String)]

    R_Gx = Gx
    R_Gy = Gy

    for currentBit in Binary_String:
        slope = (3 * (R_Gx **2) * Extended_Uclidean(dp, 2 * R_Gy))%dp
        PR_Gx = R_Gx
        R_Gx = ((slope **2) - PR_Gx - PR_Gx) % dp
        R_Gy = (slope * (PR_Gx - R_Gx) - R_Gy) % dp

        if currentBit == '1':
            if R_Gx >= Gx:
                slope = ((R_Gy-Gy) * (Extended_Uclidean(dp,R_Gx-Gx)))%dp
                R_Gx = ((slope**2) - Gx - R_Gx) % dp
                R_Gy = (slope * (Gx - R_Gx) - Gy) % dp
            else:
                PR_Gx = R_Gx
                slope = ((Gy-R_Gy) * (Extended_Uclidean(dp,Gx-R_Gx)))%dp
                R_Gx = ((slope**2) - R_Gx - Gx) % dp
                R_Gy = (slope * (PR_Gx - R_Gx) - R_Gy) % dp


    print("공개키(16진수) : " + hex(R_Gx))
    print("공개키(10진수) : " + str(R_Gx))
    print("공개키(16진수) : " + hex(R_Gy))
    print("공개키(10진수) : " + str(R_Gy))

    return

def random_key_generate():
    r = str(os.urandom(32)) + str(random.random()) + str(int(time.time() * 1000000))
    r = bytes(r, 'utf-8')
    h = hashlib.sha256(r).digest()
    key = ''.join('{:02x}'.format(y) for y in h)
    return key

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F


while (1):
    private_key = random_key_generate()
    if int(private_key, 16) < p:
        break




Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

print("개인키(16진수) : " + private_key)
print("개인키(10진수) : " + str(int(private_key,16)))
print("")
Double_And_Add_Operation(Gx, Gy, private_key,p)
