import turtle

import pandas

screen = turtle.Screen()
screen.title("us state game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
all_list = states_data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/ 50 states correct", prompt="what's another states name").title()

    if answer_state == "Exit":
        un_answerd = []
        for answer in all_list:
            if answer not in guessed_state:
                un_answerd.append(answer)
        data = pandas.DataFrame(un_answerd)
        data.to_csv("unanswerd states .csv")
        break

    if answer_state in all_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        data = states_data[states_data.state == answer_state]
        t.goto(int(data.x), int(data.y))
        t.write(answer_state)

