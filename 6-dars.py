# class MyData:
#     def __init__(self,datas:list):
#         self.datas = datas

#     def __enter__(self):
#         return self


#     def __exit__(self,a,b,s):
#         print("exit ishladi")
#         if a :
#             self.datas.clear()
#         else:
#             print("error bolmadi")
#             data.datas.append(self)
#             print(self.datas)
#         print("Exit ishladi")        
# my_data = MyData([1,2,3,4,5,6])

# with my_data as data :
#     data.datas.append(1)
#     data.datas.append(2)
#     data.datas.append(3)




# import time 

# def fun_1():
#     for i in range(2):
#         time.sleep(1)
#         print(True)

# def fun_2():
#     for i in range(3):
#         time.sleep(1)
#         print(False)

# # task_1 = threading.Thread(target = fun_1 ,args = ([2,10]))

# # task_2 =  threading.Thread(target=fun_2,args=([10,15]))
# task_2 =  threading.Thread(target=fun_2)
# # task_1.run()
# # task_2.run()
# task_2.start()
# print(threading.active_count())

# from * import *


# with open() as file:
    # print(file)

import threading
import os


txt_file_1 = [] 
a = 0
directory = r'C:\Users\a\OneDrive\Документы\FN 20\M5' 

files = os.listdir(directory)

for file in files:
    if ".txt" in file:
        a += 1
        txt_file_1.append(file) 
        print(f"umumiy ochilgan filelar : {a}inchi filening nomi {file}")


def fun_3():
    unilar_soni = 0
    for link in txt_file_1:
        with open(f"{link}") as file:
            for world in file:
                for char in world:
                    if char.lower() in "aoiue":
                        unilar_soni += 1
    return f"umumiy unilar soni : {unilar_soni}"
    
        
                
print(fun_3())
task_1 = threading.Thread(target=fun_3)
task_1.start()

task_1.join()
