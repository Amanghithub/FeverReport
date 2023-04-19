from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Fever Report")
root.geometry("600x600")
root.configure(background="#FFDCB6")

q1_rb = StringVar(value="0")
q1_lbl = Label(root,text="Do you have headache and sore throat?")
q1_lbl.pack()
q1_rb_1 = Radiobutton(root,text="Yes",variable=q1_rb,value="yes")
q1_rb_1.pack()

q1_rb_2 = Radiobutton(root,text="No",variable=q1_rb,value="no")
q1_rb_2.pack()

#2nd question
q2_rb = StringVar(value="0")
q2_lbl = Label(root,text="Is your body temperature high?")
q2_lbl.pack()
q2_rb_1 = Radiobutton(root,text="Yes",variable=q2_rb,value="yes")
q2_rb_1.pack()

q2_rb_2 = Radiobutton(root,text="No",variable=q2_rb,value="no")
q2_rb_2.pack()

#3rd question

q3_rb = StringVar(value="0")
q3_lbl = Label(root,text="Are there any symptoms of eye redness?")
q3_lbl.pack()
q3_rb_1 = Radiobutton(root,text="Yes",variable=q3_rb,value="yes")
q3_rb_1.pack()

q3_rb_2 = Radiobutton(root,text="No",variable=q3_rb,value="no")
q3_rb_2.pack()

#condtitons

def fever_score():
    score = 0
    if q1_rb.get() == "yes":
        score = score+20
        
    if q2_rb.get() == "yes":
        score = score+20
        
    if q3_rb.get() == "yes":
        score = score+20
        
    if score<=20:
        messagebox.showinfo("Report","You Don't Need To Visit a Doctor")
        
    elif score>20 and score<=40:
        messagebox.showinfo("Report","You Might Perhaps Have To Visit a Doctor")
    else:
        messagebox.showinfo("Report","You Strongly Adviced To Visit a Doctor")
        
btn_check = Button(root,text="Check",command=fever_score)
btn_check.pack()
root.mainloop()