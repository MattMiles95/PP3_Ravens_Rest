from pyfiglet import figlet_format
import time
import random

# Player Charater Option 1
lee_kennedy = {
    "Name": "Lee",
    "HP": 100,
    "Attack Power": random.randint(5, 10),
    "Weapon": "Unarmed",
    "Skill": "lockpick",
    "Inventory": ["flashlight"],
    "Insight": []
}

# Player Charater Option 1
claire_greenfield = {
    "Name": "Claire",
    "HP": 120,
    "Attack Power": random.randint(15, 20),
    "Weapon": "Unarmed",
    "Skill": "hack",
    "Inventory": ["flashlight"],
    "Insight": []
}

# Populated once Player Character selected
player_card = {
    "Name": "",
    "HP": 100,
    "Attack Power": 10,
    "Weapon": "Unarmed",
    "Skill": "",
    "Inventory": [],
    "Insight": []
    }

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

cultist_chris_room = {
    "ID": "Cultist (Chris Room)",
    "Name": "Jawless Cultist",
    "HP": 40,
    "Attack Power": random.randint(15, 25)
}

cultist_library = {
    "ID": "Cultist (Library)",
    "Name": "Mutilated Cultist",
    "HP": 40,
    "Attack Power": random.randint(10, 20)
}

mr_whateley = {
    "ID": "Mr Whateley",
    "Name": "Mr Whateley",
    "HP": 100,
    "Attack Power": random.randint(25, 35)
}

chris = {
    "ID": "Chris",
    "Name": "Chris",
    "HP": 120,
    "Attack Power": random.randint(35, 45)
}

# Help variable, for use in game
help = (
"\nHere are a few common commands you will use:\n" 
"\n(Not all of these can be used all \nof the time - for example, you can't"
" move north if there's nowhere north to go!)\n"
"\nEnter 'exit' to quit to main menu."
"\nEnter 'pc' to view Player Card."
"\nEnter 'n', 'e', 's', 'w', to move north, east, south and west."
"\nEnter 'l' to look around."
"\nEnter 'i' followed by an OBJECT to interact with that OBJECT."
"\nEnter 'heal' to use a First Aid Kit."
"\nEnter 'atk' to attack."
"\nEnter 'flee' to escape a fight in a random direction.\n"
"\nHINT: The 'l' command is great if you need a clue as to what you can do in"
" the room you're in!\n")

generic_error = ("\nYou can't do that... Use the 'help' command if you're "
"stuck, or 'l' to look around for clues.\n")

# Global functions for repeated actions
def fa_kit_loot(): 
    """
    Adds First Aid Kit to player inventory
    """
    player_card["Inventory"].append("First Aid Kit")
    type_text("\nYou rummage through the First Aid Kit and take some "
    "supplies.\n")
    return

def heal():
    """
    Uses a First Aid Kit to heal 30 HP
    """
    if "First Aid Kit" in player_card["Inventory"]:
        player_card["HP"] += 30
        player_card["Inventory"].remove("First Aid Kit")
        type_text("\nYou use a First Aid Kit and heal 30 HP.\n")
        return
    else:
        type_text("\nYou don't have any First Aid Kits!\n")

def atk():
    """
    Function for Player to attack Enemy
    """
    # Vary Enemy Attack Power per Attack
    if enemy["ID"] == "Cultist (Bar)":
        enemy["Attack Power"] = random.randint(10, 20)
    elif enemy["ID"] == "Cultist (Chris Room)":
        enemy["Attack Power"] = random.randint(15, 25)
    elif enemy["ID"] == "Cultist (Library)":
        enemy["Attack Power"] = random.randint(10, 20)
    elif enemy["ID"] == "Mr Whateley":
        enemy["Attack Power"] = random.randint(25, 35)
    elif enemy["ID"] == "Chris":
        enemy["Attack Power"] = random.randint(35, 45)
        
    # Vary Player Attack Power per Attack
    if player_card["Weapon"] == "Unarmed":
        if player_card["Name"] == "Claire":
            player_card["Attack Power"] = random.randint(10, 20)
        else:
            player_card["Attack Power"] = random.randint(1, 10)
    elif player_card["Weapon"] == "Bloody Knife":
        player_card["Attack Power"] = random.randint(10, 20)
    elif player_card["Weapon"] == "Pitchfork":
        player_card["Attack Power"] = random.randint(20, 30)
    elif player_card["Weapon"] == "Handgun":
        player_card["Attack Power"] = random.randint(30, 40)
    elif player_card["Weapon"] == "Shotgun":
        player_card["Attack Power"] = random.randint(35, 50)

    if enemy["ID"] in slain_enemies:
        type_text(f"{enemy['Name']} is already dead!")
    else:
        enemy["HP"] = enemy["HP"] - player_card["Attack Power"]
        type_text(f"You hit {enemy['Name']} for {player_card['Attack Power']}")
        if enemy["HP"] <= 0:
            type_text(f"\nWith a final rasping breath, {enemy['Name']} drops "
            "to the floor, his BODY cold and still.\n")
            slain_enemies.append(enemy["ID"])
            return
        else:
            player_card["HP"] = player_card["HP"] - enemy["Attack Power"]
            type_text(f"{enemy['Name']} hit you for {enemy['Attack Power']}")
            if player_card["HP"] <= 0:
                game_over()
            else:
                type_text(f"You have {player_card["HP"]} remaining HP."
                " Attack again or flee?\n")
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
            
#def end_game_good():

#def end_game_bad():

def type_text(text):
    """
    Prints text one character at a time to create a 'typing' animation.
    """
    #for char in text:
    #    print(char, end='', flush=True)
    #    time.sleep(random.uniform(0.001, 0.09))
    print(text)

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
    "\nIf this is your first time playing, please be sure to read the rules before"
    "\nyou start.\n"
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
    type_text("\nRaven's Rest is a text-based adventure game. You control your"
    " character by \nentering commands in the terminal. The goal is to"
    " navigate the Raven's Rest \nHotel and find your brother, completing"
    " puzzles and defeating enemies as you go.\n"
    "\nHere are the rules:\n")

    print(figlet_format("How to Play\n", justify="center"))

    type_text("\n1. Mind your manners! Don't interrupt your GM. If you type"
    "\nwhilst Poe is typing, you might cause an error, preventing your"
    "\nnext command from being recognised. Let him finish before typing"
    "\nanything.\n"
    "\n2. If you type something that isn't a command, you'll be prompted"
    "\nto try again.\n"
    "\n3. You can quit to the main menu at any time by using the 'exit'"
    "\ncommand. But be aware, you'll lose all progress and there's no way to"
    "\nreload a previous game.\n"
    "\n4. If you get stuck, type 'help' to see a list of commands you"
    "\ncan use.\n"
    "\n5. Once you start the game, you will have to select a character."
    "\nTake note of your character's bio, as their individual skills and"
    "\nexperiences might be useful later on.\n"
    "\n6. You can bring up your character's 'Player Card' at any time"
    "\nby using the 'pc' command. Here you'll see your character's current"
    "\nstats and any items in your inventory.\n"
    "\n7. The Raven's Rest can be a dangerous place. Your 'Attack Power'"
    "\nstat determines how much damage you can do in a single attack."
    "\nBe sure to pick up any weapons you might find to help you deal"
    "\nmore damage.\n"
    "\n8. Keep an eye on your HP. If it drops to zero, that's"
    "\ngame over. Healing items can be found and used to keep you going.\n"
    "\nThe following are common commands you'll use throughout the game:\n")
    
    type_text(help)

    type_text("\nThis list is not exhaustive. It just gives examples of common"
    "\ncommands you'll use. Remember to use the 'help' command if you get"
    "\nstuck, or consult your Player Card by using the 'pc' command to see if"
    "\nyour character has a skill or item that might be useful.\n"
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
        character_choice = input("\nType 'l' for Lee or 'c' for Claire:")

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
        else:
            character_choice_error = "\nI don't know that one...\n"
            type_text(character_choice_error)     

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
    "\nInnsmouth, England\n"
    "\nYou wake with a jolt to the sound of knuckles rapping on glass. Sat in"
    " a \ncarriage being drawn by two horses - a far cry from the black cabs"
    " you're used \nto in London - you peer out of the window. Presumably the"
    " carriage driver was \nletting you know that you're approaching your"
    " destination, but there's no way \nof knowing that by looking outside."
    " Nights never get this dark in the city, \nbut here in Innsmouth, you may"
    " as well be staring into a pot of ink. Add to \nthat the heavy rain"
    " beating against the glass, and trying to make out anything \nbeyond the"
    " dimly light interior of the carriage was truly an exercise in"
    "\nfutility.\n"
    "\nYou remove a PHOTOGRAPH from your jacket pocket. It's a picture of your"
    "\nbrother, Chris. The last time he was seen or heard from. He's grinning"
    " at the \ncamera and giving a cheery thumbs up. Behind him, lurking like"
    " a shadow, lies \na dark building. You can just about make out a sign" 
    " that reads, 'Raven's Rest'.\n")

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
    f"\n{player_card["Name"]},\n"
    "\nThink I've finally made some headway with the article… Currently"
    " visiting a \nchap in Innsmouth who apparently knew one of the students"
    " that went missing - \nhis brother in fact! I'm staying at an old hotel,"
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
            player_card["Inventory"].append("photograph")
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
    type_text("\nYou slide the photograph back into your pocket. A loud crunch"
    " comes from the \nwheels as the carriage veers off the road and onto a"
    " gravel track. Bouncing \nuncomfortably on the bench for a minute or so,"
    " you're relieved when the horses \ncome to a halt. A thin grate on the"
    " driver's side of the carriage slides open.\n"
    "\n'Make it quick,' he says. 'The horses are spooked.'\n"
    "\nYou swing open the door and step into the stormy night, tossing the"
    " driver's \nfare into a cup on the way out. You're immediately bitten by"
    " the cold and \nfumble with your collar to turn it against the wind and"
    " rain.\n"
    "\n'What's got them spooked?' you call out, fighting to be heard over the"
    " weather.\n"
    "\n'You'll find out soon enough, I'm sure.' He called back. With that, he"
    " spurred \nhis horses and set off. It seems to you as though it wasn't"
    " just the horses \nthat were spooked. As the carriage draws away with its"
    " lantern, so does your \nonly source of light. You're quickly plummeted"
    " into pitch darkness.\n"
    "\nEnter 'pc' to open your Player Card and view your inventory.\n")

    while True:
        intro_c_choice = input()
        global flashlight 

        if intro_c_choice.lower() == "pc":
            print(player_card)
            type_text("\nA flashlight! That'll help. Enter 'use"
            " flashlight'.\n")
        elif intro_c_choice.lower() == "use flashlight":
            if flashlight == True:
                type_text("\nYou've already swithced your flashlight on. Try"
                " entering 'l' to look around.\n")
            else:
                type_text("\nYou pull your flashlight from your pocket and"
                " switch it on. A beam of bright \nlight bursts forth, slicing"
                " through the dark like a butcher's knife.\n"
                "\nEnter 'l' to look around.\n")
                flashlight = True
        elif intro_c_choice.lower() == "l":
            if flashlight == True:
                type_text("\nYou're stood in a small, wooded enclosure, just"
                " off the gravel track. A path \nthrough the trees to the"
                " north appears to be your only choice forward.\n"
                "\nEnter 'n' to walk northwards.")
            else:
                type_text("\n'I can't see a thing!'\n")
        elif intro_c_choice.lower() == "n":
            if flashlight == True:
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
            if flashlight == True:
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
    " eyes follow the slate grey walls, receding into the \ndarkness above. As"
    " though the hotel seems much larger than it really is.\n"
    "\nEventually you come across a long wooden porch that leads you to the"
    " hotel \nentrance. Double black DOORS set against white wooden slats. In"
    " the gloom of \nnight, it looks like the gaping maw of a beast. 'Raven's"
    " Rest', is scrawled in \nblack lettering above the DOORS.\n")

    while True:
        intro_d_choice = input("\nEnter 'i doors' to open the DOORS and enter the"
        " Raven's Rest.\n")

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
    The Hotel Foyer - the first room the Player enters.
    """
    foyer_text_initial = ("\nYou step into a wide, empty Foyer. The beam of"
    " your flashlight barely \npenetrates the surrounding shadows as you pan"
    " across the room. Ahead of you \nbeneath the gloomy red glow of an"
    " emergency lamp, you see the reception DESK."
    "\nOn both the EAST and WEST sides of the room are doors leading out of"
    " the Foyer.\n")

    foyer_text_return = ("\nYou step again into the wide, empty Foyer.\n")

    if "Foyer" in checked_rooms:
        type_text(foyer_text_return)
    else:
        type_text(foyer_text_initial)
        checked_rooms.append("Foyer")

    foyer_look = ("\nYou look around the Foyer. You see the reception DESK"
    " ahead of you. A door to \nthe east ('e') with a sign that reads, 'East"
    " Wing, Maintenance and Bar'. A door to \nthe west ('w') with a sign that"
    " reads, 'West Wing and Library'. Behind you, to \nthe south ('s'), is the"
    " Hotel entrance.\n")

    desk_inspect = ("You approach the desk for a closer look. A COMPUTER and"
    " a BELL sit on the desk. \nBehind the desk is a DOOR with a sign that"
    " reads, 'Staff Only'.\n")

    def foyer_computer_use():
        if power == True and player_card["Skill"] == "hack":
            foyer_computer()
        elif power == True and player_card["Skill"] == "lockpick":
            type_text("\nThe computer is locked.\n")
        elif power == False:
            type_text("\nThe power is still out. Maybe you can find a way to"
            " turn it back on...\n")

    def foyer_door_use():
        if player_card["Skill"] == "lockpick":
            type_text("\nThe door is locked, but you manage to pick it.\n")
            foyer_staff_cupboard()
        elif player_card["Skill"] == "hack":
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
            type_text("\nYou exit out of the east door.\n")
            east_wing()
            break
        elif foyer_choice.lower() == "w":
            type_text("\nYou exit out of the west door.\n")
            west_wing()
            break
        elif foyer_choice.lower() == "s":
            if chris_status == "alive":
                end_game_good()
            elif chris_status == "dead":
                end_game_bad()
            elif chris_status == "vessel":
                end_game_bad()
            else:
                type_text("I'm not leaving until I've found Chris.")
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
        else:
            type_text(generic_error)

def foyer_computer():
    """
    The Foyer Computer - Options
    """
    type_text("\nThe computer is locked, but you manage to hack it.")
    
    while True:
        foyer_computer_choice = input("\nEnter 'rooms' to see reservation"
        " list.\n"
        "\nEnter 'messages' to see saved massages.\n"
        "\nEnter 'back' to log off computer.")

        if foyer_computer_choice.lower() == "rooms":
            if "Raven's Rest Owner Name" in player_card["Insight"]:
                type_text("\nYou flick through some files and discover Chris'"
                " room number, located in the \nWest Wing. You also notice"
                " that Mr Whateley, the owner, has a room adjacent to \nthe"
                " Library.\n")
                player_card["Insight"].append("Chris' Room Location")
                player_card["Insight"].append("Whateley's Room Location")
                type_text("\n'Chris' Room Location' added to Insight.\n")
                type_text("\n'Whateley's Room Location' added to Insight.\n")
            elif "Chris' Room Location" in player_card["Insight"]:
                type_text("You've already read these files.")
            else:
                type_text("\nYou flick through some files and discover Chris'"
                " room number, located in the \nWest Wing.")
                player_card["Insight"].append("Chris' Room Location")
                type_text("\n'Chris' Room Location' added to Insight.\n")
        elif foyer_computer_choice.lower() == "messages":
            type_text("\nYou find a message that reads:\n"
            "\nDear employees,\n"
            "\nI understand there has been some confusion about the new"
            " locking systems I've \nhad installed. Whilst I appreciate that"
            " some of you may find them \n'impractical', or perhaps even"
            " 'excessive', may I remind you that we have a \ncertain aesthetic"
            " to maintain here in the Raven's Rest. To that end, please"
            "\nremember:\n"
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
            foyer()
            break
        elif foyer_computer_choice.lower() == "help":
            print(help)
        elif foyer_computer_choice.lower() == "pc":
            print(player_card)
        elif foyer_computer_choice.lower() == "exit":
            main_menu()
            break

def foyer_staff_cupboard():
    """
    The Foyer Staff Cupboard - Game Location.
    """
    foyer_staff_cupboard_text_initial = ("\nThe door leads into a small"
    " cupboard space. Whilst inspecting, the beam of your \nflashlight passes"
    " over something slumped on the floor. Your heart sinks. It's a \ndead"
    " BODY. A bloody KNIFE protruding from the side of it's neck.\n")

    foyer_staff_cupboard_text_return = ("\nYou enter the cupboard, trying your"
    " best not to look at the dead BODY.\n")

    if "Foyer Staff Cupboard" in checked_rooms:
        type_text(foyer_staff_cupboard_text_return)
    else:
        type_text(foyer_staff_cupboard_text_initial)
        checked_rooms.append("Foyer Staff Cupboard")

    while True: 
        foyer_staff_cupboard_choice = input("\nWhat do you do? (If you're"
        " stuck, try using the 'l' command to look around.)\n")

        if foyer_staff_cupboard_choice.lower() == "l":
            if "Bloody Knife" in looted_items:
                type_text("\nA dead BODY lies slumped on the floor. The foyer"
                " is to your south ('s').\n")
            else: 
                type_text("\nYou take a moment to collect yourself, then look"
                " around the cupboard. The \nbloody KNIFE sticks out of the"
                " dead BODY's neck. The foyer is to your south \n('s').\n")
        elif foyer_staff_cupboard_choice.lower() == "help":
            print(help)
        elif foyer_staff_cupboard_choice.lower() == "pc":
            print(player_card)
        elif foyer_staff_cupboard_choice.lower() == "exit":
            main_menu()
            break
        elif foyer_staff_cupboard_choice.lower() == "heal":
            heal()
        elif foyer_staff_cupboard_choice.lower() == "i body":
            type_text("\nYou take a closer look at the body. It's a young"
            " man, probably in his 20s. He \nlooks to be one of the staff"
            " members of the Hotel. His name tag reads, 'Jack'.\n")
        elif foyer_staff_cupboard_choice.lower() == "i knife":
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
                player_card["Weapon"] = "Bloody Knife"
                player_card["Attack Power"] = random.randint(10, 20)
        elif foyer_staff_cupboard_choice.lower() == "s":
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
    " adorned with silver room numbers \nrun along both sides of the corridor."
    " There is no trace of any patron or \nemployee. As you creep through the"
    " silent passage, you notice a Supplies \nCupboard to the south ('s')." 
    " Further east ('e') appears to be a Maintenance \nRoom. To the north"
    " ('n') are a set of double doors, leading to the Bar. To the \nwest ('w')"
    " is the Foyer.\n")

    east_wing_return = ("\nYou step into the East Wing.\n")

    newspaper_inspect = ("You take a closer look at the newspaper. 'The"
    " Innsmouth Daily'. The headline \nreads, 'BODY SNATCHER STRIKES AGAIN?"
    " FOURTH MISSING PERSON REPORTED THIS YEAR'. \nYou flick through the"
    " paper, pausing when your eye is caught by a picture of \nthe Raven's"
    " Rest. The caption reads 'One year since the Raven's Rest came under"
    "\nnew management. New owner Mr Whateley says he has 'big plans' for the"
    " hotel'.\n")

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
            "\nTo the north ('n') is a set of double doors leading"
            " to the Bar.\n"
            "\nTo the east ('e') is the Maintenance Room.\n"
            "\nTo the south ('s') is a Supplies Cupboard.\n"
            "\nTo the west ('w') is the Foyer.\n")
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
            type_text(newspaper_inspect)
            player_card["Insight"].append("Raven's Rest Owner Name")
            type_text("\n'Raven's Rest Owner Name' added to Insight.\n")
        elif east_wing_choice.lower() == "n":
            type_text("\nYou pass through the double doors into the Bar.\n")
            bar()
            break
        elif east_wing_choice.lower() == "e":
            if "Raven's Beak Key" in player_card["Inventory"]:
                type_text("\nYou use the Raven's Beak Key to access the"
                " Maintenance Room.\n")
                maintenance_room()
                break
            else:
                if player_card["Skill"] == "lockpick":
                    type_text("\nThis door is locked with a strange mechanism."
                    " It looks like the key would need \nto be beak"
                    " shaped...\n")
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
            if "First Aid Kit EW" in looted_items:
                type_text("\nThere's nothing else of use here. The East Wing"
                " is to your north ('n').\n")
            else: 
                type_text("\nA FIRST AID KIT sits on the shelf. The East Wing"
                " is to your north ('n').\n")
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
            if "First Aid Kit SC" in looted_items:
                type_text("\nYou've already taken the First Aid Kit.\n")
            else:
                fa_kit_loot()
                looted_items.append("First Aid Kit SC")
                type_text("\nAs you put the First Aid Kit back, a previously"
                " hidden note is knocked to the floor. It reads:\n"
                "\nJill,\n"
                "\nThings here have been getting weirder and weirder lately."
                " I was working a shift \nthe other night, and when I went for"
                " a smoke in the Garden, I could've sworn I \nheard chanting"
                " coming from the Cellar. And those freaks with the black"
                " robes \n- I still get shivers when I remember seeing them"
                " come up from the basement. \nThe screams I heard coming from"
                " down there... I'm still sure it's got something \nto do with"
                " all these missing people. And I'm not waiting around to be"
                " the next \nface on a 'Missing' poster. Apparently Whateley's"
                " got a hidden safe somewhere \nin his room - I'm breaking in"
                " there tonight, clearing out anything worth a damn \nand"
                " getting the hell out of this town. I'll be gone by the time"
                " you read this, \nbut if you know what's good for you, you'll"
                " follow my lead.\n"
                "\nSerious, get out before it's too late.\n"
                "\n- Jack\n")
                player_card["Insight"].append("Hidden Safe Location")
                type_text("\n'Hidden Safe Location' added to Insight.\n")
        elif supplies_cupboard_choice.lower() == "n":
            type_text("\nYou exit to the north, returning to the East Wing.\n")
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
            if power == True:
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
            if power == True:
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

    bar_return = ("\nYou cautiously creep back into the bar. Immediately you spot"
    " the \nmutilated man, frantically searching around with his hands"
    " outstretched.\n")

    bar_safe = ("\nYou step into the bar. To the west, a door leads into the Garden. Behind you, to the south, is the East Wing.\n")

    if "Cultist (Bar)" in slain_enemies and "Bar" in checked_rooms:
        type_text(bar_safe)
    elif "Cultist (Bar)" not in slain_enemies and "Bar" in checked_rooms:
        enemy.update(cultist_bar)
        type_text(bar_return)
    else:
        enemy.update(cultist_bar)
        checked_rooms.append("Bar")
        type_text(bar_initial)
        flashlight = False
        type_text("\nEnter 'use flashlight' to turn on your flashlight.\n")

    while True:
        bar_choice = input()

        if bar_choice == "use flashlight":
            if flashlight == True:
                type_text("\nYour flashlight is already on!\n")
            elif power == False and flashlight == False:
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
            if flashlight == True and enemy not in slain_enemies:
                atk()
            elif flashlight == False and power == False:
                type_text("\n'I can't see a thing!'\n")
            else:
                type_text(generic_error)
        elif bar_choice.lower() == "flee":
            if flashlight == True and enemy not in slain_enemies:
                flee()
                break
            elif "Cultist (Bar)" in slain_enemies:
                type_text("\nThere's nothing to run from right now.\n")
            elif flashlight == False and power == False:
                type_text("\n'I can't see a thing!'\n")
            else:
                type_text(generic_error)
        elif bar_choice.lower() == "l":
            if flashlight == False and power == False:
                type_text("\n'I can't see a thing!'\n")
            elif flashlight == True and "Cultist (Bar)" not in slain_enemies:
                type_text("\nNow's not the time for looking around!\n")
            elif "Cultist (Bar)" in slain_enemies:
                type_text("\nThe BODY of the mutilated man lies still on the"
                " floor, a puddle of crimson \ngrowing beneath him. To the"
                " west, you see a door that leads outside. The sign \nnext to"
                " it reads, 'Garden area this way'. At the far end of the room"
                " is a \nrather impressive BAR, with plenty of expensive"
                " looking bottles on display. The \ndoor to East Wing is to"
                " your south.\n")
            else:
                type_text(generic_error)
        elif bar_choice.lower() == "i bar":
            if flashlight == False and power == False:
                type_text("\n'I can't see a thing!'\n")
            else:
                type_text("\nYou creep over to the bar to have a closer look."
                " Behind the bar, you spot a LEDGER that looks to show"
                " people's open tabs.\n")
        elif bar_choice.lower() == "i ledger":
            if flashlight == False and power == False:
                type_text("\n'I can't see a thing!'\n")
            else:
                type_text("\nInspecting the ledger, you find Chris' name. His"
                " room number is written in the \ncolumn next to it.\n")
                if "Chris' Room" not in player_card["Insight"]:
                    player_card["Insight"].append("Chris' Room Location")
                    type_text("\n'Chris' Room Location' added to Insight.\n")
        elif bar_choice.lower() == "i body":
            if "Cultist (Bar)" in slain_enemies and "Raven's Beak Key" not in player_card["Inventory"]:
                type_text("\nYou crouch down and rummage through the dead"
                " man's robes. You find a strange, beak shaped key in his"
                " pocket.\n"
                "\n'Raven's Beak Key' added to Inventory.\n")
                player_card["Inventory"].append("Raven's Beak Key")
            elif "Cultist (Bar)" in slain_enemies and "Raven's Beak Key" in player_card["Inventory"]:
                type_text("\nYou've already looted this body for anything"
                " usesful.\n")
            else:
                type_text("\n'I can't do that now.'\n")
        elif bar_choice.lower() == "s":
            if flashlight == False and power == False:
                type_text("\n'I can't see where I'm going!\n")
            elif flashlight == True and "Cultist (Bar)" not in slain_enemies:
                type_text("\nIn your panic, you flee in a random direction.\n")
                flee()
                break
            else:
                type_text("\nYou leave out the south door to the East Wing.\n")
                east_wing()
                break
        elif bar_choice.lower() == "w":
            if flashlight == False and power == False:
                type_text("\n'I can't see where I'm going!\n")
            elif flashlight == True and "Cultist (Bar)" not in slain_enemies:
                type_text("\nIn your panic, you flee in a random direction.\n")
                flee()
                break
            else:
                type_text("\nYou leave out the west door to the Garden.\n")
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
    if power == True:
        flashlight = True
        type_text("\nStepping into the dark and stormy night, you turn your flashlight on.\n")

    garden_initial = ("\nA sense of relief washes over you as you escape into"
    " the downpour outside. It's \na welcome break from the oppressive hotel,"
    " which felt as though it had \nswallowed you whole. You take a moment to catch"
    " your breathe. Feeling the sting \nof cold wind and rain on your face"
    " reassures you that you're not simply trapped \nin a nightmare. After a"
    " moment, you allow your mind to be dragged back to the \nhorrors of the"
    " Raven's Rest and the task at hand. Sweeping the beam of your"
    "\nflashlight across the garden, you make out a tall hedge that runs the"
    " perimeter. \nAn impressive water fountain takes the pride of the garden"
    " space, sporting an \nelegent statue of (rather predictably) a raven at"
    " it's centre. Benches are \nscattered throughout the garden, with several"
    " FLOWER BEDS dotted around. \nTo the west, a set of doors lead into the"
    " Hotel's Library. The Bar is to the \neast. In between these doors, up"
    " against the southern wall of the Hotel, you \nsee the entrance to the"
    " cellar.\n")

    garden_return = ("\nYou step outside into the wind and rain, glad to"
    " escape the suffocating \ninterior of the Raven's Rest for a while.\n"
    "\nTo the west is the Library.\n"
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
            "\nTo the west is the Library.\n"
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
            type_text("\nYou inspect a nearby flowerbed. Unusual plants seem to"
            " be growing here. Thick \npurple stems support dark, drooping"
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
                player_card["Weapon"] = "Pitchfork"
                player_card["Attack Power"] = random.randint(20, 30)
        elif garden_choice.lower() == "w":
            if power == True:
                type_text("\nYou switch off your flashlight before heading"
                " into the Library.\n")
                flashlight = False
            else:
                type_text("\nYou head through the western door into the"
                " Library.\n")
            library()
            break
        elif garden_choice.lower() == "e":
            if power == True:
                type_text("\nYou switch off your flashlight before heading"
                " into the Bar.\n")
                flashlight = False
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

# Title Screen
#main_menu()

# Determines if the hotel has power
power = False

# Determines if the player's flashlight is on
flashlight = False

# In-game feature to determine Chris' status
chris_status = "Unknown"

character_selection()