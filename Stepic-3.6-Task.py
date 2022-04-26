import requests

with open('dataset_3378_2.txt', 'r') as file_url:
    url = file_url.readline().strip()

r = requests.get(url)

with open('answ.txt', 'w') as answ:
    answ.writelines(r.text)

count = 0

with open('answ.txt', 'r') as inpt:
    for i in inpt:
        count += 1

print(count)

