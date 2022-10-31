
![World_of_Warcraft](https://user-images.githubusercontent.com/106535566/199048366-e35591d3-14c2-4f36-97e0-6d15ad79b32b.png)


# World-of-Warcraft-in-Python
## A simplified version of one of the most famous RPG games ever created:World of Warcraft

World of Warcraft (WoW) is a massively multiplayer online role-playing game (MMORPG) released in 2004 by Blizzard Entertainment. Set in the Warcraft fantasy universe, World of Warcraft takes place within the world of Azeroth, approximately four years after the events of the previous game in the series, Warcraft III: The Frozen Throne.[3] The game was announced in 2001, and was released for the 10th anniversary of the Warcraft franchise on November 23, 2004. Since launch, World of Warcraft has had eight major expansion packs: The Burning Crusade (2007), Wrath of the Lich King (2008), Cataclysm (2010), Mists of Pandaria (2012), Warlords of Draenor (2014), Legion (2016), Battle for Azeroth (2018), and Shadowlands (2020), with a ninth, Dragonflight, currently in development.

Similar to other MMORPGs, the game allows players to create a character avatar and explore an open game world in third- or first-person view, exploring the landscape, fighting various monsters, completing quests, and interacting with non-player characters (NPCs) or other players. The game encourages players to work together to complete quests, enter dungeons and engage in player versus player (PvP) combat, however, the game can also be played solo without interacting with others. The game primarily focuses on character progression, in which players earn experience points to level up their character to make them more powerful and buy and sell items using in-game currency to acquire better equipment, among other game systems.

## Scope of the Project
Once I first came across Object Oriented Programming in Python, I  had a hard time wrapping my head around the core concepts, so I was determined to, conquer this programming milestone by making a project that actually highlights the use of OOP.
Being a huge fan of WoW, and later DOTA2, I thought about making a simplified version of WoW using Python OOP.

## Details of the Game
### Character Class

1. ✔️ It will start by initializing the name
2. ✔️ Health(Initialized as 100)
3. ✔️ Attack Speed(Default initialization is 2, and takes values in the range [1, 10] inclusive
4. ✔️ Delay (Indicates how long should  the character must wait in order to strike again(Default Initialization in 0)
  
> > **Also the class must have the below functionalities:**
> > 1. ✔️ Attack function:Returns an integer between 3-10 inclusive and sets the delay to be equal to 10 - attack_speed
> > 2. ✔️ Is dead function:Returns True of False whether or not the player is dead or alive (Health = 0 or dropping below 0)
> > 3. ✔️ The end_round function that increases health by 1 unit and reduces delay by 1
> > 4. ✔️ Print function that prints the attributes of the character(In a later commit it will be replaced by the __str__(self)

### Arena Class
**Two teams A and B that will be character lists will have the below functionality**
1. ✔️ The function print_state that prints the state of the characters in the lists(health, delay, name)
2. ✔️ The function play that organizes the game as we will see below, that in every every time will do this:
>> **Functionalities of the Arena Class**
>> 1. ✔️ Creates a list with the characters that are able to play(delay = 0)
>> 2. ✔️ Every character that is able to play chooses an opposing character and hits him(From the opposing character is deducted the same amount of health as the attack
>> 3. ✔️ A check of dead characters is taking place and the dead characters are deleted from their respective lists
>> 4. ✔️ A check takes place to see whether or not there is a team that wins(If the opposing list of players has no player in it
>> 5. ✔️ The end round function is called for every living player

### Main File
**We are gonna play the game inside the main file**

👹 *The first team is gonna be consisted of 5 orcs(attack_speed = 2 and random initialization of delays rannging from 0 to 3)*

🧝 *The second team is gonna be consisted of 2 night_elfs(attack_speed = 3, and random initialization of delays ranging from 0 to 2)*

We must make sure to inject informative prints in the course of the game to have a general image about where we are in the game.

## Warnings
⚠️ This project is not finished yet.Weapons will be included in a future commit and more characters also.

