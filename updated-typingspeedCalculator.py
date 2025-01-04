import tkinter as tk
import random
from tkinter import messagebox

# List of predefined paragraphs
paragraphs = [
    "The quick brown fox jumps over the lazy dog. This classic sentence includes all the letters of the alphabet, making it a popular tool for practicing typing. It is often used to test typewriters, keyboards, and even typing speed. Typing this sentence repeatedly can help improve muscle memory, hand coordination, and overall accuracy in typing exercises over time.",
    "Typing speed is an important skill in the modern digital world. Being able to type quickly and accurately can improve productivity and communication in both personal and professional settings. Practice and dedication are key to mastering this skill. By consistently working on typing exercises and tests, one can significantly boost their words per minute and enhance their efficiency in daily tasks.",
    "Practice makes perfect when it comes to improving typing accuracy. Regularly challenging yourself with different typing tasks can train your fingers to move effortlessly over the keyboard. It's important to focus on typing without looking at your hands, as this builds muscle memory. Over time, you'll find that your typing speed and precision improve dramatically, enabling you to complete tasks more quickly.",
    "Python is a versatile programming language used for various applications. From web development to data analysis, Python is a favorite among developers due to its simplicity and vast library support. Learning Python not only enhances your coding skills but also opens doors to careers in artificial intelligence, machine learning, and software development. It's a tool that can help you achieve your programming goals.",
    "Tkinter is a Python library used for creating graphical user interfaces. With Tkinter, developers can create interactive applications with buttons, menus, labels, and more. It is an excellent choice for beginners learning GUI development, as it is easy to use and well-documented. Creating apps with Tkinter helps programmers visualize their ideas while developing user-friendly software solutions for diverse needs.",
    "Random paragraphs make typing tests more engaging and challenging. They ensure that users are exposed to various words, sentence structures, and punctuation marks. This diversity helps improve overall typing skills, as users learn to adapt to different styles of writing. By incorporating random content, typing tests become more effective in preparing individuals for real-world typing scenarios across multiple contexts.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. This quote reminds us to focus on pursuing our passions and finding joy in our daily lives. By doing so, we not only achieve personal satisfaction but also inspire others around us to follow their dreams and be their best selves.",
    "Artificial intelligence is transforming the way we interact with technology. From virtual assistants to autonomous vehicles, AI is revolutionizing industries worldwide. Its ability to analyze vast amounts of data quickly has made it invaluable in fields such as healthcare, finance, and education. As AI continues to evolve, it holds the potential to solve complex problems and enhance the quality of life for people globally.",
    "Good communication skills are crucial for personal and professional growth. Being able to express your thoughts clearly and listen actively to others fosters strong relationships. In the workplace, effective communication ensures smooth collaboration and understanding among team members. By practicing empathy, maintaining eye contact, and choosing words carefully, you can build trust and establish meaningful connections in all areas of your life.",
    "The journey of a thousand miles begins with a single step. This ancient proverb encourages us to take action, no matter how daunting the goal may seem. By breaking tasks into smaller, manageable steps, we can steadily work toward achieving our objectives. Consistency and perseverance are key to overcoming obstacles, learning from challenges, and ultimately reaching success in both personal and professional endeavors.",
    "Consistent effort leads to mastery in any skill or profession. Whether it's learning to play an instrument, mastering a language, or excelling in a career, dedication is essential. By practicing regularly and seeking constructive feedback, individuals can identify areas for improvement and refine their abilities. Over time, this commitment to growth fosters confidence, competence, and the expertise needed to excel in any field.",
    "Reading is to the mind what exercise is to the body. It expands our knowledge, enhances our vocabulary, and stimulates critical thinking. Regular reading also improves focus and concentration, making it an essential habit for personal development. Whether it's fiction, non-fiction, or technical material, dedicating time to read every day enriches our perspectives and equips us with valuable insights to navigate life's challenges."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test with Real-Time Feedback")
        self.root.geometry("800x500")
        
        self.time_left = 60
        self.selected_paragraph = random.choice(paragraphs)  # Select a random paragraph
        
        self.setup_ui()

    def setup_ui(self):
        # Heading
        heading = tk.Label(self.root, text="Typing Speed Calculator", font=("Arial", 24, "bold"))
        heading.pack(pady=10)
        
        # Display Random Paragraph
        self.paragraph_display = tk.Text(self.root, height=6, width=80, font=("Arial", 14), wrap="word", state="disabled")
        self.paragraph_display.pack(pady=10)
        self.paragraph_display.tag_configure("correct", foreground="green")
        self.paragraph_display.tag_configure("incorrect", foreground="red")
        self.paragraph_display.tag_configure("pending", foreground="black")
        self.display_paragraph()

        # Typing Area (with word wrap enabled)
        self.text_area = tk.Text(self.root, height=5, width=70, font=("Arial", 14), wrap="word", state="disabled")
        self.text_area.pack(pady=10)
        self.text_area.bind("<KeyRelease>", self.highlight_text)  # Bind typing to highlight function
        
        # Buttons
        start_button = tk.Button(self.root, text="Start Test", command=self.start_test, font=("Arial", 14), bg="green", fg="white")
        start_button.pack(side="left", padx=20, pady=10)
        
        reset_button = tk.Button(self.root, text="Reset Test", command=self.reset_test, font=("Arial", 14), bg="red", fg="white")
        reset_button.pack(side="right", padx=20, pady=10)
        
        # Timer Label
        self.timer_label = tk.Label(self.root, text="Time Left: 60s", font=("Arial", 16))
        self.timer_label.pack(pady=10)
    
    def display_paragraph(self):
        """Displays the paragraph with default colors."""
        self.paragraph_display.config(state="normal")
        self.paragraph_display.delete("1.0", tk.END)
        for word in self.selected_paragraph.split():
            self.paragraph_display.insert(tk.END, word + " ", "pending")
        self.paragraph_display.config(state="disabled")

    def start_test(self):
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        self.text_area.focus()
        self.time_left = 60
        self.timer_label.config(text="Time Left: 60s")
        self.root.after(1000, self.update_timer)
    
    def highlight_text(self, event=None):
        """Tracks typing and updates the color of the displayed paragraph letter by letter."""
        typed_text = self.text_area.get("1.0", tk.END).strip()  # Get user input
        original_text = self.selected_paragraph  # Original paragraph
        
        self.paragraph_display.config(state="normal")
        self.paragraph_display.delete("1.0", tk.END)  # Clear the paragraph display
        
        for i, char in enumerate(original_text):
            if i < len(typed_text):
                if typed_text[i] == char:  # Correct letter
                    self.paragraph_display.insert(tk.END, char, "correct")
                else:  # Incorrect letter
                    self.paragraph_display.insert(tk.END, char, "incorrect")
            else:  # Remaining letters
                self.paragraph_display.insert(tk.END, char, "pending")
        
        self.paragraph_display.config(state="disabled")
    
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_test()
    
    def end_test(self):
        self.text_area.config(state="disabled")
        typed_text = self.text_area.get("1.0", tk.END).strip()
        original_words = self.selected_paragraph.split()
        typed_words = typed_text.split()
        
        correct_words = sum(1 for i, word in enumerate(typed_words) if i < len(original_words) and word == original_words[i])
        total_words = len(typed_words)
        
        wpm = correct_words  # Words Per Minute (based on correct words)
        accuracy = (correct_words / total_words) * 100 if total_words else 0
        
        messagebox.showinfo("Test Results", f"Words Per Minute (WPM): {wpm}\nAccuracy: {accuracy:.2f}%\nTotal Words Typed: {total_words}\nCorrect Words: {correct_words}")
    
    def reset_test(self):
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        self.text_area.config(state="disabled")
        self.selected_paragraph = random.choice(paragraphs)  # Pick a new random paragraph
        self.display_paragraph()
        self.time_left = 60
        self.timer_label.config(text="Time Left: 60s")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
