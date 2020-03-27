
class Rooms(object):  # a parent of all rooms

    def __init__(self, name, message):
        self.message = message
        self.name = name


welcome = Rooms('Welcome', """You are about to be deployed what you better say good bye to
your love ones and get ready to go to war. You are going to have to make hard decistions and
hurt others but remember it is for god and country! Understand?
A. Yes B.You go to jail (restart the game)
""")

office = Rooms('Sgts office', """Welcome to the sgts office soldier what department would you like to
join? A. Army B.Navy C.Airforce""")

jail = Rooms('Jail dude', """Well you are kind of in Jail now. There is no point to continue.
well I mean if you like jail... Sure why not. This is your life now boy, this is your home. A. Sleep in jail B.Read a book in Jail C. Go use the rest
room in jail (in front of your jail mate.)""")

dead = Rooms('You have died in battle',
             """You are with your dead brothers who knows if your name will be remembered.""")
