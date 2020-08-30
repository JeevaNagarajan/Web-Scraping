from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ur

web_url = 'https://www.flipkart.com/search?q=boat+headphones&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&as-pos=1&as-type=RECENT&suggestionId=boat+headphones%7CHeadphones+%26+Earphones&requestId=493a648d-a9ab-4451-8dcd-0ad615e7ea65&as-searchtext=%20boat%20headphones'

with ur(web_url) as url:
    page_html = url.read()

soup = bs(page_html, 'html.parser')

containers = soup.findAll('div',{'class':'_3liAhj'})
print('Total count is ',len(containers))

#print(bs.prettify(containers[0]))

product_number = 1

for container in containers:

    name = container.div.img['alt']

    product_price = container.findAll('div',{'class':'_1vC4OE'})
    spliting_price = product_price[0].text.replace(',','').split('₹')
    price = 'Rs.' + spliting_price[1]


    product_rating = container.findAll('div',{'class':'hGSR34'})
    rating = product_rating[0].text

    print('Product No.:',product_number)
    print('Name       : ' + name)
    print('Price      : ' + price)
    print('Rating     : ' + rating)
    print()

    with open('product_detials.csv','a',encoding='utf-8') as file:
        file.write('Product No.: ' + str(product_number) + '\n')
        file.write('Name       : ' + name + '\n')
        file.write('Price      : ' + price + '\n')
        file.write('Rating     : ' + rating + '\n\n')
    product_number+=1

print('product_detials written on the file succesfully')
