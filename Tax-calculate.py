'''
 Modification required add email and lining i.e boxes
'''

from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from tkinter.font import Font

######## ROOT WINDOW    ################
root = tk.Tk()
root.geometry("800x450")
root.resizable(False, False)
root.title("Tax Calculator")

# 10*120 120*280
############# DRAW BOXES ################
canvas = Canvas(root)
canvas.place(x=0, y=0, width=800, height=450)
# canvas.create_line(5, 115, 5, 285, dash=(4, 2))
# Input Box
canvas.create_line(5, 115, 5, 320)
canvas.create_line(5, 320, 220, 320)
canvas.create_line(220, 320, 220, 115)
canvas.create_line(220, 115, 5, 115)
# Seperator
canvas.create_line(250, 25, 250, 425, dash=(4, 2))

############# VARIABLES ################
TotalIncome = StringVar(root, value="")
Invested80c = StringVar(root, value="")
LoanAmt = StringVar(root, value="")

############# FUNCTIONS ################
def reset():
    TotalIncome.set("")
    Invested80c.set("")
    LoanAmt.set("")
def tax():
    if ((TotalIncome.get() != "") or (Invested80c.get() != "") or (LoanAmt.get() != "")):
        if (TotalIncome.get().isdigit() and Invested80c.get().isdigit() and LoanAmt.get().isdigit()):
            totalIc = int(TotalIncome.get())
            invest80 = int(Invested80c.get())
            loneHome = int(LoanAmt.get())
            healthIn = 30_000
            expense = 30_000+invest80
            actualLoan = int(totalIc*0.3)
            if (totalIc > 30000):
                if(totalIc-invest80 >= 30000):
                    if(invest80 <= 150000):
                        if (totalIc >= expense):
                            if (loneHome <= totalIc-expense):
                                if(loneHome <= actualLoan):
                                    amount = totalIc - expense - loneHome
                                    totalTax = 0
                                    if (amount > 2_000_000):
                                        totalTax += ((amount-2_000_000)*0.3 + 200_000 + 37_500 + 25_000)
                                    elif (amount > 1_000_000):
                                        totalTax += ((amount-1_000_000)*0.2 + 37_500 + 25_000)
                                    elif (amount > 750_000):
                                        totalTax += ((amount-750_000)*0.15 + 25_000)
                                    elif (amount > 500_000):
                                        totalTax += ((amount-500_000)*0.1)
                                    result = Label(root, text=f"{totalTax}", font=Font(family='Courier', size=25, weight='bold')).place(x=50, y=350)
                                    output(amount)
                                else:
                                    messagebox.showinfo("Invalid", f"Home loan sholud be {actualLoan} or less.")
                                    LoanAmt.set("")
                            else:
                                messagebox.showinfo("Invalid", f"Home loan sholud be {totalIc-expense} or less.")
                                LoanAmt.set("")
                        else:
                            messagebox.showinfo("Sorry", f"You can't pay for Home Loan this month.\n As Your Income is {totalIc} and expense is {expense}")
                            LoanAmt.set("0")
                    else:
                        messagebox.showinfo("Invalid", "Max income can be invested in 80c is 1,50,000.")
                        Invested80c.set("")
                else:
                    messagebox.showinfo("Sorry", "You can't invest this much as you have to pay for HEALTH INSURANCE(30,000).")
                    Invested80c.set("")
            else:
                messagebox.showinfo("Invalid", "Total income should be atleast greater then HEALTH INSURANCE(30,000).")
                TotalIncome.set("")
        else:
            messagebox.showerror("Error", "Numbers ONLY.")
            reset()
    else:
        messagebox.showerror("Warning", "All fields are compulsory.")

####### ADDING COMPONENETS #############
incomeInput = Label(root, text="Total Income :")
incomeInput_ip = Entry(root, textvariable=TotalIncome)
invest80c = Label(root, text="80c Investment :")
invest80c_ip = Entry(root, textvariable=Invested80c)
homeLoan = Label(root, text="Home Loan Amount :")
homeLoan_ip = Entry(root, textvariable=LoanAmt)
submit = Button(root, text="Calculate", command=tax)

###### ARRANGE COMPONENT ON WINDOW #####
incomeInput.place(x=10, y=120)
incomeInput_ip.place(x=40, y=140)
invest80c.place(x=10, y=170)
invest80c_ip.place(x=40, y=190)
homeLoan.place(x=10, y=220)
homeLoan_ip.place(x=40, y=240)
submit.place(x=120, y=280)

################# OUTPUT ###############
def output(amount):
    a = int( int(TotalIncome.get()) * 0.3 )
    b =int(TotalIncome.get()) - 30000 - int(Invested80c.get()) - int(LoanAmt.get())
    c = int( LoanAmt.get() )
    opt = Frame(root)
    opt.place(x=275, y=25, width=500, height=400)
    # Max. Home Loan
    Label(opt, text="Max. Home Loan : ").place(x=10, y=25)
    Label(opt, text=f"{TotalIncome.get()} * 0.3 = {a}").place(x=45, y=40)
    # Taxable. Amt
    Label(opt, text=f"  {TotalIncome.get()}").place(x=275, y=25)
    Label(opt, text="Total Income").place(x=350, y=25)
    Label(opt, text=f"- {Invested80c.get()}").place(x=275, y=45)
    Label(opt, text="80c Investment").place(x=350, y=45)
    Label(opt, text="- 30000").place(x=275, y=65)
    Label(opt, text="Health Insurance").place(x=350, y=65)
    Label(opt, text=f"- {LoanAmt.get()}").place(x=275, y=85)
    Label(opt, text="Home Loan").place(x=350, y=85)
    Label(opt, text=f"{b}", font=Font(weight='bold')).place(x=275, y=110)
    Label(opt, text="Taxable Amount", font=Font(weight='bold')).place(x=350, y=110)
    # Final Tax
    Label(opt, text="5,00,000  to  7,00,000").place(x=50, y=200)
    Label(opt, text="10 %").place(x=220, y=200)
    Label(opt, text=" 7,00,000 to 10,00,000").place(x=50, y=220)
    Label(opt, text="15 %").place(x=220, y=220)
    Label(opt, text="10,00,000 to 20,00,000").place(x=50, y=240)
    Label(opt, text="20 %").place(x=220, y=240)
    Label(opt, text="More    >      20,00,000").place(x=50, y=260)
    Label(opt, text="30%").place(x=220, y=260)
    totalTax = 0
    if (amount > 2_000_000):
        totalTax += ((amount-2_000_000)*0.3 + 200_000 + 37_500 + 25_000)
        Label(opt, text="25000").place(x=260, y=200)
        Label(opt, text="37500").place(x=260, y=220)
        Label(opt, text="20000").place(x=260, y=240)
        Label(opt, text=f"{(amount-2_000_000)*0.3}").place(x=260, y=260)
    elif (amount > 1_000_000):
        totalTax += ((amount-1_000_000)*0.2 + 37_500 + 25_000)
        Label(opt, text="25000").place(x=260, y=200)
        Label(opt, text="37500").place(x=260, y=220)
        Label(opt, text=f"{(amount-1_000_000)*0.2}").place(x=260, y=240)
        Label(opt, text="0").place(x=260, y=260)
    elif (amount > 750_000):
        totalTax += ((amount-750_000)*0.15 + 25_000)
        Label(opt, text="25000").place(x=260, y=200)
        Label(opt, text=f"{(amount-750_000)*0.15}").place(x=260, y=220)
        Label(opt, text="0").place(x=260, y=240)
        Label(opt, text="0").place(x=260, y=260)
    elif (amount > 500_000):
        totalTax += ((amount-500_000)*0.1)
        Label(opt, text=f"{totalTax}").place(x=260, y=200)
        Label(opt, text="0").place(x=260, y=220)
        Label(opt, text="0").place(x=260, y=240)
        Label(opt, text="0").place(x=260, y=260)
    else:
        Label(opt, text="0").place(x=260, y=200)
        Label(opt, text="0").place(x=260, y=220)
        Label(opt, text="0").place(x=260, y=240)
        Label(opt, text="0").place(x=260, y=260)
    result = Label(opt, text=f"Total Tax : {totalTax}", font=Font(family='Courier', weight='bold')).place(x=100, y=300)

tk.mainloop()
