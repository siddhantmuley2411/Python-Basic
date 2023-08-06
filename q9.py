while True:
    try:

        input_line = input("Enter Here: ")

        if not input_line:

            break
        print(input_line.upper())

    except EOFError:

        break
