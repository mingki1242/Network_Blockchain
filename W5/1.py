import hashlib
from bitmap import BitMap

class BloomFilter:
    n=0
    def __init__(self , m , k , bm):
        self.m = m
        self.k = k
        self.bm = bm

    def getPositions(self ,item):
        arr_list = [0 for i in range(self.k)]
        for i in range(self.k):
            h = hashlib.sha256()
            h.update(str(item + str(i+1)).encode())
            hash_data = h.hexdigest()
            arr_list[i] = int(hash_data,16) % self.m
        return arr_list
    def add(self , item):
        temp_arr = item
        for i in range(self.bm.size()):
            for j in range(len(temp_arr)):
                if i == temp_arr[j]:
                    self.bm[i] = True
        return self.bm

    def contains(self , item):
        count = 0
        temp_arr = item
        for i in range(len(temp_arr)):
            for j in range(self.bm.size()):
                if j == temp_arr[i] and self.bm[j] == 1:
                    count = count+1
        if count == self.k:
            return True
        else:
            return False

    def reset(self):
        for i in range(self.bm.size()):
            self.bm[i] = 0
    def __repr__(self):
        count = 0
        print("비트 맵의 길이 : " + self.m)
        print("해시 함수의 갯수 : " + self.k)
        for i in len(self.bm):
            print(self.bm[i])
        for i in len(self.bm):
            if self.bm[i] == 1:
                count = count +1
        print("1인 비트의 수 : " + count)
        print("항목의 수 : " + self.bm.size())

num1 = input("비트맵 길이 : ")
num2 = input("해시 함수의 수 : ")
bm = BitMap(int(num1))
bf = BloomFilter(int(num1) , int(num2) , bm)



for ch in "AEIOU":
    bf.add(bf.getPositions(ch))
print("비트 맵 : " + bf.bm.tostring())

for ch in "ABCDEFGHIJ":
    print(ch , bf.contains(bf.getPositions(ch)))

