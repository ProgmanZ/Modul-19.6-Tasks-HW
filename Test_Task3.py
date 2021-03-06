data = {
    'id': '01',
    'address': {
        'ip': '192.168.0.10',
        'mask': '255.255.255.0',
        'gateway': '192.168.0.1',
        'dns': [
            {'dns_primary': '192.168.0.230',
             'dns_secondary': '192.168.0.231'},
            {'dns_inet1': '8.8.8.8',
             'dns_inet2': '8.8.8.4'
             }
                ]
    }
}


def find_keys(user_dict, list_keys):
    for k in user_dict:
        if type(user_dict[k]) is dict:
            list_keys.append(k)
            find_keys(user_dict[k], list_keys)
        elif type(user_dict[k]) is list:
            for l in user_dict[k]:
                find_keys(l, list_keys)
        else:
            list_keys.append(k)
    return list_keys


def find_vol(user_dict, list_vol):
    for k in user_dict:
        if type(user_dict[k]) is dict:
            find_vol(user_dict[k], list_vol)
        elif type(user_dict[k]) is list:
            for l in user_dict[k]:
                find_vol(l, list_vol)
        else:
            list_vol.append(user_dict[k])
    return list_vol


list_user_key = list()
list_user_vol = list()

print('Все ключи словаря:', find_keys(data, list_user_key))
print('Все значения словаря:', find_vol(data, list_user_vol))
