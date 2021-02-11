import json
from pprint import pprint



def json_file():
    """функция иммитирующая json файл"""
    
    future_json_data = {
        "displayedName": {
            "displayedName": {
                "value": [
                    "Профиль маячковый ПВХ 10 мм L3м"
                ],
                "description": "Полное наименование товара для клиента"
                }
            },
        "stock": {
            "stocks": {
                    "34": {
                    "2": "35",
                    "3": "42",
                    "4": "58",
                    "5": "57",
                    "6": "112",
                    "20": "51",
                    "22": "78",
                    "26": "34",
                    "32": "22",
                    "35": "358",
                    "40": "28",
                    "43": "68",
                    "45": "58",
                    "49": "31",
                    "51": "29",
                    "56": "42",
                    "62": "26",
                    "64": "0",
                    "65": "57",
                    "86": "15",
                    "114": "41",
                    "117": "46",
                    "143": "46",
                    "162": "4",
                    "171": "0",
                    "176": "12"
                }
            }
        }
    }
    
    json_file = json.dumps(future_json_data)
    
    return json.loads(json_file)


def good_name():
    """функция выводящая название продука"""
    name = json_file()
    return name['displayedName']['displayedName']['value'][0]


def available_in(region=34):
    """
    функция проверят наличие товара в магазинах региона, 
    по умолчанию 34рег и выводит список маг
    """
    region = str(region)
    search_in = json_file()
    available_shops = search_in['stock']['stocks'][region]
    shops_with_good = []
    for key, value in available_shops.items():
        if value == '0':
            continue
        else:
            shops_with_good.append(int(key))
    return str(sorted(shops_with_good))


def higest_ratio(region=34):
    """ выводит номер магазина с наибольщим кол-вом товара """
    region = str(region)
    search_in = json_file()
    available_shops = search_in['stock']['stocks'][region]
    max_quantity_in = [0, 0]
    for key, value in available_shops.items():
        # pass
        # print(int(value) > max_quantity_in[1] )
        if int(value) < max_quantity_in[1]:
            continue
        else:
            max_quantity_in = [int(key), int(value)]
    return max_quantity_in[0], max_quantity_in[1]
    


# print(dir(dict))
print(higest_ratio())

"""
Сервер с информацией о товарах вернул ответ в виде json: 

  stocks - остатки товара в регионе,
  34 - номер региона,
  2, 3, 4, ... 176 - номера магазинов региона,
  "2": "35" означает, что в магазине 2 товар в наличии в количестве 356 штук
Необходимо написать на JavaScript три метода:
 1 получить название товара
 2 получить массив номеров магазинов, в которых есть товары в наличии
 3 найти максимальное количество товара в регионе, вернуть это количество и номер магазина
Операции чтения и записи из файла можно опустить - объект можно сразу положить в переменную.
"""

if __name__ == '__main__':
    main()
