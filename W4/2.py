import hashlib
import os
import time
import random
import hashlib
import base58check
import hashlib
import base58check
from Crypto.Hash import RIPEMD160

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
def Add_Operation(P , Q , dp):
    if P == Q:
        slope = ((3 * (P[0]**2)) * Extended_Uclidean(dp , (2 * P[1])))%dp
    else:
        if Q[0] > P[0] :
            slope = ((Q[1] - P[1]) * Extended_Uclidean(dp , (Q[0] - P[0])))%dp
        else:
            slope = ((P[1] - Q[1]) * Extended_Uclidean(dp , (P[0] - Q[0])))%dp

    Tx = ((slope ** 2) - P[0] - Q[0])%dp
    Ty = (slope*(P[0]-Tx)-P[1])%dp
    return [Tx , Ty]

def Double_And_Add_Operation(Gx, Gy, key, dp):
    Binary_String = bin(key)
    Binary_String = Binary_String[3:len(Binary_String)]

    R_Gx = Gx
    R_Gy = Gy

    for currentBit in Binary_String:
        slope = ((3 * (R_Gx **2)) * (Extended_Uclidean(dp, 2 * R_Gy)))%dp
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

    return [R_Gx , R_Gy]

Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F


def random_key_generate():
    r = str(os.urandom(32)) + str(random.randrange(2**256)) + str(int(time.time() * 1000000))
    r = bytes(r, 'utf-8')
    h = hashlib.sha256(r).digest()
    key = ''.join('{:02x}'.format(y) for y in h)
    return key

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

message = input("희망하는 주소의 문자열?")
print("문자열을 찾고있습니다 잠시만 기다려주십시오...\n")

while(1):
    private_key = random_key_generate()
    Result = Double_And_Add_Operation(Gx, Gy, int(private_key,16),p)
    val = hex(Result[0])[2:]

    if Result[1]%2==0:
        Temp = "0x02" + val.zfill(64)
    else:
        Temp = "0x03" + val.zfill(64)

    tmp_arr=bytes.fromhex(Temp[2:])
    h = hashlib.sha256()
    h.update(tmp_arr)
    hash_data = h.hexdigest()

    tmp_arr = bytes.fromhex(hash_data)
    h = RIPEMD160.new()
    h.update(tmp_arr)
    answer = h.hexdigest()

    answer = "0x00" + answer
    tmp = answer[2:]

    tmp_arr = bytes.fromhex(tmp)
    h = hashlib.sha256()
    h.update(tmp_arr)
    hash_data = h.hexdigest()

    tmp_arr = bytes.fromhex(hash_data)
    h = hashlib.sha256()
    h.update(tmp_arr)
    hash_data = h.hexdigest()

    check = hash_data[0:8]
    public_hash = answer[2:]+check

    final = base58check.b58encode(bytes.fromhex(public_hash))

    if final.decode()[1:].startswith(message):
        final_answer = final.decode()
        final_private_key = private_key
        break

print("주소 = " + final_answer)
print("개인키 = " + final_private_key)

