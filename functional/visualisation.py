#принимает словарь
def visualise(data):
    f=open("data.txt","a+")
    z=2
    for i in data.items():
        if z==3:
            f.write("\n")
            z=0
        f.write(str(i[0])+"    "+str(i[1])+"\n")
        z=z+1
    f.write("\n")