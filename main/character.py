"""class for the character"""

import functions

class Character():
    """character template"""
    health = 100
    defense = 1
    attack = 10
    magic = 10
    luck = 0

    current_health = health

    name = None

    species = None

    calling = None
    
    def dead(self):
        """kills the character"""
        functions.text("nice try")
        functions.text("ur ded")

    def take_damage(self, dmg):
        """character's health goes down"""
        self.current_health -= dmg - self.defense

        functions.text(f"you took {dmg} damage")
        functions.text(f"now you're at {self.current_health} health")

        if self.current_health < 0:
            Character.dead(None)

    def heal_damage(self, heal):
        """character's health goes up"""
        self.current_health += heal

        functions.text(f"you healed {heal} health")
        functions.text(f"now you're at {self.current_health} health")

        if self.current_health > self.health:
            self.current_health = self.health
