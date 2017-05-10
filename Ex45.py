class Describe():
    def __init__(self, room_name, rooms):
        self.room = room_name
        self.a = rooms[room_name]
        if self.room == 'gold':
            print """
                You are in gold room
                To the left is bear room
                do you want to go?"""
            GoldRoom().gold_room()
        elif self.room == 'bear':
            print """
                You are in bear room
                To the right is gold room
                do you want to go?"""
            BearRoom().bear_room()
rooms = {
    "bear": "BearRoom()",
    "gold": "GoldRoom()",
}

class GoldRoom():

    @staticmethod
    def gold_room():
        print "This room is full of gold. How much do you take?"

        next = raw_input(">")
        # if '0' in next or '1' in next:
        try:
            how_much = int(next)
            # print how_much, type(how_much)
            if how_much < 50:
                print "Nice, you're not greedy, you win!"
                exit(0)
            else:
                print "You greedy bastard!"
                print "Go to bear room"
                BearRoom().bear_room()
        except ValueError:
            print "Man, learn to type a number"


class BearRoom():

    # def __init__(self, direction):
    #     if direction == "left":
    #         GoldRoom()
    #     elif direction == "right":
    #         MonkeyRoom()
    @staticmethod
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
                dead("I got no idea what that means")


def dead(why):
    print why, "Good Job!"
    exit(0)

print "These are the rooms", rooms.keys()
enter_room = raw_input("choose one from these")
print "you have chosen to enter", enter_room, "room"
#enter = Describe()
a = Describe(enter_room, rooms)

