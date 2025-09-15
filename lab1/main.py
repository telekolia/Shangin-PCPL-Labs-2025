import sys
import math


def ConvertAbstractRootsToReal(abstractRoots, realRoots):
    for tempRoot in abstractRoots:
        if tempRoot >= 0:
            tempRoot = math.sqrt(tempRoot)
            negativeRoot = - tempRoot
            realRoots.append(tempRoot)
            if negativeRoot != tempRoot:
                realRoots.append(negativeRoot)


def GetAbstractRoots(a, b, c):
    abstractRoots = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        abstractRoots.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        abstractRoots.append(root1)
        abstractRoots.append(root2)
    return abstractRoots

def PrintRoots(roots):
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))

def GetCoef(index, prompt):
    try:
        coefStr = sys.argv[index]
    except:
        print(prompt, end=' ')
        coefStr = input()

    isImputCorrect = False
    while (isImputCorrect == False):
        try:
            coef = float(coefStr)
            isImputCorrect = True
        except:
            print("Invalid input, try again")
            print(prompt, end=' ')
            coefStr = input()
    return coef


def Menu(coefs):
    coefs.append(GetCoef(1, 'Введите коэффициент А:'))
    coefs.append(GetCoef(2, 'Введите коэффициент B:'))
    coefs.append(GetCoef(3, 'Введите коэффициент C:'))
    print('\n\nРешаем биквадратное уравнение: ({})x^4+({})x^2+({}) = 0\n\n'.format(coefs[0], coefs[1], coefs[2]))


def biquadralSolver():
    coefs = []
    Menu(coefs)

    realRoots = []
    abstractRoots = GetAbstractRoots(coefs[0], coefs[1], coefs[2])
    ConvertAbstractRootsToReal(abstractRoots, realRoots)

    PrintRoots(realRoots)

def main():
    biquadralSolver()


if __name__ == "__main__":
    main()
