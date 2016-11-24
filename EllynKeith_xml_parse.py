## Import library for XML parser
from bs4 import BeautifulSoup

## Open XML file
xml = open("data.xml", "rb")
data = xml.read()
xml.close()

## Make BeautifulSoup object
soup = BeautifulSoup(data, "html.parser")

## Create en/fr text files
eng = open("eng.txt", "w")
fren = open("fren.txt", "w")

## Extract documents from soup
docs = soup.find_all("document")


## Create lists for all english abstracts and french abstracts
eList = []
fList = []

## Create lists for only abstracts with equal number of sentences
engEq = []
frenEq = []

## Extract sentences and language label from documents
for doc in docs:
    lang = doc.infon.contents
    sents = doc.find_all("text")
    
    ## Add abstract sentences to English list or French list
    if lang == ["EN"]:
        eList.append([sent.contents for sent in sents])
    elif lang == ["FR"]:
        fList.append([sent.contents for sent in sents])


## Iterating over each document, add documents of equal length to respective lists   
for i in range(len(eList)):
    if len(eList[i]) == len(fList[i]):
        engEq.append(eList[i])
        frenEq.append(fList[i])

    
## Write text from abstracts to text files
for doc in engEq:
    for sent in doc:
        eng.write(sent[0].strip()+ "\n")
for doc in frenEq:
    for sent in doc:
        fren.write(sent[0].strip()+ "\n")

eng.close()
fren.close()