import tkinter as tk
import random
import string

def generate_password():
    password_len = int(password_len_entry.get())
    if password_len <= 0:
        password_label.config(text="Invalid password length.")
        return

    character = string.ascii_letters + string.digits
    password = ''.join(random.choice(character) for _ in range(password_len))
    password_label.config(text="Generated Password: " + password)

def reset_password():
    password_label.config(text="")
    password_len_entry.delete(0, tk.END)


# Create the main application window
window = tk.Tk()
window.geometry("350x350")
custom_font_size = ("Arial", 20)
name = tk.Label(window, text="Password Generator", font=custom_font_size )
name.pack(pady=30)

#creating name tag
name = tk.Label(window, text="Enter your name:")
name.pack(pady=5)
#creating block to enter name
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

# Creating password tag
password_length_label = tk.Label(window, text="Enter password length:")
password_length_label.pack(pady=10)

password_len_entry = tk.Entry(window)
password_len_entry.pack(pady=5)

#generate password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
#generate reset button
reset_button = tk.Button(window, text="Reset", command=reset_password)
reset_button.pack(pady=10)

password_label = tk.Label(window, text="")
password_label.pack()


window.mainloop()
