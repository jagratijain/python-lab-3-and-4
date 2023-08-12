#Write a function in Python with a string such that it accepts a parameter
def decode_encoded_string(stringsplit):
    parts = stringsplit.split('_')
    
    name = parts[0].strip()
    domain_name = parts[1].strip()
    regno = parts[2].strip()
    
    decoded_dict = {
        "name": "jagratijain",
        "Domain_name": "hostel management",
        "Regno": 2347225
    }
    
    return decoded_dict

# Test the function
encoded_string = " jagratijain___hostelmanagement____2347225"
decoded_dict = decode_encoded_string(encoded_string)
print(decoded_dict)






