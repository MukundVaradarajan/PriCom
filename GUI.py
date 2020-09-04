import urllib2 as url
import bs4 as bs
from Tkinter import *
import webbrowser
from bs4 import BeautifulSoup as BS

#GUI

flipkart=[None for x in range(3)]
amazon=[None for x in range(3)]
shopclues=[None for x in range(3)]

root=Tk()

#Set grid columns to equal width
root.grid_columnconfigure(0,weight=1,uniform="fred")
root.grid_columnconfigure(1,weight=1,uniform="fred")
root.grid_columnconfigure(2,weight=1,uniform="fred")
root.grid_columnconfigure(3,weight=1,uniform="fred")

root.title("PriCom")

flipkart_link='https://www.flipkart.com/'
amazon_link='https://www.amazon.in/'
shopclues_link='http://www.shopclues.com/'

def project():
    product=e.get()
    def flipkart(filpkart_link):
        product_details=[None for x in range(3)]
        try:
            flipkart_page=url.urlopen(flipkart_link).read()
        except:
            return product_details
        
        flipkart_page=bs.BeautifulSoup(flipkart_page,'html.parser')
    
        try:
            flipkart_searches=flipkart_page.find('div',{'class':'col _2-gKeQ'})
        except:
            return product_details
    
        if flipkart_searches == None:
            return product_details
        
        href_tag=flipkart_searches.find('a')
        product_details[2]=href_tag.get('href')

        if product_details[2]:
            flip_href=product_details[2]
            
        product_details[0]=flipkart_searches.find('div',{'class':'_3wU53n'})
    
        product_details[1]=flipkart_searches.find('div',{'class':'_1vC4OE _2rQ-NK'})
        print('Flipkart')
        if product_details[0] and product_details[1]:
            product_details[0]=product_details[0].text
            product_details[1]=product_details[1].text
        return product_details
    
    
    def shopclues(shopclues_link):
        product_details=[None for x in range(3)]
        try:
            shopclues_page=url.urlopen(shopclues_link).read()
        except:
            return product_details
        shopclues_page=bs.BeautifulSoup(shopclues_page,'html.parser')
        try:
            shopclues_searches=shopclues_page.find('div',{'class':'column col3'})
        except:
            return product_deatails
    
        if shopclues_searches == None:
            return product_details
        
        href_tag=shopclues_searches.find('a')
        
        product_details[2]=href_tag.get('href')

        if product_details[2]:
            shop_href=product_details[2]
            
        product_details[0]=shopclues_searches.find('h3')
    
        product_details[1]=shopclues_searches.find('span',{'class':'p_price'})
        print('Shopclues')
        if product_details[0] and product_details[1]:
            product_details[0]=product_details[0].text
            product_details[1]=product_details[1].text
        return product_details
    
    def amazon(amazon_link):
        product_details=[None for x in range(3)]
        try:
            amazon_page=url.urlopen(amazon_link).read()
        except:
            return product_details
        amazon_page=bs.BeautifulSoup(amazon_page,'html.parser')
        try:
            amazon_searches=amazon_page.find('li',{'id':'result_0'})
        except:
            return product_details
        if amazon_searches == None:
            return product_details
        
        href_tag=amazon_searches.find('a')
        
        product_details[2]=href_tag.get('href')

        if product_details[2]:
            amaz_href=product_details[2]
            
        product_details[0]=amazon_searches.find('div',{'class':'a-row a-spacing-none'})
    
        product_details[1]=amazon_searches.find('span',{'class':'a-size-base a-color-price s-price a-text-bold'})
        print('Amazon')

        if product_details[0] and product_details[1]:
            product_details[0]=product_details[0].text
            product_details[1]=product_details[1].text
        return product_details

    productformat_1=product.replace(' ','%20')
    productformat_2=product.replace(' ','+')
    global shopclues_link
    global flipkart_link
    global amazon_link
    shopclues_link='http://www.shopclues.com/search?q='+productformat_1+'&sc_z=4444&z=1&count=9'
    flipkart_link='https://www.flipkart.com/search?q='+productformat_1+'&otracker=start&as-show=on&as=off'
    amazon_link='https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='+productformat_2+'&rh=i%3Aaps%2Ck%3A'+productformat_2
    amazon=amazon(amazon_link)
    shop=shopclues(shopclues_link)
    flip=flipkart(flipkart_link)
    change_label(amazon,flip,shop)


def flip_browser():
    webbrowser.open_new_tab(flipkart_link)

def amazon_browser():
    webbrowser.open_new_tab(amazon_link)

def shop_browser():
    webbrowser.open_new_tab(shopclues_link)


#Entry
l1=Label(root,text="Product")
l1.grid(row=0,column=0)
e=Entry(root)
e.grid(row=0,column=1,columnspan=2)
b=Button(root,text="Search",borderwidth=0,command=project)
b.grid(row=0,column=3)

#Labels
headLabel=Label(root,text="Websites")
headLabel.grid(row=1,column=0)

w1=Label(root,text="Flipkart")
w1.grid(row=1,column=1)

w2=Label(root,text="Amazon")
w2.grid(row=1,column=2)

w3=Label(root,text="Shopclues")
w3.grid(row=1,column=3)

name=Label(root,text='Name',fg='green')
name.grid(row=2,column=0)

#Name of product in different websites
name_flipkart=Label(root,text=flipkart[0],fg='red')
name_amazon=Label(root,text=amazon[0],fg='red')
name_shop=Label(root,text=shopclues[0],fg='red')
name_flipkart.grid(row=2,column=1)
name_amazon.grid(row=2,column=2)
name_shop.grid(row=2,column=3)

#Prices
price=Label(root,text='Price',fg='green',)
price.grid(row=3,column=0)

link=Label(root,text='Links',fg='green')
link.grid(row=4,column=0)

price_flipkart=Label(root,text=flipkart[1],fg='red')
goto_flip=Button(root,text='Go To Site',fg='blue',command=flip_browser)
goto_flip.grid(row=4,column=1)

price_amazon=Label(root,text=amazon[1],fg='red',cursor="hand1")
goto_amaz=Button(root,text='Go To Site',fg='blue',command=amazon_browser)
goto_amaz.grid(row=4,column=2)

price_shop=Label(root,text=shopclues[1],fg='red',cursor="hand1")
goto_flip=Button(root,text='Go To Site',fg='blue',command=shop_browser)
goto_flip.grid(row=4,column=3)

price_flipkart.grid(row=3,column=1)
price_amazon.grid(row=3,column=2)
price_shop.grid(row=3,column=3)

def change_label(amaz,flip,shop):
    name_flipkart.config(text=flip[0])
    name_amazon.config(text=amaz[0])
    name_shop.config(text=shop[0])

    price_flipkart.config(text=flip[1])
    price_amazon.config(text=amaz[1])
    price_shop.config(text=shop[1])

#Run
root.mainloop()
