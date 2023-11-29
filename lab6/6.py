import os
from functools import reduce
from operator import xor
from Crypto.Cipher import DES

def LFSR():
    c = [int(x) for x in input("State coefficients : ").split()]
    c.reverse()
    s = [int(x) for x in input("State values: ").split()]
    
    if len(c) != len(s):
        return
        
    period, initial_seed, output_seq = 0, s, []

    while True:
        print(s)
        period += 1
        s = s[1:] + [reduce(xor, [x & y for x, y in zip(c, s)])]
        output_seq.append(s[-1:])
        if s == initial_seed:
            break

    print(period)

def ex2():
    pass
""" 
a) Obtinem $data criptat cu $key

b) ECB, textul criptat are redundanta

c) Nu, chunck-urile din $data sunt translatate 1:1 in textul cifrat

d) |$key| = 128bits, exact cat a blocului AES

e) ```
    from Crypto.Util.Padding import pad
    
    data = pad(b'test', AES.block_size)
    
   ```

f) ```
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    from Crypto.Util.Padding import pad

    key = get_random_bytes(16)
    data = b'test'
    iv = get_random_bytes(16)
    
    padded_data = pad(data, AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(padded_data)
   ```
"""

def ex3():
    key1 = b"\x00" * 7
    key2 = b"\x00" * 7
    plaintext = b"Provocare MitM!!"
    ciphertext = b"G\xfd\xdfpd\xa5\xc9'C\xe2\xf0\x84)\xef\xeb\xf9"

    middle_text, candidate_keys, ciphers, keys_nr = {}, [], [], 0

    for i in range(16):
        key = (i << 4).to_bytes(1, byteorder="big") + key1
        cipher = DES.new(key, DES.MODE_ECB)
        candidate_keys.append(key)
        ciphers.append(cipher)
        encryption = cipher.encrypt(plaintext)
        middle_text[encryption] = key

    for key, cipher in zip(candidate_keys, ciphers):
        keys_nr += 1
        decryption = cipher.decrypt(ciphertext)
        if decryption in middle_text.keys():
            key1 = middle_text[decryption]
            key2 = key
            break
    
    print(f"chei testate = {keys_nr}\nkey1 = {key1}\nkey2 = {key2}")


if __name__ == "__main__":
    os.system("clear")
    while True:
        match int(input("1. LINEAR FEEDBACK SHIFT REGISTER\n3. Exercitiul 3\nyour choice: ")):
            case 1:
                LFSR()
            case 2:
                ex2()
            case 3:
                ex3()
        input("Press any key")
        os.system("clear")
