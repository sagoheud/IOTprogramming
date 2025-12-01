# infile  = open("C:\\Users\\SAMSUNG\\Documents\\IOT\\source\\20251201\\filehand\\input.txt","r", encoding="utf-8")
infile  = open("filehand/input.txt","r", encoding="utf-8")

line = infile.readline()

print(line)

while line != "":
    print(line)
    line = infile.readline()
    
outfile = open("filehand/output.txt", "w")
outfile.write("김영희\n")

infile.close()
infile.close()