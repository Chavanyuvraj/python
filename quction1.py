f=open("practice.text","w")
f.write("Hi everone\n we are larning file i/o\n")
f.write("using java.\n l like programing in java")

word="hi"
f=open("practice.text","r")
data=f.read()
if(data.find(word)!=-1):
    print("found")
else:
    print("not found")