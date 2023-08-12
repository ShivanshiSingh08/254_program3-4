def decode_string(stringsplit):
    parts = stringsplit.split('__')
    
    name = parts[0].strip()
    domain_name = parts[1].strip()
    regno = parts[2].strip()
    
    decoded_dict = {
        "name": name,
        "Domain_name": domain_name,
        "Regno": regno,
    }
    
    return decoded_dict

input_string = input("Enter the encoded string: ")
decoded_result = decode_string(input_string)
print(decoded_result)
