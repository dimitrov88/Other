import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# #get cor of the states
# def get_mouse_click(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct ",
                                    prompt="What is another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



turtle.exitonclick()
