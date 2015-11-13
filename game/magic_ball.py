#! /usr/bin/env python3.5
# -*- coding: utf-8 -*-

# More info about Magic 8 Ball, http://en.wikipedia.org/wiki/Magic_8-Ball

import random
import sys

# 8 Ball Answers
answers = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good", 
    "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it",
    "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now",
    "Dont count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

print ('Welcome to Magic 8 Ball!')
print ('Please ask your question!')
question = input()

play = True
while play == True:    
    what = random.choice(answers)
    print ('My answer is: '+ what +'!')
    print ('If you want to exit, type quit or ask again!')
    question = input()
    if question == 'quit':
        quit = sys.exit("Good bye!")
        play = False