# name : sahil wagh
   div : m roll no:65
   gr no:11810821

from easygui import *
import sys
while 1:
    msgbox("Welcome to Flipbazaar")

    msg ="Which site would you like?"
    title = "Site Names"
    choices = ["AMAZON", "FLIPKART", "JABONG"] 
    choice = choicebox(msg, title, choices)
    if choice=="AMAZON":
          msg1="which department?"
          title1="which section?"
          choices1=["cloths","footwear","food"]
          choice1=choicebox(msg1,title1,choices1)
          if choice1=="cloths":
                   msg11="which brand?"
                   title11="choose discount"
                   choices11=["armani","levis"]
                   choice11=choicebox(msg11,title11,choices11)  
    elif choice=="FLIPKART":
          msg2="which department?"
          title2="which section?"
          choices2=["sofa","table","poster"]
          choice2=choicebox(msg2,title2,choices2)
    elif choice=="JABONG":
          msg3="which department?"
          title3="which section?"
          choices3=["poster","chairs","doors"]
          choice3=choicebox(msg3,title3,choices3)             
    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Shopping bag")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)

