import os

infileName = os.getcwd()+"\\filehand\\"+input("입력파일 이름: ")
outfileName = os.getcwd()+"\\filehand\\"+input("출력파일 이름: ")

# infile = open("C:\\Users\\SAMSUNG\\Documents\\IOT\\source\\20251201\\filehand\\sales.txt","r")
# outfile = open("C:\\Users\\SAMSUNG\\Documents\\IOT\\source\\20251201\\filehand\\summary.txt","w")
infile = open(infileName+".txt","r")
outfile = open(outfileName+".txt","w")

sum = 0
count = 0

line = infile.readline()
while line != "":
    s = int(line)
    sum += s
    count += 1
    line = infile.readline()
    
outfile.write("총 매출은" + str(sum)+"\n")
outfile.write("평균 일매출 = "+ str(sum/count ))

infile.close()
outfile.close()