yes = "yes"
no = "no"
left = "left"
right = "right"

print ("You are wandering around in the thick woods alone when you get lost. Suddenly, a unicorn with a rainbow horn appears. It says hello.")
answer = input ("Do you respond to the unicorn's greeting?")
if answer == no:
    print ("You can not find your way out and are still here five days later. ")
if answer == yes:
    print ("The unicorn asks, Are you lost?")
    answer = input("Then the unicorn asks you, Where do you want to go? You can either go left or right.")
    if answer == left:
        print ("The unicorn guides you to a hot, barren desert and disappears. You are now alone.")
        print ("You meet two dinosaurs. The dinosaurs say hello.")
        answer = input("Do you respond to the dinosaurs' greetings?")
        if answer == no:
            print ("The dinosaurs are very hungry. You are eaten.")
        if answer == yes:
            print ("The dinosaurs like you and give you a ball as a present.")
        
    if answer == right:
        print ("The unicorn guides you to the moon and disappears. You are now alone.")
        print ("You meet two aliens. The aliens say hello.")
        answer = input("Do you respond to the aliens' greetings?")
        if answer == no:
            print ("The aliens left you on the moon and you can not return to earth.")
        if answer == yes:
            print ("The aliens like you and give you a star as a present")
