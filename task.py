import json

f = open('Python_task.json')
data = json.load(f)

# Task 1: Find the min shown price
print('======Task 1=====')
min_price = float("inf")
obj = ''
for i in data['assignment_results']:
    for k, v in i['shown_price'].items():
        if float(v) < min_price:
            min_price = float(v)
            obj = k +': '+ v

print(min_price)

# Task 2: Find and return the room type, number of guest with the cheapest price 
print('======Task 2=====')
print(obj)
print('Number of guest:',data['assignment_results'][0]['number_of_guests'])

# Task 3: Print the total price (Net price + taxes) for all rooms along with the room type
print('======Task 3=====')
taxes = data['assignment_results'][0]['ext_data']['taxes']
taxes = json.loads(taxes)
total_tax = 0

for k, v in taxes.items():
    total_tax += float(v)

for i in data['assignment_results']:
    for k, v in i['net_price'].items():
        output = k +': '+ str(round(float(v)+total_tax,2))
        print(output)