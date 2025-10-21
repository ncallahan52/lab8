def intro(input_str: str):
    print("You wake up in a dark forest. You can go left or right.")
    choice = input_str.strip().lower()
    if choice == "left":
        return left_path()
    elif choice == "right":
        return right_path()
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path():
    return "You walk left and find a mysterious glowing sword stuck in a stone."

def right_path():
    return "You walk right and encounter a talking squirrel who challenges you to a duel."

if __name__ == "__main__":
    choice = input("Which direction do you choose? (left/right): ")
    print(intro(choice))