import bcrypt

password = input("Password: ")

byte = password.encode("utf-8")

salt = bcrypt.gensalt()

hashed_password = bcrypt.hashpw(byte,salt)
print(hashed_password)
