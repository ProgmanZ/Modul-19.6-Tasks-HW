# import math
# print(math.pi * 2 * float(input()))

# import sys
# print(' '.join(sys.argv[1:]))
# import requests
# import os
import subprocess

with open('test-input.txt', 'w') as inpt:
    # l = subprocess.call(['python', '-h'], stdout=1)
    l = subprocess.call(['python', '-h'], stdout=inpt)



#
#
# url = 'https://outlook.office365.com'
#
# key = {'key1':'value1', 'key2':'value2'}
# r = requests.get(url, params=key)
# print(r.url)