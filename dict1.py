#pop
student = {
    "Name":"Rutuja",
    "Dep":"CSE",
    "class":"TY"
    }
student.pop("class")
print(student)

#copy
original_marks ={'Physis':80,'Maths':89}
copied_marks =original_marks.copy()
print('Original Marks:', original_marks)
print('copied marks:',copied_marks)

#fromkey()
seq = ('a','b','c')
print(dict.fromkeys(seq,None))



#get
person ={"name":"xyz","age":20,"gender":"female"}
name = person.get("name")
print(name)
