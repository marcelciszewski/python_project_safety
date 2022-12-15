# Import important stuff
#======================================================================================
#Name: Marcel Ciszewski
#07/12/2022 (09:50am)
#COMPLETED: Five Scenarios with five to eight questions each.
#PLANNED: Eight scenarios, with at least five to ten question each.
#======================================================================================
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
import time
import datetime
import webbrowser
import sys
from time import sleep
import os
import time
import platform
arch = platform.machine()
if arch == "i386":
    print("=========================================================================================================")
    print("Warning! The computer you are running uses a CPU (Computer Processing Unit)")
    print("that has an archieture of 32-bits. The python modules (specifcally 'wget') work best on 64-bit machines, ")
    print("or alternatively, arm64 processors. Either way, it is not recommended to continue.")
    print("You can bypass this. Press Enter to continue with the program and enter 'no' if you wish")
    print("to exit.")
    print("=========================================================================================================")
    archerror = input()
    if archerror == "no" or archerror == "No":
        exit()
    else:
        print("That's okay. You may experience errors later on.")
else:
    print("Passed architecture tests. You are NOT running a i386 / 32-bit based machine.")
current_time = datetime.datetime.now()
print("===============================================================================")
if(os.name == 'posix'):
    osname = "Linux or MacOS."
else:
    osname = "Windows."
print("You are using," ,osname)
print("===============================================================================")

print("===============================================================================")
print("""
                             888                                888        888        .d8888b. 
                             888                                888        888       d88P  Y88b
                             888                                888        888            .d88P
888  888  888  .d88b.  .d88b. 888888   88888b.d88b.  .d88b.  .d88888888  888888 .d88b.   .d88P" 
888  888  888 d88P"88bd8P  Y8b888      888 "888 "88bd88""88bd88" 888888  888888d8P  Y8b  888"   
888  888  888 888  88888888888888      888  888  888888  888888  888888  88888888888888  888    
Y88b 888 d88P Y88b 888Y8b.    Y88b.    888  888  888Y88..88PY88b 888Y88b 888888Y8b.             
 "Y8888888P"   "Y88888 "Y8888  "Y888   888  888  888 "Y88P"  "Y88888 "Y88888888 "Y8888   888    
                   888                                                                          
              Y8b d88P                                                                          
               "Y88P"                                         
""")
print("===============================================================================")
print("Before you proceed, have you got a module called wget installed?")
print("It's fine if you do not, but there is a feature later on requiring it.")
wgetcheck = input()
if wgetcheck == "yes" or wgetcheck == "Yes":
    print("===============================================================================")
    print("Attempting to import module...")
    time.sleep(1)
    import wget
    time.sleep(1)
    print("Successfully imported the 'wget' module.")
else:
    print("===============================================================================")
    print("Nah. No worries. It is only used once, and in an optional section.")
print("===============================================================================")
print("""
                               .d888        888           
                              d88P"         888           
                              888           888           
 .d88b.       .d8888b  8888b. 888888 .d88b. 888888888  888
d8P  Y8b      88K         "88b888   d8P  Y8b888   888  888
88888888888888"Y8888b..d888888888   88888888888   888  888
Y8b.               X88888  888888   Y8b.    Y88b. Y88b 888
 "Y8888        88888P'"Y888888888    "Y8888  "Y888 "Y88888
                                                       888
                                                  Y8b d88P
                                                   "Y88P" 
""")
print("""
                         d8b                888                      d8b        
                         Y8P                888                      Y8P        
                                            888                                 
88888b. 888d888 .d88b.  8888 .d88b.  .d8888b888888    .d88888888  88888888888888
888 "88b888P"  d88""88b "888d8P  Y8bd88P"   888      d88" 888888  888888   d88P 
888  888888    888  888  88888888888888     888      888  888888  888888  d88P  
888 d88P888    Y88..88P  888Y8b.    Y88b.   Y88b.    Y88b 888Y88b 888888 d88P   
88888P" 888     "Y88P"   888 "Y8888  "Y8888P "Y888    "Y88888 "Y8888888888888888
888                      888                              888                   
888                     d88P                              888                   
888                   888P"                               888                   
""")
print("===============================================================================")
print("""
                            _________
                           /         /.
    .-------------.       /_________/ |
   /             / |      |         | |
  /+============+\ |      | |====|  | |
  ||C:\>        || |      |         | |
  ||            || |      | |====|  | |
  ||            || |      |   ___   | |
  ||            || |      |  |166|  | |
  ||            ||/@@@    |   ---   | |
  \+============+/    @   |_________|./.
                     @          ..  ....'
  ..................@     __.'.'  ''
 /oooooooooooooooo//     ///
/................//     /_/
------------------
""")

print("===============================================================================")
# Functions and Define
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("The time it took you to answer was: {0}:{1}:{2}".format(int(hours),int(mins),sec))
# Function: Lives Check
h = 0
h = int(h)

print("You have the option of HARD mode or NORMAL. Hard = 3 lives")
print("NORMAL = 9 lives.")
print("a) Hard")
print("b) Normal")
livesoption = input()
if livesoption == "a" or livesoption == "A":
    h = 3
    h = int(h)
    print("Okay! ¡Caliente, mi amigo!")
elif livesoption == "B" or livesoption == "b":
    h = 9
    h = int(h)
    print("Mild, but okay.")
print("==========================================================")
def hcheck():
    print("Commencing checking of health.")
    time.sleep(1)
    if h == 0:
        print("Nope. That's the end for you. You lost all nine/three lives")
        exit()
    else:
        print(f"You are on {h} lives. Don't lose any!")
# Name Request
print("Welcome! May I please know your name?")
nameinput = input()
print("Good day," ,nameinput)
print("The time now is," ,current_time)
print(h)
#TESTING AREA - START!
#=====================

#q1s1 = input()
#if q1s1 == "a" or q1s1 == "A":
    #print("Correct")
#else:
   #print("Nope.")

#NOTE TO SELF:
#NEED TO PUT "q1s1 ==" when doing or.

#TESTING AREA - END!
#===================

# Explain Project
print("================================================================================")
print(" ______ __  __  ______ __  __  ______  __   __     ______   ______  ______  ______ ______ ______ __  __ ")
print("/\  == /\ \_\ \/\__  _/\ \_\ \/\  __ \/\ \-.\ \   /\  ___\ /\  ___\/\  __ \/\  ___/\  ___/\__  _/\ \_\ \ ")
print("\ \  _-\ \____ \/_/\ \\ \  __ \ \ \/\ \ \ \-.  \  \ \  __\ \ \___  \ \  __ \ \  __\ \  __\/_/\ \\ \____ \ ")
print(" \ \_\  \/\_____\ \ \_\\ \_\ \_\ \_____\ \_\\-\_\  \ \_____\\/\_____\ \_\ \_\ \_\  \ \_____\\ \_\\/\_____\ ")
print("  \/_/   \/_____/  \/_/ \/_/\/_/\/_____/\/_/ \/_/   \/_____/ \/_____/\/_/\/_/\/_/   \/_____/ \/_/ \/_____/")
print("                                                                                                           ")
print("================================================================================")
print("Alright, greetings out of the way, let's explain the game and its objective.")
print("The aim of the project is to educate young people in how to act in different situations of the internet and the dangers of it.")
print("It is crucial for these demographics to know about this situations and how to act correctly and appropriately.")
print("These scenarios are fictional and are only educational. The way the game works is you are presented with a scenario.")
print("You are given anywhere from five to eight questions. These questions are key to act well in the scenario.")
print("There are EIGHT scenarios present in the E-SAFETY PROJECT BY MARCEL CISZEWSKI.")
print("If you are wrong, you will lose a life, and you will not be able to answer again!")
print("Each answer to a question will have a reasoning behind it!")
print("It’s good to read the reasoning if you are interested in knowing why that was the correct choice.")
print("Sometimes, questions may have more than one correct answer however pick the one that is the best one.")
print("Even if you disagree with it and you would have of gone a different route,")
print("please understand that this game is to educate about the correct solutions on E-Safety.")
print("You have 9 or 3 lives to do this game/project; lose everything: you will have to restart the game.")
print("ACHTUNG! Sometimes there are more than two answer. ALWAYS select the BEST option.")
print("=================================================================================")
# Prompt
print("Ready to continue?")
continue1 = input()
if continue1 == "no" or continue1 == "No":
    print("Alright. Come back when you are ready!")
    print("Thank you.")
    exit()
else:
    print("Good, let's carry on.")
# Scenario 1
print("=================================================================================")
print(".d88888b                                               oo             d88 ")
print("88.    8'                                                              88 ")
print("`Y88888b. .d8888b. .d8888b. 88d888b. .d8888b. 88d888b. dP .d8888b.     88 ")
print("      `8b 88'  `"" 88ooood8 88'  `88 88'  `88 88'  `88 88 88'  `88     88 ")
print("d8'   .8P 88.  ... 88.  ... 88    88 88.  .88 88       88 88.  .88     88 ")
print(" Y88888P  `88888P' `88888P' dP    dP `88888P8 dP       dP `88888P'    d88P")
print("                                                                          ")
print("=================================================================================")
print("This scenario is all about online grooming. You may wish to know more about this.")
print("Would you like to know more about online grooming?")
continue2 = input()
# \/\/\/\/\/\/\/\/
# 
if continue2 == "yes" or continue2 == "Yes":
    print("Alright.")
    print("Let's answer the question: what actually is Online Grooming?")
    print("=================================================================================")
    print("Online grooming is when someone builds a relationship with a young person online")
    print("because they want to trick or pressure them into doing something that may hurt or harm them.")
    print("Sadly, there are over 4300 cases of online grooming every year.")
    print("Whilst that number may sound small, first of, this is all recorded cases just in the UK. Secondly, this number is the recorded amount.")
    print("People estimate that over 10,560 cases happen in the UK, every MONTH.")
    print("This is more than double, approaching triple, the amount of cases reported by all the counties respective police group (Metropolitan Police, Norfolk Police and etc).")
    print("Online grooming, unfortunately, if successful, could let you with a risk of life.")
    print("Some cases reported have had adolescents sexually abused, or potentially murdered.")
    print("=================================================================================")
    print("There is a website explaining this better than I am. Would you like to visit it?")
    continue3 = input()
    if continue3 == "yes" or continue3 == "Yes":
        print("Alright. Taking you there!")
        time.sleep(1)
        print("Off you go!")
        webbrowser.open("https://www.childnet.com/help-and-advice/grooming-11-18-year-olds")
    else:
        print("Good, let's carry on.")
    
else:
    print("Good, let's carry on.")
print("===========================================================================================================")
print("8:34pm - You’re sitting down, looking at Instagram, possibly at cute pets or just some plain old funny memes.")
print("Either way, a short while after, you receive a message. The person only recently followed you,")
print("and they are already striking up a conversation. They greet you formally, and you reply back,")
print("asking for the purpose of messaging you. You get no reply. You ignore them and put down your phone.")
print("                                                                                                   ")
print("8:45pm - Your phone gets pinged; a lot. It’s that person again. He ignores your last message and")
print("starts complimenting you about how nice you look, how cute your dog you posted a couple days back is, and")
print("generally tries to get you to befriend him/her. He also sounds extremely impatient in his messages. You politely thank him,")
print("and decline his request to befriend them. The person now takes on a different persona and approach. He sounds more calmer, and")
print("seems to have a bit more respect for you. He also starts talking about your hobbies and how he has a top notch job, potentially your dream job. ")
print("===========================================================================================================")  
print("""
                                      dP   oo                      d88 
                                      88                            88 
.d8888b. dP    dP .d8888b. .d8888b. d8888P dP .d8888b. 88d888b.     88 
88'  `88 88    88 88ooood8 Y8ooooo.   88   88 88'  `88 88'  `88     88 
88.  .88 88.  .88 88.  ...       88   88   88 88.  .88 88    88     88 
`8888P88 `88888P' `88888P' `88888P'   dP   dP `88888P' dP    dP    d88P
      88                                                               
      dP                                                               
                                                                                                                                                    
""")
print("===========================================================================================================")
print("You seem awfully suspicious about the change in persona. You do not know what to do. Do you:")
print("a) - Question them, and see what they have to say.")
print("b) - Ignore them, and go about your day.")
print("c) - Block them, and remove them from your follower list.")
print("Answer with a, b or c.")
start_time = time.time()
q1s1 = input()
end_time = time.time()
if q1s1 == "c" or q1s1 == "C":
    print("Yes, that is right. Congrats. That WOULD HAVE of been the right thing to do.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: C ")
    print("Would you like to see an explanation as to why 'C' is the correct answer?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("The correct answer was…technically all of them. All of them showed a sense of")
        print("suspicion in the person, however, c) was the best answer. This stops them")
        print("from contacting you from the account they are using.")
        print(" ")
        print("b) could work, but over time, could become quite annoying.")
        print(" ")
        print("a) is the worst one, however studies suggest that befriending friendly,")
        print("and harmless people on the Internet is actually extremely good for your mental and social esteem.")         
    else:
        print("Alright.")
    h = h - 1
    hcheck()
######print("Ready to continue?")
######continue1 = input()
#time.sleep(2)
#####if(os.name == 'posix'):
    ###os.system('clear')
####else:
    ##os.system('cls')
#time.sleep(0.1)  
print("===========================================================================================================")
print("You think you’ll hear no more of them. But yet, they do.")
print("However this time, they use a different account, and it looks to be with a lot of followers.")
print("You definitely know it’s them as you recognise that same arrogance in the first complements.")
print("Let’s just say that you are extremely interested in becoming a NASA engineer.")
print("He says that he noticed your passion for spacecraft engineering. You are immediately interested in")
print("it and time flies as you both are talking about each other’s knowledge and dreams.")
print("You then move from chat to voice. However, your parents are skeptical about who you are talking to.")
print("===========================================================================================================")
print("""

                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                                888
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.         .d88P
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b    .od888P" 
888  888888  88888888888"Y8888b.888   888888  888888  888   d88P"     
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   888"      
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888   888888888 
     888                                                              
     888                                                              
     888           
""")
print("===========================================================================================================")
print("Your parents are requesting who you are talking to. Do you:")
print("a) Lie and tell them something else.")
print("b) Tell them and potentially see their response.")
print("c) Tell them, but you assure them that you know the person.")
start_time = time.time()
q2s1 = input()
end_time = time.time()
if q2s1 == "b" or q2s1 == "B":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: B ")
    print("Would you like to see an explanation as to why 'B' is the correct answer?")
    moreinfo_option2 = input()
    if moreinfo_option2 == "yes" or moreinfo_option2 == "Yes":
        print("The correct answer was in fact b). This is something not many kids do but is crucial.")
        print("a) and c) could potentially be dangerous, as it is almost")
        print("always better to hear an older person’s opinion.")
        print("Remember, they gone through more and therefore have more experience in overall life.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("Your parents do not think it is as suspicious, as they believe")
print("you have a right mindset to notice such dangerous things. You keep talking and finally,")
print("that dreadful question; Where do you live? A couple minutes later, he follows up,")
print("making some sort of excuse for the question")
print("(e.g he wants to buy computer parts for you, and etc.).")
print("===========================================================================================================")
print("""
                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                              .d88P
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.        8888" 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y8b.
888  888888  88888888888"Y8888b.888   888888  888888  888   888    888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P" 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("Simple. Do you do it or not? Do you trust the person with your soul that he will not use it against you?")
print("a) Do not agree, and refuse to give the address.")
print("b) Give it but be extremely cunning and give a fake address, leading to nowhere.")
print("c) Do not agree, and block him.")
print("d) Give your real address.")
start_time = time.time()
q3s1 = input()
end_time = time.time()
if q3s1 == "b" or q3s1 == "B" or q3s1 == "C" or q3s1 == "c" or q3s1 == "A" or q3s1 == "a":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: B, C or A")
    print("Would you like to see an explanation as to why 'B' or 'C' or 'A' are the correct answers?")
    moreinfo_option3 = input()
    if moreinfo_option3 == "yes" or moreinfo_option3 == "Yes":
        print("The correct answers were a), b) and c). Just don’t give it, simple. b) is interesting,")
        print("it depends: you mightjust waste his time instead of them having a new victim.")
        print("a) coule lead into the person pressuring you to give them the address. ")
        print("d) is not the right choice. That could jeopardise you and your family’s safety and health.In addition,")
        print("later on, the person might want a ransom in exchange for not putting your address publicly on the Internet.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("You decide not to send him your address and you block him.")
print("You think you have heard the last of him. Think again.")
print("Unfortunately, you remembered that you accidently revealed a couple private")
print("questions to him during your voice call.")
print("You don’t even remember it…")
print("He is now threatening you with “leaking” your full name, your birthplace and much more.")
print("Your jaw drops as you read through the message with the demands.")
print("===========================================================================================================")
print("""
                                888   d8b                       d8888 
                                888   Y8P                      d8P888 
                                888                           d8P 888 
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.     d8P  888 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b   d88   888 
888  888888  88888888888"Y8888b.888   888888  888888  888   8888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888         888 
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888         888 
     888                                                              
     888                                                              
     888                                                              
""")
print("===========================================================================================================")
print("You are terrified as the information keeps growing.")
print("You need to do something. What do you do?")
print("a) Ignore it and never see it again.")
print("b) Report it to the police, other respective agencies, and consult your parents on the matter.")
print("c) Report it to the police, and other respective agencies,")
print("   BUT you do not wish to tell your parents.")
start_time = time.time()
q4s1 = input()
end_time = time.time()
if q4s1 == "b" or q4s1 == "B":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: B")
    print("Would you like to see an explanation as to why 'B' is the correct answer?")
    moreinfo_option4 = input()
    if moreinfo_option4 == "yes" or moreinfo_option4 == "Yes":
        print("The obvious answer and the best one was in fact b).")
        print("You must consult the police and agencies such as NSPCC and etc.")
        print("c) does have right in it, but telling your parents is the best option.")
        print("I understand why many might not tell their parents, in risk of arguments.")
        print(" ")
        print("a) is honestly the worst one. You are potentially again, risking your entire personal information.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("You do the honourable thing and contact the police and your parents.")
print("The police have said that they will do everything in their power to stop the “leak” of your personal information.")
print("The person starts to notice something is horribly wrong...")
print("and starts deleting their messages, potentially deleting the evidence forever.")
print("===========================================================================================================")  
print("""
                                888   d8b                   888888888              .d888d8b                888        
                                888   Y8P                   888                   d88P" Y8P                888        
                                888                         888                   888                      888        
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.    8888888b.             88888888888888b.  8888b. 888 .d88b. 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y88b            888   888888 "88b    "88b888d8P  Y8b
888  888888  88888888888"Y8888b.888   888888  888888  888          888   888888   888   888888  888.d88888888888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P            888   888888  888888  888888Y8b.    
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P"             888   888888  888"Y888888888 "Y8888 
     888                                                                                                              
     888                                                                                                              
     888                                                                                                              
""")
print("===========================================================================================================")
print("The information is deleted fast. You need to do something. Do you:")
print("a) Ignore and block them, and wait for the police to take action.")
print("b) Screenshot the messages and evidence, and ask the company for the history of your messages")
print(" (Some companies actually can recover deleted messages, normally in criminal cases.)")
print("c) Taunt the groomer and annoy them.")
start_time = time.time()
q5s1 = input()
end_time = time.time()
if q5s1 == "b" or q5s1 == "B":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still answered it wrong. :(")
    print("The correct answer was: B")
    print("Would you like to see an explanation as to why 'B' is the correct answer?")
    moreinfo_option5 = input()
    if moreinfo_option5 == "yes" or moreinfo_option5 == "Yes":
        print("If you are logically thinking about the situation, you are obviously going to go with b).")
        print("You need evidence in order to arrest the groomer. Without it, you could be held liable. ")
        print("a) is simply waiting for the evidence to be destroyed.")
        print("c) is honestly, the worst thing you can do.")
        print("This is a similar scenario to taunting a grown alligator. Just don’t.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                                               d8b            .d8888b. 
                                               Y8P           d88P  Y88b
                                                                    888
.d8888b  .d8888b .d88b. 88888b.  8888b. 888d888888 .d88b.         .d88P
88K     d88P"   d8P  Y8b888 "88b    "88b888P"  888d88""88b    .od888P" 
"Y8888b.888     88888888888  888.d888888888    888888  888   d88P"     
     X88Y88b.   Y8b.    888  888888  888888    888Y88..88P   888"      
 88888P' "Y8888P "Y8888 888  888"Y888888888    888 "Y88P"    888888888
""")
print("===========================================================================================================")
print("Firstly, you need to know what phishing and scamming is for the next part.")
print("This section is optional.")
print("Enter 'yes' in order to see more infomation about the above topic,")
print("or enter 'no' in order to proceed without viewing.")
infoinput = input()
if infoinput == "yes" or infoinput == "Yes":
    print("Alright.")
    print("Phishing is when someone tries to get your personal information or log in details by pretending")
    print("to be a trustworthy company or organisation. A bit like fishing, they are trying to hook you in and get you")
    print("to type in this information. Phishing may come as an email or direct message and will be designed to look like an organisation")
    print("or company that you know and trust. Online scams are any scheme or method used to trick and deceive others into")
    print("giving up their personal information, account logins, money or virtual video game items on the internet.")
    print("Phishing is one form of internet scam but not the only one. Others can include messages that encourage you")
    print("to enter prize draws, complete surveys or click on unfamiliar links, all aiming to get you to share your details.")
else:
    print("That's fine.")
print("===========================================================================================================")
print("Billy, your typical 9 year old, was just playing his regular game of Fortnite, screaming some not very")
print("catholic things at his friends and throwing his keyboard (which is missing four keys) and")
print("nine year old monitor around, when he gets a message from an unknown account. He starts a conversation normally")
print("and then the account wants to give up their exclusive and rare items in exchange for…nothing.")
print(" ")
print("No money or anything. He makes a random excuse, e.g “leaving the game and want to give you all my items.”")
print("To us, that is a simple sign of scamming and something that has “some strings attached”. To Billy, this")
print("is a dream come true, all his favourite skins, gifted to him for absolutely no reason and completely free.")
print("He immediately replies back, later on pleading for it. The scammer definitely know they’ve got Billy on the hook.")
print("===========================================================================================================")
print("""

                                888   d8b                    d888  
                                888   Y8P                   d8888  
                                888                           888  
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.      888  
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b     888  
888  888888  88888888888"Y8888b.888   888888  888888  888     888  
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888     888  
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888   8888888
     888                                                           
     888                                                           
     888
""")
print("===========================================================================================================")
print("Let’s rewind, Billy gets the message. Confused and not knowing who it’s from, he questions himself.")
print("Does Billy open the message?")
print(" ")
print("a) Ah, of course, it’s a time for an adventure, wahoo!")
print("b) Yes, but approach with caution.")
print("c) No, block immediately and report the person.")
start_time = time.time()
q1s2 = input()
end_time = time.time()
if q1s2 == "b" or q1s2 == "B" or q1s2 == "C" or q1s2 == "c":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: B or C")
    print("Would you like to see an explanation as to why 'B' or 'C' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("The correct answers were b) and c). Of course c) is the best option.")
        print("but literally no one is going to immediately block a person for no reason.")
        print("(This is based of the fact that Billy does not know what the message contains)")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""

                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                                888
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.         .d88P
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b    .od888P" 
888  888888  88888888888"Y8888b.888   888888  888888  888   d88P"     
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   888"      
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888   888888888 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("Let’s imagine Billy checks the message. He is greeted with a friendly response, acting with culture and manners.")
print("The person also asking to “friend” you. ")
print("What should Billy do?")
print(" ")
print("a) Reply positively, but clearly indicate skepticism, and refuse to “friend” him.")
print("b) Reply positively, and thank them, returning the warm gesture, and friend them.")
print("c) Deny, and block him, with no warning.")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "A" or q2s2 == "a" or q2s2 == "C" or q2s2 == "c":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: A or C")
    print("Would you like to see an explanation as to why 'A' or 'C' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("The correct answers were a) and c), however c) is the best one. A person acting nicely,")
        print("is ALMOST ALWAYS a bad omen,")
        print("and normally with zero good intentions.")
        print("a) is alright, and is probably what most people would do. ")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                              .d88P
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.        8888" 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y8b.
888  888888  88888888888"Y8888b.888   888888  888888  888   888    888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P" 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("Billy goes ahead and replying but since he remembers some stuff from his e-safety lesson,")
print("he refuses to friend him. The person is visibly annoyed, but proceeds, complimenting him")
print("on his wonderful gameplay and “ses manières” on voice chat. Billy is charmed and delighted to hear this.")
print("No one else has ever said anything about him.")
print("How will Billy respond to this situation?")
print(" ")
print("a) Deny, and block him. Additionally, report.")
print("b) Thank them, but keep your guard up, and keep refusing to friend him. ")
print("c) Thank for the compliments and friend them.")
start_time = time.time()
q3s2 = input()
end_time = time.time()
if q3s2 == "A" or q3s2 == "a" or q3s2 == "b" or q3s2 == "B":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: A or B")
    print("Would you like to see an explanation as to why 'A' or 'B' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("The correct answers are a) and b). There is some debate about this.")
        print("a) could be good, but reporting the person will do nothing.")
        print("You do not have solid evidence to report him on the grounds of scamming and phishing.")
        print("b) COULD lead you to your demise. c) is just plain stupid,")
        print("because you are trusting the stranger as a friend/family member. ")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                                888   d8b                       d8888 
                                888   Y8P                      d8P888 
                                888                           d8P 888 
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.     d8P  888 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b   d88   888 
888  888888  88888888888"Y8888b.888   888888  888888  888   8888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888         888 
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888         888 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("Billy, unfortunately, is too flattered with the compliments and")
print("falls for the trap and friends him. Over the next couple of days,")
print("the person and Billy are in close contact and regularly play. However,")
print("two weeks later, a bombshell drops. The person announces that they are")
print("quitting the game and")
print("they want to give Billy their exclusive items.")
print("===========================================================================================================")
print("How will Billy respond to this situation?")
print(" ")
print("a) Accept with gratitude, and agree to further conditions.")
print("b) Accept, but continue to be skeptical, and ask for any strings attached. ")
print("c) Deny, and block. Additionally, report.")
start_time = time.time()
q4s2 = input()
end_time = time.time()
if q4s2 == "C" or q4s2 == "c" or q4s2 == "b" or q4s2 == "B":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: C or B")
    print("Would you like to see an explanation as to why 'B' or 'C' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("The answers are b) and c). b) is good, and c) is the best option as well,")
        print("as you now have evidence on the suspicion of scamming and phishing.")
        print("a) is, again bad. As the Germans would say, “du gräbst dein eigenes grab!”")
        print("or in English,")
        print("“You are digging your own grave.”")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                                888   d8b                   888888888              .d888d8b                888        
                                888   Y8P                   888                   d88P" Y8P                888        
                                888                         888                   888                      888        
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.    8888888b.             88888888888888b.  8888b. 888 .d88b. 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y88b            888   888888 "88b    "88b888d8P  Y8b
888  888888  88888888888"Y8888b.888   888888  888888  888          888   888888   888   888888  888.d88888888888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P            888   888888  888888  888888Y8b.    
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P"             888   888888  888"Y888888888 "Y8888 
     888                                                                                                              
     888                                                                                                              
     888                                                                                                              
""")
print("===========================================================================================================")
print("Billy does fall for it :(. The person asks for his password, and Billy")
print("sends him a piece of paper with his password (Password: billyfortniterock124).")
print("The person blocks Billy and Billy has less than 10 seconds to react or")
print("he can kiss his hard-earned items goodbye.")
print("Quick, you have 5 seconds left, to answer one questions.")
print("- Decide what you need to do. What should Billy do?")
print(" ")
print("a) Change his password.")
print("b) Change his password, quickly enable two-step verification.")
print("c) All the above, block the person and additionally, create a report")
print("   to prepare support for a breach into your account.")
start_time = time.time()
q5s2 = input()
end_time = time.time()
if q5s2 == "C" or q5s2 == "c" :
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    if time_lapsed <= 5:
        finalresult = 1
    else:
        finalresult = 2
    print("Let's see if you answered within 5 seconds.")
    if finalresult == 1:
        print("You're safe. You answered within 5 seconds.")
    else:
        print("Nope. You're too late. Oof. Your items got stolen.")
        h = h - 1
        hcheck()
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: C")
    print("Would you like to see an explanation as to why 'C' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("Congrats. c) is the choice. b) is also good. a) is the worst…")
        print("Billy thinks wisely and the small amount of brain cells he has, have decided to complete step c). ")
        print("It works, well partially…")
        print("The person/scammer, has taken about one third of the total items. The person cannot access the account no longer. ")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("Billy is furious and starts screaming not very catholic things. So much so,")
print("that his older brother are questioning him.")
print("Billy tells them about his situation, and tells them that he has been scammed")
print("and phished. His brother decides to help.")
print("—> You now switch to the brother.")
print(" ")
print("The brother needs to do something. What in particular?")
print("a) Contact support and await their response.")
print("b) Do nothing.")
start_time = time.time()
q5bs2 = input()
end_time = time.time()
if q5bs2 == "A" or q5bs2 == "a":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: C or B")
    print("Would you like to see an explanation as to why 'A' is the correct answer?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("Both are technically right, but if you wish to get your “items back”, a) is the best. b) is good if you")
        print("wish not to communicate anymore with the situation with the person/scammer.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                                               d8b            .d8888b. 
                                               Y8P           d88P  Y88b
                                                                  .d88P
.d8888b  .d8888b .d88b. 88888b.  8888b. 888d888888 .d88b.        8888" 
88K     d88P"   d8P  Y8b888 "88b    "88b888P"  888d88""88b        "Y8b.
"Y8888b.888     88888888888  888.d888888888    888888  888   888    888
     X88Y88b.   Y8b.    888  888888  888888    888Y88..88P   Y88b  d88P
 88888P' "Y8888P "Y8888 888  888"Y888888888    888 "Y88P"     "Y8888P" 
""")
print("===========================================================================================================")
print("The part will not be based on a story and instead, skip straight to the questions.")
print("This next part will contain 6 questions to test your knowledge on screen time.")
print("If you wish to find an example of screen time scenarios, you find such on the Internet. ")
print("What is Screen Time? Screen time is the amount of time we spend using devices and technology.")
print("There are some concerns that we are spending too long looking at screens and many devices")
print("now provide tools to track our screen time. Spending too much time on devices is now linked")
print("quite closely to low-risk and brief irritation. Children aged between 2-5, screen time should")
print("be one hour at the max. For older children (normally 12+), two to three hours should be the normal")
print("per day. As of writing this PowerPoint, my average screen time, is normal and something slightly over (25 minutes over).")
print("===========================================================================================================")
print("For this next part, you need to read an article to answer the following questions.")
print("You have a couple options to read this:")
print(" 1) This website is stored in HTML in the folder this .py file is in. (offline)")
print(" ")
print(" 2) Alternatively, you may iew an up-to-date version of the website.")
print(" This does requires a good internet connection and a web browser.")
print(" 3) Like said earlier, you may download an HTML file (the website) and an educational video")
print(" >>> (requires the wget modules to be installed)")
print("===========================================================================================================")
print("Select your option:")
optionmodule = input()
if optionmodule == "1":
    print("Alright. Please go to the folder and read the website.")
    print("Come back when you are ready.")
if optionmodule == "2":
    print("Alright. This will open up a web browser with the link.")
    print("Off you go.")
    webbrowser.open("https://ezyschooling.com/parenting/expert/good-screen-time-vs-bad-screen-time")
if optionmodule == "3":
    print("If you DO NOT have wget installed, python will refuse to run this.")
    print("It is more than likely that you will get an error if that is the case.")
    print("......................................................................")
    print("Connecting to GitHub and downloading the files.")
    print("Depending on the internet connection you have, this may take a while.")
    URL = "https://github.com/realinteldiscord2004/python_project_safety/raw/main/websites/scenario3.txt"
    response = wget.download(URL, "scenario3.txt")
    URL = "https://github.com/realinteldiscord2004/python_project_safety/raw/main/videos/scenario3.mp4"
    response = wget.download(URL, "scenario3.mp4")
    print(" ")
    print("Done! Check your folder for the .txt and the .mp4 (you need to extract it first from the zip file.)")
print("===========================================================================================================")
print("Simply read or/and watch the provided files, and then press enter when you are ready.")
print("Waiting for response...")
checkchallenge = input()
print("Alright. Let's continue (on the assumption that you finished reading.)")
print("===========================================================================================================")
print("""
                       888       d888              .d888       d8888 
                       888      d8888             d88P"       d8P888 
                       888        888             888        d8P 888 
88888b.  8888b. 888d888888888     888      .d88b. 888888    d8P  888 
888 "88b    "88b888P"  888        888     d88""88b888      d88   888 
888  888.d888888888    888        888     888  888888      8888888888
888 d88P888  888888    Y88b.      888     Y88..88P888            888 
88888P" "Y888888888     "Y888   8888888    "Y88P" 888            888 
888                                                                  
888                                                                  
888  
""")
print("===========================================================================================================")
print("Question 1: What is the normal screen time for smaller and younger children?")
print("a) Under 1 hour.")
print("b) 2-3 hours.")
print("c) 5+ hours.")
q1s4 = input()
if q1s4 == "a" or q1s4 == "A":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 2: Can screen time, and specifically too much of it, damage your eyes?")
print("a) Potentially.")
print("b) That's a lie.")
print("c) Of course, it degrades your eyes over time.")
q2s4 = input()
if q2s4 == "a" or q2s4 == "A":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                       888       .d8888b.             .d888       d8888 
                       888      d88P  Y88b           d88P"       d8P888 
                       888             888           888        d8P 888 
88888b.  8888b. 888d888888888        .d88P    .d88b. 888888    d8P  888 
888 "88b    "88b888P"  888       .od888P"    d88""88b888      d88   888 
888  888.d888888888    888      d88P"        888  888888      8888888888
888 d88P888  888888    Y88b.    888"         Y88..88P888            888 
88888P" "Y888888888     "Y888   888888888     "Y88P" 888            888 
888                                                                     
888                                                                     
888
""")
print("===========================================================================================================")
print("Question 3: Can screen time be educational and informative?")
print("a) Yes, always.")
print("b) Yes, not always.")
print("c) No, never.")
q3s4 = input()
if q3s4 == "b" or q3s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 4: Is too much screen time linked to insomnia? ")
print("a) Potentially.")
print("b) That’s a lie.")
print("c) Always happens.")
q4s4 = input()
if q4s4 == "b" or q4s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("""
c
""")
print("===========================================================================================================")
print("Question 5: A mother on Facebook posted: “Electronic gadgets will not help my")
print("child to create a hobby of any sorts.” Do you agree with the statement?")
print("a) Yes.") 
print("b) No.")
print("c) Depends on the content.")
q5s4 = input()
if q5s4 == "c" or q5s4 == "C":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 6: Installing a screen-guard for your monitor is useless. True or False?")
print("a) Quality matters.")
print("b) True.")
print("c) False.")
q6s4 = input()
if q6s4 == "a" or q6s4 == "A":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("""
                       888          d8888             .d888       d8888              .d888d8b                888        
                       888         d8P888            d88P"       d8P888             d88P" Y8P                888        
                       888        d8P 888            888        d8P 888             888                      888        
88888b.  8888b. 888d888888888    d8P  888     .d88b. 888888    d8P  888             88888888888888b.  8888b. 888 .d88b. 
888 "88b    "88b888P"  888      d88   888    d88""88b888      d88   888             888   888888 "88b    "88b888d8P  Y8b
888  888.d888888888    888      8888888888   888  888888      8888888888   888888   888   888888  888.d88888888888888888
888 d88P888  888888    Y88b.          888    Y88..88P888            888             888   888888  888888  888888Y8b.    
88888P" "Y888888888     "Y888         888     "Y88P" 888            888             888   888888  888"Y888888888 "Y8888 
888                                                                                                                     
888                                                                                                                     
888                                             
""")
print("===========================================================================================================")
print("Question 7: Should be aware of what you are viewing/watching?")
print("a) Yes, of course. I am Catholic.")
print("b) No. I DON’T particularly pay attention")
print("c) Yes, and if I see anything, I tell my parents. ")
q6s4 = input()
if q6s4 == "c" or q6s4 == "C":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 8: Can too much screen time cause fatigue, both physically and mentally? ")
print("a) True")
print("b) False")
q7s4 = input()
if q7s4 == "A" or q7s4 == "a":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("""
                                               d8b               d8888 
                                               Y8P              d8P888 
                                                               d8P 888 
.d8888b  .d8888b .d88b. 88888b.  8888b. 888d888888 .d88b.     d8P  888 
88K     d88P"   d8P  Y8b888 "88b    "88b888P"  888d88""88b   d88   888 
"Y8888b.888     88888888888  888.d888888888    888888  888   8888888888
     X88Y88b.   Y8b.    888  888888  888888    888Y88..88P         888 
 88888P' "Y8888P "Y8888 888  888"Y888888888    888 "Y88P"          888
 """)
print("===========================================================================================================")
print("This section is about Medical Misinfomation.")
print("Would you like to see what this is about?")
contiune1 = input()
if contiune1 == "yes" or continue1 == "Yes":
    print("It can sometimes confuse, mislead, or influence people. COVID-19 is a new")
    print("virus, which means it is sometimes easy for people to misunderstand")
    print("information, interpret it incorrectly,")
    print("or come to their own inaccurate conclusions.")
    print("Most people don’t share this type of information knowingly.")
    print("They may have genuinely believed something they read from an unofficial news")
    print("source. They may also not have enough previous knowledge to accurately distinguish between")
    print("information sources that are genuine, and those that are not.")
    print("There is a website explaining it better than I am. Would you like to visit it?")
    continueprompt = input()
    if continueprompt == "yes" or continueprompt == "Yes":
        print("Alright, taking you there.")
        time.sleep(1)
        print("Off you go.")
        webbrowser.open("https://www.childnet.com/help-and-advice/medical-misinformation/")
    else:
        print("That's fine.")
else:
    print("Alright.")
print("===========================================================================================================")
print("""

                                888   d8b                    d888  
                                888   Y8P                   d8888  
                                888                           888  
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.      888  
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b     888  
888  888888  88888888888"Y8888b.888   888888  888888  888     888  
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888     888  
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888   8888888
     888                                                           
     888                                                           
     888
""")
print("===========================================================================================================")
print("You see an advertisement for finger enlargement pills. The advertisement")
print("looks poorly made, and the price seems a  b i t  too sketchy.")
print("What should you do?")
print(" a) Hell yeah, got to have a finger enlargement pill. No questions asked.")
print(" b) Check the website for details, and shipment origin.")
print(" c) Do not go on the website.")
q6s4 = input()
if q6s4 == "c" or q6s4 == "C":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("""
                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                                888
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.         .d88P
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b    .od888P" 
888  888888  88888888888"Y8888b.888   888888  888888  888   d88P"     
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   888"      
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888   888888888 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("Your friend Billo, looked up pain relief for his head.")
print("You finds out that you should rub Sulfuric Acid on your head.")
print("However, with the small amounts of brain cells he has, he has")
print("asked you to confirm it.")
print("Considering if you did not know what Sulfuric Acid is, what should you do?")
print("a) Check careful what the chemical is normally used for.")
print("b) Assure your friend that it is completely fine.")
print("c) Test it out yourself, and give him the results.")
q6s4 = input()
if q6s4 == "a" or q6s4 == "A":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("""
                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                              .d88P
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.        8888" 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y8b.
888  888888  88888888888"Y8888b.888   888888  888888  888   888    888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P" 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("You find out that COVID-19 is cured by drinking Dettol disinfectant")
print("that kills 99.9 percent of pathogens including COVID-19.")
print("This was said by USA president, Donald Trump.")
print("I know, it seems like common sense, but believe, some people still")
print("believe in such absolute, stupid, lies. Would you follow this advice?")
print("a) Yes, of course, the USA president never lies.")
print("b) No, never, I have common sense.")
q6s4 = input()
if q6s4 == "b" or q6s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("""
                                888   d8b                       d8888 
                                888   Y8P                      d8P888 
                                888                           d8P 888 
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.     d8P  888 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b   d88   888 
888  888888  88888888888"Y8888b.888   888888  888888  888   8888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888         888 
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888         888 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("You are ill. You do not have time to go to the doctor. You decide to go")
print("to an online doctor. You see the price and...you stop. You don't know.")
print("What should you check carefullly?")
print("a) Check reviews of the doctor.")
print("b) Check price and authencity.")
print("c) All of the above.")
q6s4 = input()
if q6s4 == "c" or q6s4 == "C":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("""                              
                                888   d8b                   888888888              .d888d8b                888        
                                888   Y8P                   888                   d88P" Y8P                888        
                                888                         888                   888                      888        
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.    8888888b.             88888888888888b.  8888b. 888 .d88b. 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y88b            888   888888 "88b    "88b888d8P  Y8b
888  888888  88888888888"Y8888b.888   888888  888888  888          888   888888   888   888888  888.d88888888888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P            888   888888  888888  888888Y8b.    
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P"             888   888888  888"Y888888888 "Y8888 
     888                                                                                                              
     888                                                                                                              
     888  
""")
print("===========================================================================================================")
print("You go on Instagram, and you see a really, REALLY fit person")
print("literally on the brink of being underweight. They say that")
print("to get this fit, you just need to eat raw fish and baked beans...")
print("What should you do?")
print("a) No fact checking, quickly hop on me mum's car, off to")
print("   me local morrisons...")
print("b) Check whether this type of diet is appropriate, escpially at a")
print("   young age")
print("c) Have a simple and basic understanding in life morales.")
q6s4 = input()
if q6s4 == "b" or q6s4 == "b" or q6s4 == "c" or q6s4 == "C":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Well done, and good news. We've completely finished four sceanrios, and you've")
print("made it this far. This is halfway (Scenario 4 out of 8).")
print("As a gift, you may accept 2 extra lives. This is optional")
print("if you want to play with no extra help.")
print("Would you like to accept 2 additional lives?")
q6s4 = input()
if q6s4 == "Yes" or q6s4 == "yes":
    print("Good. Always nice to have a little help alone the way.")
    time.sleep(0.5)
    h = h + 2
    time.sleep(0.5)
    print("Done!")
else:
	if h == 9:
		print("Brave and great, but you've lost no lives. That's fine!")
	else:  
		print("Brave and bold coming from you. You've lost lives.")
		print("Are you completely sure that you don't need additional lives?")
		askoption = input()
		if askoption == "yes" or askoption == "Yes":
			print("That's fine. We'll see how you'll do...")
		else:
			print("That's what I thought. Let me add some lives.")
			time.sleep(0.5)
			h = h + 2
			time.sleep(0.5)
			print("Done!")
hcheck()
print("===========================================================================================================")
print("""

                                               d8b           888888888 
                                               Y8P           888       
                                                             888       
.d8888b  .d8888b .d88b. 88888b.  8888b. 888d888888 .d88b.    8888888b. 
88K     d88P"   d8P  Y8b888 "88b    "88b888P"  888d88""88b        "Y88b
"Y8888b.888     88888888888  888.d888888888    888888  888          888
     X88Y88b.   Y8b.    888  888888  888888    888Y88..88P   Y88b  d88P
 88888P' "Y8888P "Y8888 888  888"Y888888888    888 "Y88P"     "Y8888P" 

""")
print("===========================================================================================================")
print("This scenario is all about sexual harassment. Would you to see more infomation on this?")
q6s4 = input()
if q6s4 == "Yes" or q6s4 == "yes":
    print("Okay.")
    print("Online sexual harassment is any unwanted sexual behaviour that occurs online. It can ")
    print("happen on any online platform and could include content such as photos, videos, posts,")
    print("webpages, messages or fake profiles. Even if the harassment was intended as a joke, or ")
    print("was a misunderstanding, it is the experience of the victim that defines whether it is ")
    print("sexual harassment or not.")
    print("Online sexual harassment can take place anywhere! Online sexual harassment can take place anywhere ")
    print("online and on any device. You might see or experience it in a game chat or on social media for example.")
    print("The online sexual harassment could be shared publicly or privately.")
    print("It can mentally affect the person, causing into situations, that are just too sad to say.")
    print("There is a website explaining this much better than I am. Would you like to visit it?")
    checkchallenge = input()
    if checkchallenge == "yes" or checkchallenge == "Yes":
        print("That's good. Taking you there!")
        print("Woosh! Off you go!")
        time.sleep(1.2)
        webbrowser.open("https://www.childnet.com/help-and-advice/online-sexual-harassment-11-18-year-old/")
        time.sleep(1.2)
        print("There you go!")
    else:
        print("Okay, that's fine.")
print("===========================================================================================================")
print("You are doing your homework, listening to music without any interruptions, when you receive a message. ")
print("It's a long friend from your old school. Huh, you haven't seen them for five years. You're not even sure it's your friend.") 
print("Maybe it's someone else? It's not a particularly friend you're on good terms on. ")
print("You decide to play along and reply back to her, returning that same friendly message back of 'hello, how are you?'")
print("She starts playing like a well known friend, talking about her daily life.")
print("===========================================================================================================")
print("""
                                888   d8b                    d888  
                                888   Y8P                   d8888  
                                888                           888  
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.      888  
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b     888  
888  888888  88888888888"Y8888b.888   888888  888888  888     888  
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888     888  
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888   8888888
     888                                                           
     888                                                           
     888
""")
print("===========================================================================================================")
print("You're introduced to this person, with her immediately taking a stance on being friendly.")
print("With no more additional infomation, should you potentially talk to her/him?")
print("a) Yes, of course, there is nothing wrong.")
print("b) Keep talking, but be on high alert.")
print("c) Don't talk. Just block the person. You don't know what's happened.")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "b" or q2s2 == "B" or q2s2 == "C" or q2s2 == "c":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: B or C")
    print("Would you like to see an explanation as to why 'B' or 'C' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("You can continue talking to the person, but you must be on high alert.")
        print("You NEVER know what's going to happen.")
        print("Maybe blocking immediately is good, but also again, that person may have good")
        print("intentions. I would wait to just let it play it out.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("You, being the normal person you are, continue talking. You reply to everything with 'ok'.")
print("They continue talked and later start some...weird conversations. Some very non-christian.")
print("They talk like you've been together for years. You are obviously a bit confused.")
print("They start about your R-Rated body parts and how they'd like to see it.")
print("You feel grossed out, and you find the situation gross. ")
print("===========================================================================================================")
print("""
                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                                888
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.         .d88P
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b    .od888P" 
888  888888  88888888888"Y8888b.888   888888  888888  888   d88P"     
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   888"      
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888   888888888 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("You consider blocking the person. Should you:")
print("a) Do not talk to them, block them and report them on grounds of sexual harassment.")
print("b) Continue talking, there is nothing wrong.")
print("c) Block them, but report them on the grounds of suspected/attempted sexual harassment.")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "b" or q2s2 == "B" or q2s2 == "C" or q2s2 == "c":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: C")
    print("Would you like to see an explanation as to why 'C' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("C allows the user to get blocked and reported successfully. B will work partially,")
        print("but the Social Media company will see nothing wrong and will deny your request. ")
        print("A is definitely the worst, you could end up somewhere on dangerous ground.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("You do the honourable thing and block and report on ground of suspected sexual harassment.")
print("It works like a charm. Their account is blocked and three days later, is removed and deleted. You go back to ")
print("your everyday life. But similarly as in the previous scenarios, they come back with a brand new account.")
print("Again, they come back with this 'sexy talk' of you. You honestly think you can't escape them.")
print("They also start sending alleged photos of you and your...(yeah, no, I wouldn't mention this in school")
print("I'd get shipped off to Sheffield in a Tesco Express cart if I did ;0 ).")
print("And now, you finally decide, it's about time to do something once and for all.")
print("===========================================================================================================")
print("""
                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                              .d88P
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.        8888" 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y8b.
888  888888  88888888888"Y8888b.888   888888  888888  888   888    888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P" 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("Once again, YOU have enough of this play. You want to do the honourable. What should you do?")
print("a) Tell your parents, and see what they have to see to the situation.")
print("b) Tell your friend, and ask him/her on what to do.")
#print("c) (joke) Optionally, launch a ballastic missile into the person's house.")
print("c) Do nothing, and delete your account.")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "A" or q2s2 == "a":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: A")
    print("Would you like to see an explanation as to why 'A' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("A is correct, because, I swear I've said this a million times (but it's true) ")
        print("your parents know how to deal with it. Even if they are the least tech savy people on the planet.")
        print("They will apply knowledge of their social life to resolve your matter. Honestly.")
        print("B is not good, as your friends are the exact opposite of your parents. They DO NOT have")
        print("the good knowledge of their social life. They will do little to help in the situation.")
        print("(No offense to your friends though, they are probably better at other things.)")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("You do not tell your parents. You fear the consquences. Disappointing, but you will not overcome this fear.")
print("You also do not tell your friend. You fear that they may tell your other friends. ")
print("They continue harassing you, and your mental health drastically decreases. Your test scores drop.")
print("You used to be the perfect student. Now, you're moody, you fall asleep, and are isolated from")
print("society. Your german teacher notices and asks you what's wrong. ")
print("===========================================================================================================")
print("""
                                888   d8b                       d8888 
                                888   Y8P                      d8P888 
                                888                           d8P 888 
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.     d8P  888 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b   d88   888 
888  888888  88888888888"Y8888b.888   888888  888888  888   8888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888         888 
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888         888 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("Your german teacher asks what's wrong. You tremble to the question. How do you deal with the situation?")
print("a) Hang on, my teacher has no place in my mental life?!")
print("b) Yes, please help me.")
print("c) Nein, Ich habe meine Meinung geandert. Ich muss es meinen Eltern sagen. ")
print("   Sie sind die einzigen, denen ich bis zu einem gewissen Grad vertraue.")
print("   (I have changed my mind. I need to tell my parents. They are the only")
print("    ones I trust to a certain degree.)")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "A" or q2s2 == "a" or q2s2 == "c" or q1s1 == "C":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: A")
    print("Would you like to see an explanation as to why 'A' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("A is correct, because you need help if your mental health goes down.")
        print("B is incorrect. Your mental health will ONLY get worse. ")
        print("C is also correct. Your teacher, abeit German only speaking, may be able to help, (or transfer")
        print("the situation over to someone who can help.)")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("You do the thy honourable and tell your german teacher (ja!). He is concerned and listens. He")
print("is concerned about how long this is going on. He wants to contact the police and rectify the matter.")
print("He tells that he will not do it without your strict and direct permission. ")
print("===========================================================================================================")
print("""
                                888   d8b                   888888888              .d888d8b                888        
                                888   Y8P                   888                   d88P" Y8P                888        
                                888                         888                   888                      888        
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.    8888888b.             88888888888888b.  8888b. 888 .d88b. 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y88b            888   888888 "88b    "88b888d8P  Y8b
888  888888  88888888888"Y8888b.888   888888  888888  888          888   888888   888   888888  888.d88888888888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P            888   888888  888888  888888Y8b.    
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P"             888   888888  888"Y888888888 "Y8888 
     888                                                                                                              
     888                                                                                                              
     888  
""")
print("===========================================================================================================")
print("Will you let the police interfere? ")
print("a) Yes.")
print("b) Oh, heck nah!")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "A" or q2s2 == "a":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: A")
    print("Would you like to see an explanation as to why 'A' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("A is correct, the police is known to successfully resolve situations.")
        print("B is incorrect. You will not stop the person. There may be other young people")
        print("who fall victim to the person.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("After a succesful police interference, the police stop a 15 year old from Luton, who was playing the ")
print("prank. You were not the only person affected by this child. He was sentenced to pay reparations of £120,000, and")
print("at least 4 weeks of community service. You feel relieved.")
print("===========================================================================================================")
print("You have crossed the SCENARIO 5, congrats. You are five out of eight sceanarios through the project/quiz.")
print("""
                                               888                    
                                               888                    
                                               888                    
 .d8888b .d88b. 88888b.  .d88b. 888d888 8888b. 888888.d8888b          
d88P"   d88""88b888 "88bd88P"88b888P"      "88b888   88K              
888     888  888888  888888  888888    .d888888888   "Y8888b.         
Y88b.   Y88..88P888  888Y88b 888888    888  888Y88b.      X88      d8b
 "Y8888P "Y88P" 888  888 "Y88888888    "Y888888 "Y888 88888P'      Y8P
                             888                                      
                        Y8b d88P                                      
                         "Y88P"                                       
""")
print("===========================================================================================================")
print("This is where there are three more scenarios.")
print("Let's a continue!")
print("===========================================================================================================")
print("""
                                               d8b            .d8888b. 
                                               Y8P           d88P  Y88b
                                                             888       
.d8888b  .d8888b .d88b. 88888b.  8888b. 888d888888 .d88b.    888d888b. 
88K     d88P"   d8P  Y8b888 "88b    "88b888P"  888d88""88b   888P "Y88b
"Y8888b.888     88888888888  888.d888888888    888888  888   888    888
     X88Y88b.   Y8b.    888  888888  888888    888Y88..88P   Y88b  d88P
 88888P' "Y8888P "Y8888 888  888"Y888888888    888 "Y88P"     "Y8888P" 
""")
print("===========================================================================================================")
print("This section is all about cyberbullying. Would you like to see it?")
check = input()
if check == "yes" or check == "Yes":
    print("Sometimes called cyberbullying. Any behaviour that uses technology ")
    print("and devices to deliberately target or upset someone.")
    print("The internet is a tool, but how we use it is up to us. Some people choose to deliberately ")
    print("target or harass others, with the intention of upsetting or humiliating them. This is never")
    print("okay and, for the victims, can be incredibly difficult and damaging.")
    print("This can be done through your friends or someone you completely do not know.")
    print("Scenario 6 is about this.")
    print("There is a website explaining it better than I am. Would you like to visit it?")
    if checkchallenge == "yes" or checkchallenge == "Yes":
        print("That's good. Taking you there!")
        print("Woosh! Off you go!")
        time.sleep(1.2)
        webbrowser.open("https://www.childnet.com/help-and-advice/online-bullying-11-18-year-olds/")
        time.sleep(1.2)
        print("There you go!")
    else:
        print("Okay, that's fine.")
else:
    print("That's fine.")
print("===========================================================================================================")  
print("Bobby and Fartlek are on YouTube. Thery set up a channel, they post great videos, with no bad motivation. ")
print("They enjoy it and slowly gain subscribers. Soon, with 1,000 subscribers, they post even videos.")
print("/////////// YOU ARE BOBBY! //////////////////////////////////////////////////////////////////")
print("It's not long after Bobby gets a very bad comment on one of his videos, disrespecting his videos.")
print("He feels bad, and dismotivated by this comment. ")
print("===========================================================================================================")  
print("""
                                888   d8b                    d888  
                                888   Y8P                   d8888  
                                888                           888  
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.      888  
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b     888  
888  888888  88888888888"Y8888b.888   888888  888888  888     888  
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888     888  
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888   8888888
     888                                                           
     888                                                           
     888
""")
print("===========================================================================================================") 
print("You feel very dismotivated by the comment. What should you do?")
print("a) Ignore it, and continue creating videos.")
print("b) Take on the critcism the guy says and improve your videos.")
print("c) Leak his IP address to the world.")
print("d) Delete his comment and block him from commenting.")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "D" or q2s2 == "d" or q2s2 == "A" or q2s2 == "a":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: A or D")
    print("Would you like to see an explanation as to why 'A' or 'D' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("D and A and the best options. They don't hurt you or offend/provoke the person on the other end.")
        print("B would have been right, but most of the time now, it's a joke comment.")
        print("C is bad, it will affect you, because you're doing something illegal.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================") 
print("You decide to delete the comment on the video. Unfortantely, the person now")
print("has turned your videos, edited them, and turned into works of evil. Pure, non-catholic evil.")
print("Fartlek has left your channel, he doesn't want to be linked in the drama.")
print("You soon end up getting lots of attention, not for the right cause.")
print("In addition, the person has created a horrible rumor that you are linked to the AL QAEDA.")
print("This is not a good situation to be in.")
print("===========================================================================================================") 
print("""
                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                                888
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.         .d88P
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b    .od888P" 
888  888888  88888888888"Y8888b.888   888888  888888  888   d88P"     
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   888"      
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888   888888888 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("You feel like deleting your channel. What should you do?")
print("a) Delete the channel and report to polizei.")
print("b) Delete your channel and follow the princples of say nothing, do nothing, act like nothing.")
print("c) Don't delete the channel, but commence a report to the polizei.")
print("d) Don't delete your channel, and don't report it to the polizei.")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "c" or q2s2 == "C" or q2s2 == "A" or q2s2 == "a":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: A or D")
    print("Would you like to see an explanation as to why 'A' or 'C' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("A and C are good because you should report it to the police and get the person who started it")
        print("pay for it. B could be good, but sooner or later, that could be a bad decision in the long term. Besides,")
        print("you don't want to delete a channel with 1,000 subscribers, don't you?")
        print("D is the worst.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("You report it to the police. They tell you they will investigate. This will take a couple weeks.")
print("You still get hate comments on all socials. Even your friends at school have turned against you.")
print("You want to delete the channel mid-investigation.")
print("===========================================================================================================")
print("""
                                888   d8b                    .d8888b. 
                                888   Y8P                   d88P  Y88b
                                888                              .d88P
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.        8888" 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y8b.
888  888888  88888888888"Y8888b.888   888888  888888  888   888    888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P" 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("You consider deleting your channel. Do you though?")
print("a) Let's end this nightmare.")
print("b) Hold up, wait, we need to consider. Wait for a bit.")
print("c) You want to delete the channel, but you'll ask the police for permission first. ")
print("d) Fight back to all the people.")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "c" or q2s2 == "C" or q2s2 == "B" or q2s2 == "b":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: B or C")
    print("Would you like to see an explanation as to why 'B' or 'C' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("You need to ask the permission of the polizei before deleting evidence.")
        print("They'll need to make a backup of your website.")
        print("Therefore, B and C are the best. A and D are the worst.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("You do not delete the channel. You do not fight back. You wait. Meanwhile the person continues to ")
print("create horrible rumors. This is seriously damaging your online and social reputation. He calls you ")
print("racist words, discrimates you and bullys you to into oblivation.")
print("This is not good. Absolutely shocking. In addition, he wants money to stop this rouse.")
print("===========================================================================================================")
print("""
                                888   d8b                       d8888 
                                888   Y8P                      d8P888 
                                888                           d8P 888 
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.     d8P  888 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b   d88   888 
888  888888  88888888888"Y8888b.888   888888  888888  888   8888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888         888 
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888         888 
     888                                                              
     888                                                              
     888
""")
print("===========================================================================================================")
print("Simple. Do it or not?")
print("a) Pay that person, and make them go away.")
print("b) Continue to take your stance.")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "b" or q2s2 == "B":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: B")
    print("Would you like to see an explanation as to why 'B' are the correct answers?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("You never know what he'll do with the money. You need to make sure.")
        print("Therefore, B is the right answer.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("You get a result. Shockingly, the police has stopped the drama and everything, but have decided not to press")
print("charges towards the person, even though they know who it is. ")
print("You consider pressing an appeal.")
print("===========================================================================================================")
print("""
                                888   d8b                   888888888              .d888d8b                888        
                                888   Y8P                   888                   d88P" Y8P                888        
                                888                         888                   888                      888        
 .d88888888  888 .d88b. .d8888b 888888888 .d88b. 88888b.    8888888b.             88888888888888b.  8888b. 888 .d88b. 
d88" 888888  888d8P  Y8b88K     888   888d88""88b888 "88b        "Y88b            888   888888 "88b    "88b888d8P  Y8b
888  888888  88888888888"Y8888b.888   888888  888888  888          888   888888   888   888888  888.d88888888888888888
Y88b 888Y88b 888Y8b.         X88Y88b. 888Y88..88P888  888   Y88b  d88P            888   888888  888888  888888Y8b.    
 "Y88888 "Y88888 "Y8888  88888P' "Y888888 "Y88P" 888  888    "Y8888P"             888   888888  888"Y888888888 "Y8888 
     888                                                                                                              
     888                                                                                                              
     888  
""")
print("===========================================================================================================")
print("Do you press charges?")
print("a) Yes")
print("b) No, let him have peace.")
start_time = time.time()
q2s2 = input()
end_time = time.time()
if q2s2 == "A" or q2s2 == "A":
    print("Yes, that is right. Congrats.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
else:
    print("Nope. That was not the right answer.")
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    print("And you still got it wrong!")
    print("The correct answer was: B")
    print("Would you like to see an explanation as to why 'A' is the correct answer?")
    moreinfo_option1 = input()
    if moreinfo_option1 == "yes" or moreinfo_option1 == "Yes":
        print("You should definitely press charges. You need him to repay you for the stress and social life ruin caused.")
        print("Therefore A is correct.")
    else:
        print("Alright.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                                               d8b           8888888888
                                               Y8P                 d88P
                                                                  d88P 
.d8888b  .d8888b .d88b. 88888b.  8888b. 888d888888 .d88b.        d88P  
88K     d88P"   d8P  Y8b888 "88b    "88b888P"  888d88""88b      8888
"Y8888b.888     88888888888  888.d888888888    888888  888     d88P    
     X88Y88b.   Y8b.    888  888888  888888    888Y88..88P    d88P     
 88888P' "Y8888P "Y8888 888  888"Y888888888    888 "Y88P"    d88P    
""")
print("===========================================================================================================")
print("This section is all about cyberbullying. Would you like to see it?")
check = input()
if check == "yes" or check == "Yes":
    print("Location-based services are found on most smart devices including phones ")
    print("and use technology to pinpoint the location of your device")
    print("Your location refers to where you are and devices often track this in the background even when you don’t have internet or")
    print("reception. These location-based services are found on most smart devices")
    print("including phones and use technology to pinpoint the location of your device, and therefore you!")
    print("There is a website explaining it better than I am. Would you like to visit it?")
    if checkchallenge == "yes" or checkchallenge == "Yes":
        print("That's good. Taking you there!")
        print("Woosh! Off you go!")
        time.sleep(1.2)
        webbrowser.open("https://www.childnet.com/help-and-advice/location-services-11-18-year-olds/")
        time.sleep(1.2)
        print("There you go!")
    else:
        print("Okay, that's fine.")
else:
    print("That's fine.")
print("===========================================================================================================")
print("For this next part, you need to read an article to answer the following questions.")
print("You have a couple options to read this:")
print(" 1) This website is stored in HTML in the folder this .py file is in. (offline)")
print(" ")
print(" 2) Alternatively, you may view an up-to-date version of the website.")
print(" This does requires a good internet connection and a web browser.")
print(" 3) Like said earlier, you may download an HTML file (the website) and an educational video")
print(" >>> (requires the wget modules to be installed)")
print("===========================================================================================================")  
print("Select your option:")
optionmodule = input()
if optionmodule == "1":
    print("Alright. Please go to the folder and read the website.")
    print("Come back when you are ready.")
if optionmodule == "2":
    print("Alright. This will open up a web browser with the link.")
    print("Off you go.")
    webbrowser.open("https://ico.org.uk/for-organisations/guide-to-data-protection/ico-codes-of-practice/age-appropriate-design-a-code-of-practice-for-online-services/10-geolocation/")
if optionmodule == "3":
    print("If you DO NOT have wget installed, python will refuse to run this.")
    print("It is more than likely that you will get an error if that is the case.")
    print("/////////////////////////////////////////////////////////////////////////")
    print("Connecting to GitHub and downloading the files.")
    print("Depending on the internet connection you have, this may take a while.")
    URL = "https://github.com/realinteldiscord2004/python_project_safety/raw/main/websites/scenario7.txt"
    response = wget.download(URL, "scenario7.txt")
    URL = "https://github.com/realinteldiscord2004/python_project_safety/raw/main/videos/scenario7.mp4"
    response = wget.download(URL, "scenario7.mp4")
    print(" ")
    print("Done! Check your folder for the .txt and the .mp4 (you need to extract it first from the zip file.)")
print("===========================================================================================================")
print("Simply read or/and watch the provided files, and then press enter when you are ready.")
print("Waiting for response...")
checkchallenge = input()
print("Alright. Let's continue (on the assumption that you finished reading.)")
print("===========================================================================================================")
print("""
                       888       d888              .d888       d8888 
                       888      d8888             d88P"       d8P888 
                       888        888             888        d8P 888 
88888b.  8888b. 888d888888888     888      .d88b. 888888    d8P  888 
888 "88b    "88b888P"  888        888     d88""88b888      d88   888 
888  888.d888888888    888        888     888  888888      8888888888
888 d88P888  888888    Y88b.      888     Y88..88P888            888 
88888P" "Y888888888     "Y888   8888888    "Y88P" 888            888 
888                                                                  
888                                                                  
888  
""")
print("===========================================================================================================")
print("Question 1: What is Geological Data?")
print("a) The fact of location getting taken from your phone and being shared publicly.")
print("b) The fact of location of geological seismic activity being near your house.")
print("c) The fact of present data about rare soil near your house.")
q1s4 = input()
if q1s4 == "a" or q1s4 == "A":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 2: Can location services reveal too much about you?")
print("a) Of course...")
print("b) That's a lie.")
print("c) Potentially.")
q2s4 = input()
if q2s4 == "c" or q2s4 == "C":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                       888       .d8888b.             .d888       d8888 
                       888      d88P  Y88b           d88P"       d8P888 
                       888             888           888        d8P 888 
88888b.  8888b. 888d888888888        .d88P    .d88b. 888888    d8P  888 
888 "88b    "88b888P"  888       .od888P"    d88""88b888      d88   888 
888  888.d888888888    888      d88P"        888  888888      8888888888
888 d88P888  888888    Y88b.    888"         Y88..88P888            888 
88888P" "Y888888888     "Y888   888888888     "Y88P" 888            888 
888                                                                     
888                                                                     
888
""")
print("===========================================================================================================")
print("Question 3: Can location services cause make vulnerablity to risks such")
print("as abduction, physical and mental abuse, sexual abuse and trafficking?")
print("a) False.")
print("b) True.")
q1s4 = input()
if q1s4 == "b" or q1s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 4: Billy has location services on by default. Is this correct? ")
print("a) Of course...")
print("b) Nope, that's dangerous!")
q2s4 = input()
if q2s4 == "b" or q2s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                       888       .d8888b.             .d888       d8888 
                       888      d88P  Y88b           d88P"       d8P888 
                       888           .d88P           888        d8P 888 
88888b.  8888b. 888d888888888       8888"     .d88b. 888888    d8P  888 
888 "88b    "88b888P"  888           "Y8b.   d88""88b888      d88   888 
888  888.d888888888    888      888    888   888  888888      8888888888
888 d88P888  888888    Y88b.    Y88b  d88P   Y88..88P888            888 
88888P" "Y888888888     "Y888    "Y8888P"     "Y88P" 888            888 
888                                                                     
888                                                                     
888                                                                     
""")
print("===========================================================================================================")
print("Question 5: Does location services threaten their privacy, freedom of association, and freedom from ")
print("economic exploitation, irrespective of threats to their physical safety?")
print("a) False.")
print("b) True.")
q1s4 = input()
if q1s4 == "b" or q1s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 6: The law says that you do not need to know whether location services are on. True or false? ")
print("a) Of course, true! You should know!")
print("b) Nope, that's dangerous! You need to know.")
q2s4 = input()
if q2s4 == "b" or q2s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                       888          d8888             .d888       d8888              .d888d8b                888        
                       888         d8P888            d88P"       d8P888             d88P" Y8P                888        
                       888        d8P 888            888        d8P 888             888                      888        
88888b.  8888b. 888d888888888    d8P  888     .d88b. 888888    d8P  888             88888888888888b.  8888b. 888 .d88b. 
888 "88b    "88b888P"  888      d88   888    d88""88b888      d88   888             888   888888 "88b    "88b888d8P  Y8b
888  888.d888888888    888      8888888888   888  888888      8888888888   888888   888   888888  888.d88888888888888888
888 d88P888  888888    Y88b.          888    Y88..88P888            888             888   888888  888888  888888Y8b.    
88888P" "Y888888888     "Y888         888     "Y88P" 888            888             888   888888  888"Y888888888 "Y8888 
888                                                                                                                     
888                                                                                                                     
888  
""")
print("===========================================================================================================")
print("Question 7: Does location services threaten their privacy, freedom of association, and freedom from ")
print("economic exploitation, irrespective of threats to their physical safety?")
print("a) False.")
print("b) True.")
q1s4 = input()
if q1s4 == "b" or q1s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 8: If a company does not provide infomation when location services are on, what are they violating?")
print("a) PCEAR")
print("b) PEARS")
print("c) PECR")
q2s4 = input()
if q2s4 == "C" or q2s4 == "c":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                                               d8b            .d8888b. 
                                               Y8P           d88P  Y88b
                                                             Y88b. d88P
.d8888b  .d8888b .d88b. 88888b.  8888b. 888d888888 .d88b.     "Y88888" 
88K     d88P"   d8P  Y8b888 "88b    "88b888P"  888d88""88b   .d8P""Y8b.
"Y8888b.888     88888888888  888.d888888888    888888  888   888    888
     X88Y88b.   Y8b.    888  888888  888888    888Y88..88P   Y88b  d88P
 88888P' "Y8888P "Y8888 888  888"Y888888888    888 "Y88P"     "Y8888P" 
""")
print("===========================================================================================================")
print("This section is all about livestreaming. Would you like to see it?")
check = input()
if check == "yes" or check == "Yes":
    print("People use livestreaming to broadcast live video footage of ")
    print("themselves to others, usually their friends/family or the general public")
    print("Livestreaming is a way for people to broadcast themselves online. Apps such as Instagram, ")
    print("Facebook, TikTok, Twitch and YouTube all offer livestreaming services.")
    print("People use livestreaming to broadcast live video footage of themselves to others, usually their ")
    print("friends/family or the general public. This could be something specific such as playing an online ")
    print("game alongside a voiceover or a more general day-to-day run through of their lives.")
    print("Celebrities, influencers or vloggers may use it to communicate with their fans or to spread messages, ")
    print("including advertising and marketing.")
    print("Livestreaming is also used to communicate to the world what is happening at a specific moment in time. ")
    print("For example, to document breaking news stories on large media channels.")
    print("There is a website explaining this better. Would you like to visit it?")
    if checkchallenge == "yes" or checkchallenge == "Yes":
        print("That's good. Taking you there!")
        print("Woosh! Off you go!")
        time.sleep(1.2)
        webbrowser.open("https://www.childnet.com/help-and-advice/livestreaming-11-18-year-olds/")
        time.sleep(1.2)
        print("There you go!")
    else:
        print("Okay, that's fine.")
else:
    print("That's fine.")
print("===========================================================================================================")
print("For this next part, you need to read an article to answer the following questions.")
print("You have a couple options to read this:")
print(" 1) This website is stored in HTML in the folder this .py file is in. (offline)")
print(" ")
print(" 2) Alternatively, you may view an up-to-date version of the website.")
print(" This does requires a good internet connection and a web browser.")
print(" 3) Like said earlier, you may download an HTML file (the website) and an educational video")
print(" >>> (requires the wget modules to be installed)")
print("===========================================================================================================")  
print("Select your option:")
optionmodule = input()
if optionmodule == "1":
    print("Alright. Please go to the folder and read the website.")
    print("Come back when you are ready.")
if optionmodule == "2":
    print("Alright. This will open up a web browser with the link.")
    print("Off you go.")
    webbrowser.open("https://nationalonlinesafety.com/wakeupwednesday/livestreaming-what-are-the-online-risks-for-children-and-young-people")
if optionmodule == "3":
    print("If you DO NOT have wget installed, python will refuse to run this.")
    print("It is more than likely that you will get an error if that is the case.")
    print("/////////////////////////////////////////////////////////////////////////")
    print("Connecting to GitHub and downloading the files.")
    print("Depending on the internet connection you have, this may take a while.")
    URL = "https://github.com/realinteldiscord2004/python_project_safety/raw/main/websites/scenario8.txt"
    response = wget.download(URL, "scenario8.txt")
    URL = "https://github.com/realinteldiscord2004/python_project_safety/raw/main/videos/scenario8.mp4"
    response = wget.download(URL, "scenario8.mp4")
    print(" ")
    print("Done! Check your folder for the .txt and the .mp4 (you need to extract it first from the zip file.)")
print("===========================================================================================================")
print("Simply read or/and watch the provided files, and then press enter when you are ready.")
print("Waiting for response...")
checkchallenge = input()
print("Alright. Let's continue (on the assumption that you finished reading.)")
print("===========================================================================================================")
print("""
                       888       d888              .d888       d8888 
                       888      d8888             d88P"       d8P888 
                       888        888             888        d8P 888 
88888b.  8888b. 888d888888888     888      .d88b. 888888    d8P  888 
888 "88b    "88b888P"  888        888     d88""88b888      d88   888 
888  888.d888888888    888        888     888  888888      8888888888
888 d88P888  888888    Y88b.      888     Y88..88P888            888 
88888P" "Y888888888     "Y888   8888888    "Y88P" 888            888 
888                                                                  
888                                                                  
888  
""")
print("===========================================================================================================")
print("Question 1: How many people can watch your live stream?")
print("a) Hundreds.")
print("b) Thousands.")
print("c) You don't know how much.")
print("d) All the above.")
q1s4 = input()
if q1s4 == "d" or q1s4 == "D":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("Question 2: Livestreaming can be saved to anyone's device at any time.")
print("a) Of course.")
print("b) Nope.")
print("c) Potentially.")
q2s4 = input()
if q2s4 == "c" or q2s4 == "C":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                       888       .d8888b.             .d888       d8888 
                       888      d88P  Y88b           d88P"       d8P888 
                       888             888           888        d8P 888 
88888b.  8888b. 888d888888888        .d88P    .d88b. 888888    d8P  888 
888 "88b    "88b888P"  888       .od888P"    d88""88b888      d88   888 
888  888.d888888888    888      d88P"        888  888888      8888888888
888 d88P888  888888    Y88b.    888"         Y88..88P888            888 
88888P" "Y888888888     "Y888   888888888     "Y88P" 888            888 
888                                                                     
888                                                                     
888
""")
print("===========================================================================================================")
print("Question 3: They cannot be used by people with malicious intent.")
print("a) False.")
print("b) True.")
q1s4 = input()
if q1s4 == "a" or q1s4 == "A":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 4: Billy wants to livestream his gaming. Should he reveal his face?")
print("a) Of course. No harm in doing so.")
print("b) Nope, that's dangerous! Not yet.")
q2s4 = input()
if q2s4 == "b" or q2s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                       888       .d8888b.             .d888       d8888 
                       888      d88P  Y88b           d88P"       d8P888 
                       888           .d88P           888        d8P 888 
88888b.  8888b. 888d888888888       8888"     .d88b. 888888    d8P  888 
888 "88b    "88b888P"  888           "Y8b.   d88""88b888      d88   888 
888  888.d888888888    888      888    888   888  888888      8888888888
888 d88P888  888888    Y88b.    Y88b  d88P   Y88..88P888            888 
88888P" "Y888888888     "Y888    "Y8888P"     "Y88P" 888            888 
888                                                                     
888                                                                     
888                                                                     
""")
print("===========================================================================================================")
print("Question 5: State the amount of live stream that increased during the COVID-19 pandemic.")
print("a) 2.3m > 5.2m")
print("b) 3.2m > 5.2m")
print("c) 2.3m > 4.2m")
q1s4 = input()
if q1s4 == "c" or q1s4 == "C":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 6: State the percentage of people aged 8-17 that have gone live (during the Pandemic). ")
print("a) 10%")
print("b) 25%")
print("c) 12.6%")
print("c) 34%")
q2s4 = input()
if q2s4 == "a" or q2s4 == "A":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                       888          d8888             .d888       d8888              .d888d8b                888        
                       888         d8P888            d88P"       d8P888             d88P" Y8P                888        
                       888        d8P 888            888        d8P 888             888                      888        
88888b.  8888b. 888d888888888    d8P  888     .d88b. 888888    d8P  888             88888888888888b.  8888b. 888 .d88b. 
888 "88b    "88b888P"  888      d88   888    d88""88b888      d88   888             888   888888 "88b    "88b888d8P  Y8b
888  888.d888888888    888      8888888888   888  888888      8888888888   888888   888   888888  888.d88888888888888888
888 d88P888  888888    Y88b.          888    Y88..88P888            888             888   888888  888888  888888Y8b.    
88888P" "Y888888888     "Y888         888     "Y88P" 888            888             888   888888  888"Y888888888 "Y8888 
888                                                                                                                     
888                                                                                                                     
888  
""")
print("===========================================================================================================")
print("Question 7: Can children view age-inappropriate content as well as")
print("sexual or violent content if they are watching other people's livestreams?")
print("a) False.")
print("b) True.")
q1s4 = input()
if q1s4 == "b" or q1s4 == "B":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h -1
    hcheck()
print("===========================================================================================================")
print("Question 8: If a teacher live-streams you in a lesson, what are they violating?")
print("a) TGBBO")
print("b) GDPR")
print("c) GDR")
q2s4 = input()
if q2s4 == "B" or q2s4 == "b":
    print("Correct. Well done.")
else:
    print("Nope. That ain't right, mate.")
    h = h - 1
    hcheck()
print("===========================================================================================================")
print("""
                                               888                    
                                               888                    
                                               888                    
 .d8888b .d88b. 88888b.  .d88b. 888d888 8888b. 888888.d8888b          
d88P"   d88""88b888 "88bd88P"88b888P"      "88b888   88K              
888     888  888888  888888  888888    .d888888888   "Y8888b.         
Y88b.   Y88..88P888  888Y88b 888888    888  888Y88b.      X88      d8b
 "Y8888P "Y88P" 888  888 "Y88888888    "Y888888 "Y888 88888P'      Y8P
                             888                                      
                        Y8b d88P                                      
                         "Y88P"  
""")
print("////////////////////////////////////////////////////////////////////")
print("You have now finished the E-SAFETY PROJECT BY MARCEL CISZEWSKI.")
print("You had this much lives left:" ,h)
print("Congrats. Thank you for playing. This took me over 3 weeks to code.")
print("////////////////////////////////////////////////////////////////////")
print("Credits:")
print("All code - Marcel Ciszewski")
print("Debugging - StackOverflow.")
print("////////////////////////////////////////////////////////////////////")
print("Finish?")
continue1 = input()
time.sleep(2)
if(os.name == 'posix'):
    os.system('clear')
else:
    os.system('cls')
time.sleep(0.1)
print(Flush=True)
exit()

