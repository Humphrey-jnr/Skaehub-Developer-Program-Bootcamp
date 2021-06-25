def sort_dict():
    cars = [{'make':'Subaru', 'model':'Impreza', 'color':'Grey'}, {'make':'Toyota', 'model':'Mirai', 'color':'Blue'}, {'make':'Range rover', 'model': 'Vellar', 'color':'Black'}]

    sorted_cars = sorted(cars, key = lambda x: x['make'])
    print("\nSorted Car list :")
    print(sorted_cars)

sort_dict()