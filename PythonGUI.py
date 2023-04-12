# Experimenting use of Python and tkinter GUI interface - John Meni Williams - 20210689

# Below is also in the "readme.txt" file
# In my example, objective is to use Python and tkinter to provide a GIU interface. The GUI has five input fields
# for the user to enter their personal information, and three buttons
# for the user to submit their information, reset the form, or close the application
# when the user clicks the "submit" button, their information is written to a text file at "e:/coursequery.txt". The "Reset" button clears
# note that the previous line destination export file called "coursequery.txt" will need to be created before this code is run
# all input fields, and the "Close" button closes the application
#
# Following are a list of Objects in the code:
#
# self.window: the main window of the GUI.
# self.full_name_entry, self.street_address_entry, self.suburb_entry, self.city_entry, self.email_entry: Entry objects for the user to input their details.
# self.courses_listbox: Listbox object for displaying selected courses.
# self.add_course_button, self.submit_button, self.reset_button, self.close_button: Button objects for adding courses, submitting the form, resetting the form, and closing the GUI.
#
# Following are a list of Methods in the code:
#
# __init__: the constructor method that sets up the GUI window and all the widgets.
# add_course: method for adding a course to the list of selected courses.
# submit: method for writing the user's details and selected courses to a file.
# reset: method for clearing all the input fields and selected courses.
#
# My Loop example:
#
# for course in selected_courses:: a loop that writes each selected course to the output file in submit method.
#
#
# Resources used for my Project:
#
# Instructors/Lecturers:   Roman Mitch, Pinal Shah and Marina Kharitonova
# Advisor:  Jacqueline Joy Strom - 20230773 (fellow student)
# Python.org - Official Python documentation and tutorials: https://www.python.org/about/gettingstarted/
# TkDocs - Comprehensive Tkinter documentation: https://tkdocs.com/tutorial/
# Real Python - Python tutorials for all skill levels: https://realpython.com/
# Codecademy - Python and Tkinter courses: https://www.codecademy.com/learn/learn-python-3 and https://www.codecademy.com/learn/learn-tkinter
# Coursera - Python and Tkinter courses: https://www.coursera.org/courses?query=python%20tkinter
# YouTube - There are many Python and Tkinter tutorials available on YouTube, such as those by Tech With Tim, Corey Schafer, and Sentdex.
# Bro Code  https://www.youtube.com/watch?v=VkTrrqnWjsg


import tkinter as tk
import math


class MyCourseQueryApp:
    def __init__(self):
        self.window = tk.Tk()  # tk.Tk(): creates the main window for the GUI
        self.window.title("Course Query App")

        # Set the font size
        font = ('Arial', 12)

        # Note: the below is a description of required fields for data input and capture and this information needs to be in SDLC file
        # # Full Name
        # #tk.Label(self.window, text="Full Name", anchor="w", font=font).grid(row=0, column=0)
        # tk.Label(self.window, text="Full Name", font=font, anchor="w", justify="left").grid(row=0, column=0)
        # self.full_name_entry = tk.Entry(self.window, font=font)
        # self.full_name_entry.grid(row=0, column=1)
        #
        # # Street Address
        # tk.Label(self.window, text="Street Address", anchor="w", font=font).grid(row=1, column=0)
        # self.street_address_entry = tk.Entry(self.window, font=font)
        # self.street_address_entry.grid(row=1, column=1)
        #
        # # Suburb
        # tk.Label(self.window, text="Suburb", anchor="w", font=font).grid(row=2, column=0)
        # self.suburb_entry = tk.Entry(self.window, font=font)
        # self.suburb_entry.grid(row=2, column=1)
        #
        # # City
        # tk.Label(self.window, text="City", anchor="w", font=font).grid(row=3, column=0)
        # self.city_entry = tk.Entry(self.window, font=font)
        # self.city_entry.grid(row=3, column=1)
        #
        # # Email
        # tk.Label(self.window, text="Email", anchor="w", font=font).grid(row=4, column=0)
        # self.email_entry = tk.Entry(self.window, font=font)
        # self.email_entry.grid(row=4, column=1)

        # Full Name
        tk.Label(self.window, text="Full Name", font=font, anchor="w", justify="left", width=15).grid(row=0, column=0, padx=5, pady=5)
        #self.full_name_entry = tk.Entry(self.window)
        self.full_name_entry = tk.Entry(self.window, width=40)
        self.full_name_entry.grid(row=0, column=1, padx=15, pady=15)

        # Street Address
        tk.Label(self.window, text="Street Address", font=font, anchor="w", justify="left", width=15).grid(row=1, column=0, padx=10,pady=5)
        self.street_address_entry = tk.Entry(self.window, width=40)
        self.street_address_entry.grid(row=1, column=1, padx=15, pady=15)

        # Suburb
        tk.Label(self.window, text="Suburb", font=font, anchor="w", justify="left", width=15).grid(row=2, column=0, padx=15, pady=15)
        self.suburb_entry = tk.Entry(self.window, width=40)
        self.suburb_entry.grid(row=2, column=1, padx=15, pady=15)

        # City
        tk.Label(self.window, text="City", font=font, anchor="w", justify="left", width=15).grid(row=3, column=0, padx=15, pady=15)
        self.city_entry = tk.Entry(self.window, width=40)
        self.city_entry.grid(row=3, column=1, padx=15, pady=15)

        # Email
        tk.Label(self.window, text="Email", font=font, anchor="w", justify="left", width=15).grid(row=4, column=0,  padx=15, pady=15)
        self.email_entry = tk.Entry(self.window, width=40)
        self.email_entry.grid(row=4, column=1, padx=15, pady=15)

        # Submit and Reset Buttons
        button_font = ('Arial', 12)

        self.submit_button = tk.Button(self.window, text="Submit", font=button_font, command=self.submit)
        self.submit_button.grid(row=5, column=0)

        self.reset_button = tk.Button(self.window, text="Reset", font=button_font, command=self.reset)
        self.reset_button.grid(row=5, column=1)

        self.close_button = tk.Button(self.window, text="Close", font=button_font, command=self.window.destroy)
        self.close_button.grid(row=5, column=2)

        # Set the window size and position
        # screen_width = self.window.winfo_screenwidth()
        # screen_height = self.window.winfo_screenheight()
        # width = math.floor(screen_width * 0.6)
        # height = math.floor(screen_height * 0.6)
        # x = math.floor((screen_width - width) / 2)
        # y = math.floor((screen_height - height) / 2)
        # self.window.geometry(f"{width}x{height}+{x}+{y}")
        # Center the window on the screen
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 20)
        y = (self.window.winfo_screenheight() // 5) - (height // 80)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

        self.window.mainloop()

    # export input to destination file
    def submit(self):
        full_name = self.full_name_entry.get()
        street_address = self.street_address_entry.get()
        suburb = self.suburb_entry.get()
        city = self.city_entry.get()
        email = self.email_entry.get()

        with open("e:/coursequery.txt", "a") as file:
            file.write(f"Full Name: {full_name}\n")
            file.write(f"Street Address: {street_address}\n")
            file.write(f"Suburb: {suburb}\n")
            file.write(f"City: {city}\n")
            file.write(f"Email: {email}\n\n")

        self.reset()

    def reset(self):
        self.full_name_entry.delete(0, tk.END)
        self.street_address_entry.delete(0, tk.END)
        self.suburb_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


if __name__ == "__main__":
    MyCourseQueryApp()




