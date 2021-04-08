from PIL import Image


imageSource = Image.open("ch9.png")
listePixels = list(imageSource.getdata())



def recupereMessage(liste):
    l = []

    for i in range (0, len(liste)):
        for j in range (0,3):
            octet = liste[i][j]
            bin_octet = bin(octet)[2:].zfill(8)
            l.append(bin_octet[7])

    return l

def separerbits(liste):
    l = []
    octet = ""
    for i in range (0, len(liste)-8):
        for j in range (0,8):
            if(i+j>len(liste)):return l
            octet += liste[i+j]

        l.append(octet)
        octet = ""

    return l


def lstring(liste):
    l = []
    for i in range(0, len(liste)):
        n = int(liste[i],2)
        if (n>47 and n<123):
            l.append(int(liste[i], 2))
    return l

def lastring(liste):
    m = ""
    for i in range (0, len(liste)):
        c = chr(liste[i])
        m += c
    return m

print(lastring(lstring(separerbits(recupereMessage(listePixels)))))