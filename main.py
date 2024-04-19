# Importing necessary modules
import tkinter as tk 
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup  
from collections import Counter  
import nltk  
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  

# Downloading NLTK resources
nltk.download('punkt')  
nltk.download('stopwords')  

# Function to retrieve text content from a website
def get_website_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text
    else:
        return None

# Function to extract keywords from text
def extract_keywords(text, num_words, include_short_words):
    words = word_tokenize(text)
    if not include_short_words:
        words = [word.lower() for word in words if word.isalnum() and len(word) > 2]
    else:
        words = [word.lower() for word in words if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(num_words)
    return most_common_words

# Function to process URL entered by user
def process_url():
    url = url_entry.get()
    num_words = int(num_words_entry.get())
    include_short_words = include_short_words_var.get()
    if url:
        text = get_website_text(url)
        if text:
            keywords = extract_keywords(text, num_words, include_short_words)
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            for keyword, frequency in keywords:
                result_text.insert(tk.END, f"{keyword} - {frequency}\n")
            result_text.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Failed to retrieve website content.")
    else:
        messagebox.showerror("Error", "Please enter a URL.")

# Creating the main Tkinter window
root = tk.Tk()
root.title("Website Keyword Extractor")

# Creating a frame for widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Label and entry widget for entering the URL
url_label = tk.Label(frame, text="Enter the URL of the website:")  
url_label.grid(row=0, column=0, sticky="w")  
url_entry = tk.Entry(frame, width=50) 
url_entry.grid(row=0, column=1, padx=5, pady=5) 

# Label and entry widget for specifying number of words
num_words_label = tk.Label(frame, text="Number of words to search for:")
num_words_label.grid(row=1, column=0, sticky="w")
num_words_entry = tk.Entry(frame, width=10) 
num_words_entry.grid(row=1, column=1, padx=5, pady=5)  

# Checkbox for including short words
include_short_words_var = tk.BooleanVar()  
include_short_words_checkbox = tk.Checkbutton(frame, text="Include words with less than 3 letters", variable=include_short_words_var)  
include_short_words_checkbox.grid(row=2, columnspan=2, sticky="w", pady=5)  

# Button to trigger keyword extraction process
process_button = tk.Button(frame, text="Extract Keywords", command=process_url)
process_button.grid(row=3, columnspan=2, pady=10) 

# Text widget to display extracted keywords
result_text = tk.Text(root, width=50, height=10, state=tk.DISABLED) 
result_text.pack()  

# Start the Tkinter event loop
root.mainloop() 