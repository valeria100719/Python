#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

game=["scissor", "paper", "rock"]

while player == False:
    pc=random.choice(game)
    player=False
    user=input("play!").lower()
    if user == pc:
        print("tie")
        
    elif user == "paper":
        if pc == "scissor":
            print("u lose")
        else:
            print("you win")
            
    elif user == "scissor":
        if pc == "rock":
            print("u lose")
        else:
            print("you win")
            
    elif user == "rock":
        if pc == "paper":
            print("u lose")
        else:
            print("you win")


# In[ ]:




