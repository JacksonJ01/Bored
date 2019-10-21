# Jared Jackson
# 10/17/19
# I am at work at te moment. Although I'm not bored out of my mind,
# but I am on a four shift for today am tmw. I have an hour and a half left, so here I am
# Scratch that, a young buck can't count. It was actually two and a half hours
# I realized it once it said four and not 5
# Anyhow, I will be making the user do math problems, but the values they enter into a list,
# and then compare those values other values from another list that has been checked mathematically

# from random import *
# rn = randint(0, 50)


user_inputs = []
answers = []


# This function name kills me every time I see it.
# This is gonna take so long
def pregame():
    print("How are you doing, Good or Bad? *Choose one*")
    doing = input(">>>\n").title()
    if doing == "Good" or doing == "G":
        print(f"That's very nice to hear {name}! I'm glad you're alright.")
        print("And why would you say it's been good?")
        print("School? Work? Everything? No clue? *Choose one*")

        def why_dg():
            why_good = input(">>>").title()

            if why_good == "School" or why_good == "S":
                print("Ahh, that wouldn't be my answer, but what ever floats your boat.")

            elif why_good == "Work" or why_good == "W":
                print("Hmm. Work? I could see how that would be the case.")
                print("My job is pretty cool too. I get to bother users who fall into my \"PRESS ENTER\" trap...")
                print("What I meant to say was, where exactly do you work?")
                input(">>>")
                print("Oh, that's awesome. No wonder you like it.")

            elif why_good == "Everything" or why_good == "E":
                print("Well someone is optimistic. I guess that's a pretty good thing.")
                print("You've got everything in your life going right. Don't stray from the path.")

            elif why_good == "No Clue" or why_good == "N":
                print("What? No clue? You're just in a good mood, huh. I need to be more like that.")

            elif why_good != "School" or why_good != "Work" or why_good != "Everything" or why_good != "No Clue":
                print("Uhm... I didn't get that. Old hardware inside.")
                print(f"Try again {name}, this time using one of the provided options!")
                print("Your options are:")
                print("School")
                print("Work")
                print("Everything")
                print("No clue")
                print("Re-running software\n")
                why_dg()

        why_dg()  # This calls the function above

    elif doing == "Bad" or doing == "B":
        print(f"Awe, {name}, that's not okay")
        print("You should go seek some professional help. We have services here on campus")
        print("But while you're here...")

        def why_db():
            why_bad = input(">>>").title()

            if why_bad == "School" or why_bad == "S":
                print("That'd be my answer too. What about school has you feeling yuck?")
                print("Is it the classes or workload? *Yes or No*")

                def wl1():
                    wl = input(">>>").title()
                    if wl == "Yes" or wl == "Y":
                        print("Oh boy have I been there. You know, even this right here is a lot of work; me existing")
                        print("I should charge you!")
                        print("Ha Ha Ha")
                        print("Did I make you laugh?")

                        def laugh1():
                            laugh = input(">>>").title()

                            if laugh == "Yes" or laugh == "Y":
                                print("Yay, I feel accomplished. My work here is done. Go get some real help though.")

                            elif laugh == "No" or laugh == "N":
                                print("Oof, well that sucks. At least I tried. Go seek some real help.")

                            else:
                                print("Sorry, only Yes or No answers")
                                laugh1()

                        laugh1()

                    elif wl == "No" or wl == "N":
                        print("Hmm, okay then.")
                        print("That's a doosey.")
                        print("Then what seems to be the problem?")
                        input(">>>")
                        print("Well you should go talk to a real person.")
                        print("My skills can go no further for that.")

                    else:
                        print("Can you say that again")
                        print("Yes or no")
                        wl1()

                wl1()

            elif why_bad == "Work" or why_bad == "W":
                print("And about work?")
                print("Is it the work load and/ or the hours?")

                def wl3():
                    wl2 = input(">>>").title()
                    if wl2 == "Yes" or wl2 == "Y":
                        print("Well have you talked with your Supervisor?")
                        talked = input(">>>").title()

                        if talked == "Yes" or talked == "Y":
                            print("And what did they say?")
                            print("I'm assuming you guys couldn't come to a consensus, seeing as how you answered yes.")
                            print("Well don't do anything too drastic, but you should look over your options.")

                        elif talked == "No" or talked == "N":
                            print("Then why are you here? Go do that...")
                            print("Well, actually, you can stay a bit longer")

                        else:
                            print("I didn't get that")
                            print("Yes or No")
                            wl3()

                    elif wl2 == "No" or wl2 == "No":
                        print("Then why did you take the job?...")

                    else:
                        print("Was that a Yes or No?")
                        wl3()

                wl3()

            elif why_bad == "Everything" or why_bad == "E":
                print("Okay for this you should actually go seek some real help.")
                print("If everything has you like this then...")
                print("You should go definitely go vent")

            elif why_bad == "No Clue" or why_bad == "N":
                print("Maybe you should try meditation")
                print('"Look deep within yourself and find the cause, only then can you find salvation"')

            else:
                print(f"Sorry {name}, I didn't catch that.")
                print("Okay, allow me to ask again.")
                print("This time use the given options. Okay?")
                print("You can choose from:")
                print("School")
                print("Work")
                print("Everything")
                print("No clue")
                print("Re-running software\n")
                why_db()

        print(f"Can I ask you some questions {name}?")

        def ask1():
            ask = input(">>>").title()
            if ask == "Yes" or ask == "Y":
                print("Okay")
                print("ENTERING THERAPY MODE\n")
                print("Now as an old computer, my capabilities are quite limited")
                print("But I will still do my best to help you")
                print("Now what seems to be the problem?")
                print("Is it School? Work? Everything? No clue? *Choose one*\n")
                why_db()

            elif ask == "No" or ask == "N":
                print("Oh, okay then. That's fine too")
                print("Are you sure though?")

                def sure1():
                    sure = input(">>>").title()
                    if sure == "Yes" or "Y":
                        print("Alright, let's continue")

                    elif sure == "No" or sure == "N":
                        print("I knew you would come around")
                        why_db()

                    else:
                        print("Sorry, i didn't catch that")
                        sure1()

                sure1()

            else:
                print("Yes or no answers please")
                print("I'd like to know if I can help")
                ask1()

        ask1()

    else:
        print("Wait, I'm not sure what that means...")
        print("My processor isn't up to date.")
        print("Please answer that again for me using the optional answers")
        pregame()


input("CLICK THE"
      " SCREEN THEN PRESS ENTER TO START\n")
name = input("""Hello there, what is your name?
>>>""").title()
print(f"Hello there {name}, it is nice to meet you.")
pregame()
# It is now 17:50, meaning it took me over 3 hours to write this code
# and the actual "game" hasn't even started

# Now that that's over with, I can finally get started on the function for the game.
# It's a new day... another 4 hours of work
# Plenty of code time. . .
# *2 hours later* I actually had to fix a couple of things
# Just kidding, it is now 16:08. I was doing actual work for a while but
# I still haven't started my game because I keep adding and fixing shit
# It is now 21:11. I think I'm done with that section above, for now
# I should make another repository and add journal entries into it

print("\n\nSo now that that's over with, I'm gonna have you do some math problems.")
print("You will only be able to attempt each math problem once...")
print("Meaning you should check your values before you press enter!")


def game():
    print("")


game()
