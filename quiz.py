def show_menu():

    print ("Quiz game")
    print ("xxxxxxxxxx")
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
  
    

    
while True:
    
    option = show_menu()
    
    if option == "3":
        print("\n Goodbye :(")
        break
        
    if option == "1":
        print("\n Let's run the Quiz! \n")
    
    if option == "2":
        add_a_question()
    