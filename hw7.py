with open("hazi.txt","r",encoding="UTF-8") as f:
    a = ""
    hiba = ",!-?:<;.aeuioéáőúöüóí\"() "
    ready = ""


    for line in f.readlines():
        if line=="\n":
            continue

        for i in range(len(line)):
            if line.lower()[i] not in hiba:
                ready += line[i]
            else:
                ready += ""
    a += ready



with open("out.txt","w",encoding="UTF-8") as outf:
    outf.write(a)

with open("out.txt","r",encoding="UTF-8") as outf:
    j=0
    b=""
    for lines in outf.readlines():
        j+=1
        if (j) % 3 ==0:
            b+=lines
    print(b)
with open("out.txt","w",encoding="UTF-8") as f:
    f.write(b)
