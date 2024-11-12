cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
#1
cars.append("ferrari")
print(cars)
#2
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars.insert(3,"porsche")
print(cars)
#3
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars.clear()
print(cars)
#4
cars=["bow", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars.sort()
print(cars)
#5
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars.remove("audi")
print(cars)
#6
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
print(cars.index("mustang"))
#7
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars.extend(["tesla", "nissan"])
print(cars)
#8
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
print(cars.pop())
print(cars)
#9
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
print(cars.count("bow"))
#10
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars.append(["jaguar", "fiat"])
print(cars)
#11
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars.insert(2, ["volvo", "honda"])
print(cars)
#12
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
if not cars:
    cars.clear()
    print("List was empty and has been cleared.")
else:
    print("List is not empty, so it will not be cleared.")
    print("Current list:", cars)
#13
cars=["bow", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars.sort(reverse=True)
print(cars)
#14
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars = [car for car in cars if car != 'bmw'] ##list comprehension
print(cars)
#15
cars=["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata","audi", "mustang"]
cars.reverse()
print(cars)
cars.remove("tata")
print(cars)
#16
cars = ["bmw", "mahindra", "rolls royce", "bentley", "aston martin", "tata", "audi", "mustang"]
# Check if the list filtered for 'bmw' is empty
if [car for car in cars if car == 'bmw']:
    cars.extend(["ferrari", "lamba"])
    print(cars)
else:
    print("cannot be extend")

