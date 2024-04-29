import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = ''.join(random.choices(characters, k=length))
    password_entry.config(state='normal') 
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state='readonly')
    
root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()
password_entry = tk.Entry(root, state='readonly')
password_entry.pack()

root.mainloop()
