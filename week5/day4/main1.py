
f = open('file1.txt.py')
txt_file = f.readlines()
print(txt_file)

with open(r"file1.txt.py", 'r') as fp:
    # read line 5
    x = fp.readlines()[5]
    print(x)

f = open('file1.txt.py','r')
txt_file = f.read(5)
print(txt_file)

fileobj=open("file1.txt.py")
lines=[]
for line in fileobj:
    lines.append(line.strip())
print(lines)
lines.append(line.split())
print(lines)

text = open("file1.txt.py", "r")

d = dict()

for line in text:

    line = line.strip()
    line = line.lower()

    words = line.split(" ")

    for word in words:

        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, ":", d[key])


f = open("file1.txt.py","a+")
name =f.write(" \n oce ")


f= open("file1.txt.py","r")
lines = f.readlines()
f.close()

with open("file1.txt.py",'w') as f:
    for line in lines:
        if "luke" in lines:
            f.write(line[:-1]+ " SkyWalker\n")
        else:
            f.write(line + '\n')


