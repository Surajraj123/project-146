from tkinter import * 

root = Tk()

root.title("Fibonacci Sum")
root.geometry("400x400")
root.configure(background = "magenta")

input1 = Entry(root)

label_1 = Label(root, text = "Fibonacci Series: ", bg = "cyan", fg = "black")
label_2 = Label(root, bg = "gold", fg = "black")

def Fibonacci():
    num = int(input1.get())
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    sum2 = 0
    while(counter <= num):
        label_1["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + second_no
        label_2["text"] = "Fibonacci Sum: " + str(sum2)
        
btn = Button(root, text = "Show Fibonacci Series", command= Fibonacci, bg = "pink", fg = "blue")

input1.pack()
btn.pack()
label_1.pack()
label_2.pack()

root.mainloop()


        