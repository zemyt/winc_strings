# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

### part 1 ###

player_1 = "Ruud Gullit"
player_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = player_1 + " " + str(goal_0) + ", " + player_2 + " " + str(goal_1)
report = f"{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute"

### part 2 ###

player = "Ronald Koeman"

first_name = player[:player.find(" ")]

last_name_len = len(player) - player.find(" ") - 1

name_short = f"{player[0]}. {player[-last_name_len:]}"

chant = f"{player[:len(first_name)]}! " * len(first_name)
if chant[-1] == " ":
    chant = chant[:-1]

good_chant = " " != chant[-1]
print(good_chant)