import json


class GoodsDetails:
    
    def __init__(self):
        self.region = '34'
        self.server_response = self.json_file()
        self.available_shops = self.server_response['stock']['stocks'][self.region]
        self.good_name = self.set_name()
        self.in_stock = self.check_stock_status()
        self.highest_ratio = self.highest_ratio_atm()
        
        
    def json_file(self):
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
        
    def set_name(self):
        return self.server_response['displayedName']['displayedName']['value'][0]
        

    def check_stock_status(self):
        shops_with_good = []
        for key, value in self.available_shops.items():
            if value == '0':
                continue
            else:
                shops_with_good.append(int(key))
        return str(sorted(shops_with_good))
        
    def highest_ratio_atm(self):
        max_quantity_in = [0, 0]
        for key, value in self.available_shops.items():
            if int(value) < max_quantity_in[1]:
                continue
            else:
                max_quantity_in = [int(key), int(value)]
        return 'magazine №{} in quantity: {}'.format(max_quantity_in[0], max_quantity_in[1])
        
if __name__ == '__main__':
    a = GoodsDetails()
    print(a.region)
    print(a.good_name)
    print(a.in_stock)
    print(a.highest_ratio)
