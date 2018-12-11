from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

import datetime as dt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


font1 = ("kokonor", 40, "bold", "underline")
font11 = ("kokonor", 30, "bold")
font2 = ("marion", 20, "bold")
font3 = ("marion", 15, "bold")
font4 = ("kokonor", 25, "bold",)
fontx = ("Times New Roman", 18)


window = Tk()
window.configure(background = "#383838")
window.title("Window 2")
window.geometry("1300x700+0+0")




# first function that runs the Present value calculator
def pv():

    window.destroy()


    root = Tk()
    # root.configure(background = )
    root.title("Present Value")
    root.configure(background = "black")
    root.geometry("1300x700+0+0")

    def quit():
        exit()

#Algorithm that processes the user input
    def doit():
        x = float(iv.get())
        y = float(cp.get())
        ytm = float(ex.get())
        t = int(ti.get())

        ytm = ytm * 0.01
        ytm = ytm + 1
        a = 0

        for i in range(1, t):
            z = y / (ytm ** i)
            a = a + z

        z = (y + x) / (ytm ** t)
        a = a + z
        a = round(a, 3)

        if a > x:
            answer_label = Label(root, text="The present value is: ", font=font2, fg="white", bg="black").place(x=10, y=375)
            answer_label2 = Label(root, text=a, font=font2, fg="green", bg="black").place(x=395, y=375)
        else:
            answer_label = Label(root, text="The present value is: ", font=font2, fg="white", bg="black").place(x=10, y=375)
            answer_label2 = Label(root, text=a, font=font2, fg="red", bg="black").place(x=395, y=375)

    # - - - - Labels - - -

    heading = Label(root, text="Present Value Calculator", font=font1, fg="gold",bg="black").pack()

    description = Label(root, text="* This is a calculator that will tell you how much a bond is worth ", font=font3,
                        fg="white", bg="black").place(x=10, y=130)
    description2 = Label(root, text="depending on the initial value, coupon per year, yield to maturity,", font=font3,
                         fg="white", bg="black").place(x=10, y=150)
    description3 = Label(root, text="and number of years until the bond matures.", font=font3,
                         fg="white", bg="black").place(x=10,y=170)

    label1 = Label(root, text="What is the initial value of the bond?", font=font2, fg="white", bg="black").place(x=10, y=235)
    label2 = Label(root, text="What is the coupon for the bond?", font=font2, fg="white", bg="black").place(x=10, y=270)
    label2_1 = Label(root, text="%", font=font2, fg="white", bg="black").place(x=470, y=270)
    label3 = Label(root, text="What is the yield to maturity?", font=font2, fg="white", bg="black").place(x=10, y=305)
    label3_1 = Label(root, text="%", font=font2, fg="white", bg="black").place(x=470, y=305)
    label4 = Label(root, text="In how many years will the bond mature?", font=font2, fg="white", bg="black").place(x=10, y=340)


    # - - - - Entries - - -

    iv = IntVar()
    entry1 = Entry(root, textvariable=iv, width=7).place(x=395, y=235)

    cp = IntVar()
    entry2 = Entry(root, textvariable=cp, width=7).place(x=395, y=270)

    ex = IntVar()
    entry3 = Entry(root, textvariable=ex, width=7).place(x=395, y=305)

    ti = IntVar()
    entry4 = Entry(root, textvariable=ti, width=7).place(x=395, y=340)

    # - - - - Buttons - - -

    work = Button(root, text="Calculate", width=10, font=fontx, fg="black", command=doit).place(x=280, y=425)
    quit = Button(root, text="Quit", width=10, font=fontx, fg="black", command=quit).place(x=395, y=425)

    root.mainloop()


# Function that runs the compund interest visualizer
def cg():

    window.destroy()


    frame = Tk()
    frame.title("Compound Interest")
    frame.geometry("1300x700")
    frame.configure(background = "black")


    def quit_2():
        exit()

# algorithm that processes the user input
    def calculate_command():
        x = int(ii.get())
        y = int(ci.get())
        t = int(ti.get())


        y = y * 0.01
        y = y + 1
        t += 1
        list_t = []
        list_x=[]

        for i in range(1, t):
            list_t.append(i)
            z = x * y
            z = round(z, 2)
            list_x.append(z)
            x = x * y

        t = t-1
        t = str(t)
        print("The values are: ", list_x)
        plt.plot(list_t, list_x)
        plt.xlabel("Years")
        plt.ylabel("Amount")
        plt.title("Compound interest over " + t + " years")
        plt.show()

    # - - - - Buttons - - -

    bt1 = Button(frame, text="Run", width=10, font=fontx, command=calculate_command)
    bt1.place(x=200, y=330)

    bt2 = Button(frame, text="Quit", width=10, font=fontx, command=quit_2)
    bt2.place(x=300, y=330)

    # - - - - Labels - - -

    heading = Label(frame, text="Compound Interest Visualizer", font=font1, fg="gold", bg="black")
    heading.place(x=385, y=10)

    lb1 = Label(frame, text="Initial Investment", font=fontx, fg="white", bg="black" )
    lb1.place(x=200, y=200)

    lb2 = Label(frame, text="Compound Interest", font=fontx, fg="white", bg="black")
    lb2.place(x=200, y=230)

    lb3 = Label(frame, text="Years to display", font=fontx, fg="white", bg="black")
    lb3.place(x=200, y=260)

    lb4 = Label(frame, text="* This tool will allow you to visualize the future value of an", font=fontx, fg="white", bg="black")
    lb4.place(x=700, y=140)

    lb5 = Label(frame, text="investment when applying a compound interest.", font=fontx, fg="white",
                bg="black")
    lb5.place(x=700, y=160)

    # - - - - Entries - - -

    ii = IntVar()
    et1 = Entry(frame, textvariable=ii, width = 12)
    et1.place(x=400, y=200)

    ci = IntVar()
    et2 = Entry(frame, textvariable=ci, width = 12)
    et2.place(x=400, y=230)

    ti = IntVar()
    et3 = Entry(frame, textvariable=ti, width=12)
    et3.place(x=400, y=260)




    frame.mainloop()


# Project manager function
def pj():
    window.destroy()

    frame2 = Tk()
    frame2.title("Income Statement")
    frame2.geometry("1920x1080")
    bg_color = "#f66666"
    # bg_color = "#383838"
    entriescolor = "#b8b8b8"

    tablecolor = "#f29a7f"
    frame2.configure(background=bg_color)

    # fonts used
    headingfont = ("Arial Bold", 20)
    use_font = ("marion", 10)
    subheadingfont = ("Arial", 11, "bold")

    # these are all the labels fot the table
    lbl = Label(frame2, text="Project Manager", font=("Arial Bold", 30, "underline"), width=30, background=bg_color)
    lbl.grid(column=3, row=0)

    lbl_sales = Label(frame2, text="Total nº Sales", font=headingfont, width=25, background=tablecolor)
    lbl_sales.grid(column=0, row=1)

    lbl_revenues = Label(frame2, text="Total Revenue", font=headingfont, width=25, background=tablecolor)
    lbl_revenues.grid(column=0, row=3)

    lbl_costsheading = Label(frame2, text="Total Cost for 5 years", font=headingfont, width=25, background=tablecolor)
    lbl_costsheading.grid(column=0, row=5)

    lbl_pretax_profit = Label(frame2, text="Total Pre-Tax Profit", font=headingfont, width=25, background=tablecolor)
    lbl_pretax_profit.grid(column=0, row=7)

    lbl_aftertax_profit = Label(frame2, text="Total After-tax Profit", font=headingfont, width=25,
                                background=tablecolor)
    lbl_aftertax_profit.grid(column=0, row=9)

    def doProfits():
        tx = float(tax.get() / 100)

        # following code calculates the revenue again
        a = PPP.get()
        x = int(s1.get())
        y = int(s2.get())
        z = int(s3.get())
        u = int(s4.get())
        v = int(s5.get())
        saleslist = []
        saleslist.append(x)
        saleslist.append(y)
        saleslist.append(z)
        saleslist.append(u)
        saleslist.append(v)

        sales = sum(saleslist)

        revenue = a * sales

        # calculate the cost again
        c = CPP.get()

        x1 = float(s1.get())
        y1 = float(s2.get())
        z1 = float(s3.get())
        u1 = float(s4.get())
        v1 = float(s5.get())
        saleslist1 = []
        saleslist1.append(x1)
        saleslist1.append(y1)
        saleslist1.append(z1)
        saleslist1.append(u1)
        saleslist1.append(v1)

        sales1 = sum(saleslist1)
        costs = c * sales1
        costs = round(costs, 3)

        pre_tax_profit = revenue - costs

        if pre_tax_profit <= 0:
            lbl_profit = Label(frame2, text="#error", font=headingfont, width=15, background=bg_color).grid(column=1,
                                                                                                            row=9)  # if the pretax profit is negative or equal to 0 you can't tax it
        else:
            taxed_profit = pre_tax_profit * tx  # multiply by the tax the user entered in the GUI
            taxed_profit = round(taxed_profit, 3)
            lbl_profit = Label(frame2, text=taxed_profit, font=headingfont, width=15, background=bg_color).grid(
                column=1, row=9)

        lbl_profit = Label(frame2, text=pre_tax_profit, font=headingfont, width=15, background=bg_color).grid(column=1,
                                                                                                              row=7)

        revenue = 0
        costs = 0

    def doRevenue():  # name is self explanatory, calculates the revenue by taking the entire number of sales and multiplying it by the price of each product being sold (entered by the user)
        a = PPP.get()
        x = int(s1.get())
        y = int(s2.get())
        z = int(s3.get())
        u = int(s4.get())
        v = int(s5.get())
        saleslist = []
        saleslist.append(x)
        saleslist.append(y)
        saleslist.append(z)
        saleslist.append(u)
        saleslist.append(v)

        sales = sum(saleslist)

        revenue = a * sales

        lbl_price = Label(frame2, text=revenue, font=headingfont, width=15, background=bg_color).grid(column=1, row=3)
        revenue = 0

    def doCosts():  # calculates total number of sales and multiplies it by the cost per product so it gives you the total Cost of the project
        c = CPP.get()

        x = float(s1.get())
        y = float(s2.get())
        z = float(s3.get())
        u = float(s4.get())
        v = float(s5.get())
        saleslist = []
        saleslist.append(x)
        saleslist.append(y)
        saleslist.append(z)
        saleslist.append(u)
        saleslist.append(v)

        sales = sum(saleslist)
        costs = c * sales
        costs = round(costs, 3)
        lbl_costs = Label(frame2, text=costs, font=headingfont, width=15, background=bg_color).grid(column=1, row=5)
        costs = 0  # resets the cost to 0 so it doesn't stack and therefore the total cost would be increasing everytime ou wanted to change the cost per product (as costs are not getting in any list)

    def doSales():  # does the number of sales
        x = int(s1.get())
        y = int(s2.get())
        z = int(s3.get())
        u = int(s4.get())
        v = int(s5.get())
        saleslist = []
        saleslist.append(x)
        saleslist.append(y)
        saleslist.append(z)
        saleslist.append(u)
        saleslist.append(v)

        sales = sum(saleslist)
        lbl_sale_result = Label(frame2, text=sales, font=headingfont, background=bg_color).grid(column=1,
                                                                                                row=1)  # shows the result of the total number of sales for the 5 years when pressing the button

    def doGraph():
        x = int(s1.get())
        y = int(s2.get())
        z = int(s3.get())
        u = int(s4.get())
        v = int(s5.get())
        saleslist = []  # needed to plot a graph
        saleslist.append(x)
        saleslist.append(y)
        saleslist.append(z)
        saleslist.append(u)
        saleslist.append(v)

        # the graph will change color in respect to the sales of the company in the project
        if x < y and y < z and z < u and u < v:
            plt.plot(saleslist, color="green")
            plt.xlabel("Years (counting from year 0)")
            plt.ylabel("Amount of sales")
            plt.title("Sales of Project")
            plt.show()
        elif x > y and y > z and z > u and u > v:
            plt.plot(saleslist, color="red")
            plt.xlabel("Years (counting from year 0)")
            plt.ylabel("Amount of sales")
            plt.title("Sales of Project")
            plt.show()
        else:
            plt.plot(saleslist, color="orange")
            plt.xlabel("Years (counting from year 0)")
            plt.ylabel("Amount of sales")
            plt.title("Sales of Project")
            plt.show()

    # all the inputs for each years sales and the sales labels at the bottom

    lbl_sales1 = Label(frame2, text="Sale 1", width=10, font=("Arial", 10), background=bg_color)
    lbl_sales1.place(x=0, y=520)

    lbl_sales2 = Label(frame2, text="Sale 2", width=10, font=("Arial", 10), background=bg_color)
    lbl_sales2.place(x=0, y=550)

    lbl_sales3 = Label(frame2, text="Sale 3", width=10, font=("Arial", 10), background=bg_color)
    lbl_sales3.place(x=0, y=580)

    lbl_sales4 = Label(frame2, text="Sale 4", width=10, font=("Arial", 10), background=bg_color)
    lbl_sales4.place(x=0, y=610)

    lbl_sales5 = Label(frame2, text="Sale 5", width=10, font=("Arial", 10), background=bg_color)
    lbl_sales5.place(x=0, y=640)

    # my subheadings
    lblinputsales = Label(frame2, text="Input Sales", font=subheadingfont, width=12, background=bg_color).place(x=0,
                                                                                                                y=480)

    lbl_price_per_product = Label(frame2, text="Type your Price Per Product:", font=subheadingfont, width=25,
                                  background=bg_color).place(x=190, y=480)

    lbl_cost_per_product = Label(frame2, text="Type the Cost Per Product:", font=subheadingfont, width=25,
                                 background=bg_color).place(x=460, y=480)

    lbl_tax = Label(frame2, text="What are the taxes in your country?", font=subheadingfont, width=27,
                    background=bg_color).place(x=740, y=480)

    lbl_profit = Label(frame2, text="CALCULATE PROFIT \n FOR \n THE PROJECT", font=subheadingfont, width=35,
                       background="#e9e18b").place(x=710, y=530)

    # all the entries
    s1 = IntVar()
    etsale1 = Entry(frame2, textvariable=s1, font=use_font, width=7, bg=entriescolor)
    etsale1.place(x=100, y=520)

    s2 = IntVar()
    etsale2 = Entry(frame2, textvariable=s2, font=use_font, width=7, bg=entriescolor)
    etsale2.place(x=100, y=550)

    s3 = IntVar()
    etsale3 = Entry(frame2, textvariable=s3, font=use_font, width=7, bg=entriescolor)
    etsale3.place(x=100, y=580)

    s4 = IntVar()
    etsale4 = Entry(frame2, textvariable=s4, font=use_font, width=7, bg=entriescolor)
    etsale4.place(x=100, y=610)

    s5 = IntVar()
    etsale5 = Entry(frame2, textvariable=s5, font=use_font, width=7, bg=entriescolor)
    etsale5.place(x=100, y=640)

    PPP = DoubleVar()
    etPPP = Entry(frame2, textvariable=PPP, font=use_font, width=5, bg=entriescolor)
    etPPP.place(x=410, y=483)

    CPP = DoubleVar()  # Needs to get a doubleVar do the multilication in the docosts method works properly
    etCPP = Entry(frame2, textvariable=CPP, font=use_font, width=5, bg=entriescolor)
    etCPP.place(x=680, y=483)

    tax = IntVar()
    etTax = Entry(frame2, textvariable=tax, font=use_font, width=3, bg=entriescolor)
    etTax.place(x=995, y=483)

    # all the buttons used are at the bottom so no accesibility problems appear in the methods
    btnsales = Button(frame2, text="Calculate Sales", width=15, height=2, font=use_font, fg="#000000", command=doSales,
                      bg=entriescolor)
    btnsales.place(x=20, y=670)

    btnprice = Button(frame2, text="Calculate Revenue", width=15, height=2, font=use_font, command=doRevenue,
                      bg=entriescolor, fg="#000000")
    btnprice.place(x=250, y=520)

    btnsales = Button(frame2, text="Calculate Costs", width=15, height=2, font=use_font, fg="#000000", command=doCosts,
                      bg=entriescolor)
    btnsales.place(x=520, y=520)

    btnprofit = Button(frame2, text="Calculate Profit", font=use_font, command=doProfits, width=16, height=4,
                       bg=entriescolor, fg="#000000")
    btnprofit.place(x=800, y=600)

    btngraph = Button(frame2, text="Sales Graph", font=use_font, command=doGraph, width=15, height=2, bg=entriescolor,
                      fg="#000000")
    btngraph.place(x=140, y=670)

    frame2.mainloop()













# main page GUI

#- - - - Labels - - -

heading = Label(window, text="Welcome to the ultimate financial tool", font=font1, fg="#e3570b", bg = "#383838")
heading.place(x=300, y=10)

heading_2 = Label(window, text="How can I help you?", font=font11, fg="#e3570b", bg = "#383838")
heading_2.place(x=490, y=300)

#- - - - Buttons - - -
pv = Button(window, text = "PV Calculator", width = 13, height=1, font = font4, fg="blue", command=pv)
pv.place(x=240, y=500)

cg = Button(window, text = "Compound Interest", width = 17, height=1, font = font4, fg="blue", command=cg)
cg.place(x=510, y=500)

st = Button(window, text = "Project Manager", width = 17, height=1, font = font4, fg="blue", command=pj)
st.place(x=840, y=500)

window.mainloop()