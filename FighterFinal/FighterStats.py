"""
Class used to generate the stats for the fighting characters
"""

class Fighter_stats:
    
    
    def __init__(self, name, strength, health, speed, luck):
        """Initializes all attributes for the Fighter_stats class

        Args:
            name (str): String that states the fighter's name
            strength (int): Integer used to calculate damage the fighter does
            health (int): Integer used to define the fighter's health
            speed (int): Integer used to determine which fighter attacks first
            luck (int): Integer used to define the luck of the fighter for use in critical hits
        """
        self.name = name
        self.strength = strength
        self.health = health
        self.speed = speed
        self.luck = luck
        
    # Sets all the getters for class Fighter_stats 
    def name(self):
        return self.name
    def strength(self):
        return self.strength
    def health(self):
        return self.health
    def speed(self):
        return self.speed
    def luck(self):
        return self.luck
    
    # Greater than, Less than, Equal to operators for Fighter_stats
    # Compared the speed attribute of the object
    
    def __gt__(self, other):
        if isinstance(other,Fighter_stats):
            return self.speed > other.speed
        
    def __lt__(self, other):
        if isinstance(other, Fighter_stats):
            return self.speed < other.speed
        
    def __eq__(self, other):
        if isinstance(other, Fighter_stats):
            return (self.speed == other.speed and
                    self.name == other.name)
        
    def __str__(self):
        """String that is returned when the Fighter Stats object is printed
        Displays the following
        Fighter's name
        Fighter's Strength
        Fighter's Health
        Fighter's Speed
        Fighter's Luck
        """
    
        return f"""Displaying stats for {self.name}
        Strength: {self.strength}
        Health: {self.health}
        Speed: {self.speed}
        Luck: {self.luck}
"""

def main_fighter():
    """Main function driver
    This should not execute
    """
    print("You aren't supposed to be here")
    
if __name__ == '__main__':
    main_fighter()