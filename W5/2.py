import datetime
import hashlib
import sys
import time
from datetime import datetime
import random

now = datetime.now()
message = input("메시지의 내용 : ")
Target_bit = input("Target bits : ")

Target_bit = '0x' + Target_bit
exponent = int('0x'+Target_bit[2:4],16)
coefficient = int('0x'+Target_bit[4:10],16)

Target = coefficient * 2 ** (8*(exponent-3))
Target = hex(Target)[2:].zfill(64)
Target = '0x' + Target
print(Target)

result = 0
i=0
start = time.time()


while(1):
    new_time = time.time()
    h=hashlib.sha256()
    h.update((message + str(new_time) + hex(i)).encode())
    hash_data = h.hexdigest()
    print(int(hash_data,16))
    print(int(Target,16))
    if int(hash_data,16) < int(Target,16):
       result = i
       break
    else:
        i = random.randrange(0,4294967295)



print(Target)
print("메시지 학번=" + message +"Extra nonce = " + str(new_time) + "nonce : " + hex(result))
print("실행 시간" + str(time.time()-start) + "초")
print("해시 결과" + hash_data)
