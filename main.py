class Monster:
    def __init__(self,name,hp,dmg,id):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.id = id



monsters = []
def main():
    
    
    while True:
        print("[1] Display Monster")
        print("[2] Add new Monster")
        print("[3] Delete Monster")
        print("[4] Battle Mode")
        print("[5] Exit")
        print("Enter you Choice: ")
        userInput = input("[]")
        match userInput:
            case 1:
                if len(monsters) < 1:
                        print("The list is empty")
                else:
                    for monster in monsters:
                        
                            print(monster.name)
            case 2:
                name = str(input("Enter monster name: "))
                hp = int(input("Enter monster hp: "))
                id = int(input("Enter monster id: "))
                dmg = int(input("Enter monster dmg: "))
                new_monster = Monster(name,hp,dmg,id)