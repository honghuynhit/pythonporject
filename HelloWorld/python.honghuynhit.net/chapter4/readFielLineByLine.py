import os
# Check file exists
if os.path.exists('E:/Work/Project/README.txt') is False:
    print('This path not exists! Please check again!')
else:

    # Read file line by line is fast
    objFileRead = open('E:/Work/Project/README.txt','r')

    # Loop line by line 
    for linebyline in objFileRead:
        print(linebyline, end = '')

    # Close opening file 
    objFileRead.close()