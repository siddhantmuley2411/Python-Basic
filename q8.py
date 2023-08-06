input_data = input("Enter comma seperated words: ")

word_list = input_data.split(",")

word_list.sort()

print(",".join(word_list))
