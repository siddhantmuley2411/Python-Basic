import math

C = 50
H = 30

user = input("Enter comma seperated nums: ")
temp = user.split(",")

results = [str(int(math.sqrt((2 * C * int(D)) / H))) for D in temp]
print(",".join(results))
