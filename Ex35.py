

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input(">")
    #if '0' in next or '1' in next:
    try:
        how_much = int(next)
        print how_much, type(how_much)
        if how_much < 50:
            print "Nice, you're not greedy, you win!"
            exit(0)
        else:
            dead("You greedy bastard!")
    except ValueError:
        print "Man, learn to type a number"


def bear_room():
    print """
    There is a bear here
    The bear has a bunch of honey
    The fat bear is in front of another door
    How are you going to move the bear?
    """
    bear_moved = False

    while True:
        next = raw_input(">")

        if next == "take honey":
            dead("The bear looks at you")
        elif next == "taunt bear" and not bear_moved:
            print "The bear moved"
            bear_moved = True
        else:
            print "I got no idea what that means"
            gold_room()

def dead(why):
    print why, "Good Job!"
    exit(0)


def start():
    print "You arein a dark room."
    print "There is a door to your right and left"
    print "Which one do you take?"

    next = raw_input(">")

    if next == 'left':
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()