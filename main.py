import time
from collections import deque


alphabet = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", 
    "4", "5", "6", "7", "8", "9"
)

def guess_password(guess_password, real_password):
    return guess_password == real_password

def crack_password_slow(password):
    passwords_to_try = [""]
    while passwords_to_try:
        current_guess = passwords_to_try.pop(0)
        if guess_password(current_guess, password):
            return current_guess
        for letter in alphabet:
            passwords_to_try.append(current_guess + letter)

def crack_password_fast(password):
    passwords_to_try = deque([""])
    while passwords_to_try:
        current_guess = passwords_to_try.popleft()
        if guess_password(current_guess, password):
            return current_guess
        for letter in alphabet:
            passwords_to_try.append(current_guess + letter)

if __name__ == "__main__":
    target_func = crack_password_fast
    file_path = "test_data.txt"
    with open(file_path, "r") as file:
        passwords = [line.strip() for line in file]
    start_time = time.time()
    for password in passwords:
        result = target_func(password)
        print(f"Password: {password}, Cracked: {result}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")
