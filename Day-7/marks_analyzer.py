marks = [45, 89, 32, 75, 67, 90, 54, 29, 100]
Dist_count=0
pass_count=0
fail_count=0
for mark in marks:
    if mark >= 75:
        Dist_count+=1
    elif mark >=35 and mark < 75:
        pass_count+=1
    else:
        fail_count+=1
print("Average :",sum(marks)/len(marks))
print("sum of marks :",sum(marks))
print("Distinction count",Dist_count)
print("Passed count",pass_count)
print("Failed count",fail_count)