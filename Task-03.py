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

type_dict = type(data)
type_list = type(list())


# def dict_print(dict_for_prn):
#     keys_dict = dict_for_prn.keys()
#     for i in keys_dict:
#         if type(i) == type_dict:
#             dict_print(i)
#         elif type(i) == list:
#             print(f'ключ {i} содержит значения', end=' ')
#             print(vol for vol in dict_for_prn[i])
#         else:
#             print(dict_for_prn[i])


def dict_print(dict_for_prn):
    list_keys = list()
    keys = dict_for_prn.keys()
    return


print('Списки ключей и значений словаря:')
print(dict_print(data))


# В “ETH” добавить ключ “total_diff” со значением 100.
#
# Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
#
# Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
#
# Внутри "sec_token_info" изменить название ключа “price” на “total_price”.