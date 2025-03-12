import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemonn Name", ["Pikachu", "Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Charizard","Fire"])
print(table)
