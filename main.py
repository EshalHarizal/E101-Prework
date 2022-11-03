import random
import time

#----GLOBAL STUFF
#isakari determines whether or not the user is using the canon name for the protagonist of Dreamcatcher Archives
isakari = 0
#ending marks the end of the story (any route) and stops the convo whileloop.
ending = 0


#PROMPT: DREANCATCHER ARCHIVES! akari is talking with nightmare and he just wants to chat with them over tea and snacks... learn more about them and flirt with them and all that LOL. you can learn dreamcatcher archives lore thru talking to him.
#The goal the user is given is to go back to the archives. Get through to nightmare and return home! or reach the alternate ending (kinda LOL) where u just talk to him forever <3

#this base code is taken from code2college itself! i'm building off of it... i am also basing it off of my "where are you, dreamcatcher?" repl.it project i built for c2c bootcamp, in a section where you talk to nightmare :)


#TODO: make swearlist, convowords, etc


#----NAME
def userintro():
  global name
  name = input("[AH. WHAT A PLEASURE TO MEET THE DREAMCATCHER AGAIN. DO TELL, WHAT WAS YOUR NAME?]\n")
  #i've made name stuff like this before! what this does is remove spaces and stuff to more easily check for names. this is such a common line of code i have no idea if it should be attributed to someone... Here, I wrote it myself with no references.
  #(theres prob a better way to do this but this is just a first draft <3)
  
  tempname = name.lower()
  tempname = tempname.replace(" ","")
  tempname = tempname.replace(".","")
  tempname = tempname.replace("-","")
  tempname = tempname.replace("\'","")
  tempname = tempname.replace("\"","")

  #TODO: loop and wait for user input, but give user a name after they loop like, 3 times.
  if tempname == "":
    name = "Dear"
    print("[...FINE. IF YOU WON'T RESPOND, I CAN CALL YOU WHAT I WANT, YES?]\n")
  elif (tempname=='ia') or (tempname=='kuromiya') or (tempname=='akari'):
    global isakari
    isakari = 1
    print(f'[AH- {name.upper()}! OF COURSE IT\'S YOU, MY DEAR.]\n')
  else:
    print(f'[I SEE... {name.upper()}. I REMEMBER YOU.]\n')

  teatype()

#----WHAT TEA D'YA WANT?
def teatype():
  teachoice = ""
  
  time.sleep(1.5)
  if isakari == 1:
    print('[HAVE YOU COME TO VISIT AGAIN? I MISSED YOU, AKARI... COME SIT WITH ME.]')
  else:
    print('[SURELY YOU REMEMBER ME: I AM NIGHTMARE. AFTER THE FIASCO OF LAST TIME- YOU GETTING LOST HERE-, I CERTAINLY HAVEN\'T FORGETTEN YOU.]')
  time.sleep(2.3)
  teachoice = input('[OH, HOW RUDE OF ME. I HAVEN\'T EVEN OFFERED YOU A CUP OF TEA. WHAT KIND OF TEA DO YOU FANCY?]\n')

  specificteas = [
    "earlgrey", "ceylon", "assam", "darjeeling", "yunnan", "dianhong", "orientalbeauty", "whiteneedle", "breakfast", "keemun", "ladygrey", "masala", "chai", "lapsang", "souchong", "sencha"
  ]
  herbalteas = [
    "lavender", "mint", "rooibos", "rose", "ginger", "cinnamon", "jasmine", "tulsi", "barley", "gingko", "eucalyptus", "sage", "berry", "anise", "root", "flower", "hibiscus", "chrysanthemum", "osmanthus", "dandelion", "nettle", "jasmine", "yarrow", "guava", "yerbamate", "mate"
  ]
  
  tempchoice = teachoice.lower()
  tempchoice = tempchoice.replace(" ","")
  tempchoice = tempchoice.replace(".","")
  tempchoice = tempchoice.replace("-","")
  tempchoice = tempchoice.replace("/","")
  tempchoice = tempchoice.replace("\'","")
  tempchoice = tempchoice.replace("\"","")

  if tempchoice == "chamomile":
    if isakari == 1:
      print('[AH, OF COURSE. I HAVE A NEW BLEND PREPARED FOR YOU.]')
    else:
      print(f'[...CHAMOMILE? PERFECT FOR SLEEP. I THINK I LIKE YOU, DREAMCATCHER {name.upper()}.]')
  elif "black" in tempchoice:
    print('[AH, A CLASSIC CHOICE. I\'LL POUR A PERSONAL BLEND.]')
  elif "oolong" in tempchoice:
    print('[I HAVEN\'T HAD OOLONG IN QUITE A LONG TIME... HERE\'S A PICK OF ORIENTAL BEAUTY I\'VE BEEN WANTING TO TRY.]')
  elif "white" in tempchoice:
    print('[HM, WHITE TEA... I DO HAVE THAT SET OF SILVER NEEDLE LEAVES... I\'LL STEEP IT.]')
  elif "green" in tempchoice:
    print('[...GREEN TEA? DREAM HAS BEEN INFLUENCING YOU WITH HIS HORRENDOUS TASTE. HE CAN HARDLY MAKE JASMINE GREEN THE WAY I DO.]')
  elif "matcha" in tempchoice:
    print(f'[EXCELLENT CHOICE, DREAMCATCHER {name.upper()}. I AM VERY GOOD AT MAKING MATCHA.')
  elif ("herb" in tempchoice) or ("tisane" in tempchoice):
    print('[OH, I CAN PICK AN HERBAL TEA FOR YOU...]')
  #i didn't know how to find if a list item was in a string the way i wanted, and i found my answer on geeksforgeeks.com on their "Test if string contains element from list" article
  elif any(i in tempchoice for i in specificteas):
    print(f'[AH, {teachoice.upper()}? OF COURSE I HAVE THAT.]')
  elif any(i in tempchoice for i in herbalteas):
    print(f'[{teachoice.upper()}? HOW INTERESTING! IT\'S BEEN A WHILE SINCE I\'VE SERVED THESE TEAS TO SOMEONE.]')
  else: #not gonna let the user redo their choice. nightmares not gonna sit here in a loop where you cant decide what tea you want
    print('[AH... NO, IT\'D BE MUCH EASIER IF I JUST GAVE YOU A CUP OF MY CHOSING INSTEAD. I DO HOPE YOU ENJOY EARL GREY.]')

  init_chat()

def fallback_response(userinput):
  negresponses = [
    "He clearly doesn't care about what you're saying... Maybe something else?",
    "The look on his face turns into something resembling boredom, looking down at his teacup. Try a different topic..?",
    "He doesn't have a response, barely holding an interest in your words. Something else, then..."
  ]
  responses = [
    "He only nods, looking at you with an enigmatic look on his face.",
    "It doesn't seem like the comment phases him... Say something that catches his attention!",
    "You can't read the look on his face... Another topic, then?",
    "Doesn't look like he has anything to say to that."
  ]
  posresponses = [
    "...He only looks at you with a smitten smile.",
    "He's clearly more focused on you than your words. Say something that catches his attention!"
    "The smile on his face is clearly more distracted than focused..."
  ]
  blankresponses = [
    "...He waits for you to speak.",
    "He only looks at you in equal silence.",
    "[...WELL?]"
  ]
  akaresponses = responses + posresponses
  strangeresponses = negresponses + responses

  if userinput == "":
    return random.choice(blankresponses)
  elif isakari == 1:
    return random.choice(akaresponses)
  else:
    return random.choice(strangeresponses)

def init_chat():
  #quit_character = "q" #(undesired, cant leave until conclusion is reached)

  
  
  time.sleep(2)
  print('\n\nNightmare begins to brew a new pot of tea, and he looks at you from across the desk.')
  time.sleep(3)
  print(f'[WELL? SINCE YOU\'RE HERE AND ALL... TALK TO ME, DREAMCATCHER {name.upper()}.]')
  time.sleep(2)
  userinput = input("You say...\n")

  tempinput = userinput.lower()
  tempinput = tempinput.replace(" ","")
  tempinput = tempinput.replace(".","")
  tempinput = tempinput.replace("-","")
  tempinput = tempinput.replace("/","")
  tempinput = tempinput.replace("\'","")
  tempinput = tempinput.replace("\"","")

  while ending != 1:
    userinput = input("\n" + fallback_response(userinput) + "\n\n")


#-------------------------------#
#----EXPOSITION
print('...It\'s dark.')
time.sleep(2)
print('Your eyes take a moment to adjust to the marble-and-wood study surrounding you.')
time.sleep(2)
print('At the study\'s desk sits a void-like figure that you can\'t make out...')
time.sleep(2)
print('The feeling of dread overwhelms you, but it feels so familiar.')
time.sleep(2.5)
print('He speaks.\n')
time.sleep(2)
userintro()


if __name__ == "__main__":
  init_chat()