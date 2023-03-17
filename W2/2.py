import hashlib
import os
import time
import random


# doublea-and-add
def _Double_And_Add_Operation(G, key):
    answer = G
    tmp = int(key, 16)
    Binary_String = bin(tmp)
    Binary_String = Binary_String[2:len(Binary_String)]
    for bit_idx in range(1,len(Binary_String)):
        currentBit = Binary_String[bit_idx]
        answer = answer + answer
        if currentBit == '1':
            answer = answer + G

    return answer


# 역원
def _Extended_Uclidean(n, b):
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


def random_key_generate():
    r = str(os.urandom(32)) + str(random.randrange(2 ** 256)) + str(int(time.time() * 1000000))
    r = bytes(r, 'utf-8')
    h = hashlib.sha256(r).digest()
    key = ''.join('{:02x}'.format(y) for y in h)
    return key


p = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F'

while (1):
    private_key = random_key_generate()
    if int(private_key, 16) < int(p,16):
        break

print(private_key)


# 기울기 구하기
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
dec_Gx = int(Gx,16)
dec_Gy = int(Gy,16)
dec_p = int(p,16)


slope = ((3*dec_Gx*dec_Gx)*(_Extended_Uclidean(dec_p,2*dec_Gy)))%dec_p
R_Gx = (slope*slope-dec_Gx)%dec_p
R_Gy = (slope*(dec_Gx-R_Gx)-dec_Gy)%dec_p


print(_Double_And_Add_Operation(dec_Gx, private_key))
print(_Double_And_Add_Operation(dec_Gy, private_key))
