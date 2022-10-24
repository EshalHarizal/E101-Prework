import random
import time

#----GLOBAL VARIABLES
#isakari determines whether or not the user is using the canon name for the protagonist of Dreamcatcher Archives
isakari = 0

#PROMPT: DREANCATCHER ARCHIVES! akari is talking with nightmare and he just wants to chat with them over tea and snacks... learn more about them and flirt with them and all that LOL. you can learn dreamcatcher archives lore thru talking to him.
#The goal the user is given is to go back to the archives. Get through to nightmare and return home! or reach the alternate ending (kinda LOL) where u just talk to him forever <3

#this base code is taken from code2college itself! i'm building off of it... i am also basing it off of my "where are you, dreamcatcher?" repl.it project i built for c2c bootcamp, in a section where you talk to nightmare :)



#----NAME
def userintro():
  global name
  name = input("[AH. WHAT A PLEASURE TO MEET THE DREAMCATCHER AGAIN. DO TELL, WHAT WAS YOUR NAME?]\n")
  #i've made name stuff like this before! what this does is remove spaces and stuff to more easily check for names. this is such a common line of code i have no idea if it should be attributed to someone... Here, I wrote it myself with no references.
  #(theres prob a better way to do this but this is just a first draft <3)
  name = name.lower()
  name = name.replace(" ","")
  name = name.replace(".","")
  name = name.replace("-","")
  tempname = name
  if (tempname=='ia') or (tempname=='kuromiya') or (tempname=='akari'):
    global isakari
    isakari = 1
    print(f'[AH- {name.upper()}! OF COURSE IT\'S YOU, MY DEAR.]\n')
  else:
    print(f'[I SEE... {name.upper()}. I REMEMBER YOU.]\n')

  teatype()

#----WHAT TEA D'YA WANT?
def teatype():
  time.sleep(2.5)
  print('[SURELY YOU REMEMBER ME: I AM NIGHTMARE. AFTER THE FIASCO OF LAST TIME- YOU GETTING LOST HERE-, I CERTAINLY HAVEN\'T FORGETTEN YOU.]')
  time.sleep(1)
  teachoice = input('[OH, HOW RUDE OF ME. I HAVEN\'T EVEN OFFERED YOU A CUP OF TEA. WHAT KIND OF TEA DO YOU FANCY?]\n')

  teachoice = teachoice.lower()
  teachoice = teachoice.replace(" ","")
  teachoice = teachoice.replace(".","")
  teachoice = teachoice.replace("-","")

  if teachoice == "chamomile":
    if isakari == 1:
      print('[AH, OF COURSE. I HAVE A NEW BLEND PREPARED FOR YOU.]')
    else:
      print(f'[CHAMOMILE? I THINK I LIKE YOU, DREAMCATCHER {name.upper()}]')
  if "black" in teachoice:
    print('YOOO CHILL')

  init_chat()

def generate_response(user_input):
  responses = [
    "Sorry, I didn't understand that. Are you returning or exchanging an item?",
    "Didn't catch that- Are you returning or exchanging?",
    "If you want to do something other than return or exchange an item, this helpline isn't for you!"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'
  

  user_input = input("Yasss")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

  #while user_input == 


#-------------------------------#
#----EXPOSITION
print('...It\'s dark.')
time.sleep(2)
print('Your eyes take a moment to adjust to the marble-and-wood study surrounding you.')
time.sleep(2)
print('At the study\'s desk sits a void-like figure that you can\'t make out...')
time.sleep(2)
print('The feeling of dread overwhelms you, but it feels so familiar.')
time.sleep(2)
print('He speaks.\n')
time.sleep(2)
userintro()


if __name__ == "__main__":
  init_chat()