import random

print("이 낡은 도서관에 오신것을  환영합니다!")
print("당신의 목표는 이 폐교된 학교의 도서관에 숨겨져 있다는  비밀을 찾는 것입니다.")
print("돈이 떨어진 당신은 현재 반드시 그 비밀을 찾아야만 합니다....")

print("그 비밀은 당신의 모든 빚을 말끔히 지워줄수 있습니다...")
import random

#Write your code below this line 


empty_list =[]

library_2D = []

path_length = 5 
#random.randint(10,13)

bookshelf_width = random.randint(5,path_length)

#----------------------------------------------------

for i in range(path_length) :
    library_2D.append(0)
    for j in range(bookshelf_width+1) :
        library_2D.append(0)


        print(library_2D)
  
