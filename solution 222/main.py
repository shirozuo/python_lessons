import urllib.request

_encrypted_url = "https://stepik.org/media/attachments/lesson/24466/encrypted.bin"
_passwords_url = "https://stepik.org/media/attachments/lesson/24466/passwords.txt"

encrypted = urllib.request.urlopen(_encrypted_url).read()
passwords = urllib.request.urlopen(_passwords_url).read().strip().split()

print(encrypted)
print(passwords)
