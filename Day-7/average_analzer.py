students = [
    {"name": "Karthik", "marks": [78, 88, 92]},
    {"name": "Veda", "marks": [65, 70, 80]},
    {"name": "Ravi", "marks": [35, 40, 50]}
]
for student in students:
    name=student["name"]
    marks=student["marks"]
    avg=sum(marks)/len(marks)
    status='passed' if avg >=35 else 'failed'
    print(f"{name} -Avg: {avg:.2f} - {status}")