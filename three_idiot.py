score=0
#  Welcome Code
user_name=input("Enter your name: ")
print("😊 welcome 😊 ",user_name,"\n'in three idiot quiz game.'")
# Use Function & if else
def play(question,answer):
    global score
    print(question)
    Answer=input("eter option: ");
    if (Answer.upper()==answer.upper()):
        print('Right')
        print("-----------------*----------------------*---------------------------*---------------------")
        score+=1
    else:
        print('Wrong')
        print("-----------------*----------------------*---------------------------*---------------------")

# list of dictionary
questi = [{
  "question": "Q1. What was the name of the college where Rancho and Chatur studied?  \n1. Imperial College of Engineering\
    \n2. Indian College of Engineering \n3. Indian Institutes of Technology \n4. Imperial Centre of Engineering",
  "answer": '1'
}, {
  "question": "Q2. which year this movie was released?. \n1. 2002 \n2. 2009 \n3. 2008 \n4. 2007",
  "answer": '2'
}, {
  "question": "Q3. who was the girlfriend of rancho? \n1. pria \n2. preeti  \n3. ria  \n4. pia",
  "answer": '4'
}, {
  "question": "Q4. which actress name is pia?\n1. karina kapoor \n2. karishma kapoor \n3. priyanka chopra \n4. aishwrya roy",
  "answer": "1"
}, 
{"question": "Q5. Virus Viru Sahastrabuddhe took a power nap while listening to Opera. How long did the power nap last? \n1. 4 minute\n2. 5 minute\n3. 6 minute\n4. 7.5 minute","answer":"4"}
,{"question": "Q6. How many daughter have Virus Viru Sahastrabuddhe?\n1. 5\n2. 2\n3. 1\n4. 3","answer":"2"},
{"question": "Q7. What is the name of pia's sister in this movie?\n1. pria\n2. preeti\n3. Mona\n4. Sona","answer":"3"},
{"question": "Q8. whome gave Viru Sahastrabudhhe astronaut pen?\n1. pia\n2. Raju Rastogi\n3. Rancho\n4. Chatur Ramalingam","answer":"3" }
,{"question": "Q9. what is the real name of Rancho?\n1. Kabir Singh\n2. Amir khan\n3. Farhan Qureshi\n4. Phunsukh Wangdu","answer":"4"}
,{"question": "Q10. whose name is Silencer?\n1. Rancho\n2. Raju Rastogi\n3. Chatur Ramalingam \n4. Farhan Qureshi","answer":"3"}]
# Use Loop for call function
i = 0
while i<len(questi):
  queslist=questi[i]
  play(queslist["question"],queslist["answer"])
  if i<9:
    print("Do you not  want play again?")
    user_c = input("Enter 'no' for quit game:  ")
    if user_c.upper() == "NO":
          break
  i=i+1
print(user_name,",","Your final Score is ",score ,".")
print("🙏 🙏 Thankyou for playing game 😊.")