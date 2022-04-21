players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new_players = list(key + value for key, value in players.items())
print(f'Результат работы программы:\n{new_players}')