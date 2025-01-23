
def project():
    questions = [
        {"question": "What is the national song of india?", "answer": "vande mataram"},
        {"question": "who is the father of indian constitution?", "answer": "br ambedkar"},
        {"question": "where is the flag hosted on independence day?", "answer": "delhi"},
        {"question": "Which planet is known as the Red Planet?", "answer": "mars"},
        {"question": "Which is the national river of india?", "answer": "ganga"},
        {"question": "What is the capital of india?", "answer": "new delhi"},
        {"question": "name the two seas surrounding inida?", "answer": "arabian sea and bay of bengal"},
        {"question": "india is the part of which content ?", "answer": "asia"},
        {"question": "name the only desert in india?", "answer": "thar desert"},
        {"question": "which is the tallest mountain in the world?", "answer": "mount everest"}
    ] 
    score = 0   
    for i in range(len(questions)): 
        print(f"Question {i + 1}: {questions[i]['question']}")
        user_answer = input("Your answer: ").strip().lower()       
        if user_answer == questions[i]['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {questions[i]['answer']}.")
    print(f"Your final score is: {score}/{len(questions)}")
project()
