def main():
    print("Adjon meg egy szamot és egy mértékegységet (cm/inch): ")
    print()
    szam = float(input())
    mertek=input()


    if mertek== "inch":
        print(round(szam*2.54,2)," cm")
    elif mertek=="cm":
        print(round(szam/2.54,2),"  inch")
    else:
        print("Not correct unit!")

if __name__ == '__main__':
    main()
input()

