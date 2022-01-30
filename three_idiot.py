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
        print("--------------------------------------")
        score+=1
    else:
        print('Wrong')
        print("-------------------------------------")

# list of dictionary
questi = [{
  "question": " What was the name of the college where Rancho and Chatur studied?  \n1.  Imperial College of Engineering\
    \n2. Indian College of Engineering \n3. Indian Institutes of Technology \n4. Imperial Centre of Engineering",
  "answer": '1'
}, {
  "question": "which year this movie was released?. \n1. 2002 \n2. 2009 \n3.2008 \n4.2007",
  "answer": '2'
}, {
  "question": "who was the girlfriend of rancho? \n1. pria \n2. preeti  \n3. ria  \n4.pia",
  "answer": '4'
}, {
  "question": "which actress name is pia\n1.karina kapoor \n2. karishma kapoor \n3. priyanka chopra \n4.aishwrya roy",
  "answer": "1"
}, 
{"question": "Virus Viru Sahastrabuddhe took a power nap while listening to Opera. How long did the power nap last? \n1. 4minute\n2. 5 minute\n3.6minute\n7.5minute"}];
# Use Loop for call function
i = 0
while i<len(questi):
  queslist=questi[i]
  play(queslist["question"],queslist["answer"])
  i=i+1
print(user_name,"Your final Score is ",score)