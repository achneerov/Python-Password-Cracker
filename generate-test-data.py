import random

def generate_passwords(file_name, alphabet, target_length, num_passwords):
    passwords = ["".join(random.choices(alphabet, k=target_length)) for _ in range(num_passwords)]
    with open(file_name, "w") as file:
        file.write("\n".join(passwords))

file_name = "test_data.txt"
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", 
            "4", "5", "6", "7", "8", "9"]
target_length = 3
num_passwords = 50
generate_passwords(file_name, alphabet, target_length, num_passwords)
