"""
URL: https://www.udemy.com/course/100-days-of-code/learn/lecture/19115618#overview
Lost in a maze
Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an if/elif/else statement so Reeborg can find the exit. 
The secret is to have Reeborg follow along the right edge of the maze, 
turning right if it can, going straight ahead if it can’t turn right, 
or turning left as a last resort.
"""


def turn_right():
  turn_left()
  turn_left()
  turn_left()


def jump():
  turn_left()
  while wall_on_right():
    move()
  turn_right()
  move()
  turn_right()
  while not wall_in_front():
    move()
  turn_left()


def step():
  if front_is_clear():
    move()


while not at_goal():
  step()
  if right_is_clear():
    turn_right()
  elif not front_is_clear():
    turn_left()
