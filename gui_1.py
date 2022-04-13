from tkinter import *

root = Tk()
root.minsize(height=500, width=900)


def tab1():


   def tab2():

       root = Tk()
       root.title("Sudoku Solver")  # title
       root.option_add('*Font', 'Impact')  # to change text font
       root.geometry("455x450")  # the dimensions of the GUI
       root.configure(bg='#222021')

       label = Label(root, text="Fill in the numbers and click solve").grid(row=0, column=1, columnspan=10)

       errLabel = Label(root, text="", fg="red")
       errLabel.grid(row=15, columnspan=10, pady=5)

       solvedLabel = Label(root, text="", fg="green")
       solvedLabel.grid(row=15, columnspan=10, pady=5)

       cells = {}

       def ValidateNumber(P):
           out = (P.isdigit() or P == "") and len(P) < 2
           return out

       reg = root.register(ValidateNumber)

       def draw3x3Grid(row, column, bgcolor):
           for i in range(3):
               for j in range(3):
                   e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
                   e.grid(row=row + i + 1, column=column + j + 1, sticky="nsew", padx=1, pady=1, ipady=5)
                   cells[(row + i + i, column + j + 1)] = e

       def draw9x9Grid():
           color = "#ffffff"
           for rowNo in range(1, 10, 3):
               for colNo in range(0, 9, 3):
                   draw3x3Grid(rowNo, colNo, color)
                   if color == "#ffffff":
                       color = "#ffffD0"
                   else:
                       color = "#ffffff"

       def clearValues():
           errLabel.configure(text="")
           solvedLabel.configure(text="")
           for row in range(2, 11):
               for col in range(1, 10):
                   cell = cells[(row, col)]
                   cell.delete(0, "end")

       def getValues():
           board = []
           errLabel.configure(text="")
           solvedLabel.configure(text="")
           for row in range(2, 11):
               rows = []
               for col in range(1, 10):
                   val = cells[(row, col)].get()
                   if val == "":
                       rows.append(0)
                   else:
                       rows.append(int(val))

               board.append(rows)

       btn = Button(root, command=getValues, text="Solve", width=10)
       btn.grid(row=20, column=1, columnspan=5, pady=20)

       btn = Button(root, command=clearValues, text="Clear", width=10)
       btn.grid(row=20, column=5, columnspan=5, pady=20)

       draw9x9Grid()
       root.mainloop()



   label1 = Label(root, text='Instructions', font=('Times_New_Romans', 15))
   label1.pack()
   button1 = Button(root, text='GO TO SUDOKU', font=('Times_New_Romans', 20), command=tab2)
   button1.pack(side=BOTTOM)

   text = Text(root)
   text.insert(INSERT, "1. Sudoku instructions\n"
                       "2. Instructions go here..")
   text.pack()

tab1()
root.mainloop()

