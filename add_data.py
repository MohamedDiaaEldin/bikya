import csv

from modles.materials import Matrial
from modles.categories import Category
from modles.delivery import Delivery
from modles.zone import Zone
from modles.customers import Customer
from modles.matrials_categories import MatrialCategory
##  for context
from main import app


# def add_material(matrials):    
#     for material in matrials:
#         m = Matrial(name=material)
#         m.add()

# def add_category(matrials):
#     for material in matrials:
#         m = Category(name=material)
#         m.add()

# def add_zones(zones):
#     for zone in zones:
#         z = Zone(name=zone)
#         z.add()

# def add_delivery():
#     ## first deleivey 
#     delivery = Delivery(name='Zaki',  phone = '0127222222', email='zaki@bikya.com', password="zaki123", zone_id=1)
#     delivery.add()
#     ## second deleivey 
#     delivery = Delivery(name='Hossam',  phone = '0127222222', email='hosam@bikya.com', password="hosam123", zone_id=2)
#     delivery.add()
#     ## third deleivey 
#     delivery = Delivery(name='Mohaned',  phone = '0127222222', email='mohaned@bikya.com', password="mohaned123", zone_id=3)
#     delivery.add()
    
# with open('data/material.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         print(row)
#         # matrial 
#         if line_count == 0:
#             add_material(row)                        
#         elif line_count == 1:
#             add_category(row)                    
#         elif line_count == 2:
#             add_zones(row)
#         line_count += 1
#     print(f'Processed {line_count} lines.')






'''
materials 
1 | Plastic
2 | Paper
3 | Metal
4 | Glass
5 | Steel
6 | Aluminium
7 | Wood

'''
## add store data
matrials = [ {'id':1 , 'km_price':20, 'km_points':5},
            {'id':2 , 'km_price':10, 'km_points':3},
            {'id':3 , 'km_price':30, 'km_points':10},
            {'id':4 , 'km_price':15, 'km_points':4},
            {'id':5 , 'km_price':30, 'km_points':10},
            {'id':6 , 'km_price':40, 'km_points':13},
            {'id':7 , 'km_price':20, 'km_points':8},            
            ]
categories = [1, 2, 3, 4, 5, 6]

for matrial in matrials:  
    for i in range(1, 7):
        category_matrial = MatrialCategory(matrial_id=matrial['id'], category_id=i, total_weight=100, km_price=matrial['km_price'] , km_points=matrial['km_points'])
        category_matrial.add()
        




