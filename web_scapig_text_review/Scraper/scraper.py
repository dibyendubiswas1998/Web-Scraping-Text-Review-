import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq


class FScraper:
    def __init__(self, path, domain):
        self.path = path
        self.domain = domain

    def Get_Text_Data(self):
        try:
            flipkartUrl = self.path
            uClients = uReq(flipkartUrl)
            flipkartPage = uClients.read()
            flipkart_html = bs(flipkartPage, 'html.parser')
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prod_html = bs(prodRes.text, "html.parser")
            commentboxes = prod_html.find_all('div', {'class': "col _2wzgFH"})
            review = prod_html.find_all('p', {'class': "_2-N8zT"})
            review_list = []
            customer_name_list = []
            rating_list = []
            comments_list = []

            for commentbox in commentboxes:
                try:
                    reviews = commentbox.div.find_all('p', {'class': "_2-N8zT"})[0].text

                except:
                    reviews = "No reviews"

                try:
                    cname = commentbox.find_all('p', {'class': "_2sc7ZR"})[0].text
                except:
                    cname = "No name"

                try:
                    rating = commentbox.find_all('div', {'class': "_3LWZlK _1BLPMq"})[0].text
                except:
                    rating = "No rating"

                try:
                    comnts = commentbox.find_all('div', {'class': ""})[0].text
                except:
                    comnts = "No Comments"
                review_list.append(reviews)
                customer_name_list.append(cname)
                rating_list.append(rating)
                comments_list.append(comnts)

            mydct = {"Review": review_list, "Customer_Name": customer_name_list,
                     "Rating": rating_list, "Customer_Comments": comments_list}

            return mydct
        except Exception as e:
            print(e)


