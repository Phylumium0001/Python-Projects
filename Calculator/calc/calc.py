class Calculator:
    
    def addition(self,*args):        
        result = args[0]
        for i in args:
            result += i

        return result

    def substraction(self,*args):
        result = args[0]
        for i in args:
            result -= i
        return result
    
    def multiplication(self, *args):
        result = args[0]
        for i in args:
            result *= i
        return result
    
    def modulos(self, arg1, arg2):
        return arg1 % arg2
    
    def power(self,number,power):
        return number ** power

    
if __name__ == "__main__":
    c = Calculator()
    