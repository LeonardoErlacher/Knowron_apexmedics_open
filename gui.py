import json
import tkinter as tk
import urllib
import webbrowser
from tkinter import filedialog
from reportlab.pdfgen import canvas
from connect_all_methods import do_the_work

# Open the file in read mode
with open('confiq.json', 'r') as file:
    # Load the contents of the file as a Python object
    data = json.load(file)
    filename = data['FILENAME']
    api_key = data['API_KEY']
    max_tokens = data['MAX_TOKENS']
    record_time = data['RECORD_TIME']


class RecordGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x600")
        self.master.title('Apexmedics')
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack()

        #TODO make an iput for the time ??

        self.button = tk.Button(self.top_frame, text="Record", command=self.activate)
        self.button.pack(side="left")

        self.canvas = tk.Canvas(self.top_frame, width=20, height=20)
        self.canvas.pack(side="right")

        self.var = tk.BooleanVar(value=True)
        self.check_button = tk.Checkbutton(self.top_frame, text="New Recording", variable=self.var, command=self.change_button_label)
        self.check_button.pack()

        # Create a drop-down menu
        options = ["Bulletpoints", "Protocol (Report)", "Letter to Patient"]
        self.variable = tk.StringVar(self.master)
        self.variable.set(options[0])  # Set the default option
        self.dropdown = tk.OptionMenu(self.master, self.variable, *options)
        self.dropdown.pack()

        recording_time = record_time
        self.timer_label = tk.Label(self.master, font=("Arial", 20))
        self.timer_label.pack()
        self.timer_label.config(text=f"Record for: {recording_time} seconds")

        self.text_box = tk.Text(self.master, width=80, height=30)
        self.text_box.insert(1.0,
                             "Insert names you dont want to share with the AI \nThey will be removed from the spoken text that will sent to the AI.\n>>>")
        self.text_box.pack()

        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack()

        # Create a drop-down menu
        options_export_drop_down = ["Copy", "PDF", "Email"]
        self.export_drop_down = tk.StringVar(self.master)
        self.export_drop_down.set(options_export_drop_down[0])  # Set the default option
        self.dropdown = tk.OptionMenu(self.bottom_frame, self.export_drop_down, *options_export_drop_down)
        self.dropdown.pack()

        # Create a button to copy the contents of the Text widget to the clipboard
        self.copy_button = tk.Button(self.bottom_frame, text="Export", command=self.copy_to_clipboard)
        self.copy_button.pack()


    def change_button_label(self):
        if self.var.get():
            self.button.config(text="Record")
        else:
            self.button.config(text="Ask AI")

    # Define a function to export the text to a PDF file
    def export_to_pdf(self):
        # Open a file dialog to choose a file location
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf")
        # Create a new PDF file
        pdf = canvas.Canvas(file_path)
        # Write the contents of the text field to the PDF file
        #pdf.drawString(100, 750, self.text_box.get("1.0", "end"))
        line = self.text_box.get("1.0", "end").replace("\n", "")
        lines = [line[i:i + 80] for i in range(0, len(line), 80)]

        # Write each line of the text to the PDF file
        y = 800
        for line in lines:
            pdf.drawString(50, y, line)
            y -= 20
        # Save the PDF file
        pdf.save()

    # Define a function to open the default email client
    def open_email_client(self, text):
        recipient = "recipient@example.com" # TODO open a field where you can put yput mail adress
        subject = self.variable.get()
        body = text

        # Encode the parameters as URL-safe strings
        recipient_url = recipient
        subject_url = subject
        body_url = body

        # Construct the mailto URL with the recipient, subject, and body parameters
        url = "mailto:{0}?subject={1}&body={2}".format(recipient_url, subject_url, body_url)

        # Open the URL with the default web browser
        webbrowser.open_new(url)

    def copy_to_clipboard(self):
        text = self.text_box.get("1.0", "end-1c")  # Get the contents of the Text widget
        if self.export_drop_down.get() == "Copy":
            self.master.clipboard_clear()  # Clear the clipboard
            self.master.clipboard_append(text)  # Append the text to the clipboard
        elif self.export_drop_down.get() == 'PDF':
            self.export_to_pdf()
        else:
            self.open_email_client(text)

    def activate(self):
        self.button.config(state="disabled")
        self.button.config(text="Ask AI")
        if self.var.get():
            # Draw a red dot on the canvas
            x = 10
            y = 10
            r = 5
            dot = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="red")
            self.canvas.update()

        text = self.text_box.get(1.0, "end-1c").split(">>>")
        self.text_box.delete(1.0, "end-1c")
        if len(text) <= 1:
            text = do_the_work("", query_for_ai=self.variable.get(), new_record=self.var.get())
        else:
            text = do_the_work(text[1], query_for_ai=self.variable.get(), new_record=self.var.get())

        if self.var.get():
            self.canvas.delete(dot)
        self.var.set(False)
        self.canvas.update()
        self.text_box.insert(1.0, text)
        self.button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = RecordGUI(root)
    root.mainloop()
