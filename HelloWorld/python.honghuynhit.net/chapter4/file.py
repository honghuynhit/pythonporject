import os

if os.path.exists('E:\Work\Project\README.txt') is False:
    print('path not exists')
else:
    objRead = open("E:/Work/Project/README.txt","r")
    CountFile = objRead.read()

    print("Countent before write(): ", CountFile)

    # Closing the first instance
    objRead.close()

    #Opening again for write to file 

    objWrite = open('E:/Work/Project/README.txt','w')
    objWrite.write('Using "w" for writing text in the file!')

    # Close the file in write mode
    objWrite.close()

    
    objAppen = open('E:/Work/Project/README.txt','a')
    objAppen.write('Using "a" for append text in the file!')

    # Close the file in write mode
    objWrite.close()