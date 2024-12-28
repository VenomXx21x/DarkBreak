import itertools
import string

def generate_passwords(output_file, min_length, max_length):
    """
    Generate a password list and save it to a file.
    
    :param output_file: The file to save the passwords.
    :param min_length: Minimum length of passwords.
    :param max_length: Maximum length of passwords.
    """
    # Define character sets
    numbers = "0123456789"
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    special_chars = "!@#$%^&*()_+=-[]{}|;:',.<>?/`~"
    
    # Indian and common names (expandable list)
    common_names = [
        "rahul", "aman", "priya", "sneha", "ankit", "ankush", "ritesh", "abhilash",
        "shriram", "aditya", "rohan", "nikhil", "pankaj", "deepak", "manoj", "raj",
        "amit", "neha", "kajal", "swati", "arjun", "krishna", "ajay", "meena",
        "pooja", "rajat", "shivam", "akash", "ravi", "varun", "anil", "vishal"
    ]
    
    # Combine character sets
    all_chars = numbers + lower_case + upper_case + special_chars
    
    # Open the output file for writing
    with open(output_file, "w") as f:
        # Generate combinations with names
        for name in common_names:
            for year in range(1900, 2026):  # Years from 1900 to 2025
                f.write(f"{name}{year}\n")
                f.write(f"{name.capitalize()}{year}\n")
                for char in special_chars:
                    f.write(f"{name}{char}{year}\n")
                    f.write(f"{name.capitalize()}{char}{year}\n")
        
        # Generate permutations for given lengths
        for length in range(min_length, max_length + 1):
            for password in itertools.product(all_chars, repeat=length):
                f.write("".join(password) + "\n")

if __name__ == "__main__":
    output_file = "passforge_password_list.txt"  # File to save the passwords
    min_length = 6  # Minimum password length
    max_length = 8  # Maximum password length (adjust for larger lists)
    
    print(f"Generating passwords. This may take a while...")
    generate_passwords(output_file, min_length, max_length)
    print(f"Password list saved to {output_file}.")
