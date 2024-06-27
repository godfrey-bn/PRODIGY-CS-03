import string
from tkinter import *
from tkinter import messagebox
import os

def check_password_strength():
    password = entry_password.get(1.0, END).strip()
    upper_case = any(c in string.ascii_uppercase for c in password)
    lower_case = any(c in string.ascii_lowercase for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c in string.digits for c in password)

    characters = [upper_case, lower_case, special, digits]
    length = len(password)
    Rate = 0

    script_dir = os.path.dirname(os.path.abspath(__file__))
    list1_path = os.path.join(script_dir, 'list1.txt')
    list2_path = os.path.join(script_dir, 'list2.txt')
    list3_path = os.path.join(script_dir, 'list3.txt')

    with open(list1_path, 'r') as f1:
        list1 = f1.read().splitlines()

    with open(list2_path, 'r') as f2:
        list2 = f2.read().splitlines()
        
    with open(list3_path, 'r') as f3:
        list3 = f3.read().splitlines()

    if password in list1 or password in list2 or password in list3:
        show_custom_message("Password Strength", "The password is a common password. Rate 0/7", "red")
        return

    if length > 8:
        Rate += 1
    if length > 10:
        Rate += 1
    if length > 12:
        Rate += 1
    if length > 15:
        Rate += 1
    if sum(characters) > 1:
        Rate += 1
    if sum(characters) > 2:
        Rate += 1
    if sum(characters) > 3:
        Rate += 1

    if Rate < 4:
        strength = f"The password is weak! Rating: {Rate}/7"
        color = "red"
    elif Rate == 4:
        strength = f"The password is moderate! Rating: {Rate}/7"
        color = "orange"
    elif 4 < Rate <= 6:
        strength = f"The password is strong! Rating: {Rate}/7"
        color = "green"
    else:
        strength = f"The password is very strong! Rating: {Rate}/7"
        color = "darkgreen"

    show_custom_message("Password Strength", strength, color)

def show_custom_message(title, message, color):
    custom_msg = Toplevel(root)
    custom_msg.title(title)
    custom_msg.geometry("450x200")
    custom_msg.configure(bg="#2e2e2e")

    lbl_message = Label(custom_msg, text=message, fg=color, bg="#2e2e2e", font=("Helvetica", 14, "bold"))
    lbl_message.pack(pady=40)

    btn_ok = Button(custom_msg, text="OK", command=custom_msg.destroy, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
    btn_ok.pack(pady=10)

root = Tk()
root.geometry("500x300")
root.title("Password Strength Checker")
root.configure(bg="#37B7C3")

Label(root, text="Enter Password:", bg="#1c1c1c", fg="white", font=("Helvetica", 12)).place(x=50, y=20)
entry_password = Text(root, height=1, width=30, font=("Helvetica", 12))
entry_password.place(x=180, y=20)

b_check = Button(root, text="Check Strength", command=check_password_strength, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
b_check.place(x=180, y=60)

root.mainloop()