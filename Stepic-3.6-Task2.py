import requests

const_url = 'https://stepic.org/media/attachments/course67/3.6.3/'


def request_url(url):
    r = requests.get(url).text.strip()
    if r.startswith('We'):
        return r
    else:
        new_url = const_url + r
        request_url(new_url)


with open('dataset_3378_3.txt', 'r') as file_user:
    start_url = file_user.readline().strip()
print(request_url(start_url))

