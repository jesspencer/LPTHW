class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

#putting lyrics in a variable
killing_me_softly_lyrics = song(["I heard you sing a good song",
                            "I heard you had a style"])
favorite_song = killing_me_softly_lyrics

happy_bday = song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = song(["They rally around the family",
                        "With pockets full of shells"])

ring_around_the_rosie = song(["Ring around rosie",
                                "With pockets full of posie",
                                "Ashes Ashes",
                                "They all fall down"])

for_us_by_us = song(["I hope my son will bang this song so loud",
                        "That he almost makes his walls fall down",
                        "Cause his momma wants to make him proud"])

dear_momma = song(["No love from my father",
                    "Because that the fucker wasn't there"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
ring_around_the_rosie.sing_me_a_song()
for_us_by_us.sing_me_a_song()
dear_momma.sing_me_a_song()
#study drill #2
sing_me_a_song(favorite_song)

'''
Study Drills
1. Write some more songs using this, and make sure you understand that you're passing a list of strings as the lyrics.
done
2. Put the lyrics in a separt variable, then pass that variable to the class to use instead.
killing_me_softly_lyrics and favorite_song are my answer to this one
3. See if you can hack on this and make it do more things. DOn't worry if you have no idea how,
just give it a try , see what happens. Break it, trash it, you can't hurt itself.
done; error  nameError "sing_me_a_song is not defined"
4. Search online for "object-oriented programming" and try to overflow your brain with what you read. Don't worry if
it makes abs no sense to you. Half of that stuff makes no sense to me either.
'''
