def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        
ALLOWED_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

# Function to check for invalid characters
def has_invalid_chars(plate):
  return any(char not in ALLOWED_CHARS for char in plate)


def is_valid(s):
    length = len(s)
    if length < 2 or length > 6:
        return False
    if has_invalid_chars(s):
        return False
  # Check for leading letters and trailing numbers (allow 2 or 3 letters)
    if s.isalpha(): 
        return True
    else:
        # Check for number in the middle 
        # (only if the first two characters are letters and the last character is number)
        if s[:2].isalpha() and s[-2:].isdigit():
            for i in range(len(s)):
                if s[i].isdigit():
                    # Return false if number starts with 0 or the following character is letter
                    if s[i].startswith("0") or s[i:].isalpha():
                        return False
                    else:
                        return True
        else:
            return False

        
main()