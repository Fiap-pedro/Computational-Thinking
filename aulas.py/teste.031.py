def baskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    x2 = (-b + delta ** 0.5) / (2 * a)
    x1 = (-b - delta ** 0.5) / (2 * a)
    return [x1, x2]


aa = int(input('Digite um valor para a: '))
bb = int(input('Digite um valor para b: '))
cc = int(input('Digite um valor para c: '))

print(f'As raizes são: {baskara(aa, bb, cc)}')
