import tkinter as tk # Import the tkinter library for GUI development
import nltk # Import the nltk library for natural language processing
from textblob import TextBlob # Import the TextBlob library for sentiment analysis
from newspaper import Article # Import the newspaper library for article scraping

# Define a function that summarizes the article and updates the GUI
def summarize():
    # Get the URL from the "utext" Text widget and remove any whitespace
    url = utext.get("1.0", "end").strip()

    # Use the newspaper library to download and parse the article
    article = Article(url)
    article.download()
    article.parse()

    # Use the newspaper library to extract additional information from the article
    article.nlp()

    # Enable the Text widgets so that we can update them
    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    # Clear the Text widgets
    title.delete("1.0", "end")
    author.delete("1.0", "end")
    publication.delete("1.0", "end")
    summary.delete("1.0", "end")
    sentiment.delete("1.0", "end")

    # Update the Text widgets with the article's information
    title.insert("1.0", article.title)
    author.insert("1.0", article.authors)
    publication.insert("1.0", article.publish_date)
    summary.insert("1.0", article.summary)

    # Use TextBlob to perform sentiment analysis on the article's content
    analysis = TextBlob(article.text)
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    # Disable the Text widgets so that they can't be edited
    title.config(state="disabled")
    author.config(state="disabled")
    publication.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")

# Create the main window of the GUI
root = tk.Tk()
root.title("News Summarizer") # Set the title of the window
root.geometry("1200x600") # Set the size of the window

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()
             
alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

selabel = tk.Label(root, text="Sentiment")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()