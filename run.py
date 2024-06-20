from pyfiglet import figlet_format
import time
import random

# Player Charater Option 1
lee_kennedy = {
    "Name": "Lee",
    "HP": 120,
    "Attack Power": random.randint(5, 10),
    "Weapon": "Unarmed",
    "Skill": ["lockpick"],
    "Inventory": ["flashlight"],
    "Insight": []
}

# Player Charater Option 2
claire_greenfield = {
    "Name": "Claire",
    "HP": 150,
    "Attack Power": random.randint(15, 20),
    "Weapon": "Unarmed",
    "Skill": ["hack"],
    "Inventory": ["flashlight"],
    "Insight": []
}

"""
'God Mode' has been designed purely for play testing, allowing swift
progression through the game to improve the efficiency of manually testing
specific features. As such, 'God Mode' is not compatible with all game
features and should not be used as an overall playthrough test. Known
incompatiblities arise from the 'let there be light' command, which can
be used to turn on the power from the foyer at any time. This conflicts
with features such as the first time you enter the bar, where the game
presumes the power is still off due to it being narratively impossible
to have turned the power on at that point using either of the normal
player characters.
"""
god_mode = {
    "Name": "Super Shaggy",
    "HP": 1000,
    "Attack Power": 1000,
    "Weapon": "Super Punch",
    "Skill": ["hack", "lockpick"],
    "Inventory": ["flashlight", "Cipher", "Necronomicon"],
    "Insight": ["Raven's Rest Owner Name",
    "Whateley's Room Location",
    "Chris' Room Location",
    "Hidden Safe Location",
    "Spell Reversal"]
}

# Populated once Player Character selected
player_card = {
    "Name": "",
    "HP": 100,
    "Attack Power": 10,
    "Weapon": "Unarmed",
    "Skill": [],
    "Inventory": [],
    "Insight": []
}

# Continuity Variables & Lists

# Determines if the Hotel has power
power = False

# Determines if the Player's flashlight is on
flashlight = False

# Determines Whateley's status
whateley_status = True

# List of rooms Player has checked
checked_rooms = []

# List of items Player has collected
looted_items = []

# List of all slain enemies
slain_enemies = []

# Enemies
enemy = {
    "ID": None,
    "Name": None,
    "HP": 1,
    "Attack Power": 1
}

cultist_bar = {
    "ID": "Cultist (Bar)",
    "Name": "Mutilated Cultist",
    "HP": 30,
    "Attack Power": random.randint(10, 20)
}

cultist_library = {
    "ID": "Cultist (Lib)",
    "Name": "Mutilated Cultist",
    "HP": 50,
    "Attack Power": random.randint(10, 20)
}

cultist_chris_room = {
    "ID": "Cultist (CR)",
    "Name": "Mutilated Cultist",
    "HP": 40,
    "Attack Power": random.randint(10, 25)
}

mr_whateley = {
    "ID": "Whateley",
    "Name": "Whateley",
    "HP": 100,
    "Attack Power": random.randint(20, 35)
}

chris = {
    "ID": "Chris",
    "Name": "Chris",
    "HP": 110,
    "Attack Power": random.randint(20, 40)
}

# Help variable, for use in game
help = (
"\nHere are a few common commands you will use:\n"

"\n(Not all of these can be used all of the time - for example, you can't"
" move \nNorth if there's nowhere North to go!)\n"

"\nEnter 'exit' to quit to main menu."
"\nEnter 'pc' to view Player Card."
"\nEnter 'n', 'e', 's', 'w', to move north, east, South and west."
"\nEnter 'l' to look around."
"\nEnter 'i' followed by an OBJECT to interact with that OBJECT."
"\nEnter 'heal' to use a First Aid Kit."
"\nEnter 'atk' to attack."
"\nEnter 'flee' to escape a fight in a random direction.\n"
"\nHINT: The 'l' command is great if you need a clue as to what you can do in"
" the \nroom you're in!\n")

generic_error = ("\nYou can't do that... Use the 'help' command if you're "
"stuck, or 'l' to look around for clues.\n")

# Global functions for repeated actions


def fa_kit_loot():
    """
    Adds First Aid Kit to player inventory
    """
    player_card['Inventory'].append("First Aid Kit")
    type_text("\nYou rummage through the First Aid Kit and take some"
    " supplies.\n")

    type_text("\n'First Aid Kit' added to Inventory.\n")
    return


def heal():
    """
    Uses a First Aid Kit to heal 40 HP
    """
    if "First Aid Kit" in player_card['Inventory']:
        player_card['HP'] += 40
        player_card['Inventory'].remove("First Aid Kit")

        type_text("\nYou use a First Aid Kit and heal 40 HP.\n"

        f"\nYour health is now {player_card['HP']}.\n")
        return

    else:
        type_text("\nYou don't have any First Aid Kits!\n")


def atk():
    """
    Function for Player to attack Enemy
    """
    # Vary Enemy Attack Power per Attack
    if enemy["ID"] == "Cultist (Bar)":
        enemy['Attack Power'] = random.randint(10, 20)

    elif enemy["ID"] == "Cultist (Lib)":
        enemy['Attack Power'] = random.randint(15, 25)

    elif enemy["ID"] == "Cultist (Chris Room)":
        enemy['Attack Power'] = random.randint(20, 30)

    elif enemy["ID"] == "Whateley":
        enemy['Attack Power'] = random.randint(25, 35)

    elif enemy["ID"] == "Chris":
        enemy['Attack Power'] = random.randint(35, 45)

    # Vary Player Attack Power per Attack
    if player_card['Weapon'] == "Unarmed":

        if player_card['Name'] == "Claire":
            player_card['Attack Power'] = random.randint(10, 20)

        else:
            player_card['Attack Power'] = random.randint(1, 10)

    elif player_card['Weapon'] == "Bloody Knife":
        player_card['Attack Power'] = random.randint(10, 20)

    elif player_card['Weapon'] == "Pitchfork":
        player_card['Attack Power'] = random.randint(20, 35)

    elif player_card['Weapon'] == "Handgun":
        player_card['Attack Power'] = random.randint(35, 40)

    elif player_card['Weapon'] == "Shotgun":
        player_card['Attack Power'] = random.randint(30, 50)

    elif player_card['Weapon'] == "Super Punch":
        player_card['Attack Power'] = 1000

    if enemy["ID"] in slain_enemies:
        type_text(f"{enemy['Name']} is already dead!")

    else:
        enemy['HP'] = enemy['HP'] - player_card['Attack Power']
        type_text(f"\nYou hit {enemy['Name']} for"
        f" {player_card['Attack Power']} damage.\n")

        if enemy['HP'] <= 0:
            type_text(f"\nWith a final rasping breath, {enemy['Name']} drops"
            " to the floor, his body \ncold and still.\n")

            slain_enemies.append(enemy["ID"])
            return
        else:
            player_card['HP'] = player_card['HP'] - enemy['Attack Power']
            type_text(f"\n{enemy['Name']} hit you for"
            f" {enemy['Attack Power']} damage.\n")

            if player_card['HP'] <= 0:
                game_over()
            else:
                type_text(f"\nYou have {player_card['HP']} remaining HP.\n"
                "\nAttack again or flee?\n")

    return


# End Game Functions


def reset_game_values():
    """
    Resets game values to prepare for new game data.
    """
    global checked_rooms
    global slain_enemies
    global looted_items

    checked_rooms = []
    slain_enemies = []
    looted_items = []
    return


def game_over():
    type_text("\nYou let out a grunt as you drop to one knee. Bloodied and"
    " beaten, you struggle \nto focus your vision.\n"

    "\n'I'm sorry, Chris...', you mutter, before collapsing on the floor.\n")
    print(figlet_format("GAME OVER\n", justify="center"))

    while True:

        game_over_choice = input("\nEnter 'ng' to start a new game from the"
        " Character Selection Menu.\n"

        "\nEnter 'exit' to return to the Main Menu.\n")

        if game_over_choice.lower() == "ng":
            reset_game_values()
            character_selection()
            return

        elif game_over_choice.lower() == "exit":
            reset_game_values()
            main_menu()
            return

        else:
            type_text("\nThat's not an option right now...\n")


def type_text(text):
    """
    Prints text one character at a time to create a 'typing' animation.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.001, 0.05))


def main_menu():
    """
    The menu the Player is presented with when opening the app.
    """
    raven_image = r"""
                      ⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡟⠋⢻⣷⣄⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣷⣿⣿⣿⣿⣿⣶⣾⣿⣿⠿⠿⠿⠶⠄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⠟⠻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣆⣤⠿⢶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    title = r"""
    ______  ___  _   _ _____ _   _ _ _____
    | ___ \/ _ \| | | |  ___| \ | ( )  ___|
    | |_/ / /_\ \ | | | |__ |  \| |/\ `--.
    |    /|  _  | | | |  __|| . ` |  `--. \
    | |\ \| | | \ \_/ / |___| |\  | /\__/ /
    \_| \_\_| |_/\___/\____/\_| \_/ \____/

    ______ _____ _____ _____
    | ___ \  ___/  ___|_   _|
    | |_/ / |__ \ `--.  | |
    |    /|  __| `--. \ | |
    | |\ \| |___/\__/ / | |
    \_| \_\____/\____/  \_/

    """
    spacer = ' ' * 1

    for a, b in zip(raven_image.split('\n'), title.split('\n')):
        print(f"{a}{spacer}{b}")

    type_text("\nWelcome to Raven's Rest, a text-based adventure game!"
    "\nI'm Poe, your digital Game Master (or 'GM' for short)."
    "\nType out what you want to do, and I'll try my best to make it happen!"
    "\nIf this is your first time playing, please be sure to read the rules"
    " before \nyou start.\n"

    "\nTo read how to play, enter 'h2p'.\n"

    "\nTo start the game, enter 'play'.\n")

    while True:

        main_menu_choice = input()

        if main_menu_choice.lower() == "play":
            character_selection()
            break

        elif main_menu_choice.lower() == "h2p":
            how_to_play()
            break

        else:
            type_text("\nI don't know that one..."
            "Enter 'play' to start the game or 'h2p' to read how to play.\n")


def how_to_play():
    """
    Section to explain the rules to the Player and instructions on how to play
    the game.
    """
    type_text("\nRaven's Rest is a textbased adventure game. You control your"
    " character by \nentering commands in the terminal. The goal is to"
    " navigate the Raven's Rest \nHotel and find your brother, completing"
    " puzzles and defeating enemies as you go.\n"

    "\nHere are the rules:\n")

    print(figlet_format("How to Play\n", justify="center"))

    type_text("\n1. Mind your manners! Don't interrupt your GM. If you type"
    " whilst Poe is \ntyping, you might cause an error, preventing your next"
    " command from being \nrecognised. Let him finish before typing"
    " anything.\n"

    "\n2. If you type something that isn't a command, you'll be prompted to"
    " try again.\n"

    "\n3. You can quit to the main menu at any time by using the 'exit'"
    " command. But \nbe aware, you'll lose all progress and there's no way"
    " to reload a previous \ngame.\n"

    "\n4. If you get stuck, type 'help' to see a list of commonly available"
    " commands \nyou can try.\n"

    "\n5. Once you start the game, you will have to select a character. Take"
    " note \nof your character's bio, as their individual skills and"
    " experiences might be \nuseful later on.\n"

    "\n6. You can bring up your character's 'Player Card' at any time by"
    " using the \n'pc' command. Here you'll see your character's current"
    " stats and any items in \nyour inventory.\n"

    "\n7. The Raven's Rest can be a dangerous place. Your 'Attack Power' stat"
    "\ndetermines how much damage you can do in a single attack. Be sure to"
    " pick up \nany weapons you might find to help you deal more damage.\n"

    "\n8. Keep an eye on your HP. If it drops to zero, that's game over."
    " Healing \nitems can be found and used to keep you going.\n")

    type_text(help)

    type_text("\nThis list is not exhaustive. It just gives examples of"
    " common commands you'll \nuse. Remember to use the 'help' command if you"
    " get stuck, or consult your \nPlayer Card by using the 'pc' command to"
    " see if your character has a skill or \nitem that might be useful.\n"

    "\nGood luck, and have fun!\n")

    while True:

        leave_h2p = input("\nType 'play' to start the game or 'back' to"
        " return to the main menu.\n")

        if leave_h2p.lower() == "back":
            main_menu()
            break

        elif leave_h2p.lower() == "play":
            character_selection()
            break

        else:
            type_text("\nI don't know that one...\n")


def character_selection():
    """
    Section where the Player must select their Player Character.
    """
    character_selection_text = ("\nChoose your character:\n"
    "\nLee Kennedy"
    "\nAge: 36"
    "\nOccupation: Locksmith"
    "\nHobby: Bird Watching\n"

    "\nClaire Greenfield"
    "\nAge: 29"
    "\nOccupation: Programmer"
    "\nHobby: Kickboxing\n")
    type_text(character_selection_text)

    while True:
        character_choice = input("\nType 'l' for Lee or 'c' for Claire:\n")

        if character_choice.lower() == "l":
            player_card.update(lee_kennedy)
            type_text("\nYou have selected Lee Kennedy.\n")
            start_game()
            break

        elif character_choice.lower() == "c":
            player_card.update(claire_greenfield)
            type_text("\nYou have selected Claire Greenfield.\n")
            start_game()
            break

        elif character_choice.lower() == "god mode":
            player_card.update(god_mode)
            type_text("You have selected... Super Shaggy? That can't be"
            " right.")
            start_game()
            break

        else:
            type_text("\nI don't know that one...\n")


def start_game():

    while True:

        start_choice = input("\nEnter 'skip' to skip the intro and jump"
        " straight to Raven's Rest. Otherwise, \nenter 'begin' to start the"
        " game.\n")

        if start_choice.lower() == "skip":
            foyer()
            break

        elif start_choice.lower() == "begin":
            intro_a()
            break

        else:
            start_choice_error = ("\nI don't know that one...\n")


def intro_a():
    """
    Part A of the games' intro, which also acts as a tutorial.
    """
    type_text("\n9 Nov 1981\n"

    "\nDunwich, England\n"

    "\nYou wake with a jolt to the sound of knuckles rapping on glass. Sat in"
    " a \ncarriage being drawn by two horses - a far cry from the black cabs"
    " you're used \nto in London - you peer out of the window. Presumably the"
    " carriage driver was \nletting you know that you're approaching your"
    " destination, but there's no way \nof knowing that by looking outside."
    " Nights never get this dark in the city, \nbut here in Dunwich, you may"
    " as well be staring into a pot of ink. Add to \nthat the heavy rain"
    " beating against the glass, and trying to make out anything \nbeyond the"
    " dimly light interior of the carriage was truly an exercise in"
    "\nfutility.\n"

    "\nYou remove a PHOTOGRAPH from your jacket pocket. It's a picture of"
    " your \nbrother, Chris. The last time he was seen or heard from. He's"
    " grinning at the \ncamera and giving a cheery thumbs up. Behind him,"
    " lurking like a shadow, lies \na dark building. You can just about make"
    " out a sign that reads, 'Raven's Rest'.\n")

    while True:
        intro_a_choice = input("\nEnter 'i photograph' to inspect the"
        " photograph.\n")

        if intro_a_choice.lower() == "i photograph":
            intro_b()
            break

        elif intro_a_choice.lower() == "help":
            print(help)

        elif intro_a_choice.lower() == "exit":
            main_menu()
            break

        else:
            type_text("\nYou can't do that now.\n")


def intro_b():
    """
    Part B of the games' intro, which continues to act as a tutorial.
    """
    type_text("\nThere's a message on the back:\n"
    f"\n{player_card['Name']},\n"

    "\nThink I've finally made some headway with the article… Currently"
    " visiting a \nchap in Dunwich who apparently knew one of the students"
    " that went missing - \nhis son in fact! I'm staying at an old hotel,"
    " the Raven's Rest. Feels like \nit's been pulled straight out of the"
    " 1800s - but then again, so does the rest \nof this town. Anyways, hope"
    " you're well. Give mum & dad my love. Hopefully the \nnext time you read"
    " my words, it'll be on the front page of the newspaper! Got a \nfeeling"
    " I'm onto something big here.\n"

    "\nYours,\n"

    "\nChris\n")

    while True:
        intro_b_choice = input("\nEnter 'i photograph' to store the"
        " photograph in your inventory.\n")

        if intro_b_choice.lower() == "i photograph":
            player_card['Inventory'].append("photograph")
            intro_c()
            break

        elif intro_b_choice.lower() == "help":
            print(help)

        elif intro_b_choice.lower() == "exit":
            main_menu()
            break

        else:
            type_text("\nYou can't do that now.\n")


def intro_c():
    """
    Part C of the games' intro, which continues to act as a tutorial.
    """
    type_text("\nYou slide the photograph back into your pocket. A loud"
    " crunch comes from the \nwheels as the carriage veers off the road and"
    " onto a gravel track. Bouncing \nuncomfortably on the bench for a minute"
    " or so, you're relieved when the horses \ncome to a halt. A thin grate"
    " on the driver's side of the carriage slides open.\n"

    "\n'Make it quick,' the carriage driver says. 'The horses are spooked.'\n"

    "\nYou swing open the door and step into the stormy night, tossing the"
    " driver's \nfare into a cup on the way out. You're immediately bitten by"
    " the cold and \nfumble with your collar to turn it against the wind and"
    " rain.\n"

    "\n'What's got them spooked?' you call out, fighting to be heard over the"
    " weather.\n"

    "\n'You'll find out soon enough, I'm sure.' He called back. With that, he"
    " spurs \nhis horses and sets off. It seems to you as though it wasn't"
    " just the horses \nthat were spooked. As the carriage draws away with"
    " its lantern, so does your \nonly source of light. You're quickly"
    " plummeted into pitch darkness.\n"

    "\nEnter 'pc' to open your Player Card and view your inventory.\n")

    while True:

        intro_c_choice = input()
        global flashlight

        if intro_c_choice.lower() == "pc":
            print(player_card)
            type_text("\nA flashlight! That'll help. Enter 'i"
            " flashlight'.\n")

        elif intro_c_choice.lower() == "i flashlight":

            if flashlight is True:
                type_text("\nYou've already swithced your flashlight on. Try"
                " entering 'l' to look around.\n")

            else:
                type_text("\nYou pull your flashlight from your pocket and"
                " switch it on. A beam of bright \nlight bursts forth,"
                " slicing through the dark like a butcher's knife.\n"
                "\nEnter 'l' to look around.\n")
                flashlight = True

        elif intro_c_choice.lower() == "l":

            if flashlight is True:
                type_text("\nYou're stood in a small, wooded enclosure, just"
                " off the gravel track. A path \nthrough the trees to the"
                " North appears to be your only choice forward.\n"
                "\nEnter 'n' to walk northwards.\n")
            else:
                type_text("\n'I can't see a thing!'\n")

        elif intro_c_choice.lower() == "n":

            if flashlight is True:
                intro_d()
                break

            else:
                type_text("\n'I can't see where I'm going!'\n")

        elif intro_c_choice.lower() == "help":
            print(help)

        elif intro_c_choice.lower() == "exit":
            main_menu()
            break

        else:
            if flashlight is True:
                type_text("\nYou can't do that now.\n")


def intro_d():
    """
    Part D of the games' intro, which continues to act as a tutorial.
    """
    type_text("\nNearly completely hidden amongst the darkness, the black"
    " building seems to \nappear almost out of nowhere. You shine your"
    " flashlight at the looming \nstructure, but the beam is almost"
    " immediately choked by the unrelenting \nweather, preventing you from"
    " seeing even above the first storey. You get an \nuneasy feeling as your"
    " eyes follow the slate grey walls, receding into the \ndarkness above."
    " As though the hotel seems much larger than it really is.\n"

    "\nEventually you come across a long wooden porch that leads you to the"
    " hotel \nentrance. Double black DOORS set against white wooden slats. In"
    " the gloom of \nnight, it looks like the gaping maw of a beast. 'Raven's"
    " Rest', is scrawled in \nblack lettering above the DOORS.\n")

    while True:

        intro_d_choice = input("\nEnter 'i doors' to open the DOORS and enter"
        " the Raven's Rest.\n")

        if intro_d_choice.lower() == "i doors":
            type_text("\nWith a shrill creak, the doors yawn open...\n")
            foyer()
            break

        elif intro_d_choice.lower() == "l":
            type_text("The entrance to the Raven's Rest stands before you."
            " Nowhere to go but forward.")

        elif intro_d_choice.lower() == "help":
            print(help)

        elif intro_d_choice.lower() == "pc":
            print(player_card)

        elif intro_d_choice.lower() == "exit":
            main_menu()
            break

        else:
            type_text("\nYou can't do that now.\n")


def foyer():
    """
    Hotel Foyer - the first room the Player enters.
    """
    global power

    foyer_text_initial = ("\nYou step into a wide, empty Foyer. The beam of"
    " your flashlight barely \npenetrates the surrounding shadows as you pan"
    " across the room. Ahead of you \nbeneath the gloomy red glow of an"
    " emergency lamp, you see the reception DESK.\n"

    "\nOn both the East and West sides of the room are doors leading out of"
    " the \nFoyer.\n")

    foyer_text_return = ("\nYou step again into the wide, empty Foyer.\n")

    if "Foyer" in checked_rooms:
        type_text(foyer_text_return)

    else:
        type_text(foyer_text_initial)
        checked_rooms.append("Foyer")

    foyer_look = ("\nYou look around the Foyer.\n"
    "\nYou see the reception DESK ahead of you.\n"
    "\nA door to the East ('e') with a sign that reads, 'East Wing,"
    " Maintenance and \nBar'.\n"
    "\nA door to the West ('w') with a sign that reads, 'West Wing,"
    " Basement Access and \nLibrary'.\n"
    "\nBehind you, to the South ('s'), is the Hotel entrance.\n")

    desk_inspect = ("\nYou approach the desk for a closer look. A COMPUTER"
    " and a BELL sit on the desk. \nBehind the desk is a DOOR with a sign"
    " that reads, 'Staff Only'.\n")


    def foyer_computer_use():
        if power is False:
            type_text("\nThe power is still out. Maybe you can find a way to"
            " turn it back on...\n")

        else:

            if "hack" in player_card['Skill']:
                foyer_computer()

            else:
                type_text("\nThe computer is locked.\n")


    def foyer_door_use():
        if "lockpick" in player_card['Skill']:
            type_text("\nThe door is locked, but you manage to pick it.\n")
            staff_only_cupboard()

        else:
            type_text("\nThe door is locked.\n")

    while True:

        foyer_choice = input("\nWhat do you do? (If you're stuck, try using"
        " the 'l' command to look around.)\n")

        if foyer_choice.lower() == "l":
            type_text(foyer_look)

        elif foyer_choice.lower() == "help":
            print(help)

        elif foyer_choice.lower() == "pc":
            print(player_card)

        elif foyer_choice.lower() == "exit":
            main_menu()
            break

        elif foyer_choice.lower() == "heal":
            heal()

        elif foyer_choice.lower() == "e":
            type_text("\nYou exit out of the East door.\n")
            east_wing()
            break

        elif foyer_choice.lower() == "w":
            type_text("\nYou exit out of the West door.\n")
            west_wing()
            break

        elif foyer_choice.lower() == "s":
            type_text("\nI'm not leaving until I've found Chris.\n")

        elif foyer_choice.lower() == "i desk":
            type_text(desk_inspect)

        elif foyer_choice.lower() == "i computer":
            foyer_computer_use()

        elif foyer_choice.lower() == "i door":
            foyer_door_use()

        elif foyer_choice.lower() == "i bell":
            type_text("\nYou ring the bell. A high-pitched 'ding' echoes"
            " throughout the empty room for \na moment, before silence creeps"
            " back into the foyer. No one comes.\n")

        elif foyer_choice.lower() == "let there be light":

            if player_card['Name'] == "Super Shaggy":
                power = True
                type_text("\nPower is miraculously restored to the Hotel...\n"

                "\nWait, how did you do that?\n")

        else:
            type_text(generic_error)


def foyer_computer():
    """
    Foyer Computer - Options
    """
    type_text("\nThe computer is locked, but you manage to hack it.\n")

    while True:
        foyer_computer_choice = input("\nEnter 'r' to see reservation"
        " list.\n"

        "\nEnter 'm' to see saved messages.\n"

        "\nEnter 'back' to log off computer.\n")

        if foyer_computer_choice.lower() == "r":

            if "Raven's Rest Owner Name" in player_card['Insight']:
                type_text("\nYou flick through some files and discover Chris'"
                " room number, located in the \nWest Wing. You also notice"
                " that Mr Whateley, the owner, has a room adjacent to \nthe"
                " Library.\n")

                if "Whateley's Room Location" not in player_card['Insight']:
                    player_card['Insight'].append("Whateley's Room Location")
                    type_text("\n'Whateley's Room Location' added to"
                    " Insight.\n")

                if "Chris' Room Location" not in player_card['Insight']:
                    player_card['Insight'].append("Chris' Room Location")
                    type_text("\n'Chris' Room Location' added to Insight.\n")

            else:

                type_text("\nYou flick through some files and discover Chris'"
                " room number, located in the \nWest Wing.\n")

                if "Chris' Room Location" not in player_card['Insight']:
                    player_card['Insight'].append("Chris' Room Location")
                    type_text("\n'Chris' Room Location' added to Insight.\n")

        elif foyer_computer_choice.lower() == "m":
            type_text("\nYou find a message that reads:\n"

            "\nDear employees,\n"

            "\nI understand there has been some confusion about the new"
            " locking systems I've \nhad installed. Whilst I appreciate that"
            " some of you may find them \n'impractical', or perhaps even"
            " 'excessive', may I remind you that we have a \ncertain"
            " aesthetic to maintain here in the Raven's Rest. To that end,"
            " please \nremember:\n"

            "\nThe Raven's Beak Key opens the Maintenance Room.\n"

            "\nThe Raven's Wing Key opens the service lift.\n"

            "\nThe Raven's Foot key opens the Cellar.\n"

            "\nI needn't remind you that the Cellar is strictly out of bounds"
            " to ALL \nemployees. If you require something from the Cellar,"
            " you are to inform me and I \nshall fetch it for you.\n"

            "\nI hope this clears things up. Now please stop asking if we can"
            " go back to using \nthe old locks.\n"

            "\n - Mr Whateley\n")

        elif foyer_computer_choice.lower() == "back":
            type_text("\nYou log off the computer.\n")
            foyer()
            break

        elif foyer_computer_choice.lower() == "help":
            print(help)

        elif foyer_computer_choice.lower() == "pc":
            print(player_card)

        elif foyer_computer_choice.lower() == "exit":
            main_menu()
            break

        else:
            type_text(generic_error)


def staff_only_cupboard():
    """
    Staff Only Cupboard - Game Location.
    """
    staff_only_cupboard_initial = ("\nThe door leads into a small"
    " cupboard space. Whilst inspecting, the beam of your \nflashlight passes"
    " over something slumped on the floor. Your heart sinks. It's a \ndead"
    " BODY. A bloody KNIFE protruding from the side of it's neck.\n")

    staff_only_cupboard_return = ("\nYou enter the cupboard, trying your"
    " best not to look at the dead BODY.\n")

    if "Staff Only Cupboard" in checked_rooms:
        type_text(staff_only_cupboard_return)

    else:
        type_text(staff_only_cupboard_initial)
        checked_rooms.append("Staff Only Cupboard")

    while True:
        staff_only_cupboard_choice = input("\nWhat do you do? (If you're"
        " stuck, try using the 'l' command to look around.)\n")

        if staff_only_cupboard_choice.lower() == "l":
            if "Bloody Knife" in looted_items:
                type_text("\nA dead BODY lies slumped on the floor.\n"

                "\nA washing machine sits in the corner with a basket of"
                " laundry on top. A small NOTE \nlies amongst the clothes.\n"

                "\nThe foyer is to your South ('s').\n")

            else:
                type_text("\nYou take a moment to collect yourself, then look"
                " around the cupboard.\n"

                "\nA bloody KNIFE sticks out of the dead BODY's neck.\n"

                "\nA washing machine sits in the corner with a basket of"
                " laundry on top. A small NOTE \nlies amongst the clothes.\n"

                "\nThe foyer is behind you, to the South \n('s').\n")

        elif staff_only_cupboard_choice.lower() == "help":
            print(help)

        elif staff_only_cupboard_choice.lower() == "pc":
            print(player_card)

        elif staff_only_cupboard_choice.lower() == "exit":
            main_menu()
            break

        elif staff_only_cupboard_choice.lower() == "heal":
            heal()

        elif staff_only_cupboard_choice.lower() == "i body":
            type_text("\nYou take a closer look at the body. It's a young"
            " woman, probably in her 20s. She \nlooks to be one of the staff"
            " members of the Hotel. Her name tag reads, 'Jill'.\n")

        elif staff_only_cupboard_choice.lower() == "i knife":

            if "Bloody Knife" in looted_items:
                type_text("\nYou've already taken the Bloody Knife.\n")

            elif "Handgun" in looted_items:
                type_text("\nI think I'll stick with this hangun...\n")

            elif "Shotgun" in looted_items:
                type_text("\nI think I'll stick with this shotgun...\n")

            else:
                type_text("\nYou crouch beside the BODY and grab the blade by"
                " its handle. With a sickening \nsquelch, you slide the knife"
                " from their neck. Dark crimson pools around your \nfeet.\n"

                "\n'Bloody Knife' is now equipped.\n")
                looted_items.append("Bloody Knife")
                player_card['Weapon'] = "Bloody Knife"
                player_card['Attack Power'] = "10 - 20"

        elif staff_only_cupboard_choice.lower() == "i note":
            type_text("\nYou pick up the note from the laundry basket and"
            " give it a read.\n"

            "\n'Barry,\n"

            "\nI don't know why the boss has so many black robes in his"
            " laundry. Nor do I \nreally care. Just deliver the basket to his"
            " room (the one by the library) and \nstop asking pointless"
            " questions. He's little on patience and big on temper, so \ndo"
            " yourself a favour and don't pry where your nose ain't"
            " welcome.\n"

            "\nP.S.\n"

            "\nThose robes you're so interested were covered in red wine by"
            " the looks of it, so \ndon't skimp on the stain remover.'\n")

            if "Whateley's Room Location" not in player_card['Insight']:
                player_card['Insight'].append("Whateley's Room Location")
                type_text("\n'Whateley's Room Location' added to"
                " Insight.\n")

        elif staff_only_cupboard_choice.lower() == "s":
            type_text("\nYou exit to the south, returning to the Foyer.\n")
            foyer()
            return

        else:
            type_text(generic_error)


def east_wing():
    """
    East Wing - Game Location.
    """
    east_wing_initial = ("\nYou step into the East Wing. Dark wooden doors"
    " adorned with silver room numbers \nrun along both sides of the"
    " corridor. There is no trace of any patron or \nemployee. As you creep"
    " through the silent passage, you notice a Supplies \nCupboard to the"
    " South ('s'). Further East ('e') appears to be a Maintenance \nRoom."
    " To the north ('n') are a set of double doors, leading to the Bar. To"
    " the \nwest ('w') is the Foyer.\n")

    east_wing_return = ("\nYou step into the East Wing.\n")

    if "East Wing" in checked_rooms:
        type_text(east_wing_return)

    else:
        type_text(east_wing_initial)
        checked_rooms.append("East Wing")

    while True:
        east_wing_choice = input("\nWhat do you do? (If you're stuck, try"
        " using the 'l' command to look around.)\n")

        if east_wing_choice.lower() == "l":
            type_text("\nLooking around the East Wing corridor, you spot a"
            " cleaning trolley by one of the \nrooms. A NEWSPAPER is sticking"
            " out of the trash.\n"

            "\nTo the North ('n') is a set of double doors leading"
            " to the Bar.\n"

            "\nTo the East ('e') is the Maintenance Room.\n"

            "\nTo the South ('s') is a Supplies Cupboard.\n"

            "\nTo the West ('w') is the Foyer.\n")

        elif east_wing_choice.lower() == "help":
            print(help)

        elif east_wing_choice.lower() == "pc":
            print(player_card)

        elif east_wing_choice.lower() == "exit":
            main_menu()
            break

        elif east_wing_choice.lower() == "heal":
            heal()

        elif east_wing_choice.lower() == "i newspaper":
            type_text("You take a closer look at the newspaper. 'The Dunwich"
            " Daily'. The headline \nreads, 'BODY SNATCHER STRIKES AGAIN?"
            " FOURTH MISSING PERSON REPORTED THIS YEAR'. \nYou flick through"
            " the paper, pausing when your eye is caught by a picture of"
            "\nthe Raven's Rest. The caption reads 'One year since the"
            " Raven's Rest came under \nnew management. New owner Mr Whateley"
            " says he has 'big plans' for the hotel'.\n")

            if "Raven's Rest Owner Name" not in player_card['Insight']:
                player_card['Insight'].append("Raven's Rest Owner Name")
                type_text("\n'Raven's Rest Owner Name' added to Insight.\n")

        elif east_wing_choice.lower() == "n":
            type_text("\nYou pass through the double doors into the Bar.\n")
            bar()
            break

        elif east_wing_choice.lower() == "e":

            if "Raven's Beak Key" in player_card['Inventory']:
                type_text("\nYou use the Raven's Beak Key to access the"
                " Maintenance Room.\n")
                maintenance_room()
                break

            else:

                if "lockpick" in player_card['Skill']:
                    type_text("\nThis door is locked with a strange"
                    " mechanism. It looks like the key would need \nto be"
                    " beak shaped...\n")
                else:
                    type_text("This door is locked.")

        elif east_wing_choice.lower() == "s":
            type_text("\nYou enter the Supplies Cupboard to the south.\n")
            supplies_cupboard()
            break

        elif east_wing_choice.lower() == "w":
            type_text("\nYou use the western door to the Foyer.\n")
            foyer()
            break

        else:
            type_text(generic_error)


def west_wing():
    """
    West Wing - Game Location.
    """
    if "Chris' Room Location" in player_card['Insight']:
        west_wing_initial = ("\nYou step into the West Wing. Dark wooden"
        " doors adorned with silver room numbers \nrun along both sides of"
        " the corridor. Immediately you notice a BODY heaped on \nthe floor"
        " just a few metres from you. You rush over to them and drop \nto"
        " one knee.\n"

        "\n'Are you OK?' you whisper, placing your hands on their shoulders."
        " You get your \nanswer as you roll them over and see their face."
        " Jumping back and stifling a \nscream, you drop the BODY to the"
        " floor. The bottom half of their face had been \ncompletely crushed"
        " and their jaw partly torn off. You stand there dumbstruck \nfor a"
        " moment before collecting yourself and looking around.\n"

        "\nTo the North ('n'), a set of double doors lead to the Hotel's"
        " Library.\n"

        "\nTo the East ('e') is the Foyer.\n"

        "\nSouth ('s') of you, you spot Chris' Room.\n"

        "\nOn the Western ('w') side of the corridor, you see a service lift"
        " with a sign next to it that reads 'Basement Access'.\n")

    else:

        west_wing_initial = ("\nYou step into the West Wing. Dark wooden doors"
        " adorned with silver room numbers \nrun along both sides of the"
        " corridor. Immediately you notice a BODY heaped on \nthe floor just a"
        " few metres from you. You rush over to them and drop \nto one"
        " knee.\n"

        "\n'Are you OK?' you whisper, placing your hands on their shoulders."
        " You get your \nanswer as you roll them over and see their face."
        " Jumping back and stifling a \nscream, you drop the BODY to the"
        " floor. The bottom half of their face had been \ncompletely crushed"
        " and their jaw partly torn off. You stand there dumbstruck \nfor a"
        " moment before collecting yourself and looking around.\n"

        "\nTo the North ('n'), a set of double doors lead to the Hotel's"
        " Library.\n"

        "\nTo the East ('e') is the Foyer.\n"

        "\nOn the Western ('w') side of the corridor, you see a service lift"
        " with a sign \nnext to it that reads 'Basement Access'.\n")

    west_wing_return = ("\nYou step into the West Wing, averting your eyes"
    " from the mangled BODY on the \nfloor.\n")

    if "West Wing" in checked_rooms:
        type_text(west_wing_return)

    else:
        type_text(west_wing_initial)
        checked_rooms.append("West Wing")

    while True:
        west_wing_choice = input("\nWhat do you do? (If you're stuck, try"
        " using the 'l' command to look around.)\n")

        if west_wing_choice.lower() == "l":
            type_text("\nThe dead BODY lies a few feet from you.\n"

            "\nTo the North ('n') is a set of double doors leading"
            " to the Library.\n"

            "\nTo the East ('e') is the Foyer.\n"

            "\nTo the West ('w') is the service lift leading to the"
            " Basement.\n")

            if "Chris' Room Location" in player_card['Insight']:
                type_text("\nSouth ('s') of you, you spot Chris' Room.\n")

        elif west_wing_choice.lower() == "i body":
            type_text("\nYou take a closer look at the body. It's a man,"
            " maybe in his mid-thirties. \nLooks like he was an employee"
            " here. His name tag reads, 'Barry'.\n")

        elif west_wing_choice.lower() == "n":
            type_text("\nYou pass through the double doors to the North, into"
            " the Library.\n")
            library()
            break

        elif west_wing_choice.lower() == "e":
            type_text("\nYou use the Eastern door to the Foyer.\n")
            foyer()
            break

        elif west_wing_choice.lower() == "s":

            if "Chris' Room Location" in player_card['Insight']:

                if "Chris' Room" not in checked_rooms:
                    type_text("\nAs you approach Chris' Room you notice that"
                    " the door is slightly ajar, its \nwooden frame"
                    " spintered. Someone must've forced their way"
                    " inside...\n")
                    chris_room()
                    break

                else:
                    type_text("\nYou exit the corridor and step into Chris'"
                    " Room.\n")

            else:
                type_text(generic_error)

        elif west_wing_choice.lower() == "w":

            if "RW Key" in looted_items and power is True:
                type_text("\nYou use the Raven's Wing Key to unlock the"
                " service lift. The metal mesh doors \nclash and clang as you"
                " pull them open and step inside.\n")
                basement_a()
                break

            elif "RW Key" not in looted_items:

                if "lockpick" in player_card['Skill']:
                    type_text("\nThis door is locked with a strange"
                    " mechanism. It looks like the key would need \nto be"
                    " shaped like a set of wings...\n")

                else:
                    type_text("This door is locked.")

            elif "RW Key" in looted_items and power is False:
                type_text("\nYou use the Raven's Wing Key to unlock the"
                " service lift, but it has no power...\n")

        elif west_wing_choice.lower() == "help":
            print(help)

        elif west_wing_choice.lower() == "pc":
            print(player_card)

        elif west_wing_choice.lower() == "heal":
            heal()

        elif west_wing_choice.lower() == "exit":
            main_menu()
            break

        else:
            type_text(generic_error)


def supplies_cupboard():
    """
    Supplies Cupboard - Game Location.
    """
    supplies_cupboard_initial = ("\nYou step into a cramped cupboard space,"
    " littered with cleaning supplies and \nfresh bedding. You spot a FIRST"
    " AID KIT on the shelf.\n")

    supplies_cupboard_return = ("\nYou enter the cramped cupboard.\n")

    if "Supplies Cupboard" in checked_rooms:
        type_text(supplies_cupboard_return)

    else:
        type_text(supplies_cupboard_initial)
        checked_rooms.append("Supplies Cupboard")

    while True:
        supplies_cupboard_choice = input("\nWhat do you do? (If you're stuck,"
        " try using the 'l' command to look around.)\n")

        if supplies_cupboard_choice.lower() == "l":
            if "First Aid Kit (SC)" in looted_items:
                type_text("\nThere's nothing else of use here. The East Wing"
                " is to your North ('n').\n")

            else:

                type_text("\nA FIRST AID KIT sits on the shelf. The East Wing"
                " is to your North ('n').\n")

        elif supplies_cupboard_choice.lower() == "help":
            print(help)

        elif supplies_cupboard_choice.lower() == "pc":
            print(player_card)

        elif supplies_cupboard_choice.lower() == "exit":
            main_menu()
            break

        elif supplies_cupboard_choice.lower() == "heal":
            heal()

        elif supplies_cupboard_choice.lower() == "i first aid kit":

            if "First Aid Kit (SC)" in looted_items:
                type_text("\nYou've already taken the First Aid Kit.\n")

            else:

                fa_kit_loot()
                looted_items.append("First Aid Kit (SC)")
                type_text("\nAs you put the First Aid Kit back, a previously"
                " hidden note is knocked to the floor. It reads:\n"

                "\nJill,\n"

                "\nThings here have been getting weirder and weirder lately."
                " I was working a shift \nthe other night, and when I went"
                " for a smoke in the Garden, I could've sworn I \nheard"
                " chanting coming from the Cellar. And those freaks with the"
                " black robes \n- I still get shivers when I remember seeing"
                " them come up from the basement. \nThe screams I heard"
                " coming from down there... I'm still sure it's got something"
                "\nto do with all these missing people. And I'm not waiting"
                " around to be the next \nface on a 'Missing' poster."
                " Apparently Whateley's got a hidden safe somewhere \nin his"
                " room - I'm breaking in there tonight, clearing out anything"
                " worth a damn \nand getting the hell out of this town. I'll"
                " be gone by the time you read this, \nbut if you know what's"
                " good for you, you'll follow my lead.\n"

                "\nSeriously, get out before it's too late.\n"

                "\n- Jack\n")
                if "Hidden Safe Location" not in player_card['Insight']:
                    player_card['Insight'].append("Hidden Safe Location")
                    type_text("\n'Hidden Safe Location' added to Insight.\n")

        elif supplies_cupboard_choice.lower() == "n":
            type_text("\nYou exit to the north, returning to the East"
            " Wing.\n")
            east_wing()
            return

        else:
            type_text(generic_error)


def maintenance_room():
    """
    Maintenance Room - Game Location where power can be restored.
    """
    maintenance_room_initial = ("\nAs you quietly edge the door open, peering"
    " through the gap, your flashlight \nfalls upon a gruesome trail of red."
    " That's when the stench hits you. Rotting \nflesh. You fight the urge to"
    " wretch and try to focus. Someone had been dragged \nthrough here,"
    " bleeding heavily. You feel a swell of desperation as fear grips \nyou,"
    " but you force yourself to go on. Swinging the door open, you discover"
    " the \nsource of the gory trail. Lying in the centre of the room, you"
    " find what \nremains of the grounds keeper. His BODY has been completely"
    " ripped apart. The \nurge to wretch rises in you again and this time you"
    " give in. You turn to the \ncorner of the room as you double over and"
    " deposit your lunch on the floor. You \nspit out the last traces of sick"
    " and wipe your mouth across your sleeve. As you \nlook up, you spot a"
    " CIRCUIT BREAKER across the room.\n")

    maintenance_room_return = ("\nYou hold your breath and avoid looking at"
    " the savaged corpse in the centre of \nthe room.\n")

    if "Maintenance Room" in checked_rooms:
        type_text(maintenance_room_return)

    else:
        type_text(maintenance_room_initial)
        checked_rooms.append("Maintenance Room")

    while True:
        maintenance_room_choice = input("\nWhat do you do? (If you're stuck,"
        " try using the 'l' command to look around.)\n")
        global power
        global flashlight

        if maintenance_room_choice.lower() == "l":

            if power is True:
                type_text("\nThe grounds keeper's BODY lies in the centre of" 
                " the room. Behind you, to the \nwest, is the East Wing. The"
                " generator across the room now hums with power.\n")

            else: 
                type_text("\nThe grounds keeper's BODY lies in the centre of"
                " the room. At the far end, you \nsee a CIRCUIT BREAKER,"
                " connected to a large generator. Behind you, to the \nwest,"
                " is the East Wing.\n")

        elif maintenance_room_choice.lower() == "help":
            print(help)

        elif maintenance_room_choice.lower() == "pc":
            print(player_card)

        elif maintenance_room_choice.lower() == "exit":
            main_menu()
            break

        elif maintenance_room_choice.lower() == "heal":
            heal()

        elif maintenance_room_choice.lower() == "i circuit breaker":
            if power is True:
                type_text("\nThe generator seems to be running smoothly.\n")

            else: 
                type_text("\nYou grab the handle of the circuit breaker and"
                " pull down hard. After a couple \nof seconds, the generator"
                " begins to rumble loudly. You hear the buzz of \nelectricity"
                " and a click from above as the lights finally flicker to"
                " life. With \na sigh of relief, you turn off your flashlight"
                " and stow it in your pocket.\n")
            power = True
            flashlight = False

        elif maintenance_room_choice.lower() == "i body":
            type_text("\nUpon closer inspection, the grounds keeper's body"
            " appears to have been torn \napart. What on earth has the"
            " strength to do this?\n")

        elif maintenance_room_choice.lower() == "w":
            type_text("\nYou exit to the west, returning to the East Wing.\n")
            east_wing()
            break

        else:
            type_text(generic_error)


def library():
    """
    Library - Game Location.
    """

    def flee():
        """
        When called during fight, Player randomly triggers function for an
        adjacent room.
        """
        available_directions = [west_wing, garden]
        random_direction = random.choice(available_directions)
        random_direction()

    library_initial = ("\nThe door to the Library creaks open, and you're met"
    " with the largest room in \nRaven's Rest. High ceilings stretch far"
    " overhead, surpassing the equally \nimposing bookselves that divide the"
    " room.\n"

    "\nAs you roam the makeshift halls of this literary forest, you notice"
    " the warm \nglow of candlelight coming from one of the aisles. You watch"
    " for a moment as \nthe flicking light mingles with shadow, casting long"
    " dark shapes across the \nbooks. Studying the shapes as they dance from"
    " side to side, you realise their \nmovements aren't being caused by the"
    " twitch of the flame, but by the thing \ncasting the shadows. Someone"
    " else is in this library. You peer around the \ncorner and spot a figure"
    " about halfway down the aisle. Dressed in a hooded \nblack robe and"
    " stood with their back to you, they appear to be searching one of \nthe"
    " shelves. You stifle your breath for fear of making a sound and begin to"
    "\nslowly back away. Suddenly, something hard hits you in the back. You"
    " hear a \nbrief sound of fluttering then a loud thud. Spinning around,"
    " you realise you've \nbacked into one of the bookcases, and to your"
    " horror knocked one of the books \nto the floor. Instinctively, you"
    " shoot a glance towards the candlelight. The \nhooded figure is gone.\n"

    "\nPanic sets in. You take flight towards the door you \nentered from,"
    " keeping your footsteps as light and quiet as you can. Rounding \nthe"
    " corner of a bookcase, you feel a large hand grip the top of your arm"
    " and \nspin you around. From a distance, dwarfed by the size of the room"
    " and its \ncontents, you hadn't realised how big the figure was. He"
    " towers over you, \nstood at close to 7 feet tall and about half as"
    " wide. But the sheer size of the \nman isn't what shocks you. His bottom"
    " jaw is gone. His tongue lolling limply \nfrom the gaping wound, spit"
    " and blood drooling down the front of his robes. An \nawful groaning"
    " noise bellows from remainder of his mouth as he wraps his \nimpossibly"
    " large hands around your throat and lifts you off the ground. \nYou"
    " squirm for your life as he grabs your bottom jaw and begins to pull"
    " down. \nBefore he can rip you apart, you manage to kick off his chest"
    " and leverage \nyourself free, dropping to your feet.\n")

    library_return = ("\nYou quietly creep back into the library, carefully"
    " closing the door behind you. \nBut the hulking figure in black was"
    " waiting for you. Looking up, you see him pacing \ntowards you, his"
    " ghastly tongue swinging from side to side as he marches.\n")

    if "Whateley's Room Location" in player_card['Insight']:
        library_safe = ("\nYou enter the Library, casting a glance in the"
        " diretion of the jawless man's \nBODY.\n"

        "\nTo the West, you see the door to Whateley's Room.\n"

        "\nTo the South is the West Wing corridor.\n"

        "\nThe door to the East takes you to the Garden.\n")

    else:
        library_safe = ("\nYou enter the Library, casting a glance in the"
        " diretion of the jawless man's \nBODY.\n"

        "\nOver by the still flickering candles, you see a pile of NOTES.\n"

        "\nTo the South is the West Wing corridor.\n"

        "\nThe door to the East takes you to the Garden.\n")

    if "Cultist (Lib)" in slain_enemies:
        type_text(library_safe)

    elif "Cultist (Lib)" not in slain_enemies and "Library" in checked_rooms:
        enemy.update(cultist_library)
        type_text(library_return)

    else:
        enemy.update(cultist_library)
        checked_rooms.append("Library")
        type_text(library_initial)

    while True:

        if "Cultist (Lib)" in slain_enemies:
            library_choice = input("\nWhat do you do? (If you're stuck, try"
            " using the 'l' command to look around.)\n")

        else:
            library_choice = input("\nWhat do you do? Use the 'atk' command"
            " to attack, or the 'flee' command to flee.\n")

        if library_choice.lower() == "atk":
            atk()

        elif library_choice.lower() == "flee":
            if "Cultist (Lib)" in slain_enemies:
                type_text("\nThere's nothing to run from right now.\n")
            else:
                type_text("\nIn a blind panic, you sprint for the nearest"
                " door.\n")
                flee()
                break

        elif library_choice.lower() == "l":

            if "Cultist (Lib)" not in slain_enemies:
                type_text("\nNow's not the time for looking around!\n")

            else:

                if "Whateley's Room Location" in player_card['Insight']:
                    type_text("\nThe enormous BODY of the jawless man is"
                    " sprawled across the \nfloor.\n"

                    "\nOver by the still flickering candles, you see a pile"
                    " of NOTES. Not far from \nthere is the BOOK you knocked"
                    " off the shelf.\n"

                    "\nTo the South is the West Wing corridor.\n"

                    "\nThe door to the East takes you to the Garden.\n"

                    "\nYou also notice, hidden just out of view, a door"
                    " leading West. This must be \nWhateley's Room.\n")

                else:
                    type_text("\nThe enormous BODY of the jawless man is"
                    " sprawled across the \nfloor.\n"

                    "\nOver by the still flickering candles, you see a pile"
                    " of NOTES. Not far from \nthere is the BOOK you knocked"
                    " off the shelf.\n"

                    "\nTo the South is the West Wing corridor.\n"

                    "\nThe door to the East takes you to the Garden.\n")

        elif library_choice.lower() == "i notes":
            type_text("\nYou head over to the pile of notes and begin to"
            " read. Some of the notes are \ncovered in scribblings of strange"
            " runes. One, written in English, reads:\n"

            "\n'Albert.\n"

            "\nOne of my idiot employees found the book when they were"
            " tidying up and placed \nit in the library. Without the"
            " Necronomicon, we can't finish the ritual to \nseed our Banished"
            " Lord the vessel. Find it, before I rip that disgusting tongue"
            "\nout of your hideous face.\n"

            "\n- W'\n"

            "\nScanning the other notes you find what appears to be a"
            " description of \nthis 'Necronomicon':\n"

            "\n'The cover off the tombe bears a striking resemblence to a"
            " face enduring \nterrible agony. The leathery material that"
            " binds its pages is wrinkled and \nfleshy to the touch.'\n")

            if "Necronomicon Description" not in player_card['Insight']:
                player_card['Insight'].append("Necronomicon Description")
                type_text("\n'Necronomicon Description' added to Insight.\n")

        elif library_choice.lower() == "i book":

            if "Necronomicon Description" in player_card['Insight']:
                type_text("\nWhat are the odds... The book you knocked off"
                " the shelf matches the description \nof the Necronomicon."
                " You bend down to pick it off the floor. As you touch the"
                " \ncover of the book there's a flash of light and you're"
                " struck with a terrible \nvision: a writhing mass of"
                " blinking eyes and blackened tendrils wrapped around"
                "\ndozens of small, glowing orbs. At once, all the eyes"
                " focus on you. Another \nflash of light, and the vision"
                " fades. You find yourself in the Library of \nthe Raven's"
                " Rest once more.\n")

                if "Necronomicon" not in player_card['Inventory']:
                    player_card['Inventory'].append("Necronomicon")
                    type_text("\n'Necronomicon' added to Inventory.\n")

            else:
                type_text("\nYou look down at the book on the floor. Maybe"
                " you're losing it, but you could \nswear the cover looks"
                " like a twisted face. You shudder and leave the book where"
                "\nit lies.\n")

        elif library_choice.lower() == "i body":

            if "Cultist (Lib)" in slain_enemies:
                type_text("\nYou take a closer look at the body of the"
                " jawless man. You notice a strange \nsymbol carved into the"
                " flesh of his forehead. His robes are completely \nsoiled"
                " with saliva and blood.\n")

                if "First Aid Kit (Library)" not in looted_items:
                    type_text("\nYou take a knee beside the giant and pat down"
                    " his robes. You find medical \nsupplies in his pockets.")
                    fa_kit_loot()
                    looted_items.append("First Aid Kit (Library)")

            else:
                type_text("\n'I can't do that now.'\n")

        elif library_choice.lower() == "s":

            if "Cultist (Lib)" not in slain_enemies:
                type_text("\nIn your panic, you flee in a random direction.\n")
                flee()
                break

            else:
                type_text("\nYou leave out the South door to the West Wing.\n")
                west_wing()
                break

        elif library_choice.lower() == "w":

            if "Whateley's Room Location" not in player_card['Insight']:
                type_text(generic_error)

            else:

                if "Cultist (Lib)" not in slain_enemies:
                    type_text("\nIn your panic, you flee in a random direction.\n")
                    flee()
                    break

                else:
                    type_text("\nYou approach the door to Whateley's Room.\n")
                    whateleys_room()
                    break
    
        elif library_choice.lower() == "e":

            if "Cultist (Lib)" not in slain_enemies:
                type_text("\nIn your panic, you flee in a random direction.\n")
                flee()
                break

            else:
                type_text("\nYou leave out the East door into the Garden.\n")
                garden()
                break

        elif library_choice.lower() == "help":
            print(help)

        elif library_choice.lower() == "pc":
            print(player_card)

        elif library_choice.lower() == "exit":
            main_menu()
            break

        elif library_choice.lower() == "heal":
            heal()

        else:
            type_text(generic_error)


def bar():
    """
    Bar - Game Location where Raven's Beak Key can be found
    """
    global flashlight


    def flee():
        available_directions = [east_wing, garden]
        random_direction = random.choice(available_directions)
        random_direction()

    bar_initial = ("\nAs you enter the bar, the eerie silence of the hotel is"
    " disturbed. Your heart \njumps into your mouth as you realise you're not"
    " alone in this room. You quickly \nsnuff out your flashlight and root"
    " yourself to the spot, terrified you'll make \na sound if you move."
    " Somewhere across the room, hidden amongst the darkness, \nyou hear a"
    " voice. Faintly, it mutters to itself in a language you've never \nheard"
    " before. The more you listen to the incessant mumbling, the more you"
    " begin \nto wonder if the language is even human. Suddenly, the muttering"
    " stops, and the \npitch-black room falls into silence.\n")

    bar_return = ("\nYou cautiously creep back into the bar. Immediately you"
    " spot the \nmutilated man, frantically searching around with his hands"
    " outstretched.\n")

    bar_safe = ("\nYou step into the bar. To the west, a door leads into the"
    " Garden. Behind you, \nto the south, is the East Wing.\n")

    if "Cultist (Bar)" in slain_enemies:
        type_text(bar_safe)

    elif "Cultist (Bar)" not in slain_enemies and "Bar" in checked_rooms:
        enemy.update(cultist_bar)
        type_text(bar_return)

    else:
        enemy.update(cultist_bar)
        checked_rooms.append("Bar")
        type_text(bar_initial)
        flashlight = False
        type_text("\nEnter 'i flashlight' to turn on your flashlight.\n")

    while True:

        bar_choice = input()

        if bar_choice == "i flashlight":

            if flashlight is True:
                type_text("\nYour flashlight is already on!\n")

            elif power is False and flashlight is False:

                flashlight = True

                type_text("\nAlmost paralysed with fear, you force yourself to"
                " switch your flashlight on. As \nthe beam of light leaps"
                " forward, you see a man in black robes stood less than a"
                "\nmetre in front of you. Your instinct is to scream but"
                " luckily fear strangles \nyour voice, as you realise after"
                " a moment that the man hasn't seen you. In \nfact, he hasn't"
                " seen anything. Two dark sockets of crimson sit where his"
                " eyes \nshould be, and dried blood streaks his face like"
                " tears of gore. A strange \nsymbol is carved into the ghostly"
                " white flesh of his forehead, adding to his \nnightmareish"
                " visage. Despite his lack of eyes, he appears to be staring"
                "\nstraight at you.\n"

                "\nVery slowly, you begin to edge backwards towards the door."
                " Despite your efforts \nto remain silent, however, he hears"
                " you. Without uttering a single word, the \nmutilated man"
                " begins lumbering towards you, hands reaching out to grab"
                " you.\n"

                "\nEnter 'atk' to attack, or 'flee' to run away.\n")

            else:
                type_text(generic_error)

        elif bar_choice.lower() == "atk":

            if flashlight is True and enemy not in slain_enemies:
                atk()

            elif flashlight is False and power is False:
                type_text("\n'I can't see a thing!'\n")

            else:
                type_text(generic_error)

        elif bar_choice.lower() == "flee":

            if flashlight is True and enemy not in slain_enemies:
                type_text("\nIn a blind panic, you sprint for the nearest"
                " door.\n")
                flee()
                break

            elif "Cultist (Bar)" in slain_enemies:
                type_text("\nThere's nothing to run from right now.\n")

            elif flashlight is False and power is False:
                type_text("\n'I can't see a thing!'\n")

            else:
                type_text(generic_error)

        elif bar_choice.lower() == "l":

            if flashlight is False and power is False:
                type_text("\n'I can't see a thing!'\n")

            elif flashlight is True and "Cultist (Bar)" not in slain_enemies:
                type_text("\nNow's not the time for looking around!\n")

            elif "Cultist (Bar)" in slain_enemies:
                type_text("\nThe BODY of the mutilated man lies still on the"
                " floor, a puddle of crimson \ngrowing beneath him.\n"

                "\nTo the West, you see a door that leads outside. The sign"
                "\nnext to it reads, 'Garden area this way'.\n"

                "\nAt the far end of the room is a rather impressive BAR,"
                " with plenty of \nexpensive looking bottles on display.\n"

                "\nThe door to East Wing is to your South.\n")

            else:
                type_text(generic_error)

        elif bar_choice.lower() == "i bar":

            if flashlight is False and power is False:
                type_text("\n'I can't see a thing!'\n")

            else:
                type_text("\nYou creep over to the bar to have a closer look."
                " Behind the bar, you spot a LEDGER that looks to show"
                " people's open tabs.\n")

        elif bar_choice.lower() == "i ledger":

            if flashlight is False and power is False:
                type_text("\n'I can't see a thing!'\n")

            else:
                type_text("\nInspecting the ledger, you find Chris' name. His"
                " room number is written in the \ncolumn next to it.\n")

                if "Chris' Room" not in player_card['Insight']:
                    player_card['Insight'].append("Chris' Room Location")
                    type_text("\n'Chris' Room Location' added to Insight.\n")

        elif bar_choice.lower() == "i body":

            if "Cultist (Bar)" in slain_enemies and \
            "Raven's Beak Key" not in player_card['Inventory']:
                type_text("\nYou crouch down and rummage through the dead"
                " man's robes. You find a strange, beak shaped key in his"
                " pocket.\n"
                "\n'Raven's Beak Key' added to Inventory.\n")
                player_card['Inventory'].append("Raven's Beak Key")

            elif "Cultist (Bar)" in slain_enemies and \
            "Raven's Beak Key" in player_card['Inventory']:
                type_text("\nYou've already looted this body for anything"
                " usesful.\n")

            else:
                type_text("\n'I can't do that now.'\n")

        elif bar_choice.lower() == "s":

            if flashlight is False and power is False:
                type_text("\n'I can't see where I'm going!\n")

            elif flashlight is True and "Cultist (Bar)" not in slain_enemies:
                type_text("\nIn your panic, you flee in a random direction.\n")
                flee()
                break

            else:
                type_text("\nYou leave out the South door to the East Wing.\n")
                east_wing()
                break

        elif bar_choice.lower() == "w":

            if flashlight is False and power is False:
                type_text("\n'I can't see where I'm going!\n")

            elif flashlight is True and "Cultist (Bar)" not in slain_enemies:
                type_text("\nIn your panic, you flee in a random direction.\n")
                flee()
                break

            else:
                type_text("\nYou leave out the West door to the Garden.\n")
                garden()
                break

        elif bar_choice.lower() == "help":
            print(help)

        elif bar_choice.lower() == "pc":
            print(player_card)

        elif bar_choice.lower() == "exit":
            main_menu()
            break

        elif bar_choice.lower() == "heal":
            heal()

        else:
            type_text(generic_error)


def garden():
    """
    The Garden - Game Location.
    """
    global flashlight

    if power is True:

        flashlight = True

        type_text("\nStepping into the dark and stormy night, you turn your"
        " flashlight on.\n")

    garden_initial = ("\nA sense of relief washes over you as you escape into"
    " the downpour outside. It's \na welcome break from the oppressive hotel,"
    " which felt as though it had \nswallowed you whole. You take a moment to"
    " catch your breathe. Feeling the sting \nof cold wind and rain on your"
    " face reassures you that you're not simply trapped \nin a nightmare."
    " After a moment, you allow your mind to be dragged back to the \nhorrors"
    " of the Raven's Rest and the task at hand. Sweeping the beam of your"
    "\nflashlight across the garden, you make out a tall hedge that runs the"
    " perimeter. \nAn impressive water fountain takes the pride of the garden"
    " space, sporting an \nelegent statue of (rather predictably) a raven at"
    " it's centre. Benches are \nscattered throughout the garden, with"
    " several FLOWER BEDS dotted around. \nTo the west, a set of doors lead"
    " into the Hotel's Library. The Bar is to the \neast. In between these"
    " doors, up against the southern wall of the Hotel, you \nsee the"
    " entrance to the cellar.\n")

    garden_return = ("\nYou step outside into the wind and rain, glad to"
    " escape the suffocating \ninterior of the Raven's Rest for a while.\n"

    "\nTo the West is the Library.\n"

    "\nTo the East is the Bar.\n"

    "\nTo the South is the Cellar entrance.\n")

    if "Garden" in checked_rooms:
        type_text(garden_return)

    else:
        type_text(garden_initial)
        checked_rooms.append("Garden")

    while True:

        garden_choice = input("\nWhat do you do? (If you're stuck, try using"
        " the 'l' command to look around.)\n")

        if garden_choice.lower() == "l":
            type_text("\nSeveral FLOWER BEDS are dotted around the garden.\n"

            "\nTo the West is the Library.\n"

            "\nTo the East is the Bar.\n"

            "\nTo the South is the Cellar entrance.\n")

        elif garden_choice.lower() == "help":
            print(help)

        elif garden_choice.lower() == "pc":
            print(player_card)

        elif garden_choice.lower() == "exit":
            main_menu()
            break

        elif garden_choice.lower() == "heal":
            heal()

        elif garden_choice.lower() == "i flower beds":
            type_text("\nYou inspect a nearby flower bed. Unusual plants seem"
            " to be growing here. Thick \npurple stems support dark, drooping"
            " leaves. It's as though the corruption within \nthe Hotel has"
            " seeped into the earth around it, bearing these ominious plants"
            " as \nit's fruit. One section of the flower bed looks recently"
            " dug up, with a muddied \nPITCHFORK staked into the dirt.\n")

        elif garden_choice.lower() == "i pitchfork":

            if "Pitchfork" in looted_items:
                type_text("\nYou've already taken the Pitchfork.\n")

            elif "Handgun" in looted_items:
                type_text("\nI think I'll stick with this hangun...\n")

            elif "Shotgun" in looted_items:
                type_text("\nI think I'll stick with this shotgun...\n")

            else:
                type_text("\nYou lean down and grab the pitchfork, freeing it"
                " from the earth. Testing it's \nweight, you give it a couple"
                " of practice thrusts. Not bad.\n"
                "\n'Pitchfork' is now equipped.\n")
                looted_items.append("Pitchfork")
                player_card['Weapon'] = "Pitchfork"
                player_card['Attack Power'] = "20 - 30"

        elif garden_choice.lower() == "w":

            if power is True:
                type_text("\nYou switch off your flashlight before heading"
                " into the Library.\n")
                flashlight = False
                library()
                break

            else:
                type_text("\nYou head through the western door into the"
                " Library.\n")
                library()
                break

        elif garden_choice.lower() == "e":

            if power is True:
                type_text("\nYou switch off your flashlight before heading"
                " into the Bar.\n")
                flashlight = False
                bar()
                break

            else:
                type_text("\nYou head through the eastern door into the"
                " Bar.\n")
                bar()
                break

        elif garden_choice.lower() == "s":

            if "Cellar" not in checked_rooms:
                type_text("\nApproaching the Cellar doors, you begin to hear"
                " strange sounds coming from \nwithin. As you get closer, you"
                " realise it's a voice, chanting. The voice is \nthat of a"
                " man's, but the language sounds completely alien. The only"
                " words you \ncan make out are... 'Yog'... 'Sothoth'..."
                " Whatever that means.\n"

                "\nA sense of unease stirs within you. Whatever evil"
                " permeates this Hotel, \nyou can't help but feel like it's"
                " festering source is coming from below.\n")

                enter_cellar = input("\nAre you sure you want to enter? y /"
                " n\n")

                if enter_cellar.lower() == "y":
                    type_text("\nThe answer to finding Chris is in this"
                    " Cellar. You know it. You open one of the \ndoors and"
                    " quietly descend the hard, stone steps.\n")
                    cellar()
                    break

                elif enter_cellar.lower() == "n":
                    type_text("\n'I should prepare some more before going down"
                    " there.'\n")

                else:
                    type_text("You can't do that now.")

            else:
                cellar()
                break

        else:
            type_text(generic_error)


def chris_room():
    """
    Chris' Room - Game Location.
    """
    chris_room_initial = ("\nCautiously, you step into Chris' Room. Hunched"
    " over a desk in the corner is \nanother robed figure shrouded by a black"
    " hood. You watch as they rifle through \na pile of loose sheets of paper,"
    " seeming not to notice you. Slowly and \nquietly, you sneak towards them"
    " - hoping to get the drop on them. To your \ndismay, as you get within a"
    " few feet of the cultist, they happen to turn \naround. Shock flashes"
    " across the man's face before quickly twisting to \ncontempt. He howls a"
    " string of alien words at you as he grasps a knife from the \ndesk and"
    " lunges towards you.\n")

    chris_room_return = ("\nAs you step back into Chris' Room, for a moment,"
    " it appears empty. Then, \nannouncing himself with an animalistic roar,"
    " you spin around to see the hooded \nfigure charge at you from the"
    " bathroom.\n")

    chris_room_safe = ("\nYou look around Chris' Room.\n"

    "\nThere's an en suite BATHROOM to your right.\n"

    "\nIn the corner of the room is the desk the cultist was pouring over,"
    " littered \nin NOTES of paper. Also on the desk sits a COMPUTER.\n"

    "\nBeneath the desk sits a small SAFE.\n"

    "\nBehind you, to the North ('n') is the West Wing corridor.\n")

    if "Cultist (CR)" in slain_enemies:
        type_text(chris_room_safe)

    elif "Cultist (CR)" not in slain_enemies and "CR" in checked_rooms:
        enemy.update(cultist_chris_room)
        type_text(chris_room_return)

    else:
        enemy.update(cultist_chris_room)
        checked_rooms.append("CR")
        type_text(chris_room_initial)


    def trapped():
        player_card['HP'] = player_card['HP'] - enemy['Attack Power']
        type_text(f"You attempt to flee, but the {enemy['Name']} blocks the"
        f" door and slashes at you \nfor {enemy['Attack Power']} damage.\n")
        if player_card['HP'] <= 0:
            game_over()

        else:
            type_text(f"You have {player_card['HP']} remaining HP."
            " Attack or attempt to flee?\n")


    def flee():
        possible_outcomes = [west_wing, trapped]
        random_outcome = random.choice(possible_outcomes)
        random_outcome()

    while True:

        if "Cultist (CR)" in slain_enemies:
            cr_choice = input("\nWhat do you do? (If you're stuck, try"
            " using the 'l' command to look around.)\n")
        else:
            cr_choice = input("\nWhat do you do? Use the 'atk' command to"
            " attack, or the 'flee' command to flee.\n")

        if cr_choice.lower() == "atk":
            atk()

        elif cr_choice.lower() == "flee":

            if "Cultist (CR)" in slain_enemies:
                type_text("\nThere's nothing to run from right now.\n")

            else:
                flee()

        elif cr_choice.lower() == "l":

            if "Cultist (CR)" not in slain_enemies:
                type_text("\nNow's not the time for looking around!\n")

            else:
                type_text("\nYou look around the room.\n"

                "\nThe cultist lies dead on the floor, his BODY still.\n"

                "\nThere's an en suite BATHROOM to your right.\n"

                "\nIn the corner of the room is the desk the cultist was"
                " pouring over, littered \nin NOTES of paper. Also on the"
                " desk sits a COMPUTER.\n"

                "\nBeneath the desk sits a small SAFE.\n"

                "\nBehind you, to the North ('n'), is the West Wing"
                " corridor.\n")

        elif cr_choice.lower() == "i computer":

            if "Cultist (CR)" not in slain_enemies:
                type_text("\n'I can't do that now.'\n")

            else:

                if power is False:
                    type_text("\nThe power is still out. Maybe you can find a"
                    " way to turn it back on...\n")

                else:
                    chris_computer()

        elif cr_choice.lower() == "i safe":

            if "Cultist (CR)" not in slain_enemies:
                type_text("\n'I can't do that now.'\n")

            else:

                if "hack" not in player_card['Skill']:
                    type_text("\nIt's secured with an electrical lock. A small"
                    " terminal is built into the side of it.\n"
                    "\n'No way I'm breaking into this.'\n")

                else:

                    if "Handgun" in looted_items:
                        type_text("\nYou've already emptied the safe.\n")

                    else:
                        type_text("\nYou manage to hack into the safe's"
                        " terminal and find a Handgun inside.\n")
                        looted_items.append("Handgun")
                        player_card['Weapon'] = "Handgun"
                        player_card['Attack Power'] = "30 - 40"
                        type_text("'Handgun' is now equipped.")

        elif cr_choice.lower() == "i notes":

            if "Cultist (CR)" in slain_enemies:

                if "Ciper" not in looted_items:
                    type_text("\nYou look through the notes on Chris' desk."
                    " Page after page of strange glyphs, \nsome with letters"
                    " or numbers scribbled in the margins. Then it dawns on"
                    " you - \nyou're looking at a cipher. Chris was working on"
                    " translating this strange \nlanguage. Eventually you find"
                    " a page that looks to show a complete alphabet, \nwhich"
                    " you hastily stuff into your pocket.\n")
                    player_card['Inventory'].append("Ciper")
                    looted_items.append("Ciper")
                    type_text("\n'Cipher' added to Inventory.\n")

                else:
                    type_text("\nYou've already picked up the Cipher.\n")

            else:
                type_text("\n'I can't do that now.'\n")

        elif cr_choice.lower() == "i bathroom":

            if "Cultist (CR)" in slain_enemies:
                if "First Aid Kit (CR)" not in looted_items:
                    type_text("\nYou take a look inside Chris' Rooms"
                    " bathroom. The only thing of use in here \nis a First"
                    " Aid Kit, lying by the sink.\n")

                    player_card['Inventory'].append("First Aid Kit")
                    looted_items.append("First Aid Kit (CR)")

                else:
                    type_text("\nYou've already picked up the First Aid Kit"
                    " in here.\n")
            else:
                type_text("\n'I can't do that now.'\n")

        elif cr_choice.lower() == "i body":

            if "Cultist (CR)" in slain_enemies:
                type_text("\nYou take a closer look at the dead cultist. You"
                " realise now why you were able \nto sneak up on him at first."
                " The sides of his head and neck are stained a dark \nred."
                " Judging by the jagged wounds, it looks like his ears had"
                " been torn off. \nDid he do this to himself? He has the same"
                " strange marking carved into his \nforehead.\n")

            else:
                type_text("\n'I can't do that now.'\n")

        elif cr_choice.lower() == "n":

            if "Cultist (CR)" in slain_enemies:
                type_text("\nYou exit out the North door to the West Wing"
                " corridor.\n")
                west_wing()
                break

            else:
                flee()

        elif cr_choice.lower() == "help":
            print(help)

        elif cr_choice.lower() == "pc":
            print(player_card)

        elif cr_choice.lower() == "exit":
            main_menu()
            break

        elif cr_choice.lower() == "heal":
            heal()

        else:
            type_text(generic_error)


def chris_computer():
    """
    Chris' Computer - Options
    """
    while True:

        chris_computer_choice = input("\nEnter 'j' to open Journal Entries.\n"
        "\nEnter 'back' to log off the computer.\n")

        if chris_computer_choice.lower() == "j":
            type_text("\nJournal Entry #1\n"
            "\nJournal Entry #2\n"
            "\nJournal Entry #3\n"
            "\nJournal Entry #4\n"
            "\nJournal Entry #5\n")
            read_journal = input("\nWhich entry do you want to read? 1 / 2 /"
            " 3 / 4 / 5 / back\n")

            if read_journal.lower() == "1":
                type_text("\nJust arrived at the Raven's Rest. This place is"
                " about as old school as they \ncome, but Whateley's arranged"
                " a room for me with a desk and computer, so I \ncan't"
                " complain.\n"
                "\nSpent the day in town talking to people about the"
                " disappearances. Most were \nunderstandably keen to avoid the"
                " topic, but I met a couple of the town's \ngossips who were"
                " more loose lipped about it. Apparently the 6 missing persons"
                "\nreported in the papers is just the official number, some"
                " reckon the number is \nmuch higher. Of course, the rumour"
                " factory always works double shifts in \nremote backwaters"
                " like this. One day someone sees a stray cat and by the end"
                "\nof the week it's a panther stalking about, so I'll take"
                " what they say with a \npinch of salt. Tomorrow I meet with"
                " Mr Whateley. I can't wait to hear what he \nhas to say. I"
                " only hope it's worth the 8-hour round trip I've made to be"
                " here!\n")

            elif read_journal.lower() == "2":
                type_text("\nFinally spoke with the man that brought me all"
                " the way to Dunwich today - Mr \nWhateley. The very owner"
                " of this Hotel. I have to say, the conversation wasn't \nat"
                " all what I thought it would be. He seemed exceptionally"
                " uninterested in the \nmissing persons. Rather, he wanted to"
                " talk about me. Strange questions, like \nwhether there's any"
                " history of health conditions in my family. He backed off"
                "\nthe questions a bit when I brought up his son. Withdrew a"
                " little into himself. \nClearly the wound is still fresh. I"
                " think I'll finish writing up yesterday's \nnotes tonight"
                " then have another crack at him tomorrow.\n")

            elif read_journal.lower() == "3":
                type_text("\nSomething very strange is going on. One of the"
                " townsfolk approached me at the \nbar last night. Said he'd"
                " heard about the questions I've been asking and knew I \nwas"
                " staying in the old Raven's Rest Hotel. He told me there have"
                " been strange \ngoings on at this Hotel ever since Mr Whateley"
                " took over last year, and that \nhe's brought with him a band"
                " of merry weirdos to boot. Apparently, he's seen \nthem at"
                " night, travelling to and from the Hotel and dancing around"
                " burning \neffigies in the moors. The craziest thing is that I"
                " believe him. There's \nsomething very off with Whateley. I"
                " get a real uneasy feeling around him. And \nthe other night I"
                " was chatting with one of the staff, Jack I think his name is,"
                "\nand he told me he's seen gatherings of men in black robes"
                " emerging from the \ncellar in the garden. I'll keep a keen"
                " eye on Whateley and his acquaintances \nfrom now on. I'm"
                " starting to think he's at the centre of these"
                " disappearances.\n")

            elif read_journal.lower() == "4":
                type_text("\nIt's a cult. Like a full blown, robe wearing,"
                " ritual sacrificing c u l t. I \nmanaged to sneak into the"
                " Cellar the other night and I couldn't believe what \nI saw."
                " There's this, shrine, I guess, down there. Real mad hatter"
                " stuff. I \nspoke to that employee again about it and he"
                " managed to snag this terrifying \nbook he says they're"
                " obsessed with. The 'Necronomicon' or something. Apparently" 
                "\nit's written in a dead language, but I found a book on"
                " cryptography in the \nLibrary, so I'm going to spend the"
                " next couple nights trying to figure this \nout. Hopefully"
                " they don't notice their favourite book has gone"
                " walkabouts…\n")

            elif read_journal.lower() == "5":
                type_text("\nWhateley definitely suspects something. I'm not"
                " safe here anymore. Tonight, I'm \nsneaking back into that"
                " cellar and finding something tangible I can take to the"
                "\npolice. I may not have any proof, but Whately and his"
                " lunatic cult are behind \nthose disappearances, I'm sure of"
                " it. That book was pure evil. I got Jack to \nstick it in"
                " the library so it looks like it just got tidied away by"
                " accident, \nbut Whateley definitely suspects me. For now,"
                " I've locked myself in my room. \nThere's a gun in the safe"
                " should things get desperate. Just one more night, \nthen"
                " I'm getting out of this nightmare town and never looking"
                " back.\n")

            elif read_journal.lower() == "back":
                chris_computer()

            else:
                type_text("\nAn Error Message appears on screen.\n")

        elif chris_computer_choice.lower() == "back":
            type_text("\nYou log off the computer.\n")
            chris_room()
            break

        elif chris_computer_choice.lower() == "help":
            print(help)

        elif chris_computer_choice.lower() == "pc":
            print(player_card)

        elif chris_computer_choice.lower() == "exit":
            main_menu()
            break

        else:
            type_text(generic_error)


def whateleys_room():
    """
    Whateley's Room - Game Location.
    """
    whateleys_room_initial = ("\nYou give the door knob a try, expecting it to"
    " be locked. To your surprise, it \nturns. With a gentle push, the door"
    " yawns open before you and you creep inside.\n"

    "\nThe first thing you notice is the smell. A pungent mix of rotting flesh"
    " and wet \nfur, bizarrely contrasted with the heavy scent of cheap"
    " perfume. As though \nsomeone butchered a dog in here and tried to cover"
    " the scent with toilet \nfreshener. You instinctively raise a hand to"
    " cover your nose and mouth, \ndesperately trying to save yourself from"
    " the taste of the odour.\n"

    "\nAt first glance, the room looks relatively normal. The longer your gaze"
    " lingers \nin anyone one part of the room, however, the more the cracks"
    " of insanity start \nto show. Books stacked high on his desk, ranging"
    " from subjects of the occult, \nto human anatomy, to old religious texts."
    " Clumps of dark fur stuck to the walls \nand furniture. As you edge"
    " around the bed, you notice dark red spatters across \nthe floor. As your"
    " eyes follow the trail to the source, a cold chill creeps up \nyour"
    " spine. There, lying on the floor, was a man. Eyes wide open, staring"
    "\nvacantly at the ceiling. Skin pale, almost blue, his mouth hung open in"
    " a \nsilent scream. There was a trace of white foam trickling from the"
    " corner of his \nmouth and thin streaks of blood from each eye. The body"
    " lay in front of a chest \nof drawers, one of which was still drawn. You"
    " peer past the body and spot a \nsmall SAFE hidden inside the draw.\n")

    whateleys_room_return = ("\nYou look around Whateley's Room.\n"

    "\nThe BODY of the employee lies on the floor.\n"

    "\nA small SAFE lay inside the open drawer next to the BODY.\n"

    "\nThe other side of the room sits a large DESK covered in various"
    " books.\n"

    "\nTo your East ('e') is the door back to the Library.\n")

    if "Whateley's Room" in checked_rooms:
        type_text(whateleys_room_return)

    else:
        type_text(whateleys_room_initial)
        checked_rooms.append("Whateley's Room")

    while True: 

        whateleys_room_choice = input("\nWhat do you do? (If you're stuck,"
        " try using the 'l' command to look around.)\n")

        if whateleys_room_choice.lower() == "l":
            type_text("\nYou scan the room.\n"

            "\nThe dead BODY lies on the floor between the bed and the chest"
            " of drawers.\n"

            "\nThe SAFE lay inside the open drawer next to the BODY.\n"

            "\nThe other side of the room sits a large DESK covered in"
            " various books.\n"

            "\nBehind you, to the East ('e'), is the door to the Library.\n")

            if "lockpick" in player_card['Skill']:
                type_text("You also notice hung on the wall a large"
                " PORTRAIT of a magpie - a bird known \nfor coveting various"
                " treasures...\n")

        elif whateleys_room_choice.lower() == "i body":
            type_text("\nYou take a closer look at the body. A young man"
            " wearing an employee uniform, with a name tag that reads,"
            " 'Jack'. He clearly died attempting to rob the safe, but"
            " strangely, there's no visible wound. Almost like they"
            " succumbed a seizure, or perhaps poison. Or maybe some other,"
            " more nefarious afflication...\n")

        elif whateleys_room_choice.lower() == "i safe":

            if "Hidden Safe Location" in player_card['Insight']:
                type_text("\n'I guess this must be the hidden safe the Jack"
                " wrote about in his note...'\n")

            type_text("\nEdging around the body, you take a look at the small"
            " safe inside the open \ndrawer. It's a combination lock."
            " The dead man must have known the combination, \nas it's already"
            " unlocked.\n")

            while True:

                decoy_safe = input("\nDo you open the safe? y / n\n")

                if decoy_safe == "y":
                    type_text("\nYou open the door of the safe. It's empty,"
                    " other than a short passage of runes \nscratched into"
                    " the back of the safe. Before you have a chance to"
                    " react, the \nrunes flare with a purple glow. Hit with"
                    " a terrible headache, you stumble \nbackwards, ears"
                    " ringing. Tiny drops of crimson begin to smatter the"
                    " floor as \nyour vision blurs red. You drop to your"
                    " knees, the pain worsening. A desperate \nfeeling of"
                    " helplessness rapidly building in your chest.\n")
                    player_card['HP'] -= 50

                    if player_card['HP'] <= 0:
                        type_text("\nThe room spins and something heavy"
                        " strikes the side of your head. You feel \ncarpet"
                        " on your face and realise you've collapsed. A stale"
                        " taste in your mouth. \nThe tingle of foam on your"
                        " lips. Darkness.\n")
                        print(figlet_format("GAME OVER\n", justify="center"))

                        while True:

                            game_over_choice = input("\nEnter 'ng' to start a"
                            " new game from the Character Selection Menu.\n"
                            "\nEnter 'exit' to return to the Main Menu.\n")

                            if game_over_choice.lower() == "ng":
                                reset_game_values()
                                character_selection()
                                return

                            elif game_over_choice.lower() == "exit":
                                reset_game_values()
                                main_menu()
                                return

                            else:
                                type_text("\nThat's not an option right"
                                " now...\n")

                    else:
                        type_text("\nAfter a moment, the pain begins to"
                        " subside. The ringing fades and your vision"
                        "\nreturns to normal.\n"
                        "\nYou take 50 damage.\n")
                        whateleys_room()

                elif decoy_safe == "n":
                    type_text("\nGlancing at the dead body and then back at"
                    " the safe, you decide it's probably \nbest to leave"
                    " it.\n")
                    whateleys_room()

                else:
                    type_text("\nYou can't do that now.\n")

        elif whateleys_room_choice.lower() == "i desk":
            type_text("\nAmongst the many books, you find what looks to be a"
            " journal. You flick through, skim reading as you go. Much of it"
            " is written in strange symbols, other parts seem to be complete"
            " gibberish. There are several mentions of a 'Banished Lord', and"
            " a being known as 'Yog Sothoth'. One of the pages tells of a"
            " spell that can bind this 'Yog Sothoth' to an 'vessel of flesh'."
            " You turn another page and read a passage that makes your body"
            " go cold.\n"

            "\nThe journalist proved more of a nuisance than I had"
            " anticipated. The gamble, \nhowever, was worth it. As I"
            " expected, I needed a vessel from beyond this putrid \ntown. The"
            " people here may not have felt it, but the Banished Lord drained"
            " much \nof their essence when he spoke to us that beautiful"
            " night. The power it must \nhave taken to for him to tear"
            " through space and time for even a moment to bless \nus with his"
            " vision... I suppose that energy had to come from somewhere. As"
            " a \nresult, however, the people of this town have proved too"
            " weak to withstand the \nspells necessary to prepare them as"
            " vessels. Even after I reversed the process \nin an attempt to"
            " spare them, they ultimately expired. The journalist though…"
            "\nHis body and mind have been most receptive. Once I have"
            " located the book, I \nshall perform the final ritual and"
            " deliver unto this unworthy rock our Banished \nLord.\n"

            "\nYog-Sothoth guide me.\n")

            if "Spell Reversal" not in player_card['Insight']:
                player_card['Insight'].append("Spell Reversal")
                type_text("'Spell Reversal' added to Insight.")

        elif whateleys_room_choice.lower() == "i portrait":

            if "lockpick" in player_card['Skill']:

                if "Hidden Safe Location" in player_card['Insight']:
                    type_text("\nYou take a closer look at the portrait.\n"
                    "\nTracing your fingers along the edge, you realise one"
                    " side is ever so slightly \nraised. You manage to get"
                    " your fingernails under the lip of the edge and pull."
                    "\nOne sie of the large portrait swings away from the"
                    " wall; the other revealing \nitself to be fixed in"
                    " place with two small hinges.\n"

                    "\nBeneath the portrait lies a second safe, this one"
                    " having a keylock. You get \nout your pick and begin"
                    " fiddling with the tumbler. After a few seconds you hear"
                    "\na 'clunk', and the door swings open.\n"

                    "\nInside you find a compact, pump-action Shotgun. You"
                    " pick it up and rack a \nshell into the chamber. For the"
                    " first time since entering the Raven's Rest, \nyou feel"
                    " a smile spread across your face.\n"

                    "\n'Shotgun' is now equipped.\n")

                    looted_items.append("Shotgun")
                    player_card['Weapon'] = "Shotgun"
                    player_card['Attack Power'] = "35 - 50"

                else:
                    type_text("\nWhy would there be a portrait of a magpie in"
                    " the Raven's Rest...?\n")

            else:
                type_text(generic_error)

        elif whateleys_room_choice.lower() == "e":
            type_text("\nYou exit out the door to the East.\n")
            library()

        elif whateleys_room_choice.lower() == "help":
            print(help)

        elif whateleys_room_choice.lower() == "pc":
            print(player_card)

        elif whateleys_room_choice.lower() == "exit":
            main_menu()
            break

        elif whateleys_room_choice.lower() == "heal":
            heal()

        else:
            type_text(generic_error)


def cellar():
    """
    Cellar - Game Location.
    """
    global whateley_status
    cellar_initial = ("\nAs you descend the Cellar steps, the chanting grows"
    " louder. You realise now \nthat it isn't just the words that sound"
    " alien, but the voice speaking them too. \nHarsh and guttural, each"
    " syllable underscored with a low growl. Like a beast \nimitating a man."
    " Your heart pounds against your chest, a mixture of fear and \nintrigue"
    " pulling you in both directions at once.\n"

    "\nAbout two thirds of the way down, the chanting stops. A sense of dread"
    " roots \nyou to the spot as you listen for any further noises. Why did"
    " he stop? Unnerved \nbut determined, you force yourself to complete the"
    " descent.\n"

    "\nReaching the bottom of the stairs, the narrow passage opens into"
    " cavernous room \nwith a high domed ceiling. Torches affixed to rough"
    " stone walls dimly light the \ndark and foreboding space. Centre of the"
    " Cellar sits a large, irregular slab \nof black stone with an unearthly"
    " sheen that seems to absorb light. The surface \nis carved with"
    " intricate and bizarre symbols that seem to shift and change the \nmore"
    " you try to focus on them.\n"

    "\nProstrate before this dark altar, his back still turned to you, the"
    " hooded man \nrises to his knees. Staring into the empty space above the"
    " stone, he spreads \nhis arms out wide as though expecting an embrace."
    " After a single deep \nexhalation, he climbs to his feet. It's only now"
    " as he stands you realise the \nstature of the man. At least ten feet"
    " tall, he towers over you, even from the \nother side of the Cellar. A"
    " grotesque amalgamation of limbs that seem too long, \ntoo gangly,"
    " defying normal human proportions. He turns to you and lowers his"
    "\nhood, his face a twisted mockery of humanity.  Eyes coal-black and"
    " devoid of \nany warmth or kindness glimmer with a sinister"
    " intelligence. Without a word he \nstalks towards you.\n")

    cellar_return = ("\nReluctantly, you descend the steps once more. You"
    " find the robed giant back before the altar, hunched over in silent"
    " prayer.\n"

    "\nHe rises as he hears your footsteps approach, his massive frame"
    " blocking view of the altar.\n")

    if whateley_status is True:
        cellar_safe = ("\nYou descend the steps into the Cellar. Whateley's"
        " tremendous BODY lay sprawled across the cold stone floor.\n"

        "\nBeyond him, you see the terrible altar. Just being near it fills"
        " you with a deep unease.\n"

        "\nIn the corner of the Cellar appears to be a makeshift living"
        " quarters. A roll \nmat and blanket, pail of water and several"
        " discarded food packages. A NOTE and \npen lie atop the mat.\n"

        "\nBehind you, to the North ('n'), a staircase leads out of the"
        " Cellar to the Garden.\n")

    else:
        cellar_safe = ("\nYou descend the steps into the Cellar. Whateley's"
        " tattered robe lay sprawled across the cold stone floor.\n"

        "\nBeyond it, you see the terrible altar. Just being near it fills"
        " you with a deep unease.\n"

        "\nIn the corner of the Cellar appears to be a makeshift living"
        " quarters. A roll \nmat and blanket, pail of water and several"
        " discarded food packages. A NOTE and \npen lie atop the mat.\n"

        "\nBehind you, to the North ('n'), a staircase leads out of the"
        " Cellar to the Garden.\n")

    if "Whateley" in slain_enemies:
        type_text(cellar_safe)

    elif "Whateley" not in slain_enemies and "Cellar" in checked_rooms:
        enemy.update(mr_whateley)
        type_text(cellar_return)

    else:
        enemy.update(mr_whateley)
        checked_rooms.append("Cellar")
        type_text(cellar_initial)
    

    def trapped():
        player_card['HP'] = player_card['HP'] - enemy['Attack Power']
        type_text(f"You attempt to flee, but {enemy['Name']} blocks the way"
        f" out and strikes you \nfor {enemy['Attack Power']} damage.\n")
        if player_card['HP'] <= 0:
            game_over()

        else:
            type_text(f"You have {player_card['HP']} remaining HP."
            " Attack or attempt to flee?\n")


    def flee():
        possible_outcomes = [garden, trapped]
        random_outcome = random.choice(possible_outcomes)
        random_outcome()

    while True:
        
        if "Whateley" in slain_enemies:
            cellar_choice = input("\nWhat do you do? (If you're stuck, try"
            " using the 'l' command to look around.)\n")

        else:
            cellar_choice = input("\nWhat do you do? Use the 'atk' command to"
            " attack, or the 'flee' command to flee.\n")

        if cellar_choice.lower() == "atk":
            atk()

        elif cellar_choice.lower() == "flee":

            if "Whateley" in slain_enemies:
                type_text("\nThere's nothing to run from right now.\n")

            else:
                flee()

        elif cellar_choice.lower() == "l":

            if "Whateley" not in slain_enemies:
                type_text("\nNow's not the time for looking around!\n")

            else:
                type_text("\nWhateley's tremendous BODY lay sprawled across"
                " the cold stone floor. Beyond \nhim, you see the terrible"
                " altar. Just being near it fills you with a deep \nunease.\n"
                "\nIn the corner of the Cellar appears to be a makeshift"
                " living quarters. A roll \nmat and blanket, pail of water"
                " and several discarded food packages. A NOTE and \npen lie"
                " atop the mat.\n"
                "\nBehind you, to the North ('n'), a staircase leads out of"
                " the Cellar to the Garden.\n")

        elif cellar_choice.lower() == "i body":

            if "Whateley" in slain_enemies:

                if whateley_status is True:
                    type_text("\nYou examine Whateley's grotesque physique.\n"

                    "\nHis skin has a sickly, yellowish pallor, stretched"
                    " taut over his sinewy frame. \nHis mouth, perpetually"
                    " set in a sneer, reveals unnaturally sharp teeth that"
                    "\nare uneven and stained.\n"

                    "\nYour eyes, however, are drawn to the places where his"
                    " robes were torn during \nthe fight, revealling a"
                    " glimpse of the true eldritch horror that lay beneath."
                    "\nFrom his waist down, Whateley's body is entirely"
                    " covered in coarse black fur, \nappearing like the hind"
                    " legs of a goat. Where he had been wounded, a"
                    "\ngreenish-yellow ichor seeps from his body instead of"
                    " blood. Whatever creature \nyou're looking at, it was"
                    " certainly no man.\n"

                    "\nAs you stare in disbelief at the slain monster before"
                    " you, his skin begins to \nwrithe. The yellow hue of his"
                    " flesh turns grey and his body withers. With a \ngasp,"
                    " you watch as Whateley's body dissolves, leaving behind"
                    " only his tattered \nclothes and a blacked, winged"
                    " key.\n"

                    "\n'Raven's Wing Key' added to Inventory.\n")

                    whateley_status = False
                    looted_items.append("RW Key")
                    player_card['Inventory'].append("Raven's Wing Key")

                else:
                    type_text("\nWhateley's body has completely dissolved. If"
                    " it wasn't for his tattered robe \nlying on the ground"
                    " in front of you, you'd struggle to believe what you"
                    " saw.\n")

            else:
                type_text("\n'I can't do that now.'\n")

        elif cellar_choice.lower() == "i note":

            if "Whateley" in slain_enemies:
                type_text("\nYou pick up the note left on Whateley's"
                " makeshift bed. It appears to be a page \nripped from his"
                " journal:\n"

                "\n'Without the book's spells, I am unable to maintain the"
                " human half of my being. \nI shall have to relocate myself"
                " to the Cellar until Albert has managed to find \nit. I"
                " abhor hiding my true self from the insects of this town,"
                " but it is a \nnecessary sacrifice until I am able to bring"
                " our Banished Lord to this \nmisguided world. Once he has"
                " ushered in a generation of my kin, I will no \nlonger be"
                " seen as a monster, but a God.\n"

                "\nBut for now, without the book, I cannot proceed.\n"

                "\nI have instructed Albert to keep the vessel locked in the"
                " basement storage \nroom. It should be cold enough down"
                " there to preserve him, at least for a short \nwhile. Once"
                " the book has been found I will perform the final spell and"
                " complete \nthe ritual.\n"

                "\nYog-Sothoth guide me.'\n")

            else:
                type_text("\n'I can't do that now.'\n")

        elif cellar_choice.lower() == "n":

            if "Whateley" in slain_enemies:
                type_text("\nYou climb the steps to the North and head out"
                " the Cellar doors.\n")
                garden()
                break

            else:
                flee()

        elif cellar_choice.lower() == "help":
            print(help)

        elif cellar_choice.lower() == "pc":
            print(player_card)

        elif cellar_choice.lower() == "exit":
            main_menu()
            break

        elif cellar_choice.lower() == "heal":
            heal()

        else:
            type_text(generic_error)


def basement_a():
    """
    Basement A - First Section of the Basement
    """
    type_text("\nYou feel the air grow colder as you descend into"
    " the earth below the Hotel. The \nlift reaches the Basement level. With"
    " a 'ding' and a mechanical 'click', the \nlift settles and releases its"
    " lock. You slide the doors open again and step \ninto the Basement. The"
    " air is stale, and you feel the damp settling on your \nskin. Despite"
    " the restoration of power, the fluorescent bulbs overhead offer \nlittle"
    " beyond the occasional buzz and flicker of white light, revealing a"
    "\nnarrow corridor of bare brick and concrete.\n"

    "\nAt the end of the corridor is a red metal door with a small pane of"
    " reinforced \nglass at eye level. The door is locked in place with a"
    " heavy iron bar.\n")

    while True:

        basement_a_choice = input("\nEnter 'move' to move towards the"
        " door.\n")

        if basement_a_choice.lower() == "move":
            type_text("\nAs you approach the door the air grows thick with an"
            " oppressive, otherworldly \npresence. It feels heavy and"
            " difficult to breathe, with the acrid smell of \nsulphur and"
            " decay worsening as you go. An eerie silence pervades the"
            " corridor, \noccasionally broken by faint, unidentifiable"
            " whispers that seem to emanate from \nthe walls themselves.\n"
            "\nYou reach the door.\n")
            basement_b()
            break

        elif basement_a_choice.lower() == "help":
            type_text("\nI need to see if Chris is ok.\n")

        elif basement_a_choice.lower() == "pc":
            print(player_card)

        elif basement_a_choice.lower() == "exit":
            main_menu()
            break

        elif basement_a_choice.lower() == "heal":
            heal()

        else:
            type_text(generic_error)


def basement_b():
    """
    Basement B - Second Section of the Basement
    """
    type_text("\nYou peer in through the small window. At first you see"
    " nothing other than an \nempty storage room. Then, out of the shadows,"
    " Chris appears.\n"

    "\nYou instinctively cry out his name as sheer, overwhelming relief"
    " consumes you. \nYour brother is alive! But… something seems off. Why"
    " isn't he reacting to your \narrival? He's just standing there, several"
    " metres from the door, staring at you \nthrough the glass.\n"

    "\n'Chris?' You call out to him through the window. No reply. The light"
    " overhead \nflickers again, and in that blink of darkness, Chris appears"
    " the other side of \nthe window, his face less than an inch from yours."
    " You recoil in fright, \nletting out a cry as you jump away from the"
    " door. You see him more clearly now. \nHis skin is ashen and his eyes,"
    " two black pits. A smirk crawls across him lips. \nThis is not your"
    " brother anymore.\n")

    while True:

        basement_b_choice = input("\nDo you leave ('l') or open the door"
        " ('o')?\n")

        if basement_b_choice.lower() == "l":
            ending_spare()
            break

        elif basement_b_choice.lower() == "o":
            basement_c()
            break

        elif basement_b_choice.lower() == "help":
            type_text("\n'Chris... What have they done to you?'\n")

        elif basement_b_choice.lower() == "pc":
            print(player_card)

        elif basement_b_choice.lower() == "exit":
            main_menu()
            break

        elif basement_b_choice.lower() == "heal":
            heal()

        else:
            type_text(generic_error)


def basement_c():
    """
    Basement C - Third Section of the Basement
    """
    enemy.update(chris)

    type_text("\nYou remove the iron bar and prop it against the wall, before"
    " taking a step back \nfrom the door. Chris - or at least, the creature"
    " that possess him - slowly \npushes the door open and steps into the"
    " corridor, eyes fixed on you the whole \ntime. It feels as though an"
    " eternity passes by as the two of you stare at each \nother. Looking"
    " into his eyes, you find no trace of your brother there. Just the \nsame"
    " shimmer of sinister intelligence you saw in Whateley's eyes. You know"
    " what \nyou must do.\n")

    while True:

        basement_c_choice = input("\nEnter 'atk' to attack Chris.\n")

        if basement_c_choice.lower() == "atk":
            atk()

            if enemy['HP'] <= 0:
                basement_d()
                break

        elif basement_c_choice.lower() == "flee":
            type_text("\n'I can't just run from this!'\n")

        elif basement_c_choice.lower() == "help":
            type_text("\n'There's only one way this ends... I need to"
            " fight.'\n")

        elif basement_c_choice.lower() == "pc":
            print(player_card)

        elif basement_c_choice.lower() == "exit":
            main_menu()
            break

        elif basement_c_choice.lower() == "heal":
            heal()

        else:
            type_text(generic_error)


def basement_d():
    """
    Basement D - Final section of Basement
    """

    type_text("\nYou rush over to Chris' body and drop to your"
    " knees, checking to see if he's \nstill breathing. Holding"
    " your ear to his mouth, you hear a faint rasp and feel"
    "\nwarm breath on your cheek. He's weak, but alive. You"
    " don't have long.\n")

    if ("Cipher" in player_card['Inventory']) and \
    ("Necronomicon" in player_card['Inventory']) and \
    ("Spell Reversal" in player_card['Insight']):
        type_text("\nLooking down at your brother, tears blurring"
        " your vision, you suddenly remember \nwhat you read in"
        " Whateley's journal. He mentioned reversing the process"
        " of \nmaking someone a vessel by using a spell from the"
        " Necronomicon.\n"
        "\nYou hastily pull out the book you grabbed in the"
        " library and the cipher you \ntook from Chris' desk."
        " Frantically, you start searching through the pages to"
        "\nfind any reference to vessels or reversing spells. You"
        " eventually find a page \nthat looks like it could be"
        " what you're looking for. But even if it is... can \nyou"
        " wield this dark magic? And if so, what will it cost?\n")

        while True:

            ending_choice = input("\nWhat do you do?\n"

            "\nEnter 'kill' to put Chris out of his misery, and"
            " prevent whatever evil has \nrooted itself within"
            " him from spreading.\n"

            "\nEnter 'spare' to leave the Raven's Rest and spare"
            " Chris his life.\n"

            "\nEnter 'save' to try and reverse the spell that is"
            " transforming Chris into a \nvessel.\n")

            if ending_choice.lower() == "kill":
                ending_kill()
                return

            elif ending_choice.lower() == "spare":
                ending_spare()
                return

            elif ending_choice.lower() == "save":
                ending_save()
                return

            elif ending_choice.lower() == "pc":
                print(player_card)

            else:
                type_text("\n'I have to make a choice...'\n")

    else:
        while True:
            ending_choice = input("\nWhat do you do?\n"

            "\nEnter 'kill' to put Chris out of his misery, and"
            " prevent whatever evil has \nrooted itself within"
            " him from spreading.\n"

            "\nEnter 'spare' to leave the Raven's Rest and spare"
            " Chris his life.\n")

            if ending_choice.lower() == "kill":
                ending_kill()
                return

            elif ending_choice.lower() == "spare":
                ending_spare()
                return


def ending_kill():
    type_text("\nChris is gone. You have to accept that. Whatever twisted"
    " entity Whateley had \nbegun to weave into the fabric of his being…"
    " that's what you're seeing now. \nAnd after the horrors you've witnessed"
    " this evening, you know he can't ever \nleave this place.\n"

    "\nTears stream down your face as you remember the brother you loved."
    " Closing \nyour eyes and picturing the smiling face from the photograph"
    " in your pocket, \nyou bring an end to the evil that resides in Raven's"
    " Rest.\n")

    while True:
        
        type_text("\nThank you for playing. You've brought an end to the"
        " eldritch horror growing \nbeneath the Raven's Rest, but at a deep"
        " personal cost. Why not try again and \nsee if you can find a"
        f" happier ending for Chris and {player_card['Name']}?\n")

        game_over_choice = input("\nEnter 'ng' to start a new game from the"
        " Character Selection Menu.\n"

        "\nEnter 'exit' to return to the Main Menu.\n")

        if game_over_choice.lower() == "ng":
            reset_game_values()
            character_selection()
            return

        elif game_over_choice.lower() == "exit":
            reset_game_values()
            main_menu()
            return

        else:
            type_text("\nThat's not an option right now...\n")


def ending_spare():
    type_text("\nYou stare a long while at your brother. Despite the ashen"
    " skin and sunken \neyes, all you see is Chris. Everything you've been"
    " through this night - every \npain and horror endured - you did so to"
    " save him. You simply don't have it in \nyou to stop him.\n"

    "\nYou turn and head back to the service lift. Metal doors clang shut"
    " behind you. \nAscending to the ground floor of the hotel, you torture"
    " yourself with the \n'what if's. You know this basement won't hold him"
    " for long. Someone will find \nhim. All you can hope is that when they"
    " do, they have the will to do what you \ncouldn't. To put an end to the"
    " evil that resides in Raven's Rest.\n")

    while True:
        
        type_text("\nThank you for playing. You may have put a stop to"
        " dispicable Mr Whateley, but \nthe eldritch horror growing"
        " beneath the Raven's Rest lives on. Why not try \nagain and see if"
        " you can defeat the evil that has taken your brother, once and for"
        " all?\n")

        game_over_choice = input("\nEnter 'ng' to start a new game from the"
        " Character Selection Menu.\n"

        "\nEnter 'exit' to return to the Main Menu.\n")

        if game_over_choice.lower() == "ng":
            reset_game_values()
            character_selection()
            return

        elif game_over_choice.lower() == "exit":
            reset_game_values()
            main_menu()
            return

        else:
            type_text("\nThat's not an option right now...\n")


def ending_save():
    type_text("\nUsing Chris' cipher, you begin to read the spell - as best"
    " you can. Despite \nall you've seen tonight, the absurdity of you"
    " casting actual magic feels \nalmost too much to believe. Before today,"
    " you thought the occult only existed \nin books and movies. But as you"
    " speak the arcane words, your voice takes on a \nharmonious drone, as"
    " though many versions of you are speaking at once. The \nstale air of"
    " the basement seems to be given life, gusting up and down the"
    "\ncorridor, whipping at your clothes. The whispers of the walls grow"
    " louder and \nlouder until they are screaming, protesting your defiance"
    " of their Lord. You \nutter the last note of the spell, the drone of"
    " your voice and the rushing wind \ncoming to a crescendo and then…"
    " silence. The air dissipates. The wailing \nvoices cease.\n"

    "\nYou stand there in the anticlimax looking down at Chris, wondering if"
    " it \nworked. In the flickering fluorescent light, you fail to notice at"
    " first the \ngathering shadow beneath his body. Then you see it. The"
    " corruption. Gushing \nfrom your brother and spreading across the floor"
    " like ink from a shattered \nwell. It pools in the far end of the"
    " corridor, and you watch in horror as a \nbeing of slickened black"
    " begins to rise from the abyss. You hear the whispers \nbegin again,"
    " chanting their Lord's Name: 'Yog-Sothoth, Yo-Sothoth'. The \neldritch"
    " creature now stands as a man - albeit hunched and twisted - reaching"
    "\na black hand towards you. Shadows drip from the ethereal appendage."
    " Muttering \nit's foul language, it takes a lumbering step towards you."
    " It's body twitches \nand contorts unnaturally as it moves, as though"
    " pained with every moment of \nexistence. Your heart pounds as the blink"
    " of the fluorescent light snatches \nyou too and from darkness, making"
    " it impossible to track how quickly the \ncreature moves. You stand"
    " defiantly before your brother and brace for whatever \ncomes next. With"
    " a final lurch it falls before you, a blackened, slimy \nimitation of a"
    " man. A shadowy head rears up at you, revealing an aberrant"
    "\napproximation of a face, with only one eye and a crooked mouth. The"
    " wretched \ncreature lets out a final, agonising scream before crashing"
    " to the floor, a \nformless puddle of black. The shadow seems to drain"
    " away, seeping into the \nearth below. The whispers fade once more. You"
    " notice the light has stopped \nflickering, the constant hum of the bulb"
    " the only sound you now hear.\n"
 
    "\nWith a great gasp, as though surfacing from deep waters, Chris bolts"
    " upright. \nWide eyed, you stare at him, unsure what to expect. After a"
    " moment, his blank \nexpression regains some lucidity. He looks up at"
    " you.\n"

    f"\n{player_card['Name']}?\n")

    while True:

        type_text("\nCongratulations on saving Chris and putting a stop to"
        " the eldritch horror \ngrowing beneath the Raven's Rest! Your grit,"
        " determination and keen \ninvestigative prowess has led to you"
        " achieving the best outcome in the game. \nWhy not try again and see"
        " what other, less fortunate endings, you managed to \navoid.\n")

        game_over_choice = input("\nEnter 'ng' to start a new game from the"
        " Character Selection Menu.\n"

        "\nEnter 'exit' to return to the Main Menu.\n")

        if game_over_choice.lower() == "ng":
            reset_game_values()
            character_selection()
            return

        elif game_over_choice.lower() == "exit":
            reset_game_values()
            main_menu()
            return

        else:
            type_text("\nThat's not an option right now...\n")

# Title Screen
main_menu()
