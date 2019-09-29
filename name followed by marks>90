def SSLC_mark():
    student_names=[]
    student_marks = []
    marks_in_char = []
    student_90 = []
    while True:
        student_marks = input("enter your name with total marks\n")
        if student_marks == " ":
            break
        else:
            list.append(student_marks)
    
    for item in student_names:
        item = int(item[-2:])
        if item > 90 and item <= 100:
            student_marks.append(item)


    for item1 in student_marks:
        item1 = str(item1)
        marks_in_char.append(item1)

    for item2 in student_names:
        for item3 in marks_in_char:
            if item3 in item2:
                student_90.append(item2)
        
    return student_90

print(SSLC_mark())
