
f = open("plaintext.txt",encoding="utf-8")
g = open("plaincorrect.txt","w",encoding="utf-8")
for line in f:
    write_txt = line.split(" ")
    if '\n' in write_txt:
        write_txt.remove('\n')
    for i in write_txt:
        g.write(i)
        g.write('\n')


