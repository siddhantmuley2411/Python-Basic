input_data = input("Enter: ")

upper_case_count = sum(1 for c in input_data if c.isupper())

lower_case_count = sum(1 for c in input_data if c.islower())

print(f"UPPER CASE {upper_case_count}")

print(f"LOWER CASE {lower_case_count}")
