#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers
# in random order, along with the answer key

# Idea:
# creates 50 multiple-choices questions for each quiz, in random order
# provide the correct answer and three random wrong answers for each question, in random order
# writes the quizzes to 35 text files
# writes the answer keys to 35 text files

import re,random
from os import makedirs

numberofquiz = 35
# create state-capital dictionary, quiz db
text = '''Alabama	Montgomery	Montana	Helena
Alaska	Juneau	Nebraska	Lincoln
Arizona	Phoenix	Nevada	Carson City
Arkansas	Little Rock	New Hampshire	Concord
California	Sacramento	New Jersey	Trenton
Colorado	Denver	New Mexico	Santa Fe
Connecticut	Hartford	New York	Albany
Delaware	Dover	North Carolina	Raleigh
Florida	Tallahassee	North Dakota	Bismarck
Georgia	Atlanta	Ohio	Columbus
Hawaii	Honolulu	Oklahoma	Oklahoma City
Idaho	Boise	Oregon	Salem
Illinois	Springfield	Pennsylvania	Harrisburg
Indiana	Indianapolis	Rhode Island	Providence
Iowa	Des Moines	South Carolina	Columbia
Kansas	Topeka	South Dakota	Pierre
Kentucky	Frankfort	Tennessee	Nashville
Louisiana	Baton Rouge	Texas	Austin
Maine	Augusta	Utah	Salt Lake City
Maryland	Annapolis	Vermont	Montpelier
Massachusetts	Boston	Virginia	Richmond
Michigan	Lansing	Washington	Olympia
Minnesota	St. Paul	West Virginia	Charleston
Mississippi	Jackson	Wisconsin	Madison
Missouri	Jefferson City	Wyoming	Cheyenne'''
state_capital = text
state_capital1 = re.split(r'\t|\r\n|\n',state_capital)
capitals = {}
for i in range(0,len(state_capital1),2):
    capitals[state_capital1[i]] = state_capital1[i+1]

# create 35 different quizzes
makedirs('.\\quizdir')
for quizNumb in range(numberofquiz):
    # create the quiz and answer key files
    quizFile = open('.\\quizdir\\capitalsquiz%s' % (quizNumb + 1), 'w')
    answerFile = open('.\\quizdir\\capitalsquiz_answers%s' % (quizNumb + 1), 'w')
    # write out the header for each quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' '*20+'State Capitals Quiz (Form %s)\n\n' % (quizNumb + 1))
    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    # Loop through all 50 states, making a question for each
    for questionNum in range(len(states)):
        # get right and wrong answers
        correctanswer = capitals[states[questionNum]]
        wronganswer = list(capitals.values())
        del wronganswer[wronganswer.index(correctanswer)]
        # pick 3 wrong answer and 1 right answer, shuffle them
        answerOptions = random.sample(wronganswer,3) + [correctanswer]
        random.shuffle(answerOptions)
        # write out the question and answer options to quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum+1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        # write out the answer keys to answer file
        answerFile.write('%s. %s\n' % (questionNum+1, 'ABCD'[answerOptions.index(correctanswer)]))
    # close the files
    quizFile.close()
    answerFile.close()

