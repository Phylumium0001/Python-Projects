from calc.calc import Calculator
from interperate.interperate import SimpleOperation
from interperate.interperate import ComplexOperation


class Main:
    def solve(self,expression):
        if not ('(' in expression or ")" in expression):
            print("Simpe Expression")
            return SimpleOperation(expression).solve()

        else:
            print("Complex Expression")
            return ComplexOperation(expression).solve()

if __name__ == "__main__":
    app = Main()
    while True:
        expresssion = input("Enter Expression : ")
        app.solve(expresssion)