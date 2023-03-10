from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet


with open("private_key.pem","rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),None,default_backend()
    )

with open("public_key.pem","rb") as key_file :
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        default_backend()
    )


message = input("메시지(PlainText)를 입력해주세요 : ")
message = bytes(message,'utf-8')

aes_key = Fernet.generate_key()
f1 = Fernet(aes_key)
enc_msg = f1.encrypt(message)

enc_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None
    )
)


d_aes_key = private_key.decrypt(
    enc_key,
    padding.OAEP(
        padding.MGF1(hashes.SHA256()),
        hashes.SHA256(),
        None
    )
)

f2 = Fernet(d_aes_key)
d_message = f2.decrypt(enc_msg)

original_message = d_message.decode('utf-8')
print(original_message)