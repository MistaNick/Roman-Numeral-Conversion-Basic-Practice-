
while True:
    numeral_input = input("Enter a Roman numeral to Convert: ")

    numeral_input = numeral_input.upper()

    if numeral_input == "END":
        print()
        print('System Ending...')
        break



    checker = ['A', 'B', 'E', 'F', 'G', 'H', 'J', 'K', 'N', 'O', "P", 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
    count = 0
    for x in checker:
        if x in numeral_input:
            count += 1
    if count > 0:
        print()
        print("This is NOT a Roman Numeral. Please try again...")
        print()
        continue

    final_answer = 0

    if "IV" in numeral_input:
        final_answer += 4
        numeral_input = numeral_input.replace("IV", "")

    if "IX" in numeral_input:
        final_answer += 9
        numeral_input = numeral_input.replace("IX", "")

    if "XL" in numeral_input:
        final_answer += 40
        numeral_input = numeral_input.replace("XL", "")

    if "XC" in numeral_input:
        final_answer += 90
        numeral_input = numeral_input.replace("XC", "")

    if "CD" in numeral_input:
        final_answer += 400
        numeral_input = numeral_input.replace("CD", "")

    if "CM" in numeral_input:
        final_answer += 900
        numeral_input = numeral_input.replace("CM", "")

    def roman_to_int(numeral):
        global final_answer

        for i in numeral:
            if i == "M":
                final_answer += 1000
            elif i == 'D':
                final_answer += 500
            elif i == 'C':
                final_answer += 100
            elif i == 'L':
                final_answer += 50
            elif i == 'X':
                final_answer += 10
            elif i == 'V':
                final_answer += 5
            elif i == 'I':
                final_answer += 1
        print(numeral_input, "converts to", final_answer)

    roman_to_int(numeral_input)
    print()