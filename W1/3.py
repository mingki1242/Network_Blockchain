from cryptography.fernet import Fernet

fd = open("data.txt" , 'r')
data = fd.read()
E_fd = open("encrypted.txt" , 'w')
key = Fernet.generate_key()
f=Fernet(key)
token = f.encrypt(data.encode()).decode()
print("암호문 : " + token)
E_fd.write(token)
E_fd.close()
E_fd = open("encrypted.txt" , 'r')
_data = E_fd.read()
d = f.decrypt(_data.encode()).decode()
print("복호문 : " + d)