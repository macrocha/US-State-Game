import turtle
import pandas

# Create the game display
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get state names for csv file and store into a list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

# enter a loop tp ask user name of another state until all 50 have been named
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # if user enters "Exit", exit game and create a list for user to learn and put them into a .csv file
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # if user guesses a state correct, write the name of the state on the states location on the map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
