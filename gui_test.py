import tkinter as tk
from datetime import datetime
"""class MyApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Apexmedics")
        self.running = False
        self.start_time = None

        # create text input field
        self.text_input = tk.Entry(self.window)
        self.text_input.pack()

        # create button
        self.button = tk.Button(self.window, text="Start Recording", command=self.toggle_recording)
        self.button.pack()

        # create timer label
        self.timer_label = tk.Label(self.window, text="00:00")
        self.timer_label.pack()

        # create function output label
        self.output_label = tk.Label(self.window, text="")
        self.output_label.pack()

        self.window.mainloop()

    def toggle_recording(self):
        if not self.running:
            self.start_time = datetime.now()
            self.running = True
            self.button.config(text="Stop Recording")
            self.record()
        else:
            self.running = False
            self.button.config(text="Start Recording")
            self.stop_recording()

    def record(self):
        if self.running:
            elapsed_time = datetime.now() - self.start_time
            minutes = int(elapsed_time.total_seconds() // 60)
            seconds = int(elapsed_time.total_seconds() % 60)
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.window.after(1000, self.record)

    def stop_recording(self):
        self.output_label.config(text="Hello World")"""


root = tk.Tk()


# Create a drop-down menu
options = ["Option 1", "Option 2", "Option 3"]
variable = tk.StringVar(root)
variable.set(options[0])  # Set the default option
dropdown = tk.OptionMenu(root, variable, *options)
dropdown.pack()

# Create a button that prints the selected option
button = tk.Button(root, text="Print selected option", command=lambda: print(variable.get()))
button.pack()

if __name__ == '__main__':
    root.mainloop()
    #app = MyApp()
