def palindrom():
    szo = str(input("Tell me a word or sentence and i'll tell you if it is a palindrome or not: "))
    ekezet = "öüóőúéáűí"
    ekezetek_javitasa = "ouooueauj"
    hiba = " ,-.;?:!—"
    szolower = szo.lower()
    veglegesSzo = ""

    for i in range (0,len(szo)):
        if szolower[i] in ekezet:
            for j in range(0,len(ekezet)):
                if szolower[i] == ekezet[j]:
                    veglegesSzo+= ekezetek_javitasa[j]
        elif szo[i] not in hiba:
            veglegesSzo += szolower[i]
    veglegesSzo = veglegesSzo.lower()

    tesztszo = ""
    for j in reversed(range(0, len(veglegesSzo))):
        tesztszo += veglegesSzo[j]


    if tesztszo==veglegesSzo:
        print( szo, "is a palindrome ")
    else:
        print(szo, "is not a palindrome")
    input()
if __name__ == "__main__":
    palindrom()