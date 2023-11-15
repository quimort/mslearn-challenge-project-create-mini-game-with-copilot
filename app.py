import random
player_wined_games = 0
machine_wined_games = 0


start_game = input("Do you whant to start de game (y/n)?")
options = ["rock","paper","scissors"]
result = {
    1:"won",
    0:"tied",
    -1:"lost"
}
results = {
    "rock":{
        "paper":-1,
        "rock":0,
        "scissors":1
    },
    "paper":{
        "paper":0,
        "rock":1,
        "scissors":-1
    },
    "scissors":{
        "paper":1,
        "rock":-1,
        "scissors":0
    }
}
if (start_game.lower() == "y"):
    while(True):
        player_move = input("What do you chose (rock/paper/scissors)?")
        if(player_move.lower() in options):
            machine_move = options[random.randint(0,2)]
            result_value = results[player_move.lower()][machine_move]
            if (result_value == 1):player_wined_games = player_wined_games + 1
            elif (result_value == -1):machine_wined_games = machine_wined_games + 1
            print(f"you {result[result_value]}")
            keep_playing = input("do you want to keep playing (y/n)?")
            if(keep_playing.lower() != "y"):
                print(f"Player score: {player_wined_games}")
                print(f"Machine score: {machine_wined_games}")
                break
        else:
            print("Wrong option tray ageing")
else:
    print("The game has been aborted")