from random import randint

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
roles = []
for role in ROLES:
    for index in range(1, ROLES[role] + 1):
        roles.append(role)

print(roles)

# Tour
words = ["voiture", "camion"]
words.append("white")
