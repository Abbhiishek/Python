student_score=[]
score=input("Input a list of students : ").split()
for n in range (0, len(score)):
    student_score.append(int(score[n]))
heighest_score=0
for score in student_score:
    if score > heighest_score :
        heighest_score = score
print(f"The heighest_score among the students is : {heighest_score}")