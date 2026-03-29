from tkinter import *

BG = "#660000"
TEXT_COLOR = "#FFFFFF"
HEADLINE_FONT = ("Lexend", 16, "bold")
NORMAL_FONT = ("Lexend", 11, "bold")

class App(Tk):
    def __init__(self, on_submit):
        super().__init__()
        self.on_submit = on_submit

        # Resizing window
        app_width = 600
        app_height = 600
        # X and Y coordinates to center the app into the middle of monitor
        x = int((self.winfo_screenwidth() / 2) - (app_width / 2))
        y = int((self.winfo_screenheight() / 2) - (app_height / 2))
        self.geometry(f"{app_width}x{app_height}+{x}+{y}")

        # Naming app
        self.title("Habit Tracker")

        # Changing background color
        self.configure(background=BG)

        # Label for description - posting a pixel
        self.post_label = Label(text="Post a pixel: ", font=HEADLINE_FONT, fg=TEXT_COLOR, background=BG)
        self.post_label.grid(row=1, rowspan=2, column=1, sticky="w")

        # Label for entry
        self.entry_label = Label(text="How many minutes did I code?", font=NORMAL_FONT, foreground=TEXT_COLOR, background=BG)
        self.entry_label.grid(row=3, column=1, padx=(0, 15))

        # Input for user
        self.entry = Entry(highlightthickness=0)
        self.entry.grid(row=3, column=2)

        # Button to submit entry
        self.submit_button = Button(text="Submit", command=self.get_entry)
        self.submit_button.grid(row=4, column=2, padx=(0,45), pady=3)

        # Button to clear text
        self.clear_button = Button(text="Clear", command=self.clear_text)
        self.clear_button.grid(row=4, column=2, padx=(65,0), pady=3)

    # Function to get user's input
    def get_entry(self):
        time_programming = self.entry.get()
        self.on_submit(time_programming)

    # Function to clear text
    def clear_text(self):
        self.entry.delete(0, "end")


