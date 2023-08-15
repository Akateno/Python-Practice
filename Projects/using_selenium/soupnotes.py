from bs4 import BeautifulSoup 
#import lxml a different way if html.parser doesnt work 


#open file in python
# with open("name_of_file") as file:
#     contents=file.read

website="https://www.zillow.com/seattle-wa/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A47.81321617165069%2C%22east%22%3A-122.1188896279297%2C%22south%22%3A47.41235313610338%2C%22west%22%3A-122.57070237207033%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A389470%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A16037%2C%22regionType%22%3A6%7D%5D%7D"
soup=BeautifulSoup(website,"html.parser")

print(soup.prettify())
# print(soup.title.name)
#print(soup.title)

#gives first anchor tag in the website 
#print(soup.a)

#gives all the anchor tags 
all_tags=soup.find_all(name="a")
print(all_tags)

#only text in the anchor tag
for tag in all_tags:
    tag.getText()

#only links
for tag in all_tags:
    tag.get("href")


#only fir the first item that matches the query
heading=soup.find(name="h1", id="name")


section_heading=soup.find(name="h3", class_="heading")
print(section_heading.get_text())

#find specific anchor tag using CSS selectors
company_url=soup.select_one(selector='p a')

#all elements with the same class
soup.select(".heading")
