# Jack Chilton, CIS 345, 12-1:15PM, Project GUI

from tkinter import *
from PIL import Image, ImageTk
from os import path
import jrchilto_ProjectClass
import json


def check_in():
    gym_id = member_id.get()
    if len(gym_id) != 4 or gym_id.isnumeric() is False:
        enter_lbl.config(text='Member ID must be a 4 digit number.\nPlease exit and try again.')
        ball_lbl.grid_forget()
        ball_check.grid_forget()
        check_in_btn.grid_forget()
        exit_btn.grid_forget()
        exit_btn.grid(row=8, column=0, columnspan=3, pady=15)

    else:
        members = {}

        if not path.isfile('members.json'):
            with open('members.json', 'w') as fp:
                json.dump(members, fp)

        with open('members.json') as fp:
            members = json.load(fp)

        try:
            if members[gym_id]['Ball Status'] == 1:
                enter_lbl.config(text='You have not checked an LA Fitness\n basketball back in to the desk.\n'
                                      '\nYou will be fined $60 to your account\n to be allowed back into the gym.')
                ball_lbl.grid_forget()
                ball_check.grid_forget()
                check_in_btn.grid_forget()
                exit_btn.grid_forget()
                fine_btn = Button(check_in_frame, command=pay_fine, font=('Arial', 16), text='Pay Fine', width=7,
                                  bg='#FCB116', fg='#10103E')
                fine_btn.grid(row=7, column=0, columnspan=3, pady=15)
                exit_btn.grid(row=8, column=0, columnspan=3, pady=15)
            else:
                members[gym_id]['Ball Status'] = ball_status.get()
                with open('members.json', 'w') as fp:
                    json.dump(members, fp)

                enter_lbl.config(text='Have a great workout!')
                if ball_status.get() == 1:
                    ball_check_in_page_btn = Button(check_in_frame, command=ball_check_in_page, font=('Arial', 16),
                                                    text='Check Ball In', width=16, bg='#FCB116', fg='#10103E')
                    ball_check_in_page_btn.grid(row=8, column=0, columnspan=3, pady=15)
        except KeyError:
            new_member = jrchilto_ProjectClass.Member(gym_id)
            new_member.ball_status = ball_status.get()

            members[new_member.gym_id] = {}
            members[new_member.gym_id]['Ball Status'] = new_member.ball_status
            members[new_member.gym_id]['Fine'] = new_member.fine

            with open('members.json', 'w') as fp:
                json.dump(members, fp)

            enter_lbl.config(text=f'Have a great first workout\nwith us, Member {str(new_member)}!')
            if ball_status.get() == 1:
                ball_check_in_page_btn = Button(check_in_frame, command=ball_check_in_page, font=('Arial', 16),
                                                text='Check Ball In', width=16, bg='#FCB116', fg='#10103E')
                ball_check_in_page_btn.grid(row=8, column=0, columnspan=3, pady=15)

        # check_in_btn['state'] = 'disabled'

        clear_checkboxes()


def pay_fine():
    with open('members.json') as fp:
        members = json.load(fp)

    members[member_id.get()]['Ball Status'] = 0
    members[member_id.get()]['Fine'] += 60

    with open('members.json', 'w') as fp:
        json.dump(members, fp)

    enter_lbl.config(text='Fine has been added to your account.\nPlease exit and check in again.')


def ball_check_in():
    with open('members.json') as fp:
        members = json.load(fp)

    members[member_id.get()]['Ball Status'] = 0

    with open('members.json', 'w') as fp:
        json.dump(members, fp)

    ball_check_in_lbl.config(text='Basketball checked in. Thank you!')
    ball_check_in_btn.grid_forget()


def ball_check_in_page():
    check_in_frame.grid_forget()
    ball_check_in_frame.grid(columnspan=3)


def clear_checkboxes():
    ball_check.deselect()


def close():
    win.destroy()


# Window
win = Tk()
win.title('LA Fitness')
win.geometry('400x600')
win.columnconfigure(0, weight=1)
win.config(bg='#10103E')

# Canvas
canvas = Canvas(win, width=300, height=180, bg='#10103E')
canvas.grid(columnspan=3, pady=10)

# Variables
member_id = StringVar()
ball_status = IntVar()

# Logo
logo = Image.open('LaFitnessLogo.png')
new_width = 300
new_height = 180
img = logo.resize((new_width, new_height), Image.LANCZOS)
img.save('LaFitnessLogo.png')
logo = ImageTk.PhotoImage(img)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, row=0, column=0, pady=10)

# First GUI Page
check_in_frame = Frame(win, width=400, height=600, bg='#10103E')
check_in_frame.grid(columnspan=3)

# Welcome Label
welcome_lbl = Label(check_in_frame, text='Welcome to LA Fitness!', font=('Arial', 12),
                    bg='#10103E', fg='#FCB116')
welcome_lbl.grid(columnspan=3, row=1, column=0, pady=5)

# ID Label
id_lbl = Label(check_in_frame, text='Enter your Member ID: ', width=30, font=('Arial', 12), bg='#FCB116',
               fg='#10103E')
id_lbl.grid(columnspan=3, row=2, column=0, pady=10)

# ID Entry
id_entry = Entry(check_in_frame, textvariable=member_id, justify=CENTER, width=20)
id_entry.grid(columnspan=3, row=3, column=0)

# Ball Label
ball_lbl = Label(check_in_frame, text='Check the box below if you would\n like to check out a basketball',
                 width=30, font=('Arial', 12), bg='#FCB116', fg='#10103E')
ball_lbl.grid(columnspan=3, row=4, column=0, pady=20)

# Ball Checkbutton
ball_check = Checkbutton(check_in_frame, text='Basketball', bg='#FCB116', fg='#10103E',
                         bd=10, variable=ball_status, font=('Arial', 10), onvalue=1, offvalue=0)
ball_check.grid(columnspan=3, row=5, column=0)

# Enter Label
enter_lbl = Label(check_in_frame, text='Please check in below', width=30, font=('Arial', 12), bg='#10103E',
                  fg='#FCB116')
enter_lbl.grid(columnspan=3, row=6, column=0, pady=15)

# Check In Button
check_in_btn = Button(check_in_frame, command=check_in, font=('Arial', 16), text='Check In', width=7,
                      bg='#FCB116', fg='#10103E')
check_in_btn.grid(row=7, column=0, padx=(35, 0), sticky=W)

# Exit Button
exit_btn = Button(check_in_frame, command=close, font=('Arial', 16), text='Exit', width=7,
                  bg='#FCB116', fg='#10103E')
exit_btn.grid(row=7, column=2, padx=(0, 35), sticky=E)


# Second GUI Page
ball_check_in_frame = Frame(win, width=400, height=600, bg='#10103E')

# Welcome Label
ball_welcome_lbl = Label(ball_check_in_frame, text='LA Fitness Basketball Check In Page',
                         font=('Arial', 14), bg='#10103E', fg='#FCB116')
ball_welcome_lbl.grid(columnspan=3, row=1, column=0, pady=5)

# ID Label
id_lbl = Label(ball_check_in_frame, text='Ensure this is your Member ID: ', width=30, font=('Arial', 12), bg='#FCB116',
               fg='#10103E')
id_lbl.grid(columnspan=3, row=2, column=0, pady=10)

# ID Entry
id_entry = Entry(ball_check_in_frame, textvariable=member_id, justify=CENTER, width=20)
id_entry.grid(columnspan=3, row=3, column=0)

# Ball Check In Label
ball_check_in_lbl = Label(ball_check_in_frame, text='Please check in your basketball\n by clicking the button below',
                          font=('Arial', 12), bg='#10103E', fg='#FCB116')
ball_check_in_lbl.grid(columnspan=3, row=4, column=0, pady=15)

# Ball Check In Button
ball_check_in_btn = Button(ball_check_in_frame, command=ball_check_in, font=('Arial', 16), text='Check In Basketball',
                           width=18, bg='#FCB116', fg='#10103E')
ball_check_in_btn.grid(row=5, columnspan=3)

# Ball Exit Button
ball_exit_btn = Button(ball_check_in_frame, command=close, font=('Arial', 16), text='Exit', width=7,
                       bg='#FCB116', fg='#10103E')
ball_exit_btn.grid(row=6, columnspan=3, pady=100)


win.mainloop()
