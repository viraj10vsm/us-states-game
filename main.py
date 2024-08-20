from us_state import UsStates
import turtle
my_screen = turtle.Screen()
my_screen.title("U.S. States Game")
img="blank_states_img.gif"
my_screen.addshape(img)
turtle.shape(img)
us_states = UsStates()
while len(us_states.correct_guesses) != 50:
    answer_state = my_screen.textinput(title=f" {len(us_states.correct_guesses)}/{50} States Guessed.\nGuess the state",
                                       prompt="What's another state's name?").title()
    if answer_state == "Exit" or answer_state == "Done":
        us_states.to_learn()
        break
    else:
        us_states.check_guess(answer_state)
my_screen.mainloop()
