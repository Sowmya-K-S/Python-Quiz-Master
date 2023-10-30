#importing essential packages
import tkinter as tk
from tkinter import font
from tkinter import PhotoImage
from tkinter import messagebox
from PIL import Image,ImageTk

#creating main window
window=tk.Tk()

#title of window
window.title("Quiz Master")

#size of window to 100%
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

#to prevent resizing of window
window.resizable(False, False)

#setting icon to top of window
window.iconbitmap("ideas.ico")

#setting bachground color to main window
window.configure(bg="white")

#creating custom fonts
cust_font1=font.Font(family="Consolas", size=25, weight="bold")
cust_font2=font.Font(family="Consolas", size=18, weight="bold")
cust_font3=font.Font(family="Consolas", size=20, weight="bold")
cust_font4=font.Font(family="Consolas", size=10, weight="bold")
cust_font5=font.Font(family="Consolas", size=5, weight="bold")
cust_font6=font.Font(family="Consolas", size=30, weight="bold")
cust_font7=font.Font(family="Poppins",size=30,weight="bold")

#set of questions stored in the form of dictionary

#1. For C
questionsC=[
        {
            "question":"Who is the father of C language?",
            "options":["Denis Ritchie", "Charles Babbage","Max Newman", "Frances Allen"],
            "answer":0
        },
        {
            "question":"How many keywords are there in C language?",
            "options":["24", "32","25", "40"],
            "answer":1
        },
        {
            
            "question":"Which are the loops in C language?",
            "options":["for", "while","dowhile", "All of the above"],
            "answer":3
        },
         {
            "question":"In C, which data type is used to store single character?",
            "options":["char", "int","float", "double"],
            "answer":0
        },
         {
            "question":"What is the correct syntax for declaring a variable in C?",
            "options":["var_name data_type;", "data_type var_name;"," var_name : data_type;", "var_name(data_type);"],
            "answer":1
        },
         {
            "question":"Which operator is used to access the value at a specific memory address in C?",
            "options":["*", "&","->", "%"],
            "answer":0
        },
         {
            "question":"What is the result of the expression '5 + 7 / 2' in C?",
            "options":["6.5", "7.5","8.5", "9.5"],
            "answer":2
        },
         {
            "question":"In C, which operator is used for logical OR?",
            "options":["|", "&&","!", "||"],
            "answer":3
        },
         {
            "question":"In C, which header file is required for performing file input and output operations?",
            "options":["stdlib.h", "math.h","stdio.h", "string.h"],
            "answer":2
        },
         {
            "question":"What is the purpose of a semicolon in C?",
            "options":["Start a statement", "end a statement","pause a statement", "indicate a comment"],
            "answer":1
        }
    ]
#2. For Java
questionsJava=[
        {
            "question":"which concept allows you to define a blueprint for creating objects?",
            "options":["Class", "Polymorphism"," Encapsulation", "Inheritance"],
            "answer":0
        },
        {
            "question":"What is the process of hiding the implementation details and \n exposing only necessary features of an object known as in Java?",
            "options":["Inheritance", "Encapsulation","Abstraction", "Polymorphism"],
            "answer":2
        },
        {
            
            "question":"What is the term for defining multiple methods in a \n class with the same name but different parameters in Java?",
            "options":["Inheritance", "Polymorphism","Overriding", "Overloading"],
            "answer":3
        },
         {
            "question":"Which keyword is used in Java to declare a variable, method,\n or class member as accessible only within the same class?",
            "options":[" package-private", "private","protected", "public"],
            "answer":1
        },
         {
            "question":"What is the term for a method in Java that has the \n same name as the class and is used to create objects?",
            "options":["finalizer", "destructor","initializer", "constructor"],
            "answer":3
        },
         {
            "question":"What is the term for a class that cannot be instantiated \n and is typically used as a base class for other \n classes in Java?",
            "options":["Abstract class", "Final class","Static class", "Concrete class"],
            "answer":0
        },
         {
            "question":"In Java, which keyword is used to declare a constant?",
            "options":["final", "static","constant", "var"],
            "answer":0
        },
        {
            "question":"which access modifier makes a method or variable \n accessible only within the same class and its subclasses?",
            "options":["private", "protected","public", "package-private"],
            "answer":1
        },
        {
            "question":"which keyword is used to create an instance of a class?",
            "options":["instanceof", "super","this", "new"],
            "answer":3
        },
         {
            "question":"Which access modifier allows a class, method,or \n variable to be accessible from any class or package?",
            "options":["Private", "Protected","Public", "Default"],
            "answer":2
        }
]
#3.for OS
questionsOS=[
        {
            "question":"What is a process in an operating system?",
            "options":["A unit of execution", "A running program","Both a and b", "None of the above"],
            "answer":2
        },
        {
            "question":"Which scheduling algorithm in an operating system selects \n the process with the highest priority for execution?",
            "options":[" Shortest Job First","FCFS","Priority Scheduling","Round Robin"],
            "answer":2
        },
        {
            
            "question":"Which page replacement algorithm in an operating system \n selects the page that has not been used for the longest time?",
            "options":["Optimal", "MRU","LRU", "FIFO"],
            "answer":2
        },
         {
            "question":"Which of the following is NOT a state that a process can be in?",
            "options":["Completed", "Suspended","Ready", "Running"],
            "answer":1
        },
         {
            "question":"Which page replacement algorithm may suffer from the Belady's anomaly?",
            "options":["Optimal", "MRU","LRU","FIFO"],
            "answer":3
        },
         {
            "question":"Which disk scheduling algorithm tends to favor requests that \n are located close to the current position of the disk arm?",
            "options":["FCFS", "SSTF","SCAN", "C-LOOK"],
            "answer":1
        },
         {
            "question":"Which of the following scheduling algorithms provides the highest priority \n to the process with the shortest estimated time to completion?",
            "options":["Priority Scheduling", "Round Robin","SJF", "FCFS"],
            "answer":2
        },
         {
            "question":"Which memory allocation method in an operating system allocates the first \n available block of memory that is large enough to accommodate a process?",
            "options":["First fit", "Best fit","Worst fit", "Quick fit"],
            "answer":0
        },
         {
            "question":"Which of the following is NOT a component of the process control block (PCB)?",
            "options":[" CPU registers", "Process ID","File system", "Program counter"],
            "answer":2
        },
         {
            "question":"which algorithm is used in deadlock avoidance?",
            "options":["Prim's Algorithm", "Bankers algorithm","Kruskals algorithm", "Dijkstras algorithm"],
            "answer":1
        }
    ]
questionsDS=[
        {
            "question":"What is the primary principle of a stack data structure?",
            "options":["FIFO", "LIFO","Random Access", "Prority access"],
            "answer":1
        },
        {
            "question":"In a stack, which element can be accessed and removed?",
            "options":["bottom element", "top element","middle element", "Random element"],
            "answer":1
        },
        {
            
            "question":"What is the primary principle of a queue data structure?",
            "options":["FIFO", "LIFO","Random Access", "Priority access"],
            "answer":0
        },
         {
            "question":"Which operation is used to add an element to the end of a queue?",
            "options":["Dequeue", "Pop","Push", "Enqueue"],
            "answer":3
        },
         {
            "question":"In a binary tree, what is the maximum number of children a node can have?",
            "options":["1", "0","3", "2"],
            "answer":3
        },
         {
            "question":"What is the node at the top of a binary tree called?",
            "options":["Child node", "Parent node","Root node", "Leaf node"],
            "answer":2
        },
         {
            "question":"In a stack, which operation allows you to examine \nthe element at the top without removing it?",
            "options":["Push","Pop","Insert","Peek"],
            "answer":3
        },
         {
            "question":"Which type of linked list allows traversal in \nboth directions but consumes more memory?",
            "options":["Static linked list", "Circular linked list"," Doubly linked list", "Singly linked list"],
            "answer":2
        },
         {
            "question":"Which data structure is often used to implement \n undo functionality in text editors?",
            "options":["Stack", "Queue","Graph", "Tree"],
            "answer":0
        },
         {
            "question":"Which traversal of a binary tree visits the nodes \n in increasing order (sorted order)?",
            "options":["Preorder", "Inorder","Postorder", "Level-order"],
            "answer":1
        }
    ]
questionsPython=[
        {
            "question":"What does the range(5) function return?",
            "options":["Error", " [1, 2, 3, 4, 5]","[5, 4, 3, 2, 1, 0]", "[0, 1, 2, 3, 4]"],
            "answer":3
        },
        {
            "question":"Which statement is used to define a function in Python?",
            "options":["def", "fun","function", "define"],
            "answer":0
        },
        {
            
            "question":"How do you add an element to the end of a list in Python?",
            "options":["push()", "insert()","extend()", " append()"],
            "answer":3
        },
         {
            "question":"What method is used to convert a string to lowercase in Python?",
            "options":["lowercase()", "to_lower()","lower()", "convert_lowercase()"],
            "answer":2
        },
         {
            "question":"How do you find the length of a string in Python?",
            "options":["length(str)", "len(str)","str.len()", "str.length()"],
            "answer":1
        },
        {
            "question":"What is the result of not (False or True)?",
            "options":["True", "False","None", "Error"],
            "answer":1
        },
         {
            "question":"What is the primary data structure used to \n store data in key-value pairs in Python?",
            "options":["Tuple", "Dictionary","Set", "List"],
            "answer":1
        },
         {
            "question":"How do you import a module in Python?",
            "options":["use module_name", "require module_name","import module_name", "include module_name"],
            "answer":2
        },
         {
            "question":"Among these which module is used to create UI in python?",
            "options":["Tkinter", "numpy","pandas", "reportlab"],
            "answer":0
        },
        {
            "question":"Which is a popular python imaging library(PIL) fork support for \nopening, manipulating, and saving various image file formats?",
            "options":["Pillow", "winsound","ReportLab", "OpenCV"],
            "answer":0
        },
    ]
def choicepage():
    window.overrideredirect(True)

    # Function to hide widgets of start page 
    def hide_startpage():
        image_label.pack_forget()
        app_name.pack_forget()
        start_button.pack_forget()
    
    #calling hide start page function
    hide_startpage()

    #Creating new frame to choice page
    choice_frame=tk.Frame(window,bg="#f4b41a")
    choice_frame.pack(fill="both", expand=True)

    #creating label1
    label1=tk.Label(choice_frame,text="Hey!Welcome to Quiz Master", font=cust_font1,foreground="black")
    label1.configure(bg='#f4b41a', highlightthickness=0)

    #positioning label1
    label1.pack(side="top", pady=10)

    #creating label2
    label2=tk.Label(choice_frame,text="Choose your interest :)", font=cust_font1, foreground="black")
    label2.configure(bg='#f4b41a', highlightthickness=0)

    #positioning label2
    label2.pack(side="top", pady=15)

    #creating buttons and formatting them
    button1=tk.Button(choice_frame, text="C Programming", width=20, height=2, font=cust_font2,bg="#143d59",fg="white",borderwidth=2, relief="solid",command=lambda: button_fun(questionsC))
    button1.pack(pady=10)
    button2=tk.Button(choice_frame, text="Java", width=20, height=2, font=cust_font2,bg="#143d59",fg="white",borderwidth=2, relief="solid",command=lambda: button_fun(questionsJava))
    button2.pack(pady=10)
    button3=tk.Button(choice_frame, text="Operating Systems", width=20, height=2, font=cust_font2,bg="#143d59",fg="white", borderwidth=2, relief="solid",command=lambda: button_fun(questionsOS))
    button3.pack(pady=10)
    button4=tk.Button(choice_frame, text="Data structures", width=20, height=2, font=cust_font2,bg="#143d59",fg="white", borderwidth=2, relief="solid",command=lambda: button_fun(questionsDS))
    button4.pack(pady=10)
    button5=tk.Button(choice_frame, text="Python", width=20, height=2, font=cust_font2,bg="#143d59",fg="white", borderwidth=2, relief="solid",command=lambda: button_fun(questionsPython))
    button5.pack(pady=10)

    #creating label3
    label3=tk.Label(choice_frame,text="Lets start...", font=cust_font1,foreground="black")
    label3.configure(bg='#f4b41a', highlightthickness=0)

    #positioning label3
    label3.pack(side="top", pady=12)

    #function to hide widgets of choice page
    def hide_button_widgets():
        label1.pack_forget()
        label2.pack_forget()
        label3.pack_forget()
        button1.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button4.pack_forget()
        button5.pack_forget()

    #function to create question page
    def button_fun(questions):
        
        #calling function to hide widgets of choice
        hide_button_widgets()

        #creating new frame for question page
        button_frame=tk.Frame(choice_frame,bg="#87CEEB")
        button_frame.pack(fill="both", expand=True)
    
        #initialising current index to track number of questions
        global current_index
        current_index=0
        
        #initialising score
        global score
        score=0
        
        #---------------UI for frame--------------------#

        #creating label for question
        label_question=tk.Label(button_frame, text="",font=cust_font3, foreground="black")
        label_question.pack(pady=60)
        label_question.configure(bg="#87CEEB", highlightthickness=0)

        #creating buttons for options
        option_buttons=[]
        for i in range(4):
            button=tk.Button(button_frame,text="", width=20, height=1, font=cust_font2,bg="#FF7F7F", borderwidth=2, relief="solid",fg="black", command= lambda i=i: check_answer(i))
            button.pack(pady=15)
            option_buttons.append(button)
        
        #function to check whether there are questions left
        def next_question():
            global current_index
            current_index+=1
            if current_index==len(questions):
                messagebox.showinfo("Quiz completed","YOUR SCORE IS "+str(score))
                window.quit()
            else:
                response_label.config(text="")
                load_question()
        

        #label to show response
        response_label=tk.Label(button_frame,font=cust_font3,bg="#87CEEB")
        response_label.pack(pady=15)

        #creating next button    
        nxt_question=tk.Button(button_frame,text="Next",width=12, height=1, font=cust_font2,bg="#FFF44F", borderwidth=2, relief="solid",command=next_question)
        nxt_question.pack(pady=30)

        #-----Functions for validation and navigation-------#

        #function for checking the answer
        def check_answer(option):
            global score
            question_data=questions[current_index]
            right_answer=question_data["answer"]
            if option==right_answer:
                score=score+1
                response_label.config(text="Right answer!")
            else:
                correct_answer = question_data["options"][right_answer]
                response_label.config(text="Wrong answer!  \nCorrect answer:"+ correct_answer)

        #function to load question
        def load_question():
            question_data=questions[current_index]   
            label_question.config(text=question_data["question"])
            options=question_data["options"]
            for i in range(4):
                option_buttons[i].config(text=options[i])

        #calling load_question function for first time
        load_question()


#formatting of main window

#adding image to main window
image = PhotoImage(file="ideas.png")
image_label = tk.Label(window,image=image)
image_label.pack(pady=90)
image_label.config(bg="white")

#adding label
app_name=tk.Label(text="QuiZ MasteR",font=cust_font7,fg="black")
app_name.pack()
app_name.configure(bg="white")


#adding button to navigate to next page
buttonwidth=15
buttonheight=1
start_button=tk.Button(text="Start", font=cust_font2,width=buttonwidth, height=buttonheight,bg="#ff8a8a",fg="black", borderwidth=2, relief="solid",command=choicepage)
start_button.pack(pady=100)

#running main loop
window.mainloop()





