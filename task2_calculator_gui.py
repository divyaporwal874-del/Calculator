
import tkinter as tk

# Main Window
root = tk.Tk()
root.title("My Calculator")
root.geometry("350x500")
root.config(bg="#202124")
root.resizable(False, False)

# Display
expression = ""

display = tk.Entry(
    root,
    font=("Arial", 25),
    bg="#303134",
    fg="white",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=15, pady=25, ipady=15)

# Button Functions
def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def calculate():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# Buttons Layout
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "%", "="]
]

# Create Buttons
for row in buttons:
    frame = tk.Frame(root, bg="#202124")
    frame.pack(expand=True, fill="both", padx=8)

    for btn in row:
        if btn == "=":
            command = calculate
            color = "#34A853"
            
        elif btn == "C":
            command = clear
            color = "#EA4335"
        else:
            command = lambda x=btn: press(x)
            color = "#5F6368" if btn.isdigit() or btn == "." else "#4285F4"

        button = tk.Button(
            frame,
            text=btn,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            bd=0,
            command=command
        )
        button.pack(
            side="left",
            expand=True,
            fill="both",
            padx=4,
            pady=4
        )

# Run Application
root.mainloop()
