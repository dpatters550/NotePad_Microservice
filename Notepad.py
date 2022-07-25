from tkinter import *
from tkinter import filedialog, font
from PIL import ImageTk, Image
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


# generates the frame
root = Tk()
# changes the title
root.title("NotePadMicroservice")


# open file command
def open_file():
    file_path = filedialog.askopenfile(initialdir="/", title="Select a File", filetypes=(("text files", "*.txt"), ("all files", "*.*")))

    with open(file_path, "r") as f:
        # file_path = open(file_path, "r")
        junk = f.read()
        tk_textarea.insert(END, junk)

def save_file():
    file_path = filedialog.asksaveasfile()

def clear_file():
    tk_textarea.delete("1.0", END)

# Write to file via terminal
def write_to():
    # string_of_text = input()
    # for letter in string_of_text:
    #     tk_textarea.insert(END, letter)
    var = 0
    while var == 0:
        #  Wait for next request from client
        message = socket.recv()
        tk_textarea.insert(END, str(message))

        # for letter in str(message):
        #     tk_textarea.insert(END, letter)
        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        socket.send_string("Message received")

        var += 1


background_image = ImageTk.PhotoImage(file="./notepadbackground.png")

tk_background = Canvas(root, height=660, width=660,)
tk_background.pack()

tk_background.create_image(0,0,image=background_image, anchor="nw")

# generates text area
tk_textarea = Text(tk_background, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True)
tk_textarea.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# creates scroll bar
text_scroll = Scrollbar(tk_textarea)
text_scroll.pack(side=RIGHT, fill=Y)
text_scroll.config(command=tk_textarea.yview)


# main menu generate
main_menu = Menu()
root.config(menu=main_menu)

# main menu commands
file_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Clear", command=clear_file)
file_menu.add_command(label="Exit")
file_menu.add_command(label="Write To", command=write_to)

# generates our gui screen
root.mainloop()