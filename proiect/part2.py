import hashlib
import pprint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad



letters = ['c', 'o', 's', 'm', 'i', 'n']
base = 'my_name/'
files = ['c.ppm', 'o.ppm', 's.ppm', 'm.ppm', 'i.ppm', 'n.ppm']
hashes = []

key = b'asta e o cheieputernicdezvoltata'
cipher = AES.new(key, AES.MODE_ECB)

for file in files:
    with open(base + file, 'rb') as img:
        content = img.readlines()

        header = ''
        for i in range(3):
            header += content[i].rstrip().decode() + ' '
        hashes.append(hashlib.sha256(header.rstrip().encode()).hexdigest())

        data = b''
        for line in content[3 : ]:
            data += line
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))

        with open(base + "encr_" + file, 'wb') as encr_img:
            encr_img.write(encrypted_data)

pprint.pprint(hashes)
