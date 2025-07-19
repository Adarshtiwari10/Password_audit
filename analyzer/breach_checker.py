import hashlib
import requests
def is_password_breach(password:str)->bool:
    hash_object = hashlib.sha1(password.encode('utf-8'))
    hex_digest = hash_object.hexdigest().upper()
    prefix = hex_digest[:5]
    suffix = hex_digest[5:]
    # print(f"prefix: {prefix}")
    # print(f"suffix: {suffix}")
    # print(f"full Hash: {hex_digest}")

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code!=200:
        raise RuntimeError(f"API request failed with status: {response.status_code}")

    hashes = response.text.splitlines()
    for line in hashes:
        suffix_candidate, count = line.strip().split(":")
        if suffix_candidate == suffix:
            # print(f"Password found in breach database with count: {count}")
            return True #ie found the breach paasword in db
    return False
    