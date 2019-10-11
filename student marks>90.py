def student_file():
    student_name = []
    student_marks = []
    marks_in_char= []
    marks_90 =[]
    with open("students.txt") as rf:
        rf_chunk = rf.read().split()

    for item in rf_chunk:
        student_name.append(item)

    for item1 in student_name:
        item1 = int(item1[-2:])
        if item1 > 90 and item1 <= 100:
            student_marks.append(item1)
        

    for item2 in student_marks:
        item2 = str(item2)
        marks_in_char.append(item2)

    for item3 in student_name:
        for item4 in marks_in_char:
            if item4 in item3:
                marks_90.append(item3)
                


       
    return marks_90

print(student_file())
