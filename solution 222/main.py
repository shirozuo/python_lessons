import urllib.request
from simplecrypt import decrypt, DecryptionException

_encrypted_url = "https://stepik.org/media/attachments/lesson/24466/encrypted.bin"
_passwords_url = "https://stepik.org/media/attachments/lesson/24466/passwords.txt"

encrypted = urllib.request.urlopen(_encrypted_url).read()
passwords = urllib.request.urlopen(_passwords_url).read().strip().split()

decrypted_list = list()
for password in passwords:
    print("Trying password: ", password)
    try:
        message = decrypt(password, encrypted).decode("utf-8")
        decrypted_list.append(message)
        print("VALID PASSWORD:", password, "DECRYPTED MESSAGE:", message)
    except DecryptionException as e:
        print("Found error: ", e)

print("\n" + "All decrypted messages:")
print("\n".join(decrypted_list))
