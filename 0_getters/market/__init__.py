import rsa

public_key, private_key = rsa.newkeys(512)

def encrypt_data(plainText):
    return rsa.encrypt(plainText.encode(),public_key)

def decrypt_data(encryptedData):
    return rsa.decrypt(encryptedData, private_key).decode()
