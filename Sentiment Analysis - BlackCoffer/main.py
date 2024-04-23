from bs4 import BeautifulSoup
import requests
import pandas as pd
###
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from syllapy import count
from tqdm import tqdm
import os
nltk.download('punkt',quiet=True)
nltk.download('stopwords',quiet=True)

import sys
positive_words = sys.argv[1]
negative_words = sys.argv[2]
input_excel = sys.argv[3]


stop_words = set(stopwords.words('english'))

# Function to clean text using stop words
def clean_text(text):
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove punctuation and stop words
    cleaned_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
    return cleaned_tokens

# Function to calculate polarity score
def calculate_polarity_score(positive_score, negative_score):
    return (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)

# Function to calculate subjectivity score
def calculate_subjectivity_score(positive_score, negative_score, total_words):
    return (positive_score + negative_score) / (total_words + 0.000001)

# Function to calculate average sentence length
def calculate_avg_sentence_length(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    return len(words) / len(sentences)

# Function to calculate percentage of complex words
def calculate_percentage_complex_words(text):
    words = clean_text(text)
    complex_words = [word for word in words if count(word) > 2]
    return len(complex_words) / len(words)

# Function to calculate average number of words per sentence
def calculate_avg_words_per_sentence(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    return len(words) / len(sentences)

# Function to calculate complex word count
def calculate_complex_word_count(text):
    words = clean_text(text)
    complex_words = [word for word in words if count(word) > 2]
    return len(complex_words)

# Function to calculate word count
def calculate_word_count(text):
    words = clean_text(text)
    return len(words)

# Function to calculate syllable count per word
def calculate_syllable_per_word(text):
    words = clean_text(text)
    syllable_count = sum(count(word) for word in words)
    return syllable_count / len(words)

# Function to calculate personal pronouns count
def calculate_personal_pronouns(text):
    pronouns = ['i', 'we', 'my', 'mine', 'our', 'ours', 'us', 'you', 'your', 'yours', 'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its', 'they', 'them', 'their', 'theirs']
    count = sum(1 for word in text.split() if word.lower() in pronouns)
    # Exclude "US" as it might refer to the country name
    count -= text.lower().count("us")
    return count

# Function to calculate average word length
def calculate_avg_word_length(text):
    words = clean_text(text)
    total_characters = sum(len(word) for word in words)
    return total_characters / len(words)



output=pd.DataFrame(columns=["URL_ID","URL","POSITIVE SCORE","NEGATIVE SCORE","POLARITY SCORE","SUBJECTIVITY SCORE","AVG SENTENCE LENGTH","PERCENTAGE OF COMPLEX WORDS","FOG INDEX","AVG NUMBER OF WORDS PER SENTENCE","COMPLEX WORD COUNT","WORD COUNT","SYLLABLE PER WORD","PERSONAL PRONOUNS","AVG WORD LENGTH"])

def link_to_txt(name,url,output):

    response = requests.get(url)
    html_response = response.text
    doc = BeautifulSoup(html_response, "html.parser")
    title = doc.find("h1")
    if title !=None:
        title=title.text
    else:
        title=""
    body=doc.find("div",class_="td-post-content tagdiv-type")
    if body==None:
        body = doc.find_all("div")
        body.sort(key=lambda x: len(x),reverse=True)
        if body:
           body = body[0].text
        else:
           body="Body not Found"
    else:
        body=body.text
    with open("./TextFiles/"+name+'.txt',"w", encoding='utf-8') as file:
        file.write(title)
        file.write(body)
    text=title+" "+body

    cleaned_text = clean_text(text)
    positive_score = sum(1 for word in cleaned_text if word in positive_words)
    negative_score = sum(1 for word in cleaned_text if word in negative_words)
    polarity_score = calculate_polarity_score(positive_score, negative_score)
    subjectivity_score = calculate_subjectivity_score(positive_score, negative_score, len(cleaned_text))

    # Readability Analysis
    avg_sentence_length = calculate_avg_sentence_length(text)
    percentage_complex_words = calculate_percentage_complex_words(text)
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_words_per_sentence = calculate_avg_words_per_sentence(text)

    # Derived Variables
    complex_word_count = calculate_complex_word_count(text)
    word_count = calculate_word_count(text)
    syllable_per_word = calculate_syllable_per_word(text)
    personal_pronouns_count = calculate_personal_pronouns(text)
    avg_word_length = calculate_avg_word_length(text)
    output.loc[len(output.index)] = [name, url, positive_score,negative_score,polarity_score,subjectivity_score,avg_sentence_length,percentage_complex_words,\
                             fog_index,avg_words_per_sentence,complex_word_count,word_count,syllable_per_word,personal_pronouns_count,avg_word_length]



positive_words = set(open(positive_words).read().split())
negative_words = set(open(negative_words).read().split())
df=pd.read_excel(input_excel)
names=df["URL_ID"]
urls=df["URL"]
iterations=len(names)

for i in tqdm(range(iterations), desc="Processing"):
    name , url =names[i],urls[i]
    link_to_txt(name,url,output)
if os.path.exists("Output Data Structure.xlsx"):
    # If the file exists, delete it
    os.remove("Output Data Structure.xlsx")

output.to_excel("Output Data Structure.xlsx",index=False)
print("Successful execution!\nOutput stored in \"Output Data Structure.xlsx\"")