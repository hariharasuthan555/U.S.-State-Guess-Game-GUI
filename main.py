import pandas
import turtle


screen=turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")
states_list=data["state"].to_list()
ans=""
is_game_on=True
correct_ans_count=0
score=0

while is_game_on:
    screen.title(f"U.S. State Game | Score:{correct_ans_count}/50")
    ans = screen.textinput(title="Guess States in U.S", prompt="What's the state you guessed?").title()
    if ans in states_list:
            score+=1
            x=int(data[data.state==ans].x.item())
            y=int(data[data.state==ans].y.item())
            writing_turtle=turtle.Turtle()
            writing_turtle.hideturtle()
            writing_turtle.penup()
            writing_turtle.setposition(x,y)
            writing_turtle.write(ans,align="center",font=("Arial",8,"normal"))
            correct_ans_count+=1
            states_list.remove(ans)
    if ans=="Exit" or correct_ans_count>=50:
            is_game_on=False
            turtle.write("Gamme Over",align="center",font=("Arial",8,"normal"))


new_data_missing_states=pandas.DataFrame(states_list)
new_data_missing_states.to_csv("missing_states.csv")

'''rec=data[data["state"]==ans]
print(rec)'''

'''def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)'''



turtle.mainloop()


