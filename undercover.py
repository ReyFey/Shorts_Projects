from random import choice

# Rules
PLAYERS = {
    "Player1": None,
    "Player2": None,
    "Player3": None,
    "Player4": None,
    "Player5": None
}
ROLES = {
    "people": 3,
    "white": 1,
    "undercover": 1
}

# Affect roles to players
remaining_roles = []
for role in ROLES:
    for index in range(1, ROLES[role] + 1):
        remaining_roles.append(role)

for player in PLAYERS:
    choose_role = choice(remaining_roles)
    remaining_roles.remove(choose_role)
    PLAYERS[player] = choose_role

print(PLAYERS)

# Tour
words = ["voiture", "camion"]
