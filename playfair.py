
def string_prepare(cadena):
    cadena = list(cadena.upper())
    for n in range(len(cadena)-1):
        if n % 2 == 0:
            if cadena[n] == cadena[n+1]:
                cadena.insert(n+1,"X")
    if len(cadena) % 2 != 0:
        cadena.append("X")
    return cadena

def build_mt(keyword):   #Construir matriz
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alphabet = list(alphabet)
    plfr_mt = [[],[],[],[],[]]
    used = []
    positions = {}
    row = 0
    col = 0
    for i in  keyword:
        if i not in used:
            plfr_mt[row].append(i)
            positions[i] = (row,col)
            col += 1
            used.append(i)
            if len(plfr_mt[row]) == 5:
                row+=1
                col = 0

    for i in  alphabet:
        if i not in used:
            plfr_mt[row].append(i)
            positions[i] = (row,col)
            col += 1
            used.append(i)
            if len(plfr_mt[row]) == 5:
                row+=1
                col = 0
    return plfr_mt,positions

def main():
    f = open("plaincorrect.txt",encoding="utf-8")
    ans = set("XEERTIVEEGQMDZQKBYMAEKPUESETCMFIMP")
    plain_tx = string_prepare(input())

    for k in f:
        keyword = list(k.upper().replace('J','I'))
        encrypt_tx = ""
        
        i = 0
        tem = len(keyword)
        while i < tem:
            if(keyword[i] < 'A' or keyword[i] > 'Z'):
                keyword.remove(keyword[i])
                tem -= 1
            else:
                i+=1

        mt,pos = build_mt(keyword)
        row1, row2 = 0, 0
        col1, col2 = 0, 0

        for n in range(len(plain_tx)-1):
            if(n % 2 == 0):
                row1 = pos[plain_tx[n]][0]
                row2 = pos[plain_tx[n+1]][0]
                col1 = pos[plain_tx[n]][1]
                col2 = pos[plain_tx[n+1]][1]

                if row1 == row2:
                    encrypt_tx += mt[row1][(col1 + 1)%5]
                    encrypt_tx += mt[row1][(col2 + 1)%5]
                elif col1 == col2:
                    encrypt_tx += mt[(row1 + 1)%5][col1]
                    encrypt_tx += mt[(row2 + 1)%5][col1]
                else:
                    encrypt_tx += mt[row1][col2]
                    encrypt_tx += mt[row2][col1]
        
        if(ans == set(encrypt_tx)):
            print("Coincidencia")
            break
    print(mt)
    print(k)

main()
