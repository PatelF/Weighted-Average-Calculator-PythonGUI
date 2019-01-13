from tkinter import *
import tkinter.messagebox
from tkinter.font import BOLD

root = Tk()

root.title("Weighted Average Calculator")
root.geometry("390x270")

title = Label(root, text = "Weighted Average Calculator", font = ("ariel", 10, "bold"), fg = "steelblue").grid(row = 0, column = 1)
avg_One = Label(root, text = "Mark")
weight_One = Label(root, text = "Weight")
avg_One.grid(row = 1, column = 0)
weight_One.grid(row = 1, column = 2)

avg_Two = Label(root, text = "Mark")
weight_Two = Label(root, text = "Weight")
avg_Two.grid(row = 2, column = 0)
weight_Two.grid(row = 2, column = 2)

avg_Three = Label(root, text = "Mark")
weight_Three = Label(root, text = "Weight")
avg_Three.grid(row = 3, column = 0)
weight_Three.grid(row = 3, column = 2)

avg_Four = Label(root, text = "Mark")
weight_Four = Label(root, text = "Weight")
avg_Four.grid(row = 4, column = 0)
weight_Four.grid(row = 4, column = 2)

avg_Five = Label(root, text = "Mark")
weight_Five = Label(root, text = "Weight")
avg_Five.grid(row = 5, column = 0)
weight_Five.grid(row = 5, column = 2)

avg_Six = Label(root, text = "Mark")
weight_Six = Label(root, text = "Weight")
avg_Six.grid(row = 6, column = 0)
weight_Six.grid(row = 6, column = 2)

avg_Seven = Label(root, text = "Mark")
weight_Seven = Label(root, text = "Weight")
avg_Seven.grid(row = 7, column = 0)
weight_Seven.grid(row = 7, column = 2)

avg_Eight= Label(root, text = "Mark")
weight_Eight = Label(root, text = "Weight")
avg_Eight.grid(row = 8, column = 0)
weight_Eight.grid(row = 8, column = 2)

avg_Nine = Label(root, text = "Mark")
weight_Nine = Label(root, text = "Weight")
avg_Nine.grid(row = 9, column = 0)
weight_Nine.grid(row = 9, column = 2)

avg_Ten = Label(root, text = "Mark")
weight_Ten = Label(root, text = "Weight")
avg_Ten.grid(row = 10, column = 0)
weight_Ten.grid(row = 10, column = 2)

s1_avg = StringVar()
s2_avg = StringVar()
s3_avg = StringVar()
s4_avg = StringVar()
s5_avg = StringVar()
s6_avg = StringVar()
s7_avg = StringVar()
s8_avg = StringVar()
s9_avg = StringVar()
s10_avg = StringVar()

s1_weight = StringVar()
s2_weight = StringVar()
s3_weight = StringVar()
s4_weight = StringVar()
s5_weight = StringVar()
s6_weight = StringVar()
s7_weight = StringVar()
s8_weight = StringVar()
s9_weight = StringVar()
s10_weight = StringVar()

entry_avg_1 = Entry(root, width = 10, textvariable = s1_avg)
entry_avg_1.grid(row = 1, column = 1)

entry_avg_2 = Entry(root, width = 10, textvariable = s2_avg)
entry_avg_2.grid(row = 2, column = 1)

entry_avg_3 = Entry(root, width = 10, textvariable = s3_avg)
entry_avg_3.grid(row = 3, column = 1)

entry_avg_4 = Entry(root, width = 10, textvariable = s4_avg)
entry_avg_4.grid(row = 4, column = 1)

entry_avg_5 = Entry(root, width = 10, textvariable = s5_avg)
entry_avg_5.grid(row = 5, column = 1)

entry_avg_6 = Entry(root, width = 10, textvariable = s6_avg)
entry_avg_6.grid(row = 6, column = 1)

entry_avg_7 = Entry(root, width = 10, textvariable = s7_avg)
entry_avg_7.grid(row = 7, column = 1)

entry_avg_8 = Entry(root, width = 10, textvariable = s8_avg)
entry_avg_8.grid(row = 8, column = 1)

entry_avg_9 = Entry(root, width = 10, textvariable = s9_avg)
entry_avg_9.grid(row = 9, column = 1)

entry_avg_10 = Entry(root, width = 10, textvariable = s10_avg)
entry_avg_10.grid(row = 10, column = 1)


entry_weight_1 = Entry(root, width = 10, textvariable = s1_weight)
entry_weight_1.grid(row = 1, column = 3)

entry_weight_2 = Entry(root, width = 10, textvariable = s2_weight)
entry_weight_2.grid(row = 2, column = 3)

entry_weight_3 = Entry(root, width = 10, textvariable = s3_weight)
entry_weight_3.grid(row = 3, column = 3)

entry_weight_4 = Entry(root, width = 10, textvariable = s4_weight)
entry_weight_4.grid(row = 4, column = 3)

entry_weight_5 = Entry(root, width = 10, textvariable = s5_weight)
entry_weight_5.grid(row = 5, column = 3)

entry_weight_6 = Entry(root, width = 10, textvariable = s6_weight)
entry_weight_6.grid(row = 6, column = 3)

entry_weight_7 = Entry(root, width = 10, textvariable = s7_weight)
entry_weight_7.grid(row = 7, column = 3)

entry_weight_8 = Entry(root, width = 10, textvariable = s8_weight)
entry_weight_8.grid(row = 8, column = 3)

entry_weight_9 = Entry(root, width = 10, textvariable = s9_weight)
entry_weight_9.grid(row = 9, column = 3)

entry_weight_10 = Entry(root, width = 10, textvariable = s10_weight)
entry_weight_10.grid(row = 10, column = 3)


def findTotal():
    
    wAvg1 = float(s1_avg.get())*float(s1_weight.get())/100
    wAvg2 = float(s2_avg.get())*float(s2_weight.get())/100
    wAvg3 = float(s3_avg.get())*float(s3_weight.get())/100
    wAvg4 = float(s4_avg.get())*float(s4_weight.get())/100
    wAvg5 = float(s5_avg.get())*float(s5_weight.get())/100
    wAvg6 = float(s6_avg.get())*float(s6_weight.get())/100
    wAvg7 = float(s7_avg.get())*float(s7_weight.get())/100
    wAvg8 = float(s8_avg.get())*float(s8_weight.get())/100
    wAvg9 = float(s9_avg.get())*float(s9_weight.get())/100
    wAvg10 = float(s10_avg.get())*float(s10_weight.get())/100
    
    tkinter.messagebox.showinfo("Answer", wAvg1 + wAvg2 + wAvg3 + wAvg4 + wAvg5 + wAvg6 + wAvg7 + wAvg8 + wAvg9 + wAvg10)
    print ("test")
    

btn = Button(root, text = "Submit", command = findTotal)
btn.grid(padx = 2)
root.mainloop()