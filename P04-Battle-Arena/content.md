---
title: Create the Arena
slug: arena
---
## Creating the Battle Arena
Our heroes need a place to fight. This means that we're going to need an object that will manage our game for us. This object will make sure that each team gets a chance to attack the other. These are some methods that need to be completed for a battle to take place.

This `Arena` class will be responsible for making sure that all of our rules are followed in our game. It will be responsible for creating and managing our teams and regulating how they fight.

```python
class Arena:
    def __init__(self):
        """
        self.team_one = None
        self.team_two = None
        """

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
    
    def team_battle(self):
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """
```

Implement these methods in a way that allows at least one battle to take place. Feel free to add helper methods and additional features to make it a playable terminal game.

This is just the start of what you can make. Add to your game with these stretch challenges. 

## Stretch Challenges 
* Add a command line interface that allows for creating, editing, and battling of teams.
* Allow use of only "authorized" abilites, weapons, and armor controlled by the Arena.
* Add tests that cover more edge cases.
* Change the way health is dealt out across the team. i.e. create heroes that may take damage first or may take more of the teams damage.
