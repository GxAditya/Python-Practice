import json
from typing import List, Dict, Any

class QuizApp:
    def __init__(self, questions: List[Dict[str, Any]]):
        self.questions = questions
        self.score = 0
        self.results = []

    def run_quiz(self):
        print("\n=== Python Quiz App ===\n")
        print("Answer the questions by entering the option number. Let's begin!\n")
        
        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i}: {q['question']}")
            for j, option in enumerate(q['options'], 1):
                print(f"   {j}. {option}")
            
            while True:
                try:
                    user_answer = int(input("\nYour answer (enter option number): "))
                    if 1 <= user_answer <= len(q['options']):
                        break
                    print(f"Please enter a number between 1 and {len(q['options'])}")
                except ValueError:
                    print("Please enter a valid number!")
            
            is_correct = (user_answer - 1) == q['correct']
            if is_correct:
                self.score += 1
                print("\n✅ Correct! Well done!")
            else:
                print(f"\n❌ Wrong! The correct answer was: {q['options'][q['correct']]}")
            
            self.results.append({
                'question': q['question'],
                'user_answer': q['options'][user_answer - 1],
                'correct_answer': q['options'][q['correct']],
                'is_correct': is_correct
            })
            
            input("\nPress Enter to continue to the next question...")
            print("\n" + "-"*50 + "\n")  # Add separator between questions
        
        self.show_results()

    def show_results(self):
        print("\n" + "="*50)
        print("=== 🎉 QUIZ COMPLETED! ===")
        print("="*50)
        
        percentage = (self.score/len(self.questions)) * 100
        print(f"\n📊 Your Score: {self.score} out of {len(self.questions)}")
        print(f"🏆 Percentage: {percentage:.1f}%")
        
        # Add a fun message based on the score
        if percentage == 100:
            print("🎯 Perfect score! You're a quiz master!")
        elif percentage >= 70:
            print("🌟 Great job! You did really well!")
        elif percentage >= 50:
            print("👍 Good effort! Keep practicing!")
        else:
            print("💪 Keep trying! You'll do better next time!")
        
        print("\n" + "-"*50)
        print("📝 YOUR ANSWERS:")
        print("-"*50)
        
        for i, result in enumerate(self.results, 1):
            print(f"\nQ{i}: {result['question']}")
            print(f"   Your answer: {result['user_answer']}")
            print(f"   Correct answer: {result['correct_answer']}")
            print(f"   Status: {'✅ Correct' if result['is_correct'] else '❌ Incorrect'}")

def load_questions():
    # Sample questions - you can extend this list or load from a JSON file
    return [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "correct": 2  # Index starts from 0
        },
        {
            "question": "Which of these is a Python web framework?",
            "options": ["Django", "Laravel", "Ruby on Rails", "Spring"],
            "correct": 0
        },
        {
            "question": "What does 'OOP' stand for?",
            "options": ["Object-Oriented Programming", "Object-Oriented Process", "Object-Oriented Protocol", "Object-Oriented Procedure"],
            "correct": 0
        },
        {
            "question": "Which of these is NOT a Python data type?",
            "options": ["int", "str", "list", "array"],
            "correct": 3
        },
        {
            "question": "How do you start a while loop in Python?",
            "options": ["while x > y {", "while (x > y)", "while x > y:", "while x > y do"],
            "correct": 2
        }
    ]

if __name__ == "__main__":
    questions = load_questions()
    quiz = QuizApp(questions)
    quiz.run_quiz()
