# Raven's Rest

![Game Demo](/assets/readme-images/ravens_rest_title_screen.png)

Raven's Rest is a text-based adventure game with a strong narrative focus, adopting the 'cosmic horror' genre popularised by H.P. Lovecraft and taking functional inspiration from game design of the Resident Evil franchise.

When launching the app, the Player will be met with the title screen. This features ASCII art of a raven besides the game’s title, a short introduction to the game, and a choice of either viewing the ‘how to play’ section or diving right into the game.
Once the game has started, the Player will have the option of two characters. Each character experiences the same story but plays slightly differently, based on their individual character traits. The player is advised to be mindful of this when making their selection.

Beyond the character selection menu, the Player will then have the choice of playing through the introduction (which acts as a gameplay tutorial whilst also providing narrative exposition),  or skip straight to the first gameplay area (where they can begin exploring the titular Raven’s Rest Hotel).

Once the game begins proper, signalled by the Player Character entering the Raven’s Rest, they have complete freedom to explore the hotel in whatever order (and in however much detail) they like. The game rewards exploration and attention to detail with items that the Player Character can use, such as weapons and first aid kits. As the player explores, they will add key items to their ‘inventory’ and knowledge to their ‘insight’, both of which will be used to unlock previously hidden areas of the game – and even different endings. All Player stats (including health points (HP), attack damage, equipped weapon, skills, inventory and insight), are visible in the Player Card, which can be opened at any time by entering the command: ‘pc’.

Overall, Raven’s Rest is designed to be a fun and rewarding, interactive experience with a good incentive for multiple play throughs. Whilst it requires a methodical approach to achieve the best ending, the game focuses more on investigative gameplay than outright difficulty. As such, the game is highly accessible for even the least experienced gamers. Due to the cosmic horror theme of the game, however, it is not appropriate for all ages (namely young children). 


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

Once the Player has selected their character, they will be able to choose whether to play through the intro or skip straight to the start of the main game. The intro offers some exposition on the games characters and narrative, whilst also acting as a tutorial for the common commands and conventions the Player will encounter during the game.

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

As with the first two gameplay components, Equipement Management goes hand in hand with the combat encounters. The Player will have to make sure that they are properly stocked on First Aid Kits, as well as hunt for the most powerful weapons. Managing these aspects of their equipment will ultimately determine their survival of combat encounters. 

### Future Features

#### Developer Features

* When initially writing my code, I depended heavily on using template literals to push hard code into my game’s HTML files to build each playing card. It was only upon creating multiple characters for each JS array that I realised how inefficient this method was, as it required huge amounts of copy and pasting code that then needed to have small details individually. The vast amount of code also required me to split the JavaScript across 3 separate files (one for each html file) to keep the code from becoming too messy.

* A future feature I would add would be to entirely refactor this section of the JavaScript for my game. Each property within the playing cards’ divs would be written into the respective HTML file, with each value set to a placeholder. Instead of the JavaScript variables for each character being a template literal, I would set parameters for each value within the playing cards (being the image, character name, quote and stat). This way, once a character is randomly selected from their array, just their individual parameters are pulled through to the HTML file, rather than the entire code for the playing card itself.

* This would allow for much less verbose JavaScript, which would greatly improve readability as well as efficiency for working on the code at a later date.

#### User Features

* A future feature I would like to add to the game is a difficulty setting, to make it more accessible for Users with a wider spectrum of knowledge regarding Marvel characters. ‘Easy’ mode would have the opponent’s stats colour coded to indicate their strengths and weaknesses, without outright telling the User their stats (i.e., a green circle for stats ranging 1 – 3, amber circle for 4 – 7 and red for 8 – 10). ‘Normal’ mode would be the game as currently deployed. ‘Hard’ mode would also hide the User’s stats, requiring them to rely much heavier on their knowledge of the characters.

* Other future features I’d like to add are the following game modes to add variety for the User:

1. ‘Battle Royale’ mode, where the User can use a mixed deck of heroes and villains.

2. ‘Survival’ mode, where the User sees how many consecutive rounds they can win before being defeated.

* Another feature I would like to add is a variety of different card decks, as opposed to just ‘Heroes’ and ‘Villains’. For example, a deck of just X-Men cards, or multi-verse Spider-Man variants, etc.

* Over time, I would like to add more characters to the rosters, to keep the game feeling fresh for users.

### Technologies Used

#### Languages 
* [HTML 5](https://en.wikipedia.org/wiki/HTML5)
* [CSS 3](https://en.wikipedia.org/wiki/CSS#CSS_3)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

* [Visual Studio Code](https://code.visualstudio.com/)
    - IDE.

* [Git](https://git-scm.com/)
    - Version control system.

* [GitHub](https://github.com/)
    - Online storing of repository and deployment of website.

* [Google Fonts](https://fonts.google.com/)
    - Import primary font for website.

* [Font Awesome](https://fontawesome.com/)
    - Import several icons.

* [Balsamiq](https://balsamiq.com/)
    - Wireframing tool.

* [Freepik](https://www.freepik.com/)
    - Library of stock images.

* [Photopea](https://www.photopea.com/)
    - Photo editing software.

* [Chrome DevTools](https://developer.chrome.com/docs/devtools)
    - For testing and auditing code.

* [Chrome Eye Dropper](https://chromewebstore.google.com/detail/eye-dropper/hmdcmlfkchdmnmnmheododdhjedfccka)
    - For sampling colours.

### Testing

#### Validators

To ensure there were no errors in the syntax of my code, each file was separately validated using direct input in the [W3C Markup Validator](https://validator.w3.org/#validate_by_input), the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and [JSHint](https://jshint.com/)

##### HTML

<details><summary>index.html</summary>

![Homepage Validator Result](assets/images/readme-images/w3-index.webp)
</details>

<details><summary>game-heroes.html</summary>

![Heroes Page Validator Result](assets/images/readme-images/w3-heroes.webp)
</details>

<details><summary>game-villains.html</summary>

![Villains Page Validator Result](assets/images/readme-images/w3-villains.webp)
</details>

##### CSS

<details><summary>style.css</summary>

![CSS Validator Result](assets/images/readme-images/w3-css.webp)
</details>

##### JavaScript

<details><summary>home.js</summary>

![JSHint Result](assets/images/readme-images/jshint-home.webp)
</details>

<details><summary>heroes.js</summary>

![JSHint Result](assets/images/readme-images/jshint-heroes.webp)
</details>

<details><summary>villains.js</summary>

![JSHint Result](assets/images/readme-images/jshint-villains.webp)
</details>

#### Lighthouse Testing

I used the Google Lighthouse tool to test the performance, accessibility, SEO and best practices of each of webpages, generating reports for both mobile and desktop performance on each.

All Lighthouse tests were conducted using Incognito Mode to ensure there was no interference from browser plugins.

##### Lighthouse Test Results

<details><summary>index.html</summary>

![Homepage Lighthouse Result](assets/images/readme-images/lighthouse-result-index.png)
</details>

<details><summary>heroes.html</summary>

![Heroes Page Lighthouse Result](assets/images/readme-images/lighthouse-result-heroes.webp)
</details>

<details><summary>villains.html</summary>

![Villains Lighthouse Result](assets/images/readme-images/lighthouse-result-villains.webp)
</details>

#### Manual Testing 
 
To test the functionality of my JavaScript, myself and several friends and family play tested the game on various devices. I then compiled the data in the following table:

#### Browser Compatibility

Browser | Expected Outcome  | Result
--- | --- | ---
Google Chrome | No issues with appearance, functionality, performance or responsiveness | Pass
Microsoft Edge | No issues with appearance, functionality, performance or responsiveness | Pass
Mozilla Firefox | No issues with appearance, functionality, performance or responsiveness | Pass
Safari | No issues with appearance, functionality, performance or responsiveness | Pass

#### Device Compatibility

Device | Expected Outcome | Result
--- | --- | ---
Samsung Galaxy S23 Ultra (412px x 750px) | No issues with appearance, functionality, performance or responsiveness | Pass
iPhone 13 (390px x 661px) | No issues with appearance, functionality, performance or responsiveness | Pass
Apple iPad 8th Gen (580px x 548px) | No issues with appearance, functionality, performance or responsiveness | Pass
15.6" Portable Monitor (1280px x 551px) | No issues with appearance, functionality, performance or responsiveness | Pass
15.6" Windows Laptop (1536px x 695px) | No issues with appearance, functionality, performance or responsiveness | Pass 

(The above viewports were calculated using [whatismyviewport.com](https://whatismyviewport.com/) on each devices' maximised browser window.)

#### Play Testing

Feature | Expected Outcome | Result
--- | --- | ---
Play Button | Positioned centre/right of viewport, responds correctly to hovering mouse, opens 'deck choice' menu when clicked and disappears from view | Pass
Deck Choice Menu | Positioned centre of viewport, each button responds correctly to hovering mouse, each button leads to correct game page, close window button causes Play button to reappear | Pass
Games Page | All elements appear and in correct positions, correct formatting dependent on game type | Pass
Fight Button | Container appears above other content, button responds correctly to hovering mouse, when clicked triggers (1) User and CPU cards to flip over (2) randomly generated hero & villain (3) User Buttons panel to appear (4) correct SFX | Pass
User & CPU Cards | Card flip animation works as expected, randomly generates characters from respective arrays (including images, names, quotes and stats), User stats visible, CPU stats hidden, characters removed from respective arrays once selecetd to avoid repetition | Pass
User Buttons | Correctly positioned depending on viewport dimensions with correct background depending on game type, buttons respond correctly to hovering mouse, each button triggers appropriate results screen, correct SFX | Pass
Round Win | 'Win' window appears, scoreboard adjusts accordingly, User Button panel disappears, button responds correctly to hovering mouse, button resets game and adds +1 to round counter, correct SFX | Pass
Round Lose | 'Lose' window appears, scoreboard adjusts accordingly, User Button panel disappears, button responds correctly to hovering mouse, button resets game and adds +1 to round counter, correct SFX | Pass
Round Draw | 'Draw' window appears, scoreboard remains the same, User Button panel disappears, button responds correctly to hovering mouse, button resets game and adds +1 to round counter, correct SFX | Pass
Game Over - Victory | 'Victory' window appears, background image blurs, User Button panel disappears, Options buttons disappear, buttons respond correctly to hovering mouse, buttons trigger correct functions/page navigation, correct SFX | Pass
Game Over - Defeat | 'Defeat' window appears, background image blurs, User Button panel disappears, Options buttons disappear, buttons respond correctly to hovering mouse, buttons trigger correct functions/page navigation, correct SFX | Pass
Game Over - Empty Deck | 'Empty Deck' window appears, background image blurs, User Button panel disappears, Options buttons disappear, buttons respond correctly to hovering mouse, buttons trigger correct functions/page navigation, correct SFX | Pass
Options Buttons | Correctly positioned depending on viewport dimensions, respond correctly to hovering mouse, trigger correct functions when clicked | Pass
'How to Play' Window | Appears centre of viewport above all other content, close window button works as expected, correct SFX | Pass
Audio Toggle | Default set to mute, toggle effects all audio events, icon changes accordingly | Pass
Scoreboard | Appears top/centre of viewport, round counter and scores respond correctly at the appropriate events, triggers game over at expected values | Pass

#### Bugs and Fixes

During the development of my game, I encountered several bugs that required fixes. I have documented these in the table below:

Feature | Expected Outcome | Actual Outcome | Fix
--- | --- | --- | ---
Characters being randomly generated | Hero and Villain appear within User and CPU cards | Cards remained blank | moved arrays that stored characters below respective variable declarations
Power Attack (User Button) | User & CPU 'power' stats compared and appropiate result screen triggered | 'Lose' window triggering regardless of stat values | Corrected syntax used for 'if / else if' loop (previously wrote code as 'if else')
Intelligence Attack (User Button) | User & CPU 'intelligence' stats compared and appropiate result screen triggered | Button not triggering any event | Corrected spelling of intelligence button ID tag within the script
Play Again Button | Reloads page to reset game | Button not triggering any event | Added [0] to getElementsByClassName() method to correctly target the Play Again button
Play Again Button | Reloads page to reset game | Button only working within 'Victory' window | Created separate variables and event listeners for 'Victory', 'Defeat' and 'Empty Deck' windows
Round Results Window | Each time a round ends, either the 'win', 'lose' or 'draw' window appears (nothwithstanding Game Over event triggers) | Previous rounds' results windows would begin to stack over the course of multiple rounds, leading to multiple results screens appearing at once | Added function to reset each results windows' 'display' property to 'none' when using the 'Next Game' button
Audio Toggle Button | Upon hovering mouse, button should increase in size and brightness | Button not responding to hovering mouse | Corrected ID names in CSS
Game Over Event | Once a team has reached 7 points, appropriate Game Over event is triggered | Game Over event not triggering for Victory or Defeat | Created a checkScore() function to check whether score limit has been reached by either team at the end of each round (triggers appropriate Game Over event if 'true')
Removal of Previously Selected Characters | Once a character has been selected they are removed from their respective array to prevent repetition | Adding splice() method to existing card generating function caused cards to appear blank | Refactored dealCards() function into separate components to apply splice() method to only the applicable component
Play Button | Upon mouse hovering, font increases in size and glows | Hover effect causing font to overflow container in certain screen dimensions | Adjusted font sizes in relevant media queries to eliminate overflow
User Buttons Panel | Panel appears slightly below User Card on devices with viewport of max width 800px / max height 650px | Panel positioning at very bottom of viewport, causing large gap between User Card and panel | Changed positioning unit from % to px to keep position fixed just below User Card 
'How to Play' Window | Window appears above all other content | Window appeared beneath 'Fight' button container | Increase z-index value to 99 to ensure window always appears on top

### Local Development & Deployment

#### Local Development

The website was developed using Visual Studio Code, with all local files stored in my Dropbox to provide a cloud-based backup. All live code is stored in my GitHub repository – PP2_Marvel_Top_Trumps (via routine 'git push' commands). The following VS Code extensions were used in the development of the website:

* Git

* GitHub Codespaces

* GitHub Repositories

* Live Server

#### Deployment 

This site was deployed via GitHub Pages, using the following steps:

1. Open the GitHub repository - [PP2_Marvel_Top_Trumps](https://github.com/MattMiles95/PP2_Marvel_Top_Trumps).

2. Select the Settings tab.

3. Open the source-selection dropdown menu and select "Main Branch"

Upon completion of the above steps, refresh the repository homepage and scroll to the Deployments section on the right-hand side of the page. Click on "github-pages" and follow the link to the live project.

#### Forking the GitHub Repository
Forking the repository creates a copy of the original, allowing us to view and change the repository without affecting the original. This can be done by following the below steps:

1. Open the GitHub repository - [PP2_Marvel_Top_Trumps](https://github.com/MattMiles95/PP2_Marvel_Top_Trumps).

2. Select the "Fork" button in the top-right section of the page.

A copy of the repository should now be in your own GitHub account.

#### Local Clone
Cloning the repository allows you to copy the files into your own IDE for local development. This can be done by following the below steps:

1. Open the GitHub repository - [PP2_Marvel_Top_Trumps](https://github.com/MattMiles95/PP2_Marvel_Top_Trumps).

2. Navigate the 'Code' dropdown menu and select whether you wish to clone the code using HTTPS, SSH or GitHub CLI.

3. Open the a Git Bash terminal in your chosen IDE and navigate your working directory to the location you wish to clone the project.

4. Use the command 'git clone' followed by the link you copied from the repository. 

### Credits

#### Affiliations

"Marvel Top Trumps" is a game created by me solely for the purpose of this project. Any partnership or affiliation with Marvel alluded to within the game is entirely fictional and in no way represents their views.

#### Copy (Written Material)

* All copy used in the website was written by me.

* The character quotes used in the game are all direct quotes from Marvel source material, including films, television shows and comic books (notwithstanding ‘the Creator’ card).

#### Media

* All background images (notwithstanding the hero image used on the homepage) were obtained from [FreePik](https://freepik.com/).

* The hero image used for the homepage background was obtained from [MrWallpaper](https://mrwallpaper.com/wallpapers/cute-superheroes-x-marvel-villains-273jen8gcggcgfag.html).

* All character images were obtained from [Marvel Database](https://marvel.fandom.com/wiki/Marvel_Database).

* All rights to the Marvel characters featured in this game and any Marvel trademark belong to Marvel Comics.

* All audio files were obtained from [Pixabay](https://pixabay.com/).

#### Online Resources

* [Photopea](https://www.photopea.com/) was used extensively throughout this project to edit the appearance of the images used, create new images and to convert image files to .webp format for optimisation.

* [Google Fonts](https://fonts.google.com/) was used to import the primary font for the website, "News Cycle".

* [Font Awesome](https://fontawesome.com/) was used for the stat symbols on each playing card.