def main():

    mondat = input("Adjon megy egy mondatot: ")

    x={}
    ### Betuk gyakorisaga
    for i in mondat:
        if i in x:
            x[i] +=1
        else:
            x[i] =1
    print(f"Betuk gyakorisaga: {x}")
    #Forditva
    print("Forditva: ", end="")
    for betu in reversed(mondat):
        print(betu,end="")

    #Lista
    print()
    print("Listaba rendezve: ",end="")
    print(mondat.split(" "))



if __name__ == '__main__':
    main()


input()