from googletrans import Translator
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
import os

l=[]

directory =r'E:\New folder (29)\final2\www.classcentral.com'
subfolders = [ f.path for f in os.scandir(directory) if f.is_dir() ]
for filename in os.listdir(directory):
     if filename.endswith('.html'):
         fname = os.path.join(directory,filename)
         l.append(fname)

for subname in subfolders:
    for filename in os.listdir(subname):
        if filename.endswith('.html'):
            fname = os.path.join(subname,filename)
            l.append(fname)



print(len(l))
for filename in l:
    # Load the HTML file
    with open(filename, "r",encoding='utf-8') as f:
        html = f.read()

    # Parse the HTML file using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Translate the text content of each HTML tag
    translator = Translator()

    tag_not_parsed=[]

    # find all the <span> tags in the HTML
    span_tags = soup.find_all('span')
    print("Translate <span> tags:")
    # loop through each <span> tag
    for tag_index in tqdm(range(len(span_tags))):
        # get the original text inside the <span> tag
        if span_tags[tag_index].get_text()!="":
            try:
                original_text = span_tags[tag_index].get_text()
                # change the text as desired
                new_text = translator.translate(original_text, src='en', dest='hi').text
                # replace the original text with the new text
                span_tags[tag_index].string.replace_with(new_text)
            except:
                tag_not_parsed.append(span_tags[tag_index].string)


    print("Translate <h3> tags:")
    h3_tags = soup.find_all('h3')
    for tag_index in tqdm(range(len(h3_tags))):
        # get the original text inside the <span> tag
        if h3_tags[tag_index].get_text()!="":
            try:
                original_text = h3_tags[tag_index].get_text()
                # change the text as desired
                new_text = translator.translate(original_text, src='en', dest='hi').text
                # replace the original text with the new text
                h3_tags[tag_index].string.replace_with(new_text)
            except:
                tag_not_parsed.append(h3_tags[tag_index].string)


    print("Translate <h2> tags:")
    h2_tags = soup.find_all('h2')
    for tag_index in tqdm(range(len(h2_tags))):
        # get the original text inside the <span> tag
        if h2_tags[tag_index].get_text()!="":
            try:
                original_text = h2_tags[tag_index].get_text()
                # change the text as desired
                new_text = translator.translate(original_text, src='en', dest='hi').text
                # replace the original text with the new text
                h2_tags[tag_index].string.replace_with(new_text)
            except:
                tag_not_parsed.append(h2_tags[tag_index].string)


    print("Translate <strong> tags:")
    strong_tags = soup.find_all('strong')
    for tag_index in tqdm(range(len(strong_tags))):
        # get the original text inside the <span> tag
        if strong_tags[tag_index].get_text()!="":
            try:
                original_text = strong_tags[tag_index].get_text()
                # change the text as desired
                new_text = translator.translate(original_text, src='en', dest='hi').text
                # replace the original text with the new text
                strong_tags[tag_index].string.replace_with(new_text)
            except:
                tag_not_parsed.append(strong_tags[tag_index].string)

    # def hasNumbers(inputString):
    #     return any(char.isdigit() for char in inputString)


    print("Translate <a> tags:")
    a_tags = soup.find_all('a')
    for tag_index in tqdm(range(len(a_tags))):
        # get the original text inside the <span> tag
        if a_tags[tag_index]!=None:
            if len(a_tags[tag_index].get_text())!=0:
                try:            
                    original_text = a_tags[tag_index].get_text()
                    new_text = translator.translate(original_text, src='en', dest='hi').text
                    a_tags[tag_index].string.replace_with(new_text)
                except:
                    tag_not_parsed.append(a_tags[tag_index].string)



    print("Translate <p> tags:")
    p_tags = soup.find_all('p')
    for tag_index in tqdm(range(len(p_tags))):
        # get the original text inside the <span> tag
        if p_tags[tag_index]!=None:
            if len(p_tags[tag_index].get_text())!=0:
                try:
                    original_text = p_tags[tag_index].get_text()
                    new_text = translator.translate(original_text, src='en', dest='hi').text
                    p_tags[tag_index].string.replace_with(new_text)
                except:
                    tag_not_parsed.append(p_tags[tag_index].string)



    print("Translate <li> tags:")
    li_tags = soup.find_all('li')
    for tag_index in tqdm(range(len(li_tags))):
        # get the original text inside the <span> tag
        if li_tags[tag_index]!=None:
            if len(li_tags[tag_index].get_text())!=0:
                try:
                    original_text = li_tags[tag_index].get_text()
                    new_text = translator.translate(original_text, src='en', dest='hi').text
                    li_tags[tag_index].string.replace_with(new_text)
                except:
                    tag_not_parsed.append(li_tags[tag_index].string)

    print(tag_not_parsed)

    # Save the translated HTML file
    with open(filename, "w",encoding='utf-8') as f:
        f.write(soup.prettify())

