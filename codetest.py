
"""
Created on Thu Jul  2 23:52:41 2020

@author: Anasslm
"""

from PIL import Image
import pytesseract as pt
from pytesseract import image_to_string
import pandas as pd 

pt.pytesseract.tesseract_cmd = r'C:\Users\AppData\Local\tesseract.exe'

# Uploading the images
image1 = Image.open('Contract.png')
image_index = Image.open('Contract 1.png')

#Converting the text in the image into strings
text = image_to_string(image1)
text_index = image_to_string(image_index)

#Split the string lines
lines = text.splitlines()
lines_index = text_index.splitlines()

# Remove the index elements from the lines 
Element = [x.replace('Date :','').replace('First name :','').replace('Last name : ','')
         .replace('date of birth : ','').replace('Contract Number','').replace('Type of contract :','')
         .replace('signature','')for x in lines] 


# Preprocessing the index elements : removing with spaces and empty lines
while '' in lines_index: lines_index.remove('')
while ' ' in lines_index: lines_index.remove(' ')

#Creating and processing a DataFrame that contain elements of the documents
df = pd.DataFrame(Element)
df = df[df[0]!= ' '] 
df = df[df[0]!= ''] 

#Adding the index columns to the Dataframe
df['index'] = lines_index
df = df.set_index('index')

