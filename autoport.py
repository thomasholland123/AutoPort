
import shutil
from markdown import markdown
import pdfkit


print("Welcome to AutoPort.\n This will take the information about the port or harbour that you enter and make it into a PDF file for you to print")

portname = str(input("Enter port name: "))
lat = str(input("Enter port lat: "))
NS = str(input("Enter port lat N/S: "))
long = str(input("Enter port long: "))
EW = str(input("Enter port long E/W: "))
adv = []
while True:
    tempadv = str(input("Enter port advantage (press enter once done): "))
    if  tempadv == "":
        break
    else:
        adv.append(tempadv)

disadv = []

while True:
    tempdisadv = str(input("Enter port disadvantage (press enter once done): "))
    if  tempdisadv == "":
        break
    else:
        disadv.append(tempdisadv)

windaccsess = str(input("Enter port wind requirments for accsess or for safe stay: "))
depth = str(input("Enter port's minmum depth: "))

harbourchannel = str(input("Enter any harbour channels: "))
cost = str(input("Enter any cost to moor or anchor: "))


other = []

while True:
    tempother = str(input("Enter any other information (press enter once done): "))
    if  tempother == "":
        break
    else:
        other.append(tempother)





filename = str(portname + ".txt")
shutil.copyfile("template.txt", filename)

fileopen =  open(filename, "rt")
data = fileopen.read()
data2 = data.replace("(Port Name)", portname)
data3 = data2.replace("(LAT)", lat)
data4 = data3.replace("(NS)", NS)
data5 = data4.replace("(LONG)", long)
data6 = data5.replace("(EW)", EW)

advstring = ',\n'.join(map(str, adv))
data7 = data6.replace("(ADV)", advstring)

disadvstring = ',\n'.join(map(str, disadv))
data8 = data7.replace("(DISADV)", disadvstring)
data9 = data8.replace("(WINDACCSESS)", windaccsess)
data10 = data9.replace("(DEPTHACCSESS)", depth)
data11 = data10.replace("(HARBOURCHANNEL)", harbourchannel)
data12 = data11.replace("(COST)", cost)
otherstring = ',\n'.join(map(str, other))
data13 = data12.replace("(OTHER)", otherstring)



fileopen.close



fileopen = open(filename, "wt")

fileopen.write(data13)
fileopen.close()

print("Done and saved as .txt")

filenamemd = str(portname + ".md")
shutil.copyfile(filename, filenamemd)

print("Done and saved as .md")

output_filename = str(portname + ".pdf")

with open(filenamemd, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

pdfkit.from_string(html_text, output_filename)

print("Saved as PDF")
