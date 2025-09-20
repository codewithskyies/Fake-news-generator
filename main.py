#write a program of fake news detection using python
import random



subjects=[  "virat kohli",
          "elon musk",
          "naraendra modi",
          "A mumbai local train",
          "A group of monkeys",
          "prime minister modi ji"]
actions=["is a grat cricketer",
         "trains runs"
         "is a great leader"
         "furnished with new features",
         "sky run","rocket launch"]

places=["in mumbai", 
        "in taj mahal",
        "in local bus",
        "at the airport",
        " at shop",
    "in the market"]
#start the headline geaneration loop

while True:

    
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)

    headline=f"Breaking News:{subject} {action} {place}."
    print("\n"+headline)
    user_input=input("\n Do you want to geanrate another fake news headline? (yes/no)").strip().lower()
    if user_input=="yes":

        continue
    elif user_input=="no":
        break
    
        

    print("\nThank you for using the fake news Generator.Have a fun Day")

