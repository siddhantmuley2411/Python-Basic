input_data = input("Enter: ")

letter_count = sum(c.isalpha() for c in input_data)

digit_count = sum(c.isdigit() for c in input_data)

print(f"LETTERS {letter_count}")

print(f"DIGITS {digit_count}")
