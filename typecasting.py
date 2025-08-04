name="Penguin"
age=15
is_student=True
weight=38.5

print("name:", name)
print("data type of name:", type(name))

print("age:", age)
print("date type of age:", type(age))

print("is_student:", is_student)
print("date type of is_student:", type(is_student))

print("weight:", weight)
print("data type of weight:", type(weight))

print("after type casting")
age=str(age)
print(age)
print("data type of age is:", type(age))

weight=int(weight)
print(weight)
print("data type of weight:", type(weight))