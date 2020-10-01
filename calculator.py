from tkinter import *



root = Tk()


root.geometry("350x480")
root.title("Calculator using python")

displayvar = StringVar()
displayvar.set("")




def click(event):
    text = event.widget.cget("text")
    if (text == "9" or text == "8" or text == "7" or text =="6" or text == "5" or text == "4" or text == "3" or text == "2" or text == "1" or text == "0" or text == "+" or text == "-" or text == "*" or text == "/"):
        displayvar.set(displayvar.get() + text)
        display.update()
    if (text == "AC"):
        displayvar.set("")
        display.update()
    if (text == "="):
        if (displayvar.get().isdigit()):
            value = int(displayvar.get())
        else:
            value = eval(display.get())
        displayvar.set(value)
        display.update()


display = Entry(root, textvar = displayvar, font = ("comicsansms 20 bold"), borderwidth = 8, relief = SUNKEN)
display.pack(fill = X, ipadx = 20, ipady = 2, pady = 20)



frame = Frame(root, relief = SUNKEN)
b9 = Button(frame, text = "7", font = ("comicsansms 20 bold"))
b9.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b9.bind(("<Button-1>"), click)
b8 = Button(frame, text = "8", font = ("comicsansms 20 bold"))
b8.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b8.bind(("<Button-1>"), click)
b7 = Button(frame, text = "9", font = ("comicsansms 20 bold"))
b7.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b7.bind(("<Button-1>"), click)
b_ac = Button(frame, text = "AC", font = ("comicsansms 20 bold"))
b_ac.pack(ipadx = 0, ipady = 10, padx = 10, pady = 10, side = LEFT)
b_ac.bind(("<Button-1>"), click)
frame.pack(anchor = W)


frame = Frame(root)
b6 = Button(frame, text = "4", font = ("comicsansms 20 bold"))
b6.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b6.bind(("<Button-1>"), click)
b5 = Button(frame, text = "5", font = ("comicsansms 20 bold"))
b5.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b5.bind(("<Button-1>"), click)
b4 = Button(frame, text = "6", font = ("comicsansms 20 bold"))
b4.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b4.bind(("<Button-1>"), click)
frame.pack(anchor = W)
b_equal = Button(frame, text = "=", font = ("comicsansms 20 bold"))
b_equal.pack(ipadx = 12, ipady = 10, padx = 10, pady = 10, side = LEFT)
b_equal.bind(("<Button-1>"), click)



frame = Frame(root)
b3 = Button(frame, text = "1", font = ("comicsansms 20 bold"))
b3.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b3.bind(("<Button-1>"), click)
b2 = Button(frame, text = "2", font = ("comicsansms 20 bold"))
b2.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b2.bind(("<Button-1>"), click)
b1 = Button(frame, text = "3", font = ("comicsansms 20 bold"))
b1.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b1.bind(("<Button-1>"), click)
b_substract = Button(frame, text = "-", font = ("comicsansms 20 bold"))
b_substract.pack(ipadx = 16, ipady = 10, padx = 10, pady = 10, side = LEFT)
b_substract.bind(("<Button-1>"), click)
frame.pack(anchor = W)




frame = Frame(root)
b_add = Button(frame, text = "+", font = ("comicsansms 20 bold"))
b_add.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b_add.bind(("<Button-1>"), click)
b0 = Button(frame, text = "0", font = ("comicsansms 20 bold"))
b0.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b0.bind(("<Button-1>"), click)
b_Divide = Button(frame, text = "/", font = ("comicsansms 20 bold"))
b_Divide.pack(ipadx = 10, ipady = 10, padx = 10, pady = 10, side = LEFT)
b_Divide.bind(("<Button-1>"), click)
b_multiplication = Button(frame, text = "*", font = ("comicsansms 20 bold"))
b_multiplication.pack(ipadx = 18, ipady = 10, padx = 10, pady = 10, side = LEFT)
b_multiplication.bind(("<Button-1>"), click)
frame.pack(anchor = W)



root.mainloop()
