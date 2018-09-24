import random

"""
Stretch Challenges

Add a command line interface that allows for creating, editing, and battling of teams.

Allow use of only "authorized" abilites, weapons, and armor controlled by the Arena.

Add tests that cover more edge cases.

Change the way health is dealt out across the team. i.e. create heroes that may take damage first or may take more of the teams damage.
"""

class Hero:
    """Six methods:

    defend: if health > 0, run armor method defend for each piece of armor the hero is wearing. return total armor # in Int
    take_damage: take in a # in Int and subtract that # from health. if health < 1, add 1 to deaths. (# taken-in should be POSITIVE)
    add_kill: take in # in Int and add that number to the class's kill stat.
    add_ability: take in an instance of the class "Ability", and add that ability to Hero class's array "abilities".
    add_armor: add the armor to the hero array armors.
    attack: for each Ability in abilities, run the Ability method "Attack".
    listAbilities: return an array of tuples of (ability_name and attack_strength) for every ability the hero has.
    listArmors: return an array of tuples of (armor_name and defense) for every armor the hero has.

    have yet to test kills attribute

    end_Docstringtest!"""

    def __init__(self, name, health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        if len(self.armors) >= 1:
            for armor in self.armors:
                if self.health < 1:
                    return 0
                else:
                    return armor.defend()
        else: return 0

    def take_damage(self, damage_amt):
        self.health += damage_amt
        if self.health < 1:
            self.deaths += 1

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        totalAttack = 0
        for ability in self.abilities:
            totalAttack += ability.attack()
        return totalAttack

    def listAbilities(self):
        myPowers = list()
        for ability in self.abilities:
            myPowers.append((ability.name, ability.attack_strength))
        return myPowers

    def listArmors(self):
        myArmors = list()
        for armor in self.armors:
            myArmors.append((armor.name, armor.defense))
        return myArmors

class Ability:
    """Two methods:

    attack: using half the attack_strength as the lower bounds and the attack_strength as the upper bounds return a random Int in range as the attack's damage.
    update_attack: take in an Int and change the attack_strength variable of the ability to that Int.

    end_Docstringtest!"""
    def __init__(self, name, attack_strength=0):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        b = self.attack_strength
        a = self.attack_strength // 2
        return random.randint(a, b)

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Weapon(Ability):
    """One method:

    attack: using 0 as the lower bounds and the attack_strength as the upper bounds return a random Int in range as the attack's damage.

    note: weapon's have a wider spectrum of possible values, given the lower lower bounds.

    end_Docstringtest!"""

    def attack(self):
        return random.randint(0, self.attack_strength)

    def defend(self):
        return random.randint(0, self.attack_strength // 2)

class Armor:
    """One method:

    defend: using the class's instance variable "defense" as the upper bounds and 0 as the lower bounds, return a random Int in range as the Armor's defense rating.

    end_Docstringtest!"""
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


class Team:
    """A lot of methods:
    add_hero: input a Hero and append that hero to array "heroes".

    remove_hero: input Hero.name (this one might not work, maybe make a function-scope array of hero names...), if hero is in heroes, remove hero from heroes. if not in array return 0 (why 0?)

    find_hero: input Hero.name. if name is in heroes return the Hero object reference (this one works... i think). elese return 0... print(str(Team1.find_hero("Shrek").name))

    view_all_heroes: go through array heroes and return (this one doesnt work...) list an array of hero names in heroes.

    attack: add up all of the attacks from all of the abilities of all of the heroes and add it to totalAttack, then feed the totalAttack into the enemy team's method defend() (should it be negative?), then calculate the kills. (so many parts of that could be messed up)

    defend: for each hero on the team, get their defense rating and add it to the totalDefense. if the enemy's attack is greater than the team's totalDefense, call the team's  method deal_damage, which should be above this method if we're calling it... then calculate the number of heroes who are currently dead and return that number

    deal_damage: divide the damage dealt by the total number of heroes on the team and then deal that averaged damage to each team member, then then calculate the number of heroes who are currently dead and return that number (man that shit ain't dry.)

    revive_heroes: for all Hero() in heroes, set current health to starting health (magikarp has an hp of 1)

    stats: for all Hero() in heroes, print their kill to deaths ratio

    update_kills: for all Hero() in heroes, get their kills and add it to totalTeamKills, return that number.

    deadHeroes: see if all the heroes on a given team are dead, and if they are return True. (else return False?)

    end_Docstringtest!"""

    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        if name in self.heroes:
            self.heroes.remove(name)
        else:
            return 0

    def find_hero(self, hero_name):
        for hero in self.heroes:
            if hero.name == hero_name:
                return hero
            else:
                return 0

    def view_all_heroes(self):
        myHeroes = []
        for hero in self.heroes:
            myHeroes.append(hero.name)
        return myHeroes

    def view_all_heroes_stats(self):
        myHeroes = []
        abilities = []
        for hero in self.heroes:
            for ability in hero.abilities:
                abilities.append((ability.name, ability.attack_strength))
            myHeroes.append((hero.name, hero.health, abilities))
        return myHeroes

    def attack(self, other_team):
        totalAttack = 0
        for hero in self.heroes:
            totalAttack += hero.attack()
        enemiesDead = other_team.defend(totalAttack)

        for hero in self.heroes:
            hero.add_kill(enemiesDead)

        return totalAttack


    def defend(self, damage_amt):
        deadHeroes = 0
        totalDefense = 0
        for hero in self.heroes:
            totalDefense += hero.defend()
        if damage_amt > totalDefense:
            self.deal_damage(totalDefense - damage_amt)
        for hero in self.heroes:
            if hero.deaths > 0:
                deadHeroes += 1
        return deadHeroes

    def deal_damage(self, damage):
        deadHeroes = 0
        damage = damage // len(self.heroes)
        for hero in self.heroes:
            hero.take_damage(damage)
            deadHeroes += hero.deaths
        return deadHeroes

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        stats_array = []
        for hero in self.heroes:
            if hero.deaths != 0:
                ratio = hero.kills // hero.deaths
                stats_array.append((str(hero.name) + " has " + str(hero.health) + " health, killed " + str(hero.kills) + " hero(es) and died " + str(hero.deaths) + " time(s). THEIR KILLS TO DEATHS RATIO WAS " + str(ratio) + "."))
            else:
                stats_array.append((str(hero.name) + " has " + str(hero.health) + " health, killed " + str(hero.kills) + " hero(es) and never died."))
        return stats_array

    def update_kills(self):
        totalTeamKills = 0
        for hero in self.heroes:
            totalTeamKills += hero.kills
        return totalTeamKills

    def deadHeroes(self):
        deadHeroes = 0
        for hero in self.heroes:
            deadHeroes += hero.deaths
        if deadHeroes >= len(self.heroes):
            return True
        else:
            return False

class Arena:
    """Four methods:

    build_team_one: build team one

    build_team_two: build team two

    team_battle: play match if either team has at least one member still alive

    show_stats: make an array of two items: team_one, team_two, then call the Team() class method stats()

    end_Docstringtest!"""
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        hero1 = ""
        ability1 = ""
        heroDict = {}
        heroCounter = 0
        yes = ["yeah", "y", "yes", "ye"]
        print("\nHello, welcome to hell.\n")
        teamName1 = input("What is your FIRST TEAM of super hero's NAME?\n\n")
        self.team_one = Team(teamName1)
        print("\nVery cool. \n")
        while len(self.team_one.heroes) < 2:
                heroDict[heroCounter] = Hero(input("Please enter the name of a superhero on " + str(self.team_one.name) + ". \n \n"))
                self.team_one.add_hero(heroDict[heroCounter])
                print("\n\nYour team: ")
                print(self.team_one.view_all_heroes())
                print("\nEach hero can have three powers. \nThe strength of each power is randomly generated \nbetween weak (strength: <10) and strong (stength: 100+).\n")
                powerCounter = 0
                while powerCounter < 2:
                    ability1 = input("\nWhat's " + heroDict[heroCounter].name + "'s superpower # " + str(powerCounter + 1) + " called? \n\n")
                    abilityability = Ability(ability1, (powerCounter + 1) * random.randint(1,60))
                    heroDict[heroCounter].add_ability(abilityability)
                    print("")
                    powerCounter += 1
                print("Does your hero have a weapon?")
                answer = str.lower(input("Enter yes or no.\n\n"))
                if answer in yes:
                    weapon = input("\n\nWhat's your weapon?\n\n")
                    weapon1 = Weapon(str(weapon), random.randint(1,100))
                    heroDict[heroCounter].add_ability(weapon1)
                else:
                    print("\n\nYour hero has no weapon.\n\n")
                print("\n\nDoes your hero wear armor.")
                answer = str.lower(input("Enter yes or no.\n\n"))
                if answer in yes:
                    armor = input("\n\nWhat's the armor your hero is wearing?\n\n")
                    armor1 = Weapon(str(armor), random.randint(1,50))
                    heroDict[heroCounter].add_armor(armor1)
                else:
                    print("Your hero has no armor.")
                print("Your abilities are: \n\n")
                print(heroDict[heroCounter].listAbilities())
                if len(heroDict[heroCounter].armors) > 0:
                    print("Your armor is: \n\n")
                    print(armor)
                heroCounter += 1

    def build_team_two(self):
        hero1 = ""
        ability1 = ""
        heroDict = {}
        heroCounter = 0
        yes = ["yeah", "y", "yes", "ye"]
        print("\nHello, welcome to hell.\n")
        teamName2 = input("What is your SECOND TEAM of super hero's NAME?\n\n")
        self.team_two = Team(teamName2)
        print("\nVery cool. \n")
        while len(self.team_two.heroes) < 2:
                heroDict[heroCounter] = Hero(input("Please enter the name of a superhero on " + str(self.team_two.name) + ". \n \n"))
                self.team_two.add_hero(heroDict[heroCounter])
                print("\n\nYour team: ")
                print(self.team_two.view_all_heroes())
                print("\nEach hero can have three powers. \nThe strength of each power is randomly generated \nbetween weak (strength: <10) and strong (stength: 100+).\n")
                powerCounter = 0
                while powerCounter < 2:
                    ability1 = input("\nWhat's " + heroDict[heroCounter].name + "'s superpower # " + str(powerCounter + 1) + " called? \n\n")
                    abilityability = Ability(ability1, (powerCounter + 1) * random.randint(1,60))
                    heroDict[heroCounter].add_ability(abilityability)
                    print("")
                    powerCounter += 1
                print("Does your hero have a weapon?")
                answer = str.lower(input("Enter yes or no.\n\n"))
                if answer in yes:
                    weapon = input("\n\nWhat's your weapon?\n\n")
                    weapon1 = Weapon(str(weapon), random.randint(1,100))
                    heroDict[heroCounter].add_ability(weapon1)
                else:
                    print("\n\nYour hero has no weapon.\n\n")
                print("\n\nDoes your hero wear armor.")
                answer = str.lower(input("Enter yes or no.\n\n"))
                if answer in yes:
                    armor = input("\n\nWhat's the armor your hero is wearing?\n\n")
                    armor1 = Weapon(str(armor), random.randint(1,50))
                    heroDict[heroCounter].add_armor(armor1)
                else:
                    print("Your hero has no armor.")
                print("Your abilities are: \n\n")
                print(heroDict[heroCounter].listAbilities())
                if len(heroDict[heroCounter].armors) > 0:
                    print("Your armor is: \n")
                    print(armor)
                    print(" ")
                heroCounter += 1

    def team_battle(self):
        gameover1 = False
        gameover2 = False
        self.build_team_one()
        self.build_team_two()
        print("Your teams are: ")
        print(self.team_one.view_all_heroes_stats())
        print(self.team_two.view_all_heroes_stats())
        x = random.randint(0,1)
        print("\nWho strikes first??")
        if x == True:
            print("\n" + str(self.team_one.name) + " have gotten the drop on " + str(self.team_two.name) + "!!! Careful " + str(self.team_two.name) + "!")
            while gameover1 != True and gameover2 != True:
                self.team_one.attack(self.team_two)
                gameover1 = self.team_two.deadHeroes()
                gameover2 = self.team_one.deadHeroes()
                self.team_two.attack(self.team_one)
                gameover1 = self.team_two.deadHeroes()
                gameover2 = self.team_one.deadHeroes()
        else:
            print("\n" + str(self.team_two.name) + " have gotten the drop on " + str(self.team_one.name) + "!!! Careful " + str(self.team_one.name) + "!")
            while gameover1 != True and gameover2 != True:
                self.team_two.attack(self.team_one)
                gameover1 = self.team_one.deadHeroes()
                gameover2 = self.team_two.deadHeroes()
                self.team_one.attack(self.team_two)
                gameover1 = self.team_one.deadHeroes()
                gameover2 = self.team_two.deadHeroes()

    def show_stats(self):
        print("\n\nTEAM ONE STATS:")
        print(self.team_one.stats())
        print("\nTEAM TWO STATS:")
        print(self.team_two.stats())

myArena = Arena()
myArena.team_battle()
myArena.show_stats()
