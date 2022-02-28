def ask_name():
    name = input("Please enter name of player: ")
    return name 

def greet_player(name):
    print(f"Hello {name}, welcome to the game!")

def show_score(name, score):
    print(f"Hello {name}, your current score is {score}.")

def show_game_over(name):
    print(f"GAME OVER! Sorry, {name}...")