
class Rooms(object):  # a parent of all rooms

    def __init__(self, name, message):
        self.message = message
        self.name = name


# Each rooms messages and descriptions
welcome = Rooms('Welcome', """You are about to be deployed what you better say good bye to
your love ones and get ready to go to war. You are going to have to make hard decistions and
hurt others but remember it is for god and country! Understand?
A. Yes B.You go to jail
""")

office = Rooms('Sgts office', """Welcome to the sgts office soldier what department would you like to
join? A. Army B.Navy C.Airforce""")

jail = Rooms('Jail dude', """Well you are kind of in Jail now. There is no point to continue.
well I mean if you like jail... Sure why not. This is your life now boy, this is your home. A. Sleep in jail B.Read a book in Jail C. Go use the rest
room in jail (in front of your jail mate.)""")

dead = Rooms('You have died in battle',
             """You are with your dead brothers who knows if your name will be remembered.""")

airforce = Rooms('Airforce Recruitment', """Alright so you are flying with us.
You will be starting trainging on piloting soon. We look forward to see you soon.
A. Go to Airforce training B.Nevermind go back to deparment choosing C. Do we get coffee?
""")

navy_deploy = Rooms(
'Navy Deploy', """Well It is time for war non the less.
Here at the navy any man is a trained man. You have been accepted and
now you deploy date is set congrats. A. To end """
)

airforce_base = Rooms(
'Airforce Base', """Airforce is happy to have you welcome aboard. The only thing is
you will have to have 12 months of pilot training so Congrats. Good Luck"""
)

push_up = Rooms(
'Push Ups', """Push ups are a essential portion of army life. Do a couple and you graduate basic.
Congrats you have finished army training. """
)

army_train = Rooms(
'Army Training', """We are on our way to army basic training. So now it is time to find your quarters
for the rest of these long weeks. You will probably quit anyway. (You end up quiting and are a failer)
Exit game."""
)

end = Rooms(
'Ending', """Congrats you have finished the game! Press end game. """
)

army = Rooms('Army Recruitment', """Wooo aaaah, welcome to the army maggot.
Basic training will start soon but give me 50 push ups first.
A. Get on the ground and complete 50 push ups B.Say, No I am not trained yet C. Nevermind go back to department choices""")

navy = Rooms('Navy Recruitment',
             """Howdy, how you doing? So you picked the navy what a fine choice. So we dont really have time to train you here is you uniform see you at base.
             A. Go to base to be deployed B. Nevermind go back to deparment choices  """)

navy_room = Rooms(
'Navy Room', """Okay"""
)

jail_read = Rooms(
    'Jail Reading', """You read 10 pages of the Dictionary it was pleasent.
What is next? Only 824 days to go

A. Sleep

B. Use the rest room

C. Ask to go back to the war draft

D. End
    """)

jail_sleep = Rooms(
    'Jail Sleep', """You only got 3 hours of sleep if only the guys would stop yelling.
What is next? Only 824 days to go

A. Read

B. Use the rest room

C.Ask to go back to the war draft

D. End
""")

jail_restroom = Rooms('Jail Rest Room', """You used the restroom it was not so nice. Your cell mate was watching.
What is next? Only 824 days to go

A. Sleep

B. Read

C. Ask to go back to the war draft

D. End
""")
