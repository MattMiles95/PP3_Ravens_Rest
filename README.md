# Raven's Rest

![Game Demo](/assets/readme-images/ravens_rest_title_screen.png)

Raven's Rest is a text-based adventure game with a strong narrative focus, adopting the 'cosmic horror' genre popularised by H.P. Lovecraft and taking functional inspiration from game design of the Resident Evil franchise.

When launching the app, the Player will be met with the title screen. This features ASCII art of a raven besides the game’s title, a short introduction to the game, and a choice of either viewing the ‘how to play’ section or diving right into the game.
Once the game has started, the Player will have the option of two characters. Each character experiences the same story but plays slightly differently, based on their individual character traits. The player is advised to be mindful of this when making their selection.

Beyond the character selection menu, the Player will then have the choice of playing through the introduction (which acts as a gameplay tutorial whilst also providing narrative exposition),  or skip straight to the first gameplay area (where they can begin exploring the titular Raven’s Rest Hotel).

Once the game begins proper, signalled by the Player Character entering the Raven’s Rest, they have complete freedom to explore the hotel in whatever order (and in however much detail) they like. The game rewards exploration and attention to detail with items that the Player Character can use, such as weapons and first aid kits. As the player explores, they will add key items to their ‘inventory’ and knowledge to their ‘insight’, both of which will be used to unlock previously hidden areas of the game – and even different endings. All Player stats (including health points (HP), attack damage, equipped weapon, skills, inventory and insight), are visible in the Player Card, which can be opened at any time by entering the command: ‘pc’.

Overall, Raven’s Rest is designed to be a fun and rewarding, interactive experience with a good incentive for multiple playthroughs. Whilst it requires a methodical approach to achieve the best ending, the game focuses more on investigative gameplay than outright difficulty. As such, the game is highly accessible for even the least experienced gamers. Due to the cosmic horror theme of the game, however, it is not appropriate for all ages (namely young children). 


[Play the Raven's Rest live project here.](https://ravens-rest-179aff4eb889.herokuapp.com/)

## Table of Contents

### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Logic Design](#logic-design-1)
### [Features](#features-1)
* [Title Screen](#title-screen)
* [The Play Button](#the-play-button)
* [Choice of Card Deck](#choice-of-card-deck)
* [The Game](#the-game)
* [Start of the Game](#start-of-the-game)
* [The Cards](#the-cards)
* [User Buttons Panel](#user-buttons-panel)
* [Round Results](#round-results)
* [Scoreboard](#scoreboard)
* [Game Over](#game-over)
* [Options Buttons](#options-buttons)
* [Gameplay Mechanics](#gameplay-mechanics)
* [SFX](#sfx)
* [Favicon](#favicon)
### [Future Features](#future-features-1)
* [Developer Features](#developer-features)
* [User Features](#user-features)
### [Technologies Used](#technologies-used-1)
* [Languages](#languages)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
* [Validators](#validators)
* [Lighthouse Testing](#lighthouse-testing)
* [Manual Testing](#manual-testing)
* [Bugs & Fixes](#bugs-and-fixes)
### [Local Development & Deployment](#local-development--deployment-1)
* [Local Development](#local-development)
* [Deployment](#deployment)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
* [Affiliations](#affiliations)
* [Copy (Written Material)](#copy-written-material)
* [Media](#media)
* [Online Resources](#online-resources)

### User Experience (UX)
Raven's Rest combines narrative focused gameplay with light puzzle and combat mechanics. Players are encouraged to explore each game area and complete investigative-based puzzles, and in return they are rewarded with items that will aid them in each combat encounter. Combat is a simple turn-based system, where the Player's 'attack power' is determined by the weapon they have equipped, and the enemy's 'attack power' is determined by the enemy type (with each enemy having different stats).  

#### User Stories

##### Initial User Goals – First Impressions
* Immediately recognise the genre, themes and format of the game 
* Easily navigate the game’s features
* Evoke intrigue in the game's design and narrative

##### Established User Goals – Once They’ve Stayed 
* Provide enjoyable and rewarding gameplay that holds the User's attention
* Establish a desire for replayability
* Offer enough variety in gameplay to keep the user engaged without creating unwanted complexity

### Logic Design

When designing Raven's Rest, I used flowcharts to help me visualise both the logic-structure of the app and the logic design of the game itself (i.e., a 'map' of the Hotel detailing how each gameplay area is connected).

![App Logic Flowchart](/assets/readme-images/ravens_rest_logic_flowchart.png)

![Game Design Logic Map](/assets/readme-images/ravens_rest_logic_map.png)

### Features

#### Title Screen

The Title Screen is the first thing the User will see when launching the app. It features ASCII Art of a raven stood beside the game's title - Raven's Rest. Below this is a brief introduction to the game, followed by the option to either jump straight into the game, or first read through the 'How to Play' section. 

#### How to Play

The 'How to Play' section describes the funcitions of a text-based adventure game, general rules to follow to ensure the game runs correctly, and offers a list of common commands you'll use throughout the game.

#### Character Selection

Raven's Rest features two playable characters, each with their own unique features. Once the User chooses to start the game, they will need to choose which character to play as. The differences of each character are presented to the Player (with some gameplay differences alluded to but not explicitly stated), and then it is for the Player to decide who they want to choose.

#### Intro & Tutorial

Once the Player has selected their character, they will be able to choose whether to playthrough the intro or skip straight to the start of the main game. The intro offers some exposition on the games characters and narrative, whilst also acting as a tutorial for the common commands and conventions the Player will encounter during the game.

#### Gameplay

After completion of the intro (or opting to skip this segment), the Player will begin the main game. This is signalled by the Player Character entering the Raven's Rest Hotel - the explorable area in which the game takes place. The objective of the game is to locate your character's missing brother by investigating each room of the Hotel and uncovering clues that will ultimately lead you to him. Along the way, the Player will need to solve puzzles and defeat enemies, using the game's simplistic but fun combat system. Gameplay can be broken down into 4 components:

* Investigating
* Puzzle solving
* Combat encounters
* Equipment management

##### Investigating

This gameplay component requires the Player to investigate each room thoroughly, uncovering clues as to your brother's location and the overall narrative. This is achieved by looking around each room and interacting with your environment. Certain objects cannot be interacted with fully until certain prerequisites have been met (i.e., not being able to open a door until the correct key has been obtained). If the Player Character does not meet the relevant prerequisites to interact with an object, they will instead be given a clue as to what to do next.

##### Puzzle Solving

This gameplay component goes hand in hand with the last. As the player investigates, they will uncover puzzles that need solving in order to progress. These puzzles take the form of narrative obstacles that the Player must overcome. For example, to access the Basement area of the game (where the conclusion takes place), the Player Character must first restore power to the hotel and obtain a special key, thus allowing them to unlock and use the service lift to access the Basement. 

##### Combat Encounters

Throughout the game, the Player Character will be confronted by several enemies, each with their own unique stats. Of the 5 enemies within the game, two are optional. 

When in a room with a hostile enemy, the Player Character will not be able to do certain things, such as investigate that room. For this reason, Players are incentivised to defeat even the optional enemies, as the rewards will always be worth the fight.

When in a combat encounter, the Player has access to two unique commands: 'atk' and 'flee'. 'Atk' causes the Player Character to attack the enemy, dealing damage them. Once the enemy's health (which is hidden from the Player) reaches or drops below 0, that enemy is defeated and all locked commands are made available again. However, with each attack the Player makes, the enemy will retaliate (provided they are not defeated by the Player's attack). If the Player Character's Health Points (HP) reaches 0, it is Game Over.

Rather than having absolute values, each Player Character, Weapon and Enemy have a set scope for attack power. For example, when unarmed, Lee can hit for 1 - 10 points of damage. Claire on the other hand, whose listed hobby in the Character Selection menu is 'kickboxing', has an unarmed attack power of 10 - 20. This provides an element of unpredictability with every encounter, as your success or failure may come down to the roll of a dice (metaphorically). 

As well as dealing damage, Players will have to focus on maintaining their character's health too. This can be done using the'heal' command, provided the Player has at least one 'First Aid Kit' in their inventory. First Aid Kits can be located in several areas of the game.

##### Equipment Management

As with the first two gameplay components, Equipement Management goes hand in hand with the combat encounters. The Player will have to make sure that they are properly stocked on First Aid Kits, as well as hunt for more powerful weapons. Managing these aspects of their equipment will ultimately determine their survival of combat encounters. 

#### Inventory & Insight

The Player Card contains the Player Character's 'Inventory' and 'Insight'. These two features have the biggest impact on the gameplay and how the game functions as a whole. As the Player Character investigates, they will pick up items to store in their Inventory, as well as discover clues and secrtes that are stored in their Insight. The way the Player Character will interact with their environment will be dependent on the contents of these two features. For example, if the Player has not discovered the location of their brother's room, then they will not have 'Chris' Room Location' stored in their Insight. This means that when they enter the West Wing section of the game, the accompanying text will not include a reference to Chris' Room, thus preventing the Player access to this area. Storing 'Insight' as a visible section of the Player Card also serves as a hint to the Player. Having 'Hidden Safe Location' added to their Insight after reading a note they found in a cupboard hints to the Player that, when in the location mentioned in the note, they should be mindful of a hidden safe.  

#### Continuity Variables & Lists

'Continuity variables' and 'continuity Lists' are the terms I use for global variables and lists that are changed by the Player's actions, and which determine how the game then responds to further Player actions. One exmaple is the global variable, 'power'. By default, 'power = False', meaning the hotel does not have power. Whilst 'power = False', equipment that requires power (such as computers or the service lift) cannot be used. Once the Player has restored power to the Hotel, the variable 'power' is changed to equal 'True'. From this point onwards, equipment that requires power becomes usable.

Another example is the 'checked_rooms' varaible. When the Player Character first enters a room, something specific might happen, playing out almost like a cutscene in a video game. However, if that same 'cutscene' were to play out every subsequent time the Player Character enters that room, it would be jarring. It would create a substantial error in narrative continuity. Therefore, after the Player Character enters a room for the first time, that room is added to a global list called 'checked_rooms'. Each time the Player Character enters a room, the game will check to see if that room is within the 'checked_rooms' list. If so, a different passage of text will be printed to the screen, allowing continuity. 

The 'looted_items' and 'slain_enemies' global lists play similar roles, preventing the Player from picking up multiple of the same item or having previously defeated enemies reappear upon exiting and entering a room. By using continuity variables and lists, the world the Player Character is in responds and adapts to the Player's actions, creative a satisfying and coherent gameplay experience. 

#### Type Text Function

The type_text() function prints each word to the terminal one character at a time by iterating through each word individually. This coupled with the 'random' import, which allowed me to vary the time delay between each character being printed, emulates a person typing. As a result of using my type_text() function in place of print() functions, I have created a much more immersive experience for the Player. I feel this method of printing text to a terminal is especially effective for the horror aspect of the game, as the slower revealling of text helps to build suspense.

### Future Features

#### Larger Playable Area

My intial design for the game gave the Player access to additional rooms, including a gym, kitchen and an entire First Floor of the Hotel. Due to time constraints I had to downsize the playable area quite considerably, but if I were to add additional features in the fututre, this would include the original cut content. 

#### Difficulty Modes

The game presently has no difficulty settings. A future feature I would like to implement would be 'Easy', 'Medium' and 'Hard' modes, which would effect the Player Character's total health, enemies' health and attack power, and the number of healing items availble. This would make the game more accessible to players that want an easier game, and more difficult for players that want to be challenged.

#### More Variation Between Characters

My initial design for the game intended for the different Player Characters' unique 'Skills' to have a bigger impact on gameplay. However, as I reduced the number of rooms available to the Player, it made it more difficult to have certain areas of the map only be accessible by one of the two Player Characters. Therefore, if I expanded the size of the playable area in the future, I would increase the impact of the Player Character's skills, thus offering a bugger replayability incentive.

#### Unique & Randomly Generated Enemies

Another feature I originally wanted in the game were enemies that behaved uniquely, as well as areas that had randomly generated enemies.

One example of an enemy that would behave uniquely was the 'Stalker' enemy that was a part of the original concept for the game. The Stalker would only be triggered after the power had been restored, and from that point on would hunt the Player Character. Functionally, this would be achieved by the Stalker having a percentage chance of appearing in any room that the Player Character entered. Certain actions of the Player Character could increase or decrease this percentage - for example, using guns would create a lot of noise, and thus increase the likelihood of his appearance. The Stalker would be completely immune to damamge and attack the Player Character with provocation, forcing the Player to flee whenever he appeared. This would add some more variety to the gameplay, as well as create unique experiences each playthrough. It would also enhance the 'survival horror' aspect of the gameplay.

Additionally, as well as the unique enemies that already feature in the game, I wanted areas where randomly generated enemies could appear. Functionally, I would have a list containing multiple enemies, and certain rooms would be coded to randomly select one of those enemies to appear. This would again offer unique experiences to each playthrough, increasing the games replayability. 

#### Colour

I initially used the 'colorama' import to allow for coloured text in my game. I had intended to use colour to convey certain gameplay elements more easily to the User, as well as make the game more visually appealing. An example of this was using yellow for any objects that can be interacted with, making it immediately clear to the Player what they can and can't interact with. However, due to how colorama works, it was not compatiable with my type_text() function. Colorama wraps the standard output text to inject ANSI escape sequences that control the colour of the text - these ANSI escape sequences cannot be iterated through, and therefore causes an error when used in conjunction with a function such as my type_text(). As I was unwilling to remove the type_text() feature, I had to remove coloured words from the game design.

As a future feature, I would like to work out a way of enjoying the best of both worlds. I think adding colour to the game would increase the accessibility and overall aesthetic of the game significantly, and so having both these features would be the ideal outcome.

### Technologies Used

#### Languages 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

* [GitPod](https://www.gitpod.io/)
    - IDE.

* [Git](https://git-scm.com/)
    - Version control system.

* [GitHub](https://github.com/)
    - Online storing of repository and deployment of website.

* [Lucid](https://lucid.app/documents#/documents?folder_id=home)
    - Logic chart design app.

* [Heroku](https://en.wikipedia.org/wiki/Heroku)
    - Site for app deployment

### Testing

#### Validators

To ensure there were no errors in the syntax of my code, my run.py file was validated using [ExtendsClass Python Syntax Checker](https://extendsclass.com/python-tester.html).

![run.py Validator Result](/assets/readme-images/python_validator_result)

#### Manual Testing 
 
Throughout the development of this game, myself and several others have extensively play tested it via the deployed app on Heroku. I have collated all the data gathered during this process and entered into a 'Manual Testing' and 'Bugs & Fixes' table contained in a separate .md file.

You can view this data [here](/manual_testing.md)

### Local Development & Deployment

The app was developed using GitPod.

Prior to the below deployment process, enter the "pip freeze" command in your Git Bash terminal to update your requirements.txt file. Once this has been done, you can deploy with Heroku using the following steps:

1. Log in to Heroku
2. On the 'Dashboard', click "New" then "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. Under "Settings", locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", then click "Add"
7. Locate "Buildpack" and click "Add", then select "Python" and "Node.js", ensuring "Python" sits above "Node.js" in the build order.
8. Click the "Deploy" tab
9. Select GitHub as deployment method and search for your repository, then click "link"
10. Select either "Enable Automatic Deploys" or "Manual Deploy"
11. Wait for the build and publish process. Once completed, follow provided link to the deployed app to ensure successful deployment.

#### Forking the GitHub Repository
Forking the repository creates a copy of the original, allowing us to view and change the repository without affecting the original. This can be done by following the below steps:

1. Open the GitHub repository - [PP3_Ravens_Rest](https://github.com/MattMiles95/PP3_Ravens_Rest).

2. Select the "Fork" button in the top-right section of the page.

A copy of the repository should now be in your own GitHub account.

#### Local Clone
Cloning the repository allows you to copy the files into your own IDE for local development. This can be done by following the below steps:

1. Open the GitHub repository - [PP3_Ravens_Rest](https://github.com/MattMiles95/PP3_Ravens_Rest).

2. Navigate the 'Code' dropdown menu and select whether you wish to clone the code using HTTPS, SSH or GitHub CLI.

3. Open the a Git Bash terminal in your chosen IDE and navigate your working directory to the location you wish to clone the project.

4. Use the command 'git clone' followed by the link you copied from the repository. 

### Credits

#### Affiliations

"Raven's Rest" is a game created by me solely for the purpose of this project.

Inspiration has been taken from the works of H.P. Lovecraft, Edgar Allan Poe and the Resident Evil franchise. Any names or locations from these IPs featured in Raven's Rest are meant as homages to the original creators. 

#### Copy (Written Material)

* All written material (including narrative content) used in the game was written by me.

#### Online Resources

[ASCII Art - Raven](https://emojicombos.com/raven-ascii-art)