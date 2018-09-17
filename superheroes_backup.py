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
        self.health -= damage_amt
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

    def attack(self, other_team):
        totalAttack = 0
        for hero in self.heroes:
            totalAttack += hero.attack()
        other_team.defend(totalAttack)

        enemiesDead = 0
        for enemy in other_team.heroes:
            enemiesDead += enemy.deaths

        for hero in self.heroes:
            hero.add_kill(enemiesDead)

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
        for hero in self.heroes:
            if hero.deaths != 0:
                ratio = hero.kills // hero.deaths
                print(str(hero.name) + " killed " + str(hero.kills) + " hero(es) and died " + str(hero.deaths) + " time(s). THEIR KILLS TO DEATHS RATIO WAS " + str(ratio) + ".")
        else:
            for hero in self.heroes:
                print(str(hero.name) + " killed " + str(hero.kills) + " hero(es) and never died.")

    def update_kills(self):
        totalTeamKills = 0
        for hero in self.heroes:
            totalTeamKills += hero.kills
        return totalTeamKills

        totalteamKills = totalTeamKills // len(self.heroes) #this is definitely wrong...

    def deadHeroes(self):
        deadHeroes = 0
        for hero in self.heroes:
            deadHeroes += hero.deaths
        if deadHeroes == len(self.heroes):
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
        heroBool = True
        powerBool = True
        hero1 = ""
        ability1 = ""
        heroDict = {}
        counter = 0
        print("Hello, welcome to hell.\n")
        teamName1 = input("What is your first team of super hero's name?\n\n")
        self.team_one = Team(teamName1)
        print("Very cool. \n")
        while heroBool == True and counter < 5:
            if hero1 == "x":
                heroBool = False
            else:
                heroDict[counter] = Hero(input("Please enter the name of a super-hero on team " + str(self.team_one.name) + ". When you are finished adding heroes to your party, enter the letter 'x'.\n"))
                self.team_one.add_hero(heroDict[counter])
                print(self.team_one.view_all_heroes())
                print((powerBool, ability1, counter))
                powerBool = True
                while powerBool == True:
                    if ability1 == "x":
                        ability1 = ""
                        counter += 1
                        powerBool = False
                    else:
                        print(heroDict[counter].name)
                        if len(heroDict[counter].abilities) > 0:
                            print(heroDict[counter].listAbilities())
                        ability1 = input("What's your superhero's superpower called? Type 'x' to stop.\n")
                        abilityability = Ability(ability1, random.randint(0,100))
                        heroDict[counter].add_ability(abilityability)




    def build_team_two(self):
        heroBool = True
        powerBool = True
        hero2 = ""
        ability2 = ""
        heroDict = {}
        counter = 0
        print("Way to go!\n\n")
        teamName2 = input("What is your second team of super hero's name?\n\n")
        self.team_two = Team(teamName2)
        print("Very cool. \n")
        while heroBool == True and counter < 5:
            if hero2 == "x":
                heroBool = False
            else:
                heroDict[counter] = Hero(input("Please enter the name of a super-hero on team " + str(self.team_two.name) + ". When you are finished adding heroes to your party, enter the letter 'x'.\n"))
                self.team_two.add_hero(heroDict[counter])
                print(self.team_two.view_all_heroes())
                print((powerBool, ability2, counter))
                powerBool = True
                while powerBool == True:
                    if ability2 == "x":
                        ability2 = ""
                        counter += 1
                        powerBool = False
                    else:
                        print(heroDict[counter].name)
                        if len(heroDict[counter].abilities) > 0:
                            print(heroDict[counter].listAbilities())
                        ability2 = input("What's your superhero's superpower called? Type 'x' to stop.\n")
                        abilityability = Ability(ability2, random.randint(0,100))
                        heroDict[counter].add_ability(abilityability)


    def team_battle(self):
        build_team_one()
        build_team_two()
        while self.team_one.deadHeroes() == False and self.team_two.deadHeroes() == False:
            pass
            #battle

    def show_stats(self):
        teams = list(self.team_one, self.team_two)
        for team in teams:
            team.stats()



"""myHero = Hero("Shrek")
print(myHero.name)
print(myHero.__doc__)
loadedFart = Ability("loaded fart", 30)
myHero.add_ability(loadedFart)
poop = Ability("poop", 40)
myHero.add_ability(poop)
print(myHero.health)
myHero.take_damage(99)
print(myHero.defend())
print(myHero.health)
myHero.take_damage(99)
print(myHero.health)
print(myHero.defend())
print(myHero.attack())
myHero.add_kill(3)
print(myHero.kills)

scimitar = Weapon("scimitar", 100)

myHero.add_ability(scimitar)
print(myHero.listAbilities())
print(myHero.attack())

shield = Armor("shield", 50)
myHero.add_armor(shield)
print(myHero.listArmors())
print(myHero.defend())
print(len(myHero.armors))
print(myHero.health)
print(myHero.defend())

Team1 = Team("myTeam")
Team2 = Team("otherTeam")
Team2.add_hero(myHero)
print(Team2.view_all_heroes())
print(Team1.name)

Team1.add_hero(myHero)
print(Team1.view_all_heroes())
Team1.remove_hero(myHero)
print(Team1.view_all_heroes())
Team1.add_hero(myHero)
print(Team1.view_all_heroes())

print(myHero.health)

Team2.revive_heroes()

print(myHero.health)

Team1.stats()

myHero.kills = 5
myHero.deaths = 0

print(Team1.update_kills())

print(myHero.kills)
Team1.stats()
Team2.stats()
myHero.deaths = 1

print(Team1.deadHeroes())

myHero.kills = 0

print(Team1.update_kills())

print(str(Team1.find_hero("Shrek").name))

Team1.attack(Team2)


hello = Ability("hello", 2)
Team1.find_hero("Shrek").add_ability(hello)
print(Team1.find_hero("Shrek").listAbilities())
"""

myArena = Arena()

myArena.team_battle()
