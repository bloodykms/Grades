''' Created by      : Kameche Mohamed Sofiane
    Date            : 29 Juin 2020
    Supervised By   : Kameche Mohamed Sofiane
'''

student_name = 'Mohamed Sofiane';
student_id = '20201000071'

def calculate_grade(mark):
    grade = '' 
    if mark >= 81:
        grade = 'Excellent'
    elif mark >=71:
        grade = 'Very good'
    elif mark >=61:
        grade = 'Good'
    elif mark >=51:
        grade = 'Weak'
    elif mark ==50:
        grade = 'Pass'
    else:
        grade = 'Fail'
    return grade

###

print ('Name: ',student_name)
print ('ID: ',student_id)

print ('\nGrades:')
print ('Python programming 101 :',calculate_grade(87))
print ('Math :',calculate_grade(81))
print ('Physics :',calculate_grade(71))
print ('English :',calculate_grade(50))




###

