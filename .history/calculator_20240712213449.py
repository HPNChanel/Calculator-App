import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, 'bold')
SMALL_FONT_STYLE = ("Arial", 16)
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        
        self.total_expression = ''
        self.current_expression = ''
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        
    
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, 
                                bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')
        
        label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, 
                                bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        
        return total_label, label
    
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=223, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame
        
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame
    
        
    def run(self):
        self.window.mainloop()

    

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    