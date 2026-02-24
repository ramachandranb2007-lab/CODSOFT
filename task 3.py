import random
print("=== Welcome to Password Creator ===")
size = int(input("How many characters do you want in your password "))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*!?"
all_chars = letters + numbers + symbols
result = []
for count in range(size):
    random_char = all_chars[random.randint(0, len(all_chars) - 1)]
    result.append(random_char)
final_password = "".join(result)
print("Your new password is:", final_password)
print("Keep it safe!")
