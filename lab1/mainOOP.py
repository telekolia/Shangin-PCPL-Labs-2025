import sys
import math


class BiquadraticEquation:
    def __init__(self, A: float, B: float, C: float):
        self.A = A
        self.B = B
        self.C = C
        self.solutions = []


    def CalculateDiscriminant(self):
        return self.B * self.B - 4 * self.A * self.C

    def CalculateSolutions(self):
        abstractRoots = self.GetAbstractRoots()
        self.ConvertAbstractRootsToReal(abstractRoots)


    def GetAbstractRoots(self):
        abstractRoots = []
        D = self.CalculateDiscriminant()
        if D == 0.0:
            root = -self.B / (2.0 * self.uation.A)
            abstractRoots.append(root)
        elif D > 0.0:
            root1 = (-self.B + D ** 0.5) / (2.0 * self.A)
            root2 = (-self.B - D ** 0.5) / (2.0 * self.A)
            abstractRoots.append(root1)
            abstractRoots.append(root2)
        return abstractRoots

    def ConvertAbstractRootsToReal(self, abstractRoots):
        for tempRoot in abstractRoots:
            if tempRoot >= 0:
                tempRoot = tempRoot ** 0.5
                negativeRoot = - tempRoot
                self.solutions.append(tempRoot)
                if negativeRoot != tempRoot:
                    self.solutions.append(negativeRoot)


class BiquadraticSolver:
    def __init__(self):
        pass


    def Start(self):
        coefs = []
        self.SolvingMenu(coefs)
        equation = BiquadraticEquation(coefs[0], coefs[1], coefs[2])
        equation.CalculateSolutions()

        self.PrintRoots(equation.solutions)


    def GetCoef(self, index, prompt):
        try:
            coefStr = sys.argv[index]
        except:
            print(prompt, end=' ')
            coefStr = input()
        isInputCorrect = False
        while (isInputCorrect == False):
            try:
                coef = float(coefStr)
                isInputCorrect = True
            except:
                print("Invalid input, try again")
                print(prompt, end=' ')
                coefStr = input()
        return coef


    def SolvingMenu(self, coefs):
        coefs.append(self.GetCoef(1, 'Введите коэффициент А:'))
        coefs.append(self.GetCoef(2, 'Введите коэффициент B:'))
        coefs.append(self.GetCoef(3, 'Введите коэффициент C:'))
        print('\n\nРешаем биквадратное уравнение: ({})x^4+({})x^2+({}) = 0\n\n'.format(coefs[0], coefs[1], coefs[2]))


    def PrintRoots(self, roots):
        # Вывод корней
        lenRoots = len(roots)
        if lenRoots == 0:
            print('Нет корней')
        elif lenRoots == 1:
            print('Один корень: {}'.format(roots[0]))
        elif lenRoots == 2:
            print('Два корня: {} и {}'.format(roots[0], roots[1]))
        elif lenRoots == 3:
            print('Три корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
        elif lenRoots == 4:
            print('Четыре корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))


def main():
    solver = BiquadraticSolver()
    solver.Start()


if __name__ == "__main__":
    main()
