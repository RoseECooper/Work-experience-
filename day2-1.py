# open file
# read file
file1 = open('testfile.uk__2112722584__17762e5e-e1e8-11ec-a73d-001dd8b71d1a', 'r')
Lines = file1.readlines()

#finding lines
#lookup1 = input('what word do you want to find?: ')
#lookup2 = input('what word do you want to find?: ')
#with open('testfile.uk__2112722584__17762e5e-e1e8-11ec-a73d-001dd8b71d1a') as myFile1:
#    for num1, line in enumerate(myFile1, 1):
#        if lookup1 in line:
#            print('line: ', num1)
#with open('testfile.uk__2112722584__17762e5e-e1e8-11ec-a73d-001dd8b71d1a') as myFile2:
#    for num2, line in enumerate(myFile2, 1):
#        if lookup2 in line:
#            print('line: ', num2)


count = 0
for line in Lines:
    count += 1
    if count==3:
        print("Line{}: {}".format(count, line.strip()))
    if count==15:
        print("Line{}: {}".format(count, line.strip()))
