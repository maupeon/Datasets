
import os
import glob
import random
import numpy as np
import shutil
 #shutil.copy(os.path.join(sys.argv[3], name), os.path.join(dest, name))
os.chdir('training_set')
fileList = glob.glob('*')
#random.shuffle(fileList)
#print(fileList)
copy_list = []
for i in range(len(fileList)):
    #destiny = "/home/maupeon/Documents/ITESM/7. Semestre/Inteligencia Computacional/Datasets/test_set/"
    
    dest ='../test_set/'+fileList[i]
    print(fileList[i])
    #destiny+=fileList[i]
    #shutil.rmtree(str(i))

    os.chdir(fileList[i])
    imageFilesList = glob.glob('*')
    print(imageFilesList,'\n')
    copy_list.append(imageFilesList[0])
    #print(len(imageFilesList))
    #random.shuffle(imageFilesList)
    #length = len(imageFilesList)
    #veinte = (20 * length)/100
    #print(int(veinte))
    #for j in range(int(veinte)):
     #   copy_list.append(imageFilesList[j])
    #for n in range(len(copy_list)):   
     #   shutil.copy(copy_list[n],destiny )
      #  os.remove("/home/maupeon/Documents/ITESM/7. Semestre/Inteligencia Computacional/Datasets/training_set/"+fileList[i]+'/'+imageFilesList[n])
   
    #print(copy_list)

    #print(len(imageFilesList))
    os.chdir("..")
print(len(copy_list))
    # file = open(fileList[i])