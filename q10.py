input_data = input("Enter here: ")

word_list = input_data.split()

unique_words = sorted(set(word_list))

print(" ".join(unique_words))
