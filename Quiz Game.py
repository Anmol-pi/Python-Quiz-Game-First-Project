import pickle
import random
import pyfiglet as py
from termcolor import colored

def save_questions(filename, questions):
    with open(filename, "wb") as file:
        pickle.dump(questions, file)


def load(filename):
    try:
        try:
            with open(filename, "rb") as file:
                questions = pickle.load(file)
                return questions
        except EOFError:
            return {}
    except FileNotFoundError:
        with open(filename, "wb") as file:
            return {}

def intro_message():
    print("\033[1m"+"\033[4m")
    print("Welcome to this fun quiz!\nAre you ready to test your knowledge!")
    print("There are total 10 questions. You may skip a question by typing 'skip'.\n")
    input("Press any key to start the fun ;) ")
    print("\033[0m")
    


def chooseAQuestion(questions, l):
    while len(l) > 0:
        nnn = random.choice(l)

        if nnn in l:
            question = questions[nnn]

            l.remove(nnn)
            questions.pop(nnn)

            return question, nnn
    return None, None



def check_ans(question, ans, attempts, score):
    if question["answer"].lower() == ans.lower():
        print("Correct Answer!\nYour score is", score + 1, "\n")
        return True
    elif attempts>1:
        print("\033[36m"+"\nWrong Answer :("+"\033[0m"+"\033[33m"+"\nYou have", attempts - 1, "attempts left\n"+"\033[0m"+"\033[31m"+"Try again...\n"+"\033[0m")
        return False
    elif attempts==1:
        print("\033[36m"+"\nWrong Answer :("+"\033[0m"+"\033[33m"+"\nNo attempts left\n"+"\033[0m")
        return False


def alter_question(category, filename,key):
    if key in category:
        ques = input("Enter the new question: ")
        ans = input("Enter the answer of the new question: ")
        new_question = {
            "question": ques,
            "answer": ans}
        category[key] = new_question

        save_questions(filename, category)
        print("Question altered successfully!\n")
    else:
        print("\nInvalid index")

def remove_question(category, key, filename):
    if key in category:
        category.pop(key)
        save_questions(filename, category)
        print("Question removed successfully!\n")
    else:
        print("\nInvalid index")

def add_question(filename, category):
    l=[]
    for i in category:
        l.append(i)
    length=len(l)+1

    while True:
        question = input("Enter the new question:-")
        answer = input(" Enter the new answer:-")
        new_question = {
            "question": question,
            "answer": answer}
        category[length] = new_question
    
        ask = int(input("To add another Question enter 1 or enter 0 to exit:-"))
        if ask == 1:
            length += 1
            continue

        elif ask == 0:
            save_questions(filename, category)
            print("Question added successfully!\n")
            break
def log_in():
            info=load(file)
            loggg=py.figlet_format("Log In ", font= 'standard', justify="center", width=110)
            print(colored(loggg, 'yellow'))
            user_un=input("Enter your username: ")
            if user_un in info:
                user_pass=input("Enter your password: ")
                if user_pass==info[user_un]:
                    print("\033[1m"+"\033[95m"+"\n\t\t\t\t\t\t-----WELCOME", user_un.upper(),"-----\n"+"\033[0m")
                    empty_check()
                    intro_message()
                    d=code_run(user_un)
                else:
                    print(" invalid password \nplease try again")
            else:
                print("invalid username\nplease try again")

def empty_check():
    Q1 = load("Marvel.bin")
    Q2 = load("Games.bin")
    Q3 = load("History.bin")
    if Q1=={} or Q2=={} or Q3=={}:
        save_questions("Marvel.bin", D1)
        save_questions("Games.bin", D2)
        save_questions("History.bin", D3)
        print()

def code_run(name):
    Q1 = load("Marvel.bin")
    Q2 = load("Games.bin")
    Q3 = load("History.bin")
    score = 0
    while True:
        a=(py.figlet_format("Menu", font= 'standard', justify="center", width=110))
        print(colored(a, 'green'))
        print("\n1. History quiz  \n2. Marvel quiz\n3. Video game quiz\n4. check your records\n5. Top scorer\n6. To exit ")
        n = int(input("Enter your choice (1, 2, 3, 4, 5, 6): "))
        if n==1:
            a=py.figlet_format("History Quiz", font= 'standard', justify="center", width=110)
            print(colored(a, 'green'))
            category=Q3
            a=load("History.bin")
            c="HISTORY QUIZ"
            break
        elif n==2:
            a=py.figlet_format("Marvel Quiz", font= 'standard', justify="center", width=110)
            print(colored(a, 'yellow'))           
            category=Q1
            a=load("Marvel.bin")
            c="MARVEL QUIZ"
            break
        elif n==3:
            a=py.figlet_format("Video  Games  Quiz", font= 'standard', justify="center", width=110)
            print(colored(a, 'blue'))          
            category=Q2
            a=load("Games.bin")
            c="GAMES QUIZ"
            break
        elif n==4:
            d=load("data.bin")
            a=py.figlet_format("Scoreboard", font= 'standard', justify="center", width=110)
            print(colored(a, 'yellow'))
            print("\n"+"\033[1m"+"\033[4m"+"\tQuiz",'\t\t',"Score",'\t',"No. of questions\n"+"\033[0m")
            y=0
            for t in d:
                if d[t]["uname"]==name:
                    y+=1
                    print(str(y)+".  ",d[t]["quiz"],"\t  ",d[t]["score"],"\t    ",d[t]["questions"])
            code_run(name)
        elif n==5:
            a=py.figlet_format("Top  Scorer", font= 'standard', justify="center", width=110)
            print(colored(a, 'magenta'))
            top()
        elif n==6:
            return {}  
        else:
            print("Invalid choice. Exiting the program.")
            return {}

    questions = category
    otherQuestion = questions


    score=0
    while True:
        l = []
        for i in otherQuestion:
            l.append(i)


        question, keyOfQuestion = chooseAQuestion(otherQuestion, l)


        if question is None or keyOfQuestion is None:
            break

        attempts = 3

        while attempts > 0:

            print("\033[1m"+question["question"]+"\033[0m")
            answer = input("Enter Answer (To move to the next question, type 'skip'): ")
            if answer == "skip":
                print()
                break
            check = check_ans(question, answer, attempts, score)
            if check == True:
                score += 1
                break
            else:
                attempts -= 1
            
            if attempts == 2:
                print("\033[1m"+"\033[4m"+"Hint :- Length of answer (including spaces):-", len(question["answer"]), "\n"+"\033[0m")
            elif attempts == 1:
                print("\033[1m"+"\033[4m"+"Hint:- The first letter of answer is:- ", question["answer"][0], "\n"+"\033[0m")

    sc=py.figlet_format("Score :- " + str(score), font= 'standard', justify="center", width=110)
    print(colored(sc, 'magenta'))
    print("\033[1m"+"\n\t\t\t\t\t\t"+"\033[4m"+"-----Answers-----\n"+"\033[0m")
    for i in a:
        print(i,a[i]["question"],"\n","answer:-",a[i]["answer"])
        
    print("\033[1m"+"\033[4m"+"\nThanks for playing\n"+"\033[0m")

    k=[]
    for j in a:
        k.append(j)
    data=load("data.bin")
    n=[]
    for e in data:
        n.append(e)
    new_data ={
        "uname": name,
        "quiz": c,
        "score": score,
        "questions":len(k)}
    data[len(n)+1] = new_data
    save_questions("data.bin", data)
    print("\nif you want to choose something else press '1' or press 0 to halt")
    u=int(input("Enter you choice:-"))
    

    if u ==1:
        code_run(name)

def top():
    print("\n1. Top scorer of History Quiz\n2. Top scorer of Marval Quiz\n3. Top scorer of Games Quiz\n")
    t=int(input("Enter your choice: "))
    if t==1:
        quiz="HISTORY QUIZ"
    elif t==2:
        quiz="MARVEL QUIZ"
    elif t==3:
        quiz="GAMES QUIZ"
    data=load("data.bin")
    l=[]
    for j in data:
        if data[j]["quiz"]==quiz:
            l.append(j)
    if l==[]:
        print("\nNo data")
    else:
        n1_score=data[l[0]]["questions"]-data[l[0]]["score"]
        greater=n1_score
        a=[]
        for i in l:
            n2_score=data[i]["questions"]-data[i]["score"]
            if n2_score < greater:
                greater=n2_score
        for i in l:
            n3_score=data[i]["questions"]-data[i]["score"]
            b=0
            if n3_score==greater:
                for c in a:
                    if data[i]["uname"]==c:
                        b+=1
                if b==0:
                    print("\033[4m"+"\033[1m"+"\033[95m"+"\nTop scorer:-", "\033[0m",data[i]["uname"])
                    a.append(data[i]["uname"])        
# Main         


D1 = {
    1: {
        "question": "What is the first name of Iron Man?",
        "answer": "Tony"
    },
    2: {
        "question": "Who is called the god of thunder in the Marvel Universe?",
        "answer": "Thor"
    },
    3: {
        "question": "Who is the alter ego of the superhero Spider-Man?",
        "answer": "Peter"
    },
    4: {
        "question": "What is the real name of the superhero Black Widow?",
        "answer": "Natasha"
    },
    5: {
        "question": "Who is the main villain in the movie 'Avengers: Infinity War'?",
        "answer": "Thanos"
    },
    6: {
        "question": "Who is the leader of the X-Men?",
        "answer": "Xavier"
    },
    7: {
        "question": "What is the name of the fictional metal used in Captain America's shield?",
        "answer": "Vibranium"
    },
    8: {
        "question": "Who is the arch-nemesis of the superhero Iron Man?",
        "answer": "Mandarin"
    },
    9: {
        "question": "Which character has the ability to shrink and grow in size?",
        "answer": "Ant Man"
    },
    10: {
        "question": "Who is the love interest of the superhero Deadpool?",
        "answer": "Vanessa"
    }}
D2 = {
    1: {
        "question": "What is the name of the main character in the 'Legend of Zelda' series?",
        "answer": "Link"
    },
    2: {
        "question": "Which video game franchise features the character Master Chief?",
        "answer": "Halo"
    },
    3: {
        "question": "What is the best-selling video game of all time?",
        "answer": "Minecraft"
    },
    4: {
        "question": "Which game series features the character Mario?",
        "answer": "Mario"
    },
    5: {
        "question": "Which video game is set in the post-apocalyptic wasteland of a nuclear war?",
        "answer": "Fallout"
    },
    6: {
        "question": "What is the name of the main character in the 'Final Fantasy' series?",
        "answer": "Cloud"
    },
    7: {
        "question": "Which video game series features the character Lara Croft?",
        "answer": "Tomb Raider"
    },
    8: {
        "question": "Which game introduced the character 'Master Chief'?",
        "answer": "Halo: Combat Evolved"
    },
    9: {
        "question": "Which video game series is set in the world of Azeroth?",
        "answer": "World of Warcraft"
    },
    10: {
        "question": "Which game franchise features the character Kratos?",
        "answer": "God of War"
    }}

D3 = {
    1: {
        "question": "In which year did Christopher Columbus reach the Americas?",
        "answer": "1492"
    },
    2: {
        "question": "Which ancient civilization built the Great Pyramids of Giza?",
        "answer": "Egyptians"
    },
    3: {
        "question": "Who was the first President of the United States?",
        "answer": "Washington"
    },
    4: {
        "question": "Which event marked the start of World War I?",
        "answer": "Assassination"
    },
    5: {
        "question": "Who painted the famous artwork 'Mona Lisa'?",
        "answer": "Da Vinci"
    },
    6: {
        "question": "Which European country colonized a significant portion of Africa during the Scramble for Africa?",
        "answer": "Britain"
    },
    7: {
        "question": "Which war was fought between the North and the South in the United States from 1861 to 1865?",
        "answer": "Civil War"
    },
    8: {
        "question": "Which country was the first to circumnavigate the globe?",
        "answer": "Spain"
    },
    9: {
        "question": "Which document established the basic principles of the United States and declared its independence from Britain?",
        "answer": "Declaration"
    },
    10: {
        "question": "Who was the leader of the Soviet Union during World War II?",
        "answer": "Stalin"
    }}


a=py.figlet_format("Main", font= 'standard', justify="center", width=110)
print(colored(a, 'red'))

print("\033[1m"+"\033[4m"+"Log in as\n"+"\033[0m")
print("1.","\033[94m"+"Admin"+"\033[0m")
print("2.","\033[92m"+"User\n"+"\033[0m")
a=int(input("Enter your answer: "))
adm_data={"rahul":"12345678", "anmol": "1234567","shayan":" 123456", "adi": " 0001","1":"12"}
file="user_data.bin"
check=load(file)
if check=={}:
    save_questions(file,adm_data)
if a==1:
    adm_un=input("Enter your username: ")
    if adm_un in adm_data:
        adm_pass=input("Enter your password: ")
        if adm_pass==adm_data[adm_un]:
            print(py.figlet_format("WELCOME   " + adm_un.upper(),justify="center",font="small",width=110))
       
            empty_check()
            print("\033[1m"+"\033[4m"+"How may I help you...."+"\033[0m")

            print("\n\n1.Edit History quiz \n2.Edit Marvel quiz\n3.Edit Video game quiz\n4.See the records")
            req=int(input("Enter your choice: "))
            if req==1:
                print("\nif you want to reset the data of this file,"+"\033[91m"+"Enter 1 or 0 to 'skip'"+"\033[0m")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    save_questions("History.bin", D3)
                    print("File Reseted Successfully")

                Q1 = load("History.bin")
                category = Q1
                filename = "History.bin"
                a = load(filename)
                while True:
                    print("\n1. alter\n2. remove\n3. Add question\n4. no change\n")
                    ask = int(input("enter your choice (1,2,3,4):- "))
                    print()
                    if ask == 1:
                        for i in a:
                            print(i,a[i]["question"])
                        key=int(input("Enter the index of the question you want to alter "))
                        alter_question(a, filename,key)
                    elif ask == 2:
                        for i in a:
                            print(i,a[i]["question"])
                        key=int(input("Enter the index of the question you want to delete "))
                        remove_question(a, key, filename)
                    elif ask ==3:
                        add_question(filename, a)
                    elif ask==4:
                        break
                    else:
                        print("invalid input")
            elif req==2:
                print("\nif you want to reset the data of this file,"+"\033[91m"+"Enter 1 or 0 to 'skip'"+"\033[0m")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    save_questions("Marvel.bin", D1)
                    print("File Reseted Successfully")

                Q2 = load("Marvel.bin")
                category = Q2
                filename = "Marvel.bin"
                a = load(filename)
                while True:
                    print("\n1. alter\n2. remove\n3. Add question\n4. no change\n")
                    ask = int(input("enter your choice (1,2,3,4):- "))
                    print()
                    if ask == 1:
                        for i in a:
                            print(i,a[i]["question"])
                        key=int(input("Enter the index of the question you want to alter "))
                        alter_question(a, filename,key)
                    elif ask == 2:
                        for i in a:
                            print(i,a[i]["question"])
                        key=int(input("Enter the index of the question you want to delete "))
                        remove_question(a, key, filename)
                    elif ask ==3:
                        add_question(filename, a)
                    elif ask==4:
                        break
                    else:
                        print("invalid input")
            elif req==3:
                print("\nif you want to reset the data of this file,"+"\033[91m"+"Enter 1 or 0 to 'skip'"+"\033[0m")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    save_questions("Games.bin", D2)
                    print("File Reseted Successfully")

                Q2 = load("Games.bin")
                category = Q2
                filename = "Games.bin"
                a = load(filename)
                while True:
                    print("\n1. alter\n2. remove\n3. Add question\n4. no change\n")
                    ask = int(input("enter your choice (1,2,3,4):- "))
                    print()
                    if ask == 1:
                        for i in a:
                            print(i,a[i]["question"])
                        key=int(input("Enter the index of the question you want to alter "))
                        alter_question(a, filename,key)
                    elif ask == 2:
                        for i in a:
                            print(i,a[i]["question"])
                        key=int(input("Enter the index of the question you want to delete "))
                        remove_question(a, key, filename)
                    elif ask ==3:
                        add_question(filename, a)
                    elif ask==4:
                        break
                    else:
                        print("invalid input")
            elif req==4:
                data=load("data.bin")
                print("\033[1m"+"\033[4m"+"Username".center(13),'\t',"    Quiz   ",'\t',"  Score ",'\t',"  No. of questions  \n"+"\033[0m")
               
                for i in data:
                    print(str(i)+".","\t",data[i]["uname"],'\t',data[i]["quiz"],"\t    ",data[i]["score"],'\t\t     ',data[i]["questions"])
            else:
                print("invalid input")
        else:
            print(" invalid pass\nplease try again")
    else:
        print("invalid username\nplease try again")
if a ==2:
    print("1.","\033[91m"+"Log in"+"\033[0m")
    print("2.","\033[93m"+"Signup\n"+"\033[0m")

    c=int(input("Enter your choice: "))
    if c==1:
        log_in()
    if c==2:
        b=py.figlet_format("Sign Up", font= 'standard', justify="center", width=110)
        print(colored(b, 'cyan'))
        info=load(file)
        add_un=input("Enter your username: ")

        if add_un in info:
            print("\033[91m"+"\nUserename already exist"+"\033[0m")
        else:
            add_pass=input("Enter your password: ")
            com_pass=input("Comfirm your password: ")
            if add_pass==com_pass:
                f=load(file)
                f[add_un]=add_pass
                save_questions(file,f)
                print("\n"+"\033[4m","Sign up successful\nlogging in....\n"+"\033[0m")
                log_in()
            else:
                print("\033[91m"+"\nEntered passwords doesn't match\nTry again"+"\033[0m")