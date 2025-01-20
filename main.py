import time
from collections import deque
import itertools


alphabet = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", 
    "4", "5", "6", "7", "8", "9"
)

def guess_password(guess_password, real_password):
    return guess_password == real_password

# Slow version: Uses a list (which requires O(n) for pop operation), iterating through all combinations one by one.
def crack_password(password):
    passwords_to_try = [""]
    while passwords_to_try:
        current_guess = passwords_to_try.pop(0)  # Pop from the start of the list, which is slow
        if guess_password(current_guess, password):
            return current_guess
        for letter in alphabet:
            passwords_to_try.append(current_guess + letter)

# Faster version: Uses deque (double-ended queue) which allows O(1) pops from the left (front).
def crack_password_fast(password):
    passwords_to_try = deque([""])  # Deque allows popping from the front in constant time (O(1))
    while passwords_to_try:
        current_guess = passwords_to_try.popleft()  # Deque allows for fast pop from the left
        if guess_password(current_guess, password):
            return current_guess
        for letter in alphabet:
            passwords_to_try.append(current_guess + letter)

# Even faster version: Uses itertools.product to generate all combinations efficiently, iterating by length.
def crack_password_superfast(password):
    length = 1
    while True:
        # itertools.product generates combinations more efficiently by directly creating tuples of characters.
        # This avoids manually creating and managing an explicit list or deque, which would require additional memory 
        # and time to construct, append, and pop elements.
        for combo in itertools.product(alphabet, repeat=length):
            # itertools.product works by producing combinations directly from the input iterable without storing them in memory
            # at once. This makes it memory-efficient compared to storing intermediate lists or strings.
            current_guess = ''.join(combo)  # Efficiently joins the tuple to form the guess string
            if guess_password(current_guess, password):
                return current_guess
        length += 1

if __name__ == "__main__":
    target_func = crack_password_superfast
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

# Test results for cracking 50 passwords of length 3:
# - `crack_password` took 85.12 seconds: This method uses a list and pops from the front (O(n) time complexity per pop), 
#   which results in significant overhead as the list grows, leading to slower performance with increasing password lengths.
#
# - `crack_password_fast` took 1.48 seconds: This method uses a deque, which allows O(1) pops from the front, reducing the 
#   overhead compared to using a list. However, it still uses a manual approach to generate and store each password combination 
#   before checking it, leading to slower performance than the final version.
#
# - `crack_password_superfast` took 0.08 seconds: This version uses `itertools.product` to efficiently generate combinations 
#   on-the-fly without storing them all at once in memory. This allows it to quickly generate combinations without the 
#   overhead of managing additional data structures and handles increasing password lengths more efficiently. As a result, it 
#   is significantly faster than the other two methods.
