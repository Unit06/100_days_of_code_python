# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse4")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

data = [
    ['Pokemon Name', 'Type'],
    ['Pikachu', 'Electric'],
    ['Squirtle', 'Water'],
    ['Charmander', 'Fire']
]

table = PrettyTable(field_names=data[0])
for row_data in data[1:]:
    table.add_row(row_data)
table.align = 'l'

print(table)
