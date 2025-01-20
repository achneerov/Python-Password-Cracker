# Password Cracking Efficiency

This project demonstrates different techniques for password cracking, comparing their performance using various methods. It includes generating random passwords and cracking them using three different approaches: a slow version, a fast version, and a super-fast version.

## Project Structure

- **main.py**: This is the main script that attempts to crack passwords using different algorithms.
- **generate-test-data.py**: This script generates test data for the passwords to be cracked. It creates a list of random passwords and saves them to a file.
- **test_data.txt**: A file containing randomly generated passwords (created by the `generate-test-data.py` script).

## How to Run the Project

### Prerequisites

Ensure you have Python 3 installed on your machine. You also need the following Python libraries:
- `random`
- `itertools`

These are built-in libraries, so no additional installations are necessary.

### Step-by-Step Instructions

1. **Generate Test Data**:
   
   First, generate the test passwords using the `generate-test-data.py` script. This will create a file called `test_data.txt` with 50 randomly generated passwords of length 3 (you can change the number and length of passwords by modifying the script).

   ```bash
   python generate-test-data.py
   ```

2. **Crack Passwords**:
   
   Once the `test_data.txt` file is generated, run the `main.py` script to crack the passwords using the different methods defined in the code.

   ```bash
   python main.py
   ```

   The script will:
   - Read the passwords from `test_data.txt`.
   - Try to crack each password using the different techniques.
   - Print the results along with the time taken for each method.

### Code Explanation

#### `generate-test-data.py`

- **Function**: Generates random passwords and writes them to a file.
- **Parameters**:
  - `file_name`: Name of the file where passwords will be saved (default is `test_data.txt`).
  - `alphabet`: The character set used to generate passwords (letters and digits).
  - `target_length`: The length of each password to be generated.
  - `num_passwords`: The number of passwords to generate.

#### `main.py`

This file contains the following functions:

1. **guess_password**:
   - Compares the guessed password to the actual password.
   
2. **crack_password**:
   - A slow method that uses a list to store the possible password guesses and checks them one by one.
   
3. **crack_password_fast**:
   - A faster method that uses a deque (double-ended queue) to allow constant time pops from the front, which improves the speed compared to using a list.
   
4. **crack_password_superfast**:
   - The fastest method using `itertools.product` to generate password combinations efficiently on-the-fly. This avoids storing all combinations in memory at once.

#### Performance Comparison

- **`crack_password`**: The slowest method, using a list and popping from the front (O(n) time complexity per pop).
- **`crack_password_fast`**: Faster than the previous method, as it uses a deque (O(1) time complexity for pop operations).
- **`crack_password_superfast`**: The fastest method, using `itertools.product` to generate combinations on-the-fly without storing them, which reduces memory usage and time.

### Test Results

- For cracking 50 passwords of length 3, the following times were observed:
  - `crack_password`: Took **85.12 seconds** due to inefficient popping from a list.
  - `crack_password_fast`: Took **1.48 seconds**, improved by using a deque for efficient pops.
  - `crack_password_superfast`: Took **0.08 seconds**, the fastest approach by generating combinations with `itertools.product`.

### Notes

- You can modify the `alphabet`, `target_length`, and `num_passwords` parameters to change the size and complexity of the generated passwords.
- The algorithms are tested on small datasets, but they can be adapted to handle larger datasets depending on system resources.