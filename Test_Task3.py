data = {
    'id': '01',
    'address': {
        'ip': '192.168.0.10',
        'mask': '255.255.255.0',
        'gateway': '192.168.0.1',
        'dns': ['192.168.0.230', '192.168.0.231']
    }
}


def find_keys(user_dict, list_keys):

    if type(user_dict) is dict:
        key = user_dict.keys()
        for k in key:
            if type(user_dict[k]) is dict:
                find_keys(user_dict[k].keys(), list_keys)
                # print(data[k].keys())

            else:
                list_keys.append(k)
    return list_keys


list_user_key = list()
print(find_keys(data, list_user_key))
print(data.keys())
