import hashlib
import os
import time
import random

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
q = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
e1_x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
e1_y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8


#역원 구하는 함수
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

def Sign(M,d) :
    r = random.randrange(1,q)
    P = Double_And_Add_Operation(e1_x , e1_y , r, p)
    S1 = P[0] % q
    h = hashlib.sha256()
    h.update(M.encode())
    hash_data = h.hexdigest()
    S2 = ((int(hash_data,16) + d * S1) * Extended_Uclidean(q,r)) % q
    print("1. Sign:")
    print("S1 = " + hex(S1))
    print("S2 = " + hex(S2))
    return [S1 , S2]

def Verify(M , S1 , S2 , e2):
    h = hashlib.sha256()
    h.update(M.encode())
    hash_data = h.hexdigest()
    A = (int(hash_data,16) * Extended_Uclidean(q,S2)) % q
    B = (S1 * Extended_Uclidean(q,S2)) % q

    T1 = Double_And_Add_Operation(e1_x,e1_y,A,p)
    T2 = Double_And_Add_Operation(e2[0],e2[1],B,p)

    answer = Add_Operation(T1 , T2 , p)

    print("A = " + hex(A))
    print("B = " + hex(B))

    if answer[0]%q == S1%q :
        return True
    else:
        return False


def random_key_generate():
    r = str(os.urandom(32)) + str(random.random()) + str(int(time.time() * 1000000))
    r = bytes(r, 'utf-8')
    h = hashlib.sha256(r).digest()
    key = ''.join('{:02x}'.format(y) for y in h)
    return key

while (1):
    private_key = random_key_generate()
    if int(private_key, 16) < p:
        break
#개인키
d = int(private_key,16)

Message = input("메시지? ")
P = Sign(Message , d)
print("2. 정확한 서명을 입력할 경우:")
e2 = Double_And_Add_Operation(e1_x , e1_y , d ,p)
if Verify(Message , P[0] , P[1] , e2) == True :
    print("검증 성공")
else :
    print("검증 실패")
print("3. 잘못된 서명을 입력할 경우:")
if Verify(Message, P[0]-1, P[1]-1, e2) == True:
    print("검증 성공")
else:
    print("검증 실패")

print("heelo")


