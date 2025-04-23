import tkinter as tk

# Application vide
class Application(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Simple GUI")
        self.geometry("300x200")
        
        # Create a label
        self.label = tk.Label(self, text="Hello, Tkinter!")
        self.label.pack(pady=20)
        
        # Create a button
        self.button = tk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

        # Text widget
        self.text = tk.Text(self, height=5, width=30)
        self.text.pack(pady=10)
        
        

if __name__ == "__main__":
    app = Application()
    app.mainloop()
    