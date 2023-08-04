#Q.3

palin = input("Enter your choice: ")
palin_lower = palin.lower()
length = len(palin_lower)
is_palindrome = True

for i in range(length // 2):
    if palin_lower[i] != palin_lower[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print(True)
else:
    print(False)
