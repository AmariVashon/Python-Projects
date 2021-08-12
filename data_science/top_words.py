from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
from bs4.element import Comment

bad_words = ["the", "a", "in", "of", "to", "you", "\xa0", "and", "at", "on", "or", "your", "for", "from", "is", 
                 "that", "his", "are", "be", "-", "as", "&", "they", "with", "how", "was", "her", "him", "i", "has", 
                 "|"] 

def filterTags(element):
    if element.parent.name in ["style", "script", "head", "title", "meta", "[document]"]:
        return False
    
    if isinstance(element, Comment):
        return False
    
    return True

def filterWaste(word):
    if word.lower() in bad_words:
        return False
    
    return True

def addBadWord(word):
    bad_words.append(word)

def parse_site(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.find_all(text=True) # finds all text on site
    
    visible_text = filter(filterTags, text)
    
    word_count = {}
    
    for text in visible_text:
        words = text.replace("\n", "").replace("\t", "").split(" ")
        words = list(filter(filterWaste, words))
        for word in words:
            if word != "":
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    
    word_count = sorted(word_count.items(), key=lambda kv : kv[1], reverse=True)
    
    return word_count[:7]

def displayResults(words, site, save=None):
    count = [item[1] for item in words][::-1] # reverses order
    word = [item[0] for item in words][::-1]
    
    plt.figure(figsize=(20,10))
    
    plt.bar(word, count)
    
    plt.title(f"Analyzing Top Words from: {site[:50]}", fontname="Sans Serif", fontsize=24)
    plt.xlabel("Words", fontsize=24)
    plt.ylabel("Count", fontsize=24)
    plt.xticks(fontname="Sans Serif", fontsize=20)
    plt.yticks(fontname="Sans Serif", fontsize=20)
    
    plt.savefig(f"{save}")
    plt.show()

run = True

while run:
    try: 
        ans = str(input("Would you like to scrape a Website (y/n)? "))
    except:
        print("Not a string. ")
    
    if ans == "y":
        site = input("Enter a website to analyze: ")
        try:
            top_words = parse_site(site)
            top_word = top_words[0]
            print(f"The top word is: {top_word[0]}")
            displayResults(top_words, site)

            while input("Would you like to remove a word from the list (y/n)? ") == "y":
                new_word = input("What word would you like to remove? ")
                addBadWord(new_word)

            print("Here is the updated chart:")
            top_words = parse_site(site)
            displayResults(top_words, site)
        except:
            print("This site could not be accessed. ")
    elif ans == "n":
        run = False
        while input("Thank you for using this tool! Would you like to save this figure (y/n)? ") == "y":
            fileName = input("What would you like to name the file (with file type)? ")
            displayResults(top_words, site, save=fileName)
    else:
        print("Invalid input.")
