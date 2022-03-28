data = {
    'id': '01',
    'address': {
        'ip': '192.168.0.10',
        'mask': '255.255.255.0',
        'gateway': '192.168.0.1',
        'dns': ['192.168.0.230', '192.168.0.231']
    }
}


def find_keys(user_dict):
    list_keys = list()
    if user_dict is dict:
        key = user_dict.keys()
        for k in key:
            if type(user_dict[k]) is dict:
                list_keys.extend(find_keys(user_dict[k].keys()))
                # print(data[k].keys())

            else:
                list_keys.append(k)
    return list_keys

print(find_keys(data))
