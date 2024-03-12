import requests
import os

# It will fetch a web page for purpose web scrapping
r = requests.get("https://github.com/adamburd/learnxinyminutes-docs")
r.status_code # Some sort of code used for indicating a successfull
# request
r.text # To display the contains of the code
# print(r.text) # to print the content in good formated manner

# It open a file and saves the get request contents in the file
with open("learnxinyminutes.html","wb") as f:
    f.write(r.text.encode("UTF-8"))


# Good for reading a csv file using a https
# link and easy for embedding it in code
fp = "https://raw.githubusercontent.com/adambard/leanxinyminutes-docs/master/"
fn = "pets.csv"
print(fp + fn)
# It will work only for legit links
r1 = requests.get(fp + fn)
print(r1.text)

