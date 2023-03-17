import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
q = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
e1_x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
e1_y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
#개인키
d = 3
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

    if r1 > 1:
        return None
    if t1 < 0:
        t1 = n + t1
    return t1 % n

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
    r = 3
    P = Double_And_Add_Operation(e1_x , e1_y , 41003466362608940562794629182404967427451760136744234558038380002801394949900 , p)
    S1 = P[0] % q
    h = hashlib.sha256()
    h.update(M.encode())
    hash_data = h.hexdigest()
    S2 = (int(hash_data,16) + d * S1) * Extended_Uclidean(q,41003466362608940562794629182404967427451760136744234558038380002801394949900) % q
    print("S1 = " + hex(S1))
    print("S2 = " + hex(S2))

Message = input("메시지? ")
Sign(Message , 3)

'''h = hashlib.sha256()
h.update(b'Secret message')
hash_data = h.hexdigest()

r = (int(hash_data,16) + 3 * 0xf06d76e6364b9e31f36c18c4174fdd21c8aac52a7f238ba362bff718b477e70a) * Extended_Uclidean(q, 0xd46899ff4dd7be8636911a9ae29e20c3c5acb5fbd3c24c3a208e4b981a820e64) % q
print(r)'''