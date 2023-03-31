import datetime
import hashlib
import sys
import time
from datetime import datetime
import random
max_nonce = 4294967295

message = input("메시지의 내용 : ")
Target_bit = input("Target bits : ")

Target_bit = '0x' + Target_bit
exponent = int('0x'+Target_bit[2:4],16)
coefficient = int('0x'+Target_bit[4:10],16)

Target = coefficient * 2 ** (8*(exponent-3))
Target = hex(Target)[2:].zfill(64)
Target = '0x' + Target
print("Target : " + str(Target))

result = 0
i=1
start = time.time()
new_time = time.time()
temp_count = 0
while(1):
    print("작업 증명 중입니다 잠시만 기다려 주십시오..")
    new_time=time.time()
    for i in range(max_nonce):
        h=hashlib.sha256()
        h.update((message + str(new_time) + hex(i)).encode())
        hash_data = h.hexdigest()
        if int(hash_data,16) < int(Target,16):
            temp_count = 1
            result = i
            break
    if temp_count==1:
        break


print("메시지 학번 = " + message +"Extra nonce = " + str(new_time) + " nonce : " + hex(result))
print("실행 시간" + str(time.time()-start) + "초")
print("해시 결과 0x" + hash_data)
