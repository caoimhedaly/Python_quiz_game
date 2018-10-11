


def show_menu():
    print()
    print("XXXXXXXXXXXX")
    print ("XXQuiz gameXX")
    print ("XXXXXXXXXXXX")
    print()
    print("1. Run Quiz")
    print("2. Enter a question")
    print("3. Exit")
    print()

    option= input("Enter option: ")

    return option
    
    
def add_a_question():

    question = input("enter a question: ")
    answer = input("You tell me, " + question.lower()+ ": ")
    
    with open("questions.txt", "a") as f:
        line =  question + "|" + answer + "\n"
        f.write(line)
        


def ask_questions():   
    
    print("\n Let's run the Quiz! \n")
    
    with open("questions.txt") as f:
        
        questions = f.read().split("\n")[:-1]
        
        
    score = 0
    
    for q in questions:
        split =  q.split("|")
        Q = (split[0])

        Ans = (split[1])

        guess = input(Q)
        print(guess)
        
        if guess == Ans:
            score +=1
            
    print("you scored {0}".format(score))


    


while True:
    
    option = show_menu()
    
    if option == "3":
        print("\n Goodbye :(")
        break
        
    if option == "1":
        ask_questions()
      
    
    if option == "2":
        add_a_question()
    