def add(number1, number2):
    if number1 and number2:
        return number1 + number2
    
    elif number2:
        return number2
    
    elif number1:
        return number1
    
    else:
        raise(TypeError)

def substract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2