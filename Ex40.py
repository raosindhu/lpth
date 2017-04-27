# class Mystuff(object):
#     curname = 'static currname'
#     def __init__(self, name):
#         self.tangerine = "this is for testing"
#         curname = name
#         print 'local currname is ', curname
#     def apple(self):
#         print "I like apple"
#
# sindhu = Mystuff('sindhu')
# sindhu.apple()
# print sindhu.tangerine
# print sindhu.curname
#
# jayanth = Mystuff('jayanth')
# jayanth.apple()
# print jayanth.tangerine
# print jayanth.curname



class Mystuff(object):
    tangerine = "this is for testing"

    def __init__(self, name):
        self.curname = name
        print 'local currname is ', self.curname

    def apple(self):
        print "I like apple"


sindhu = Mystuff('sindhu')
sindhu.apple()
print sindhu.tangerine
print sindhu.curname

jayanth = Mystuff('jayanth')
jayanth.apple()
print jayanth.tangerine
print jayanth.curname


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["\nHappy bday to you",
                   "I dont want to get used",
                   "So i'll stop right there"])

bulls_on_parade = Song(["\nThey rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

