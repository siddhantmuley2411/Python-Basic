input_data = input("Engter Here: ")

nums = input_data.split(",")

divisible_by_5 = [i for i in nums if int(i, 2) % 5 == 0]

print(",".join(divisible_by_5))
