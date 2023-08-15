from bs4 import BeautifulSoup
import requests 

response=requests.get("https://news.ycombinator.com/")
yc_web_page=response.text

soup=BeautifulSoup(yc_web_page, "html.parser")

#find first instance where name of the tag is a
article_tag=soup.find(name="a", class_="storylink")

article_text=article_tag.get_Text()
article_link=article_tag.get("href")
article_upvote=soup.find(name="span", class_="score").getText()

#if we want to find all of the a tags instead of the first one that matches our query we do the find all method 
article_tag_2=soup.find_all(name='a', class_="storylink")
article_texts=[]
article_links=[]

for article in article_tag_2:
    article_text=article_tag.get_text()
    article_texts.append(article_text)


    article_link=article_tag.get("href")
    article_links.append(article_link)


article_upvotes = [score.getText() for socre in soup.find_all(name='span', class_='score')]
int(article_upvotes[0].split()[0])