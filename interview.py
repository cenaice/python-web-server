import random


class Interview:
    def __init__(self, questions) -> None:
        self.questions = questions

    def randInterviewQuestion(list_of_questions):
        pass


questions = ["Tell me about yourself. ", "Tell me about a time when you were balancing more than one deadline and how did you prioritize?", "Tell us about an innovative solution you came up with.", "Tell me about a time when you had to convey a vision to a group of people", "Tell me about a time when you failed", "Tell me about a time when you stepped up to be successful in a project with others",
             "Can you tell me about a time where you worked on a team?", "What is a challenge you faced in a work/school environment and how did you overcome it?", "Tell us about a time you faced criticism.", "Tell me about a time where you prioritized multiple things and were able to stay in commitment?", "Time where you worked with someone with a different perspective", "Tell me a time where you couldn't complete an assignment on time."]
script = True
while script:
    print("Welcome to the Interview Prep 2023-24")
    print("-----------------------------------------------")
    #seen_quest = set()
    for i in range(1, len(questions)+1):
        print(f"Question {i}:")
        question = random.choice(questions)
        #seen_quest.add(question)
        print(question)
        print(" ")
        print(" ")
        print("-----------------------------------------------")
        print("Press any key when you are ready to continue or type 0 to exit.")
        next_quest = input()
        if next_quest == "0":
            break
    script = False
