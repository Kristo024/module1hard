grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stu_list=list(students) # множество в список
stu_list.sort() # сортировка по алфавиту
#средний балл
first=sum(grades[0])/len(grades[0])
second=sum(grades[1])/len(grades[1])
third=sum(grades[2])/len(grades[2])
fourth=sum(grades[3])/len(grades[3])
fifth=sum(grades[4])/len(grades[4])
gra_ave=[first,second,third,fourth,fifth]
# объединение двух списков по методу zip-молнии
students_and_grades=dict(zip(stu_list,gra_ave))
print(students_and_grades)