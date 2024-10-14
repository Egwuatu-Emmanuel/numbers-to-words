number_words = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
    "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
    "hundred"
]

def function_1(number):
    if number < 21:
        return number_words[number]
    elif number < 100:
        units = number % 10
        tens = number // 10
        if units == 0:
            return number_words[tens + 18]
        else:
            return f"{number_words[tens + 18]}-{number_words[units]}"
    elif number < 1000:
        hundreds = number // 100
        rem = number % 100
        if rem == 0:
            return f"{number_words[hundreds]} hundred"
        else:
            return f"{number_words[hundreds]} hundred and {function_1(rem)}"
    elif number < 1_000_000:
        thousands = number // 1_000
        rem = number % 1_000
        if rem == 0:
            return f"{function_1(thousands)} thousand"
        else:
            return f"{function_1(thousands)} thousand, {function_1(rem)}"
    elif number < 1_000_000_000:
        millions = number // 1_000_000
        rem = number % 1_000_000
        if rem == 0:
            return f"{function_1(millions)} million"
        else:
            return f"{function_1(millions)} million, {function_1(rem)}"
    elif number < 1_000_000_000_000:
        billions = number // 1_000_000_000
        rem = number % 1_000_000_000
        if rem == 0:
            return f"{function_1(billions)} billion"
        else:
            return f"{function_1(billions)} billion, {function_1(rem)}"
    elif number < 1_000_000_000_000_000:
        trillions = number // 1_000_000_000_000
        rem = number % 1_000_000_000_000
        if rem == 0:
            return f"{function_1(trillions)} trillion"
        else:
            return f"{function_1(trillions)} trillion, {function_1(rem)}"

number = int(input("Input a number: "))
print(f"The number is {function_1(number)}")
