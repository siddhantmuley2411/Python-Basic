input_sequence = input("Enter comma seperated numbers: ")

num_list = input_sequence.split(",")

odd_square_list = [str(int(num)**2) for num in num_list if int(num) % 2 != 0]

print(",".join(odd_square_list))
