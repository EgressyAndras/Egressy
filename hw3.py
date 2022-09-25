def triangle():
    a = int(input("a oldal(cm): "))
    b = int(input("b oldal(cm): "))
    c = int(input("c oldal(cm): "))
    list = [a,b,c]
    list.sort()
    nem = " NEM "
    if list[0]+list[1] >= list[2]:
        nem = " "

    print(f"A {a}, {b} és {c} oldalú háromszög{nem}szerkezthető ")
if __name__ == '__main__':
    print("Adja meg a háromszög 3 oldalát cm-ben ")
    triangle()

