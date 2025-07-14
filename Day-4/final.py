marks = [25, 65, 89, 35, 99, 74, 12, 58, 79, 38]
pass_count=0
dist_count=0
fail_count=0
for mark in marks:
    if mark >= 75:
        dist_count+=1
    elif mark < 35:
        fail_count+=1
    elif mark >= 35:
        pass_count+=1
    
print("All marks ",marks)
print("Total average marks ",sum(marks)/len(marks))
print("Maximum marks", max(marks))
print("Minimum marks",min(marks))
print("Total number of student with distinction :",dist_count)
print("Total number of student who as failed ",fail_count)
print("Total number of student passed are : ",pass_count)