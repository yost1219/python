"""
Author: Yost
Title: Lab 3C - FunHouse
Date: 7 Sep 2018

Lab 3C: The "Fun" House

Instructions

Create a text-based game where the user is navigating through a "Fun" House. Prompt the user to make a decision and using if/elif/else statements, give them different outcomes based on their answers. Begin with an introduction to your fun house and prompt the user to choose between at least three different options. You can use nested if/elif/else statements to make the game more complex.
Requirments

    Adhere to PEP8 (Comments, formatting, style, etc)
    Utilize userinput
    Utilize proper formatting
    Utilize proper and clean if/elif/else statements
    Follow instructions above

Additional

    Take this a step further. Use some previous concepts. Here are some things you can do:
        Create a file that holds all of your prompts
        Store file prompts into a list, dict, etc
        Use if/elif/else statements to validate user input
        Use formatting to create UI elements and/or fancy prompts
        Use operators and user input to perform calculations based on prompts
        etc

Example:

print "Welcome to Fun House! Choose door 1, 2, or 3..."

input = raw_input("> ")

if input == "1":
    #<code>
    print"1"

elif input == "2":
    #<code>
    print "2"

elif input == "3":
    #<code>
    print "3"
else:
    print "Go home you're drunk."




"""
def funHouse():
    damage = 1
    armor = 1
    hp = 10
    print "During this game, if you make an invalid choice you will automatically end the game.  You have been warned."
    print "Disclaimer:  If this game offends you, suck it up snowflake."
    choice = raw_input("You come across an 'abandoned' FunHouse.  There is a creepy clown painted on the door (foreshadowing).  Do you want to go in?  (Y)es?")
    choice1 = choice.upper()
    if choice1 == 'Y':
        print "Good, good.  Chickens are no fun."
        print "Just inside the door, you find a baseball bat and a padded leather jacket.  You wisely put them on."
        print "Your damage and armor have increased.  Your HP is {}".format(hp)
        choice = raw_input("You look past the entryway and see a long, dark (h)allway and a rickety (s)taircase.  Which way do you want to go?")
        choice2 = choice.upper()
        if choice2 == 'H':
            print "That's bold of you.  You walk down the hall and stub your toe on a dead cat.  You lose 1 HP."
            hp-=1 #hp = 9
            choice = raw_input("You have come to another intersection.  You see a (k)itchen to the left, the (b)asement ahead of you, and the (l)iving room to the right.")
            choice3 = choice.upper()
            if choice3 == 'K':
                print "Lucky you!  You find a butcher's knife and swap it for your bat.  Damage + 1."
                damage+=1 #damage = 2
                choice = raw_input("You see a Swiss Cake Roll.  Do you want to eat it?  (Y)es or (n)o?")
                choice4 = choice.upper()
                if choice4 == 'Y':
                    print "It's rotten.  Maggots and everything.  You run to the bathroom and puke.  All over the place.  It's seriously nasty.  You lost 1 HP."
                    hp-=1 #hp = 8
                    choice = raw_input("Are you gonna (c)lean up after youself?")
                    choice5 = choice.upper()
                    if choice5 == 'C':
                        print "Thanks for being responsible.  I hate having to clean up after these 'adventurers'."
                        print "While cleaning up, you find a mop bucket and some rubber gloves.  You put them on.  Armor + 1."
                        armor+=1 #armor = 2
                        choice = raw_input("Unfortunately, your whistling has attracted a clown with a chainsaw.  Do you want to (f)ight him/her/it?")
                        choice6 = choice.upper()
                        if choice6 == 'F':
                            print "Bold move, Cotton.  Let's see how this works out for the player."
                            print "You hit him/her/it and he/she/it hits you back.  Your stab him/her/it right in the damn face but get your left arm chainsawed off."
                            print "I hope you're right handed or ambidextrous or it's gonna be hard to wipe later."
                            print "But you killed the clown, and saved the hostage children or whatever.  Oh, and the clown has $1M in his/her/its pants."
                            print "I guess you live happily ever after.  Now you can get a bionic arm at least, so there's that."
                            print "What else was there...let me think...  Oh yeah, game over."
                            return
                        else:
                            print "You run.  The clown says something about your mother.  You turn to reply with some snappy comeback but instead the clown cuts you in half."
                            print "Vertically, but not in the way you would think.  You have a front half and a back half.  It's super messy and super gross.  Blood everywhere."
                            return
                    else:
                        print "You have been smote (Or is it 'smited'?  'Smoten'?) for being a crapbag.  Divine punishment rocks."
                        return
                elif choice4 == 'N':
                    print "Why would you eat something you found in this nasty place?  Good call.  Let's check out the backyard."
                    choice = raw_input("You see a (w)ell and a (s)hed.  Let's check one of them out!")
                    choice7 = choice.upper()
                    if choice7 == 'W':
                        choice = raw_input("You look into the well and see something shiny in the bucket.  (P)ull the bucket up?")
                        choice8 = choice.upper()
                        if choice8 == 'P':
                            print "It's a gun.  Way better than that bat you were carrying.  It even has a few bullets, too.  Damage + 3."
                            damage=damage+3 #damage = 4
                            choice = raw_input("You look behind you and a clown with a chainsaw is staring at you.  Like a creeper.  (T)each him a lesson!")
                            choice9 = choice.upper()
                            if choice9 == 'T':
                                print "Ranged damage beats melee damage so he dead.  You live.  You saved the day, got the girl, etc.  Hooray!"
                                return
                            else:
                                print "Dude!  You had a gun!  What is wrong with you!  You some kind of pacifist?  Well, now you're a dead pacifist.  Your mother would be proud."
                                return
                        else:
                            print "While trying to decide, somebody pushes you into the well and puts a lid on it.  You starve, or drown, or something."
                            print "Point is, you die slowly.  I don't know why you didn't scream for help.  You were probably too busy regretting not pulling up the bucket."
                            return
                    elif choice7 == 'S':
                        choice = raw_input("There is a dog guarding the shed.  A zombie dog.  With rabies.  Are you going to (f)ight it?")
                        choice10 = choice.upper()
                        if choice10 == 'F':
                            print "You smash that dog in the head with your bat.  It's dead now.  Better it than you, amiright?  Yes.  The answer is yes."
                            choice = "You see a WWI era helmet.  Do you (p)ut it on?"
                            choice11 = choice.upper()
                            if choice11 == 'P':
                                print "You put it on for a nice little armor boost (+2) just in time to see a clown with a chainsaw coming to avenge the death of his/her/its faithful pooch, Nibbles."
                                armor=armor+2 #armor = 3
                                print "In the ensuing fight, you try to block the chainsaw with your bat but that works about as well as you would think, aka not at all."
                                print "You think all is lost but remember that the helmet is actually a Bavarian pickelhaube (google it) and stab that B through the temple."
                                print "You saved the day but the princess is in another FunHouse."
                                return
                        else:
                            print "Well, the dog wasn't dead because you didn't kill the brain.  It's a zombie, after all.  It rips out your throat then eats the rest of you."
                            return
                    else:
                        print "You turn to leave and step on a rake.  Like in a cartoon, it pops up and hits you in the face.  You stumble backwards into an above-ground pool."
                        print "Your mom never gave you swimming lessons as a kid and you aren't smart enough to just stand up so you drowned."
                        print "What?  Some people panic when they're drowning and can't think straight.  It's not my fault, blame evolution for taking away your gills."
                        return
                else:
                    print "While thinking about whether you should eat the treat or not, the ceiling fan breaks loose and crushes your skull.  Gonna be a closed casket for you."
                    return
            elif choice3 == 'B':
                print "Well, basements are creepy.  I'm not going down there with you.  Just kidding, I kinda have to since I'm the narrator."
                choice = raw_input("You see a babe/hot guy (not judging) chained to a support beam.  Do you (s)et them free?")
                choice12 = choice.upper()
                if choice12 == 'S':
                    print "They give you their digits as a reward and get on outta there.  You put their feeding tray under your jacket.  Armor + 1."
                    armor+=1 #armor = 2
                    choice = raw_input("Do you want (k)eep looking around the basement?")
                    choice13 = choice.upper()
                    if choice13 == 'K':
                        print "You find a battery-powered nail gun down there which still works.  Bonus.  Damage + 2."
                        damage=damage+2 #damage = 3
                        print "You hear a small engine start up at the top of the stairs.  A clown that isn't wearing any pants (gross) is menacingly revving a chainsaw."
                        print "Running isn't an option so you prepare for a fight.  As you approach, he/she/it taunts you in a gravelly voice 'I have the high ground!'."
                        print "You shoot a nail into each of his/her/its knees causing him/her/it to collapse and fall down the stairs."
                        print "You think his/her/its neck is broken but he/she/its just playing possum.  As you step past, he/she/it lunges out and cuts off your left hand."
                        print "He/she/it also manages to cut off your right leg below at the knee (don't ask me how, I'm just a narrator)."
                        print "In your fury you drive 17 nails into his/her/its head.  That's one dead clown.  Serves him/her/it right, the bastard."
                        print "You drag yourself up the stairs and get away (after applying necessary SABC).  While recovering in the hospital, you remember the hostage."
                        print "You call and ask them out and they suggest a day date.  You tell them that doesn't jive with your schedule."
                        print "You suggest next Wednesday at 7PM because you know day dates are like the express lane to the friend zone and you have less than pure intentions here."
                        print "At the date you dress up like a pirate because you're an optimist and are always trying to make the best out of a bad situation, like missing limbs."
                        print "It's awkward but a good ice breaker.  Plus, it is a constant reminder that you saved their life and earns you some pity points.  Oh yeah."
                        return
                    else:
                        print "Walking back up the stairs you slip on a bar of soap and roll down the stairs, breaking your neck.  You are a great disappointment to your mother and I."
                        return
                else:
                    print "Turns out the 'hostage' was the clown's apprentice.  They kill you when your back is turned."
                    return
            elif choice3 == 'L':
                print "You find a meal on the table.  You eat an apple, restoring 1 HP."
                hp+=1 #hp = 10
                choice = raw_input("You hear a scratching noise coming from the fireplace.  Do you want to check it out?  (N)o?")
                choice14 = choice.upper()
                if choice14 == 'N':
                    print "You move on to the laundry room and head out into the yard.  There is an axe leaning against the house.  Upgrade!  Damage + 2."
                    damage+=2 #damage = 3
                    print "There's a car in front of the garage.  It's a Lancer which triggers your rage.  You hack at the car until the axe handle breaks.  It's now a pointy stick.  Damage - 1."
                    damage-=1 #damage = 2
                    print "The ruckus you create attracts the attention of the clown cutting up a body with a chainsaw in the backyard."
                    choice = raw_input("I guess we should (f)ight him.  He's probably a bad guy and you're pretty tough.  I mean, look what you did to that car, right?")
                    choice15 = choice.upper()
                    if choice15 == 'F':
                        print "His/her/its chainsaw is so bloody from the other body that it stalls.  While he/she/it is trying to start it up again you take advantage and charge."
                        print "You drive your pointy stick through his/her/its throat faster than he/she/it can say 'Hey man, can you give me a sec to get my spinning death blade working again?  Thanks pumpkin.'"
                        print "Yeah, you're right that isn't very fast.  You're not in very good shape.  You've been spending too much time at a desk haven't you?"
                        print "Anyway, so he/she/it is dead and you're alive.  One less Lancer owner in this world.  Net positive."
                        return
                    else:
                        print "You try to run but the Lancer gets its revenge as you trip over the side view mirror that you just removed.  You roll over in time to see the clown swing down and behead you."
                        print "Pay better attention to your surroundings next time.  Oh that's right, you're dead.  You don't get a 'next time'.  Loser."
                        return
                else:
                    print "I gave you a huge hint, but did you listen?  NoooOOOooo.  30 vampire/piranha hybrids pour out of the chimney and eat you.  Not a pretty picture."
                    return
            else:
                print "Turns out the cat was sleeping.  And it wasn't a cat, it was a midget.  With an icepick, and he knows how to use it.  Brain, meet icepick."
                return
        elif choice2 == 'S':
            print "You gingerly walk up the staircase, carefully avoiding splinters (those things will kill ya)."
            choice = raw_input("Do you want to enter the (b)edroom?")
            choice4 = choice.upper()
            if choice4 == 'B':
                print "The bedroom seems like a safe enough place but there's nothing useful here.  Let's checkout the bathroom."
                choice = raw_input("Nothing here either.  Oh well.  You turn to leave but the clown is blocking the doorway.  He has a chainsaw.  You aren't prepared for a (f)ight but what can you do?")
                choice16 = choice.upper()
                if choice16 == 'F':
                    print "You strike before the clown is ready, knocking the chainsaw out of his/her/its hands.  He/she/it closes the distance to prevent you from swinging and pulls a Mike Tyson."
                    print "You give him/her/it a few kidney shots in retaliation which gives you enough room to step back a knock one out of the park.  Barry Bonds would be proud."
                    return
                else:
                    print "You turn and jump out the window which was a terrible idea because you're on the second floor and have no idea what's under the window."
                    print "You land on the iron rod fence, impaling yourself in several places.  You lay there as the blood flows out of your newly-severed femoral artery."
                    print "All you can think about is how Carol at Subway forgot the ranch dressing on your chicken bacon ranch wrap that you had for lunch."
                    print "If anybody should be slowly dying it should be Carol.  I mean, what is a 45 year old doing working minimum wage anyway?  See you in hell, Carol"
                    return
            else:
                print "You stand there for a minute, mulling things over.  You hear a creaking but can't figure out what it is.  The floor boards below you crumble and you fall to the floor below."
                print "Now your legs are broken and you have splinters all over the place.  You try to pull yourself out the door but don't see the clown walking up behind you with a chainsaw."
                print "At least it's over quickly?  I don't know, I got nothing else for you."
                return
        else:
            print "In you indecision, you walked into the pole separating the hall from the stairs JUST RIGHT and break your nose."
            print "While passed out from the pain, you drown in your own blood.  Sucks to be you."
            return
    else:
        print "You had literally one option and you blew it.  Did you eat paint chips as a child?"
        return

		
funHouse()