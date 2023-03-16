# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

### part 1 ###

player1 = "Ruud Gullit"
player2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = player1 + " " + str(goal_0) + ", " + player2 + " " + str(goal_1)
report = f"{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute"

### part 2 ###

player = "Ronald Koeman"

first_name = player[:6]
first_name_2 = player[player.find("Ronald"):player.find(" ")]

last_name_len = len(player) - player.find("Koeman")
last_name_len_2 = len(player[player.find("Koeman"):len(player)])

name_short = f"{player[0]}. {player[-last_name_len:]}"

chant = f"{player[:len(first_name)]}! " * len(first_name)
if chant[-1] == " ":
    chant = chant[:-1]

good_chant = " " != chant[-1]
print(good_chant)
