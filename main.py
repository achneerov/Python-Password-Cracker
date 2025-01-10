import itertools
import time

# Define the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Function to generate all possible combinations of increasing length and calculate the actual time
def crack_password(target_password):
    length = 1  # Start with length 1
    total_combinations = 0
    start_time = time.time()  # Start the clock for actual time
    
    while True:
        # Generate all possible combinations of the current length
        for combination in itertools.product(alphabet, repeat=length):
            # Join the tuple into a string and check if it matches the target password
            guess = ''.join(combination)
            total_combinations += 1
            if guess == target_password:
                end_time = time.time()  # End the clock
                actual_time_seconds = end_time - start_time  # Actual time in seconds
                print(f"Password found: {guess}")
                print(f"Actual Time to crack: {actual_time_seconds:.2f} seconds")
                print(f"Total combinations tried: {total_combinations}")
                return guess
        length += 1  # Increase the length and try again

# Main program
if __name__ == "__main__":
    user_password = input("Enter your password for testing (it won't be saved): ")
    crack_password(user_password)
