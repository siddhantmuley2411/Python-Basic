input_data = input("Enter two inputs: ")


X_val, Y_val = map(int, input_data.split(","))

result_matrix = [[i * j for j in range(Y_val)] for i in range(X_val)]

for row in result_matrix:
    print(row)
