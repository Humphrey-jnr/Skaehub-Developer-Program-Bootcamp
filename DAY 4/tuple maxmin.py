def max_min_cars(car_numbers):
    return_max = max(car_numbers,key=lambda item:item[1])[1]
    return_min = min(car_numbers,key=lambda item:item[1])[1]
    return return_max, return_min
    
car_numbers = [('Toyota', 620), ('Subaru', 300), ('Mazda', 345), ('Mitsubishi', 7089), ('Nissan',4574)]
print("Original list of cars:")
print(car_numbers)
print("\nMaximum and minimum car numbers:")
print(max_min_cars(car_numbers))