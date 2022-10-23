import random

#PROMPT: DREANCATCHER ARCHIVES! akari is talking with nightmare and he just wants to chat with them over tea and snacks... learn more about them and flirt with them and all that LOL. you can learn dreamcatcher archives lore thru talking to him.
#The goal the user is given is to go back to the archives. Get through to nightmare and return home! or reach the alternate ending(kinda LOL) where u just talk to him forever <3

#this base code is taken from code2college itself! i'm building off of it... i am also basing it off of my "where are you, dreamcatcher?" repl.it project i built for c2c bootcamp, in a section where you talk to nightmare :)

print('')

def generate_response(user_input):
  responses = [
    "Sorry, I didn't understand that. Are you returning or exchanging an item?",
    "Didn't catch that- Are you returning or exchanging?",
    "If you want to do something other than return or exchange an item, this helpline isn't for you!"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'
  

  user_input = input("Hello! Welcome to the Dreamy Dress Online Emporium: Are you here to return or exchange an item?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

  #while user_input == 





if __name__ == "__main__":
  init_chat()