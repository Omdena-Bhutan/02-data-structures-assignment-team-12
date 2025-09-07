# Author : Arjun Mongar 
print(" Character Profile")

#dictionary to store character information
character_profile = {
    'name': "Alistair the Brave",    
    'level': 1,                      
    'health': 100,                  
    'mana': 50,                     
    'gold': 50.75,                 
    'is_alive': True                
}

# Task 1
print(f"Character: {character_profile['name']}")
print(f"Level: {character_profile['level']}")

# Task 2
character_profile['health'] = 85
print(f"Health updated to: {character_profile['health']}")

# Task 3
character_profile['experience'] = 0
print(f"Experience added: {character_profile['experience']}")

# Task 4
print("\nFinal Character Profile:")
for key, value in character_profile.items():
    print(f"  {key}: {value}")

print()


# PART 2

print("PART 2: Managing Inventory")

#list to store inventory items
inventory = ['sword', 'shield', 'health potion']
print(f"Starting inventory: {inventory}")

# Task 1
inventory.append('mana potion')
print(f"Added mana potion: {inventory}")

# Task 2
inventory.remove('shield')
print(f"Removed shield: {inventory}")

# Task 3
print("\nCurrent inventory contains:")
for item in inventory:
    print(f"  - {item}")

print()

# PART 3

print("PART 3: Base Character Stats")

base_stats = (10, 8, 12)  

# Task 1: Explain why tuple is good for base stats
print("Why use a tuple for base stats?")
print("Tuples are immutable, meaning they cannot be changed after creation.")
print("This protects our base character stats from accidental modification.")

# Task 2
print(f"\nBase stats: Strength={base_stats[0]}, Dexterity={base_stats[1]}, Intelligence={base_stats[2]}")
print(f"Alistair's Intelligence: {base_stats[2]}")

# Task 3
print("\nTrying to change tuple value...")
try:
    base_stats[0] = 15  
except TypeError as e:
    print(f"Error occurred: {e}")
    print("This proves tuples are immutable!")

print()

# PART 4

print("PART 4: Quest Log Management")

#set to store active quests
quest_log = {'Defeat the Goblin King', 'Find the Lost Amulet'}
print(f"Starting quests: {quest_log}")

# Task 1
quest_log.add('Deliver the Old Scroll')
print(f"Added new quest: {quest_log}")

# Task 2
print("\nTrying to add duplicate quest...")
quest_log.add('Defeat the Goblin King')  
print(f"After adding duplicate: {quest_log}")
print("Notice: No duplicate was added! Sets automatically handle this.")

# Task 3
quest_log.remove('Find the Lost Amulet')
print(f"Completed and removed quest: {quest_log}")

print()

# PART 5

print("PART 5: Complete Character Sheet")

# Create a master dictionary that contains all our data structures
character_sheet = {
    'profile': character_profile,    
    'inventory': inventory,          
    'stats': base_stats,            
    'quests': quest_log             
}

print("Complete Character Sheet:")

#Print profile information
print("PROFILE:")
for key, value in character_sheet['profile'].items():
    print(f"  {key}: {value}")

#Print inventory
print("\nINVENTORY:")
for item in character_sheet['inventory']:
    print(f"  - {item}")

#Print stats
print("\nBASE STATS:")
stats = character_sheet['stats']
print(f"  Strength: {stats[0]}")
print(f"  Dexterity: {stats[1]}")
print(f"  Intelligence: {stats[2]}")

#Print active quests
print("\nACTIVE QUESTS:")
for quest in character_sheet['quests']:
    print(f"  - {quest}")

print()
print("=" * 50)
print("Adventure management system complete!")
print("Alistair is ready for his next quest!")

# BONUS: Summay of Data Types Used

print("\nDATA TYPES USED:")
print("• String: For text data like character name and item names")
print("• Integer: For whole numbers like level, health, and mana")
print("• Float: For decimal numbers like gold amount")
print("• Boolean: For True/False values like is_alive status")
print("• List: For changeable collections like inventory items")
print("• Tuple: For unchangeable collections like base stats")
print("• Dictionary: For key-value pairs like character profile")
print("• Set: For unique collections like quest log")