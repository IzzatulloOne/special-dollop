# import threading
# import os

# txt_file_1 = [] 
# a = 0
# directory = r'C:\Users\a\OneDrive\Документы\FN 20\M5' 

# files = os.listdir(directory)

# for file in files:
#     if file.endswith(".txt"):
#         a += 1
#         txt_file_1.append(file)
#         print(f"umumiy ochilgan filelar : {a}inchi filening nomi {file}")

# def fun_3():
#     unilar_soni = 0
#     unilar = ""
#     uzbek_vowels = "aoiue"
#     for link in txt_file_1:
#         with open(link) as file:
#             for line in file:
#                 for char in line:
#                     if char.lower() in uzbek_vowels:
#                         unilar_soni += 1
#                         unilar += char
#     print(f"umumiy unilar soni : {unilar_soni} huddi osha unlilar : {unilar}")

# task_1 = threading.Thread(target=fun_3)
# task_1.start()
# task_1.join()


# if __name__ == "__main__":
#     ...

import string
ismlar = ["Izzatullo","Abu","saidbosxoN"]

def a(word):
    # count = 0
    
        if word[0].isupper():
            return 1
        elif word[1:-1].isupper():
            return 2        
        elif word[:].isupper():        
            return 3      
        else:
            raise ValueError     

    

ismlar.sort(key=a)

print(ismlar)
# reversed