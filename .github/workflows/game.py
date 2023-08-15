class Room:
    def init(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return ", ".join(self.items)


class Item:
    def init(self, name, description):
        self.name = name
        self.description = description


class Player:
    def init(self):
        self.current_room = None
        self.inventory = []

    def move(self, room):
        self.current_room = room

    def take_item(self, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)

    def show_inventory(self):
        return ", ".join(item.name for item in self.inventory)


def main():
    # Створення кімнат
    kitchen = Room("Kitchen", "A room with a large table and some dirty dishes.")
    living_room = Room("Living Room", "A cozy room with a fireplace.")
    bedroom = Room("Bedroom", "A bedroom with a comfy bed.")

    # Додавання предметів до кімнат
    kitchen.add_item(Item("Knife", "A sharp kitchen knife."))
    living_room.add_item(Item("Book", "An interesting book to read."))
    bedroom.add_item(Item("Key", "A shiny golden key."))

    # З'єднання кімнат
    kitchen.exits = {'living room': living_room}
    living_room.exits = {'kitchen': kitchen, 'bedroom': bedroom}
    bedroom.exits = {'living room': living_room}

    # Стартова кімната гравця
    player = Player()
    player.move(kitchen)

    # Основний цикл гри
    while True:
        print(f"You are in the {player.current_room.name}. {player.current_room.description}")
        
        if player.current_room.items:
            print(f"You see the following items here: {player.current_room.get_items()}")

        command = input("What do you want to do? ").lower()

        if "exit" in command:
            print("You found the exit! Congratulations, you escaped!")
            break
        elif "take" in command:
            item_name = command.split(" ")[1]
            for item in player.current_room.items:
                if item.name.lower() == item_name:
                    player.take_item(item)
                    print(f"You took the {item.name}.")
                    break
            else:
                print(f"There is no {item_name} in this room.")
        elif "inventory" in command:
            print("You are carrying:", player.show_inventory())
        elif command in player.current_room.exits:
            player.move(player.current_room.exits[command])
        else:
            print("Invalid command. Try again.")


if name == "main":
    main()
