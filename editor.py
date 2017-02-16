from Tkinter import *
import tkFileDialog
import tkMessageBox

root = Tk()
root.wm_title("Text Editor")
root.configure(background='#222323')

text = Text(root)
text.grid()
text.configure(background='#222323', foreground="#0484ed", font=("Courier", 20), width=85, height=20)


def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkFileDialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


def opendoc():
    global text
    openlocation = tkFileDialog.askopenfilename()
    file2 = open(openlocation, "r")
    te = file2.read()
    text.insert('1.0', te)
    file2.close()

def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()



button = Button(root, text="Save", command=saveas)
button1 = Button(root, text="Open", command=opendoc)
button2 = Button(root, text="Quit", command=exit_command)
button.grid()
button1.grid()
button2.grid()
button.configure(background='#222323', foreground="#00ff00", font=("Courier", 10))
button1.configure(background='#222323', foreground="#00ff00", font=("Courier", 10))
button2.configure(background='#222323', foreground="#ff0000", font=("Courier", 10))


root.mainloop()
