import turtle

import pandas
from turtle import Turtle

class UsStates:
    def __init__(self):
        self.data = pandas.read_csv("50_states.csv")
        self.state_list = self.data.state.to_list()
        self.pointer = Turtle()
        self.pointer.hideturtle()
        self.pointer.penup()
        self.correct_guesses = []
    def check_guess(self, answer_state):
        if answer_state in self.state_list:
            print(f"{answer_state}")
            self.correct_guesses.append(answer_state)
            self.state_list.remove(answer_state)
            self.add_to_screen(answer_state)
        else:
            print("Not present")


    def add_to_screen(self, answer_state):
        x_cor = int(self.data[self.data['state'] == answer_state].x)
        y_cor = int(self.data[self.data['state'] == answer_state].y)
        self.pointer.goto(x_cor,y_cor)
        self.pointer.write(arg=answer_state, move=True, align="center", font=("Arial", 8, "normal"))

    def show_score(self):
        self.pointer.goto(0, 300)
        self.pointer.write(arg=f"{len(self.correct_guesses)}/{50} States Guessed.", move=True, align="center", font=("Arial", 10, "normal"))

    def to_learn(self):
        to_learn = pandas.DataFrame(self.state_list)
        to_learn.to_csv("states_to_be_learned.csv")
# ms= turtle.Screen()
# us_states = UsStates()
# us_states.add_to_screen("Arizona")
# ms.mainloop()
