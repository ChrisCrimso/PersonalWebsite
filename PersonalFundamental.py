import tkinter as tk
from tkinter import messagebox
import webbrowser
import qrcode
from PIL import Image, ImageTk

user_name = "Mike"
old_password = "David"
rose_gold = "#E0BFB8"
trickster_color = "#7A0139"




def Joki():
    webbrowser.open("https://smite.fandom.com/wiki/Joki_voicelines")

def check_input(event):
    input_text = choicebox.get("1.0", tk.END).strip()  # Get the text from the Text widget
    if input_text == "Aries" or input_text == "A":
        messagebox.showinfo("Result", "You entered: Aries")
    elif input_text == "Crimson King" or input_text =="CK":
        messagebox.showinfo("Result", "You entered: Crimson King")
    elif input_text == "Alien" or input_text == "AA":
        messagebox.showinfo("Result", "You entered: Alien")
    elif input_text == "Rose" or input_text == "R":
        messagebox.showinfo("Result", "You entered: Rose")
    elif input_text == "Death" or input_text =="D":
        messagebox.showinfo("Death", "You entered: Death")
    elif input_text == "Hades" or input_text == "H":
        messagebox.showinfo("Hades", "You entered: Hades")
        hades_page = tk.Tk()
        hades_page.title("Hades")
        hades_page.configure(bg="Black")
        hades_page.geometry("800x600")
    elif input_text == "Trickster" or input_text == "T":
        messagebox.showinfo("Trickster", "You entered: Trickster")
        # Create a new window for Trickster
        loki_page = tk.Toplevel(root)  # Use Toplevel instead of creating a new Tk instance
        loki_page.title("Trickster")
        loki_page.configure(bg=trickster_color)
        loki_page.geometry("800x1000")

        # Load and display the image
        trick_icon_path = "images/Jester.png"
        print(f"Loading image from: {trick_icon_path}")
        trick_image = Image.open(trick_icon_path)
        trick_image = trick_image.resize((100, 100), Image.LANCZOS)
        trick_icon = ImageTk.PhotoImage(trick_image)

        trickster_img_path = "images/cg_jest_update.png"
        print(f"Loading image from: {trickster_img_path}")
        trickster_img = Image.open(trickster_img_path)
        trickster_img = trickster_img.resize((200, 200), Image.LANCZOS)
        trickster_icon = ImageTk.PhotoImage(trickster_img)

        trick_label = tk.Label(loki_page, image=trickster_icon, bg=trickster_color)
        trick_label.image =trickster_icon
        trick_label.place(x=600, y=500)
        # Create a label to display the image
        image_label = tk.Label(loki_page, image=trick_icon, bg=trickster_color)
        image_label.image = trick_icon  # Keep a reference to avoid garbage collection
        image_label.place(x=0, y=0) # Add some padding

        urlTrick = "https://smite.fandom.com/wiki/Joki_voicelines"
        qrtrick = qrcode.make(urlTrick)
        qrtrick.save("Joki.png")

        qr_img = Image.open("Joki.png")
        qr_img = qr_img.resize((150, 150))  # Resize the QR code if needed
        qr_photo = ImageTk.PhotoImage(qr_img)

        # Create a label to display the QR code on the Trickster page
        qr_label = tk.Label(loki_page, image=qr_photo, bg=trickster_color)
        qr_label.image = qr_photo  # Keep a reference to avoid garbage collection
        qr_label.place(x=1200, y=0)  # Adjust x and y to position it on the right side

        haMessage = tk.Label(loki_page, text="HAHAHA", bg=trickster_color, fg='white', font=('chiller', 45))
        haMessage.place(x=400, y=500)

        trick_message = tk.Label(loki_page, text="Why follow the rules when the fun "
    "lies in bending them? Let’s dance on the "
        "edge of chaos and see where the laughter takes us!", bg=trickster_color, fg='white', font=('chiller', 16))
        trick_message.place(x=75, y=125)

        trick_button = tk.Button(loki_page, image=trick_icon, command=Joki)
        trick_button.place(x=0, y=0)

    elif input_text == "Menace" or input_text == "M":
        messagebox.showinfo("Menace", "You entered: Menace")
    elif input_text ==  "Plague" or input_text == "P":
        messagebox.showinfo("Plague", "You entered: Plague")
    else:
        error_label.config(text="Not Found", fg="red")

in_user_name = input("Enter username: ")
new_password = input("Type in new password: ")
if in_user_name == user_name:
    print("Cannot use same username")
    print("Please try another username")
    if new_password == old_password or new_password == user_name:
        print("Error!! Can't use the same username and password")
        print("Make sure that password do not match your name!")
else:
    verify_password = input("Type password again: ")
    if verify_password == new_password and verify_password != user_name and verify_password != old_password:
        print("Your new password has been saved")
        root = tk.Tk()
        root.title("Account")
        root.configure(bg=rose_gold)
        root.geometry("800x600")

        pink_label = tk.Label(root, text="This is the color rose gold in the background", fg="gold", font=("Times New Roman", 16))
        pink_label.place(x=0, y=150)

        choicebox = tk.Text(root, height=1, width=40)  # Create a Text widget
        choicebox.place(x=50, y=200)

        error_label = tk.Label(root, text="", bg=rose_gold)  # Label to show error messages
        error_label.place(x=50, y=250)

        choicebox.bind("<Return>", check_input)  # Bind the Enter key to the check_input function

        root.mainloop()