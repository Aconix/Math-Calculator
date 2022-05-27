# Math Calculator
# v1.4.1
# Aconix (c) 2022

from tkinter import *
from tkinter import messagebox
import sys
import numpy
from decimal import Decimal

version_number = '1.4.1'

print("Math Calculator\nAconix (c) 2022\nGoing into the mainframe ;)")
print("")
print("This console shouldn't be seen to the user, but is used to debug the program is something goes wrong.")
print("=====================================================================================================")
print("")
print("Python Version Information (Program built on Python 3.8.6)")
print(sys.version)
print("Version Info")
print(sys.version_info)
print("")
# Main Window is main script.
# Other windows are defined as functions as [calculation]_Window

print("Import Successful.")
# Main
window = Tk()
window.title(f"Math Calculator v{version_number}")
window.resizable(width=False, height=False)


# This code was originally written by Wouter
# Checks to see if a script returns an error or not
# Uses float instead of the imported decimal function because it doesn't want to work.
# https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
def is_float(n):
    try:

        float(n)
        return True
    except ValueError:
        return False


# Window Functions
def rectangle_window():  # Rectangle GUI
    # Calculate Rectangle Area
    def rec_calculate():
        print("Calculating Rectangle Area.")
        # Finds values for check
        r_a_check = r_length.get()
        r_b_check = r_width.get()
        # print(r_a_check.isnumeric())
        # print(r_b_check.isnumeric())

        # Checks to see if the entered value is a number or not. Changes the label and exits the script if so.
        if not is_float(r_a_check):
            print("False")
            r_calculation.config(text="Letters, special characters or nothing present in fields.")
            return
        if not is_float(r_b_check):
            r_calculation.config(text="Letters, special characters or nothing present in fields.")
            return

        # if r_a_check.isnumeric() or r_b_check.isnumeric() == False:
        #    r_calculation.config(text="Letters or special characters present in fields.")
        #    return

        # Finds value for calculation and calculates the answer.
        #
        r_a = Decimal(r_length.get())
        print(r_a)
        r_b = Decimal(r_width.get())
        print(r_b)
        r_calculate = r_a * r_b

        print(f"Answer is {r_calculate}")
        r_calculation.config(text=f"{r_calculate}mm sq")
        print(type(r_calculate))

        # Changing the answer label by adding a NEW label in place of the old one
        # Label (rectangle_w, text=r_calculate, fg="Black", font="none 16 bold") .grid(row=8, column=0, sticky=W)

    print("Rectangle_Window Pressed")
    rectangle_w = Tk()  # Window Assignment
    rectangle_w.title("Rectangle")
    rectangle_w.resizable(width=False, height=False)  # Makes the window unresizable.

    # Labels for Rectangle GUI
    Label(rectangle_w, text="Rectangle Calculator", fg="Black", font="none 16 bold").grid(row=1, column=0,
                                                                                          sticky=W)  # Main Heading
    Label(rectangle_w, text="Enter the required measurements & then click\ncalculate to find the area of a rectangle.",
          fg="Black", font="none 12", justify="left").grid(row=2, column=0, sticky=W)  # Sub Heading

    # Length Text Box & Label
    Label(rectangle_w, text="Length (mm)", fg="Black", font="none 12").grid(row=3, column=0, sticky=W)
    r_length = Entry(rectangle_w, bd=5)
    r_length.grid(row=4, column=0, columnspan=2, sticky=W)

    # Width Section & Label
    Label(rectangle_w, text="Width (mm)", fg="Black", font="none 12").grid(row=5, column=0, sticky=W)
    r_width = Entry(rectangle_w, bd=5)
    r_width.grid(row=6, column=0, columnspan=2, sticky=W)

    # Calculate Button
    Button(rectangle_w, text="Calculate", width=10, command=rec_calculate).grid(row=7, column=0, sticky=W)

    # First generated answer Label
    r_calculation = Label(rectangle_w, text="-", fg="Black", font="none 16 bold")
    r_calculation.grid(row=8, column=0, sticky=W)  # Main Heading

    # Version number and program name
    Label(rectangle_w, text=f"Math Calculator v{version_number}", fg="Grey", anchor='se', font="none 8",
          wraplength=400).grid(row=8, column=1, sticky=W)  # version

    # Starts GUI
    rectangle_w.mainloop()
    print("[Rectangle Window Loaded]")


def square_window():  # Square GUI
    # Calculate Rectangle Area
    def squ_calculate():
        print("Calculating Square Area.")
        # Find values for numeric check.
        s_a_check = s_length.get()

        # Checks to see if the entered value is a number, and changes the label and exits the script if it's not.
        if not is_float(s_a_check):
            s_calculation.config(text="Letters, special characters or nothing present in fields.")
            return

        # Finds values for calculation & calculates equation.
        s_a = Decimal(s_length.get())
        s_calculate = s_a ** 2

        print(f"Answer is {s_calculate}")
        s_calculation.config(text=f"{s_calculate}mm sq")
        # Changing the answer label by updating the config of the label.

    print("Square Pressed")
    square_w = Tk()
    square_w.title("Square")  # window title
    square_w.resizable(width=False, height=False)  # Makes the window unresizable.

    # Labels for Rectangle GUI
    Label(square_w, text="Square Calculator", fg="Black", font="none 16 bold").grid(row=1, column=0,
                                                                                    sticky=W)  # Main Heading
    Label(square_w, text="Enter the required measurements & then click\ncalculate to find the area of a square.",
          fg="Black", font="none 12", justify="left").grid(row=2, column=0, sticky=W)  # Sub Heading

    # Length Text Box & Label
    Label(square_w, text="Length (mm)", fg="Black", font="none 12").grid(row=3, column=0, sticky=W)
    s_length = Entry(square_w, bd=5)
    s_length.grid(row=4, column=0, columnspan=2, sticky=W)

    # Calculate Button
    Button(square_w, text="Calculate", width=10, command=squ_calculate).grid(row=5, column=0, sticky=W)

    # answer Label
    s_calculation = Label(square_w, text="-", fg="Black", font="none 16 bold")
    s_calculation.grid(row=6, column=0, sticky=W)  # Main Heading

    # Version number and program name
    Label(square_w, text=f"Math Calculator v{version_number}", fg="Grey", anchor='se', font="none 8",
          wraplength=400).grid(row=6, column=1, sticky=W)  # version

    # Starts GUI
    square_w.mainloop()
    print("[Square Window Loaded]")


def circle_window():  # Circle GUI
    # Calculate Rectangle Area
    def cir_calculate():
        print("Calculating Circle Area.")
        # Finds value for numeric check
        c_a_check = c_radius.get()

        # Checks to see if the entered value is a number or not. Changes the label and exits the script if it's not.
        if not is_float(c_a_check):
            c_calculation.config(text="Letters, special characters, or nothing present in fields.")
            return

        # Finds the value for calculation & performs the calculation.
        c_a = float(
            c_radius.get())  # I would use the imported decimal function, but it won't work probably because of the
        # pi variable.
        pi = numpy.pi
        c_calculate = pi * c_a ** 2

        print(f"Answer is {c_calculate}")
        c_calculation.config(text=f"{c_calculate}mm sq")
        # Changing the answer label by changing the config of the label.

    print("Circle Pressed")
    circle_w = Tk()
    circle_w.title("Circle")  # window title
    circle_w.resizable(width=False, height=False)  # Makes the window unresizable.

    # Labels for Circle GUI
    Label(circle_w, text="Circle Calculator", fg="Black", font="none 16 bold").grid(row=1, column=0,
                                                                                    sticky=W)  # Main Heading
    Label(circle_w, text="Enter the required measurements & then click\ncalculate to find the area of a Circle.",
          fg="Black", font="none 12", justify="left").grid(row=2, column=0, sticky=W)  # Sub Heading

    # Length Text Box & Label
    Label(circle_w, text="Radius (mm)", fg="Black", font="none 12").grid(row=3, column=0, sticky=W)
    c_radius = Entry(circle_w, bd=5)
    c_radius.grid(row=4, column=0, columnspan=2, sticky=W)

    # Calculate Button
    Button(circle_w, text="Calculate", width=10, command=cir_calculate).grid(row=5, column=0, sticky=W)

    # answer Label
    c_calculation = Label(circle_w, text="-", fg="Black", font="none 16 bold")
    c_calculation.grid(row=6, column=0, sticky=W)  # Main Heading

    # Version number and program name
    Label(circle_w, text=f"Math Calculator v{version_number}", fg="Grey", anchor='se', font="none 8",
          wraplength=400).grid(row=6, column=1, sticky=W)  # version

    # Starts GUI
    circle_w.mainloop()
    print("[Circle Window Loaded]")


def help_window():  # Help GUI
    def help_close():
        help_w.destroy()

    print("Help_Window Pressed")
    help_w = Tk()  # I think this assigns this variable as the window that can be referred to later.
    help_w.title("Help")  # window title
    help_w.resizable(width=False, height=False)  # Makes the window unresizable.

    # Labels for Circle GUI
    Label(help_w, text="Help", fg="Black", font="none 16 bold").grid(row=1, column=0, sticky=W)  # Main Heading
    Label(help_w,
          text="To use this program, enter the required information into the boxes in mm.\n\nFor rectangle, "
               "you need to enter the length and width of the shape.\nFor a square, you need to enter one of the "
               "sides of the shape.\nFor a circle, you need to enter the RADIUS of the circle, and not the "
               "diameter.\n\nIf the calculation is not working, you have entered characters that can't be calculated. "
               "Ensure that you only place numbers into the calculation, and no letters or special characters.",
          fg="Black", anchor='w', font="none 12", wraplength=400, justify="left").grid(row=2, column=0, sticky=W)  # Sub Heading

    Label(help_w, text="Aconix (c) 2022", fg="Grey", anchor='w', font="none 8", wraplength=400).grid(row=3, column=0, sticky=W)  # Copyright

    # Close Button
    Button(help_w, text="Close", width=10, command=help_close).grid(row=4, column=0, sticky=W)

    # Starts GUI
    help_w.mainloop()
    print("[Help Window Loaded]")


def Quit():  # Quits Program
    print("Yes pressed in close confirmation. Open GUIs should close.")
    sys.exit()


# Close Button and X button on Main Window
def close_script():
    print("close button pressed")
    close_msgbox = messagebox.askyesno('Quit', 'Are you sure you want to close all open windows?')
    if close_msgbox == YES:
        Quit()


window.protocol("WM_DELETE_WINDOW", close_script)  # References the close button (MUST USE WM_DELETE_WINDOW)

# Create Labels
Label(window, text="Math Calculator", fg="Black", font="none 20 bold").grid(row=1, column=0, sticky=W)
Label(window, text="Click on one of the buttons to access a calculation", fg="Black", font="none 12").grid(row=2,
                                                                                                           column=0,
                                                                                                           sticky=W)

# Create Button
Button(window, text="Rectangle", width=10, command=rectangle_window).grid(row=3, column=0, sticky=W)
Button(window, text="Square", width=10, command=square_window).grid(row=4, column=0, sticky=W)
Button(window, text="Circle", width=10, command=circle_window).grid(row=5, column=0, sticky=W)
Button(window, text="Help", width=10, command=help_window).grid(row=6, column=0, sticky=W)
Button(window, text="Quit", width=10, command=close_script).grid(row=7, column=0, sticky=W)
Label(window, text="Aconix (c) 2022", fg="Grey", anchor='sw', font="none 8", wraplength=400).grid(row=8, column=0,
                                                                                                  sticky=W)  # Copyright
Label(window, text=f"v{version_number}", fg="Grey", anchor='se', font="none 8", wraplength=400).grid(row=8, column=1,
                                                                                                     sticky=W)  # version

# Run Main Loop (Makes the window run)
window.mainloop()
print("[Home Window Loaded]")

# Math Calculator
# Aconix (c) 2022
