def marks(english,s_theory,s_practical,maths):
    if english < 75 and s_theory < 75 and s_practical < 25 and maths < 100:
        e_marks = (english / 75)*100
        m_marks = (maths / 100)*100
        s_marks = ((s_theory + s_practical)/100)*100
        total = (e_marks + m_marks + s_marks)/3
        if e_marks < 25 and m_marks < 35 and s_marks < 35 and s_theory < 25 and s_practical < 8:
            print("student fail")
        elif s_practical < 8:
            print("FAIL")
        elif s_theory < 25:
            print("FAIL")
        elif total > 90:
            print("GRADE 'A'")
        elif total > 75:
            print("GRADE 'B'")
        elif total < 35:
            print("fail")
        else:
            print("AVERAGE")
    else:
        print("enter valid marks")

marks(int(input("enter english marks\n")), int(input("enter science theory marks\n")), int(input("enter science practical marks\n")), int(input("enter maths marks\n")))
