import string
# import json
from analyzer.breach_checker import is_password_breach
def analyze_strength(password:str) -> dict:
    length = len(password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    with open("data/common_passwords.txt", "r") as file:
        common_passwords = {line.strip().lower() for line in file}
        is_common = password.lower() in common_passwords

    score = sum([has_lower, has_digits, has_special, has_upper])
    if length<6:
        strength = "Very weak"
    elif score==1:
        strength ="Weak"
    elif score==2:
        strength ="Moderate"
    elif score==3:
        strength = "Good"
    elif score>=3 and length>=8:
        strength = "Excellent"
    else:
        strength = "average"
    
    Analyzer_output = {
        "length": length ,
        "has_lowercase" : has_lower,
        "has_uppercase": has_upper,
        "has_digits": has_digits,
        "has_special_characters": has_special,
        "strength": strength,
        "is_common": is_common
        
    }
    # print(json.dumps(Analyzer_output, indent=4)) #using this format because the printing order is not proper with the normal print option and other option are to use for loops to print the function or use prettyprint import 
    return Analyzer_output



















