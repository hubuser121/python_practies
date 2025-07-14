questions = [
    {"question": "What is the capital of India?", "answer": "Delhi"},
    {"question": "Which language is used in web browsers?", "answer": "JavaScript"},
    {"question": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"question": "Who wrote 'Wings of Fire'?", "answer": "APJ Abdul Kalam"},
    {"question": "What is 9 * 9?", "answer": "81"}
]

points=0
crt_answer=0
wrong_answer=0


for Quest in questions:
    Question=Quest["question"]
    answer=Quest["answer"]
    print(Quest["question"])
    your_answer=input("Enter your answer\n")
    
    if your_answer.lower()== answer.lower():
         points+=1 
         crt_answer+=1
         print("your answer is correct. you secure a point congratS")
    else:
         wrong_answer+=1
         print("your answer is wrong. better luck next time ")


print("Quiz completed ")
print("Total points scored :", points)
print("Correct answers :",crt_answer)
print("wrong answer", wrong_answer)
print(f"score percentage : {crt_answer/len(questions)*100:.2f}")