class Character:
    
    def __init__(self, name, pet=None, height_cm=0):
        self.name = name
        self.pet = pet 
        
        self.height_cm = height_cm

    
    def display_info(self):
        pet_info = f"Pet: {self.pet}" if self.pet else "No Pet"
        print(f"Character: {self.name} | {pet_info} | Height: {self.height_cm}cm")


tom = Character("Tom", "Jerry (Mouse)", 30) # Tom think  Jerry is his pet i guess so.
jerry = Character("Jerry", None, 10)
harry = Character("Harry Potter", "Hedwig (Owl)", 165)
ben10 = Character("Ben 10", None, 140)

# Displaying the characters' information
characters = [tom, jerry, harry, ben10]

print("--- Cartoon Character Directory ---\n")
for char in characters:
    char.display_info()






