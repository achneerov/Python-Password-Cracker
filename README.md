# Brute-Force Password Cracker

This Python program performs a brute-force attack to crack a password by trying all possible combinations of characters, starting from 1 character in length and increasing incrementally. It measures the actual time taken to crack the password and displays the number of combinations tested.

## Features

- Uses a predefined alphabet of characters.
- Cracks passwords by generating all possible combinations.
- Displays the **actual time** taken to crack the password.
- Tracks and displays the **total number of combinations tested**.

## Requirements

- Python 3.x or higher.
- No external dependencies (uses Python's built-in `itertools` and `time` modules).

## Installation

There is no installation required other than Python itself.

1. Ensure you have Python 3.x installed on your system. You can check this by running:

   ```bash
   python --version
   ```

2. Clone or download this repository to your local machine.

3. Navigate to the folder containing the Python script.

## Usage

1. Open a terminal or command prompt.
2. Run the script by executing:

   ```bash
   python brute_force_password_cracker.py
   ```

3. When prompted, enter the password you'd like to test. For example:

   ```
   Enter your password for testing (it won't be saved): abc
   ```

   The program will attempt to crack the password using a brute-force method, starting with length 1 combinations and increasing in length. Once the password is found, it will display:

   - The cracked password
   - The actual time taken to crack the password
   - The total number of combinations tried

### Example:

```bash
Enter your password for testing (it won't be saved): abc
Password found: abc
Actual Time to crack: 0.35 seconds
Total combinations tried: 731
```

## How It Works

1. **Alphabet Definition**: The program uses a predefined set of characters, which includes:
   - Lowercase letters (`a-z`)
   - Uppercase letters (`A-Z`)
   - Digits (`0-9`)
   - Special characters (`!@#$%^&*()`)

2. **Brute Force Mechanism**: The program iterates through all possible combinations of characters, starting with 1-character combinations and increasing the length as necessary. It checks each generated string against the target password.

3. **Timing**: The program calculates and displays the actual time it takes to crack the password. It also shows the total number of combinations it tested before finding the correct one.

4. **Performance**: The time required for cracking depends on the password's length and the number of possible combinations. Longer passwords with a larger set of characters will require significantly more time to crack.

## Limitations

- **Performance**: This program uses brute-force, meaning it is computationally expensive and slow, especially for longer passwords or larger alphabets.
- **Password Length**: If the password is very long or contains many characters from a large alphabet, it will take a considerable amount of time to crack.
