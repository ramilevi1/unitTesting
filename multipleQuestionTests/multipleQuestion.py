import json
    
# open JSON file
f = open ('data.json')
# Reading from file to Python list of objects

data = json.load(f) 
# Iterating through the python object list
# for i in data['Questions_details']:
#     print(i['correctAnswer'])
#exmaple of printing a  location object attribute in the list
# print (data['Questions_details'][0]['correctAnswer'])
# Closing file


f.close()

def get_user_input(data):
    lst = []
    for Question in data:
            answer_challenge = str(input(Question.promt).lower())
            lst.append(answer_challenge)
    print(lst)
    return(lst) 


def run_quiz(lst): 
    score = 0
    for i in range(len(lst)):
       if (lst[i] == data['Questions_details'][i]['correctAnswer']):
            score +=1
    print("You got " + str(score) + "/" + str(len(lst)) + " correct" )
    
    return score
   

run_quiz(get_user_input(data))