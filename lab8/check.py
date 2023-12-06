from sys import argv
import hashlib
import requests

def getFileInfo(file_path):
    with open(file_path, "rb") as file:
        hash = hashlib.sha256(file.read()).hexdigest()
    response = requests.request("GET", f'https://www.virustotal.com/api/v3/files/{hash}', headers={'x-apikey': 'ff17926dabe4e779a98034031ce6f42561316420953dbf2c4af1b5b162418ade'})
    if response.status_code == 200:
        return response.json()

if __name__ == "__main__":
    content = getFileInfo(argv[1])
    print(content['data']['attributes']['last_analysis_stats'])
