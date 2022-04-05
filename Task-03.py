# Задача 3. Криптовалюта

data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
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

# В “ETH” добавить ключ “total_diff” со значением 100.
data['ETH']['total_diff'] = '100'
print(data)

# Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
data['tokens'][0]['fst_token_info']['name'] = 'doge'
print(data)

# Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
data['ETH']['totalOut'] = data['tokens'][0]['total_out']
del(data['tokens'][0]['total_out'])
print(data)

# Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
# data.pop(data['tokens'][1]['sec_token_info']['price'])
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
print(data)
