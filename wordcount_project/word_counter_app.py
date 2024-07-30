import tkinter as tk
from tkinter import messagebox
import string

class WordCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Counter")
        self.root.geometry("500x400")  # Increased size for better text visibility
        self.root.configure(bg="#f0f0f0")

        # Center the window on the screen
        self.center_window()

        # Create and place widgets
        self.create_widgets()

    def center_window(self):
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the center position
        window_width = 500
        window_height = 400
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Set the position of the window
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Word Counter", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Text input field
        self.text_label = tk.Label(self.root, text="Enter your text:", font=("Helvetica", 12), bg="#f0f0f0")
        self.text_label.pack(pady=5)

        self.text_entry = tk.Text(self.root, height=10, width=60, wrap=tk.WORD, bg="#ffffff", fg="#000000", font=("Helvetica", 12))
        self.text_entry.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Count Words", command=self.count_words, bg="#4CAF50", fg="#0f0f0f", font=("Helvetica", 12, "bold"))
        self.submit_button.pack(pady=10)

    def count_words(self):
        text = self.text_entry.get("1.0", tk.END).strip()

        if not text:
            self.show_message("Error", "No input provided!")
            return

        # Process text
        word_count = self.calculate_word_count(text)
        
        # Display results in a message box and the console
        result_text = f"Word count: {word_count}"
        self.show_message("Word Count Result", result_text)
        print(result_text)  # Print the result to the console

    def calculate_word_count(self, text):
        # Remove punctuation and split text into words
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator)
        words = cleaned_text.split()
        return len(words)

    def show_message(self, title, message):
        # Create a message box that appears in the center of the screen
        messagebox.showinfo(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCounterApp(root)
    root.mainloop()
