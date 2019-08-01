import json
import datetime


def write_order_to_json(item, quantity, price, buyer, date):
    with open('data/orders.json', 'r') as f:
        current_data = json.load(f)

    with open('data/orders.json', 'w') as f:
        current_data['orders'].append({
            "item": item,
            "quantity": quantity,
            "price": price,
            "buyer": buyer,
            "date": date
        })
        json.dump(current_data, f, indent=4)

    return current_data


if(__name__ == '__main__'):
    default_orders = [
        {
            "item": 'item1',
            "quantity": 2,
            "price": 5,
            "buyer": 'buyer1',
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        },
        {
            "item": 'item2',
            "quantity": 1,
            "price": 10,
            "buyer": 'buyer1',
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        },
        {
            "item": 'item1',
            "quantity": 5,
            "price": 5,
            "buyer": 'buyer2',
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        }
    ]
    
    for i, order in enumerate(default_orders):
        print(f'Writing order #{i}')
        write_order_to_json(**order)
