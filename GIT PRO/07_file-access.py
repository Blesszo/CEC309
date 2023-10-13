with open("TEXT.txt","w") as writer:
    writer.write(input("ENTER YOUR NAME: "))

file=open("TEST.txt","r")
for item in file:
    print(item)
file.close()
