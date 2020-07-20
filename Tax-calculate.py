'''
    Edit sender mail (line no. 204) and sender pasword (line no. 205)
                and smtp server (line no. 221) before runnig code
'''
"""
This code will calculate tax and inform you using email 
        ( FOR SENDING MAIL INTERNET CONNECTION IS MUST )
tax calculate on basis
1) You have to pay for 80c Investment, health Insurance, home loan
2) health Insurance is 30,000 and it is compulsary
3) Max investment in 80c is 1,50,000
4) Max. Home Loan you can pay is 30% of your Total income
    (Final Income) = (Total income) - (80c Invest) - (Health Insurance) - (Home Loan)
5) After Calculting final Income Tax is applied on following basis
        a) 5,00,000 to 7,50,000 is 10% of final Income
        b) 7,50,000 to 10,00,000 is 15% of final Income
        c) 10,00,000 to 20,00,000 is 20% of final Income
        d) More then 20,00,000 is 30% of final Income
"""

# Tkinter packages
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from tkinter.font import Font

# Email Package
import ssl,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

######## ROOT WINDOW    ################
root = tk.Tk()
root.geometry("800x450")
root.resizable(False, False)
root.title("Tax Calculator")

############# DRAW BOXES ################
canvas = Canvas(root)
canvas.place(x=0, y=0, width=800, height=450)
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
    if ((TotalIncome.get() != "") and (Invested80c.get() != "") and (LoanAmt.get() != "")):
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
                                    result = Label(root, text=f"{int(totalTax)}", font=Font(family='Courier', size=25, weight='bold')).place(x=20, y=350)
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
                    Invested80c.set("0")
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
name = StringVar(root, value="")
email = StringVar(root, value="")
taxVar = IntVar(root, value=0)
def to2Decimal(num):
    return "{0:.2f}".format(num)
def output(amount):
    opt = Frame(root)
    a = int( int(TotalIncome.get()) * 0.3 )
    b =int(TotalIncome.get()) - 30000 - int(Invested80c.get()) - int(LoanAmt.get())
    c = int( LoanAmt.get() )
    opt.place(x=275, y=25, width=500, height=400)
    # Max. Home Loan
    Label(opt, text="Max. Home Loan : ").place(x=10, y=25)
    Label(opt, text=f"{TotalIncome.get()} * 0.3 ").place(x=40, y=50)
    Label(opt, text=f"= {a}").place(x=70, y=70)
    # Taxable. Amt
    Label(opt, text="Total Income").place(x=300, y=25)
    Label(opt, text=f"  {TotalIncome.get()}").place(x=400, y=25)
    Label(opt, text="80c Investment").place(x=285, y=45)
    Label(opt, text=f"- {Invested80c.get()}").place(x=400, y=45)
    Label(opt, text="Health Insurance").place(x=275, y=65)
    Label(opt, text="- 30000").place(x=400, y=65)
    Label(opt, text="Home Loan").place(x=310, y=85)
    Label(opt, text=f"- {LoanAmt.get()}").place(x=400, y=85)
    Label(opt, text="Taxable Amount", font=Font(weight='bold')).place(x=240, y=110)
    Label(opt, text=f"{b}", font=Font(weight='bold')).place(x=400, y=110)
    # Final Tax
    Label(opt, text="5,00,000 to 7,50,000").place(x=66, y=200)
    Label(opt, text="10 %").place(x=210, y=200)
    Label(opt, text="7,50,000 to 10,00,000").place(x=58, y=220)
    Label(opt, text="15 %").place(x=210, y=220)
    Label(opt, text="10,00,000 to 20,00,000").place(x=50, y=240)
    Label(opt, text="20 %").place(x=210, y=240)
    Label(opt, text="=> 20,00,000").place(x=109, y=260)
    Label(opt, text="30%").place(x=210, y=260)
    totalTax = 0
    if (amount > 2_000_000):
        totalTax += ((amount-2_000_000)*0.3 + 200_000 + 37_500 + 25_000)
        Label(opt, text="25000.00").place(x=260, y=200)
        Label(opt, text="37500.00").place(x=260, y=220)
        Label(opt, text="20000.00").place(x=260, y=240)
        Label(opt, text=f"{to2Decimal((amount-2_000_000)*0.3)}").place(x=260, y=260)
    elif (amount > 1_000_000):
        totalTax += ((amount-1_000_000)*0.2 + 37_500 + 25_000)
        Label(opt, text="25000.00").place(x=260, y=200)
        Label(opt, text="37500.00").place(x=260, y=220)
        Label(opt, text=f"{to2Decimal((amount-1_000_000)*0.2)}").place(x=260, y=240)
        Label(opt, text="0.00").place(x=260, y=260)
    elif (amount > 750_000):
        totalTax += ((amount-750_000)*0.15 + 25_000)
        Label(opt, text="25000.00").place(x=260, y=200)
        Label(opt, text=f"{to2Decimal((amount-750_000)*0.15)}").place(x=260, y=220)
        Label(opt, text="0.00").place(x=260, y=240)
        Label(opt, text="0.00").place(x=260, y=260)
    elif (amount > 500_000):
        totalTax += ((amount-500_000)*0.1)
        Label(opt, text=f"{to2Decimal(totalTax)}").place(x=260, y=200)
        Label(opt, text="0.00").place(x=260, y=220)
        Label(opt, text="0.00").place(x=260, y=240)
        Label(opt, text="0.00").place(x=260, y=260)
    else:
        Label(opt, text="0.00").place(x=260, y=200)
        Label(opt, text="0.00").place(x=260, y=220)
        Label(opt, text="0.00").place(x=260, y=240)
        Label(opt, text="0.00").place(x=260, y=260)
    totalTax = to2Decimal(totalTax)
    taxVar.set(totalTax)
    result = Label(opt, text=f"Total Tax : {totalTax}", font=Font(family='Courier', weight='bold')).place(x=100, y=300)
    Label(opt, text="Enter your name : ").place(x=25, y=325)
    Entry(opt, textvariable=name).place(x=150, y=323)
    Label(opt, text="Enter your Email : ").place(x=25, y=353)
    Entry(opt, textvariable=email).place(x=150, y=350)
    Button(opt, text="Send !", command=check_mail).place(x=345, y=342)


def sendEmail():
    sender_email = ""
    password = ""
    receiver_email = email.get()
    message = MIMEMultipart("alternative")
    message["Subject"] = f"Tax Information for Mr.{name.get()}"
    message["From"] = sender_email
    message["To"] = receiver_email
    # Create your message
    if (taxVar.get() == 0):
        msg = f"Hello Mr.{name.get()}, You have NO TAX to pay...."
    else:
        msg = f"Hello Mr.{name.get()}, You have {taxVar.get()} to pay...."
    # Turn to MIMEText objects
    mimeObj = MIMEText(msg, "plain")
    # Attach MIMEMultipart message to message
    message.attach(mimeObj)
    # Create secure connection with server and send email
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
        server.login(sender_email, password)
        # Send the mail
        server.sendmail(sender_email, receiver_email, message.as_string())
        messagebox.showinfo("Successful", "Email Sent..")
    except:
        messagebox.showinfo("Sorry", "Unable to send message.\n TRY AGAIN")
    SERVER_STATUS.quit()


def check_mail():
    if ( name.get() != "" and email.get() != "" ):
        try:
            email.get().index('@')
            sendEmail()
        except:
            messagebox.showwarning("Invalid", "Email is invalid.")
            email.set("")
    else:
        messagebox.showwarning("Invalid", "Emails or Name are empty.")


tk.mainloop()
