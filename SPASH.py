from tkinter import *
#from tkinter import _CanvasItemId
from bs4 import BeautifulSoup
import requests
from difflib import get_close_matches
import webbrowser
from collections import defaultdict
import random
from PIL import Image, ImageTk
import time

root = Tk()
root.geometry("654x487+450+150")
root.config(bg='grey')

img = PhotoImage(file="Loader.png")
labelimg = Label(root, image=img)
labelimg.place(x=0, y=0)

class Price_compare:

    def __init__(self, master):

        def shift():
            x1,y1,x2,y2 = canvas.bbox("marquee")
            if(x2<0 or y1<0): #reset the coordinates
                x1 = canvas.winfo_width()
                y1 = canvas.winfo_height()//2
                canvas.coords("marquee",x1,y1)
            else:
                canvas.move("marquee", -2, 0)
            canvas.after(1000//fps,shift)

        self.var_ebay = StringVar()
        self.var_flipkart = StringVar()
        self.var_ebay = StringVar()

        canvas=Canvas(root,bg='#BDEFEA')
        canvas.pack()
        text_var="Welcome to SPASH Price Comparison Engine."
        text=canvas.create_text(0,-2000,text=text_var,font=('Stylus',20,'bold'),fill='black',tags=("marquee",),anchor='w')
        x1,y1,x2,y2 = canvas.bbox("marquee")
        width = x2-x1
        height = y2-y1
        canvas['width']=width
        canvas['height']=height
        fps=150    #Change the fps to make the animation faster/slower
        shift()

        self.cont = PhotoImage(file="Continue.png")
        b_continue = Button(master,image = self.cont, borderwidth = 0, command= self.page1)
        b_continue.place(x = 280, y = 415, width=105,height=29)

    def vst_grocery(self):   
        link='https://www.flipkart.com/grocery-supermart-store?marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_e37b4f0b-2cce-4c19-8394-2e3f61d6dde8_1_372UD5BXDFYS_MC.CBUR1Q46W5F1&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Grocery_CBUR1Q46W5F1&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=CBUR1Q46W5F1' 
        webbrowser.open(link)

    def vst_mobile(self):   
        link='https://www.flipkart.com/mobile-phones-store?fm=neo%2Fmerchandising&iid=M_cf226ade-2f23-41c4-aade-69644a0b4325_1_372UD5BXDFYS_MC.ZRQ4DKH28K8J&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Mobiles_ZRQ4DKH28K8J&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L0_view-all&cid=ZRQ4DKH28K8J' 
        webbrowser.open(link)

    def vst_fashion(self):   
        link='https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo,ash&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_cb605ebf-213e-436c-9731-754da26f74a1_1_372UD5BXDFYS_MC.AHHHWF67UPNB&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BTop%2BWear~All_AHHHWF67UPNB&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=AHHHWF67UPNB' 
        webbrowser.open(link)

    def vst_electronis(self):   
        link='https://www.flipkart.com/audio-video/~cs-53mrbtcuf5/pr?sid=0pm&collection-tab-name=Audio+And+Video&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&fm=neo%2Fmerchandising&iid=M_b1792f37-20d1-4e3d-8f2b-15d3ea7a84e5_1_372UD5BXDFYS_MC.9JGNW7M0TUHD&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Electronics~Audio~All_9JGNW7M0TUHD&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=9JGNW7M0TUHD' 
        webbrowser.open(link)

    def vst_application(self):   
        link='https://www.flipkart.com/tvs-and-appliances-new-clp-store?fm=neo%2Fmerchandising&iid=M_2a08020e-58fe-4b00-9799-6c44138fa9bf_1_372UD5BXDFYS_MC.LO4IWVHA61BX&otracker=hp_rich_navigation_7_1.navigationCard.RICH_NAVIGATION_Appliances_LO4IWVHA61BX&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L0_view-all&cid=LO4IWVHA61BX' 
        webbrowser.open(link)

    def page1(self):
        self.var = StringVar()
        self.pg1 = Toplevel(root)
        self.pg1.geometry("654x487+450+150")
        self.pg1.title('Price Comparison Engine')
        # self.pg1.config(bg='white')
        label = Label(self.pg1, text='Enter the product :-' , font=("Comic Sans MS", 15))
        label.place(x = 100, y = 80, width=200,height=40)

        def click(*args):
            if entry.get()=='Product Name':
                entry.delete(0, 'end')
            entry.config(fg='black')
  
        entry = Entry(self.pg1, textvariable=self.var, fg='grey', font=("Comic Sans MS", 15))
        entry.insert(0, 'Product Name')
        entry.pack(pady=10)
        entry.bind("<Button-1>", click)
        entry.place(x = 330, y = 80, width=250,height=40)
        
        button_find = Button(self.pg1, text='Find',font=("Comic Sans MS", 15), command=self.find)
        button_find.place(x = 280, y = 150, width=90,height=35)
        
        self.g = PhotoImage(file="grocery.png")
        grocery = Button(self.pg1, text = 'Grocery', image = self.g, compound= TOP, borderwidth = 2, bg='white',command= self.vst_grocery)
        grocery.pack(side=TOP)
        grocery.place(x = 60, y = 380, width=90,height=100)

        self.m = PhotoImage(file="mobile.png")
        mobile = Button(self.pg1, text = 'Mobile', image = self.m, compound= TOP, borderwidth = 2, bg='white',command= self.vst_mobile)
        mobile.pack(side=TOP)
        mobile.place(x = 180, y = 380, width=90,height=100)

        self.f = PhotoImage(file="fashion.png")
        fashion = Button(self.pg1, text = 'fashion', image = self.f, compound= TOP, borderwidth = 2, bg='white',command= self.vst_fashion)
        fashion.pack(side=TOP)
        fashion.place(x = 300, y = 380, width=90,height=100)

        self.e = PhotoImage(file="electronics.png")
        electronics = Button(self.pg1, text = 'Electronics', image = self.e, compound= TOP, borderwidth = 2, bg='white',command= self.vst_electronis)
        electronics.pack(side=TOP)
        electronics.place(x = 420, y = 380, width=90,height=100)

        self.a = PhotoImage(file="application.png")
        application = Button(self.pg1, text = 'Application', image = self.a, compound= TOP, borderwidth = 2, bg='white',command= self.vst_application)
        application.pack(side=TOP)
        application.place(x = 540, y = 380, width=90,height=100)
        

    def find(self):
        self.product = self.var.get()
        self.product_arr = self.product.split()
        self.n = 1
        self.key = ""
        self.title_flip_var = StringVar()
        self.title_ebay_var = StringVar()
        self.variable_ebay = StringVar()
        self.variable_flip = StringVar()

        for word in self.product_arr:
            if self.n == 1:
                self.key = self.key + str(word)
                self.n += 1

            else:
                self.key = self.key + '+' + str(word)

        self.window = Toplevel(root)
        self.window.geometry("654x487+450+150")
        self.window.title('Price Comparison Engine')
        label_title_flip = Label(self.window, text='Flipkart Title:')
        label_title_flip.grid(row=0, column=0, sticky=W)

        label_flipkart = Label(self.window, text='Flipkart price (Rs):')
        label_flipkart.grid(row=2, column=0, sticky=W)

        entry_flipkart = Entry(self.window, textvariable=self.var_flipkart)
        entry_flipkart.grid(row=2, column=1, sticky=W)
        
        label_title_ebay = Label(self.window, text='Ebay Title:')
        label_title_ebay.grid(row=5, column=0, sticky=W)

        label_ebay = Label(self.window, text='Ebay price (Rs):')
        label_ebay.grid(row=7, column=0, sticky=W)

        entry_ebay = Entry(self.window, textvariable=self.var_ebay)
        entry_ebay.grid(row=7, column=1, sticky=W)
        
        self.price_flipkart(self.key)
        
        self.price_ebay(self.key)
        try:
            self.variable_ebay.set(self.matches_ebay[0])
        except:
            self.variable_ebay.set('Product not available')
        try:
            self.variable_flip.set(self.matches_flip[0])
        except:
            self.variable_flip.set('Product not available')
        
        try:
            option_ebay = OptionMenu(self.window, self.variable_ebay, *self.matches_ebay)
            option_ebay.grid(row=5, column=1, sticky=W)
            lab_amz = Label(self.window, text='Not this? Try out suggestions by clicking on the title')
            lab_amz.grid(row=6, column=1, padx=4)
        except:
            lab_amz = Label(self.window, text='Product not available')
            lab_amz.grid(row=6, column=2, padx=4)

        try:
            option_flip = OptionMenu(self.window, self.variable_flip, *self.matches_flip)
            option_flip.grid(row=0, column=1, sticky=W)
            lab_flip = Label(self.window, text='Not this? Try out suggestions by clicking on the title')
            lab_flip.grid(row=1, column=1, padx=4)
        except:
            lab_amz = Label(self.window, text='Product not available')
            lab_amz.grid(row=3, column=2, padx=4)
        self.pg1.destroy()
        
        button_search = Button(self.window, text='Search', command=self.search, bd=4)
        button_search.grid(row=3, column=3, sticky=E, padx=30, pady=40)

        button_ebay_visit = Button(self.window, text='Visit Site', command=self.visit_ebay, bd=4)
        button_ebay_visit.grid(row=7, column=2, sticky=W)

        button_flip_visit = Button(self.window, text='Visit Site', command=self.visit_flip, bd=4)
        button_flip_visit.grid(row=2, column=2, sticky=W)

    def price_flipkart(self, key):
        url_flip = 'https://www.flipkart.com/search?q=' + str(key) + '&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
        map = defaultdict(list)

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        source_code = requests.get(url_flip, headers=self.headers)
        soup = BeautifulSoup(source_code.text, "html.parser")
        
        self.opt_title_flip = StringVar()
        home = 'https://www.flipkart.com'
        for block in soup.find_all('div', {'class': '_2kHMtA'}):
            title, price, link = None, 'Currently Unavailable', None
            for heading in block.find_all('div', {'class': '_4rR01T'}):
                title = heading.text
            for p in block.find_all('div', {'class': '_30jeq3 _1_WHN1'}):
                price = p.text[1:]
            for l in block.find_all('a', {'class': '_1fQZEK'}):
                link = home + l.get('href')
                
            map[title] = [price, link]

        user_input = self.var.get().title()
        self.matches_flip = get_close_matches(user_input, map.keys(), 20, 0.1)
        self.looktable_flip = {}
        for title in self.matches_flip:
            self.looktable_flip[title] = map[title]

        try:
            self.opt_title_flip.set(self.matches_flip[0])
            self.var_flipkart.set(self.looktable_flip[self.matches_flip[0]][0] + '.00')
            self.link_flip = self.looktable_flip[self.matches_flip[0]][1]
        except IndexError:
            self.opt_title_flip.set('Product not found')

    def price_ebay(self, key):
        url_ebay = 'https://www.ebay.com/sch/i.html?_nkw=' + str(key)
                    
                    
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }
        html = requests.get('https://www.ebay.com/sch/i.html?_nkw='+str(key), headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        
        map = defaultdict(list)
        home = 'https://www.ebay.com'
        
        self.opt_title = StringVar()
        
        for item in soup.select('.s-item__wrapper.clearfix'):
            title, price, link = None, 'Currently Unavailable', None
            title = item.select_one('.s-item__title').text
            price =  item.select_one('.s-item__price').text
            link = item.select_one('.s-item__link')['href']
            
            if title!= 'Shop on eBay' and link :
                map[title] = [price, link]
        
        user_input = self.var.get().title()
        self.matches_ebay = get_close_matches(user_input, list(map.keys()), 20, 0.01)
        self.looktable = {}
        
        for title in self.matches_ebay:
            self.looktable[title] = map[title]
            
        try:
            self.opt_title.set(self.matches_ebay[0])
            self.var_ebay.set(self.looktable[self.matches_ebay[0]][0] + '.00')
            self.product_link = self.looktable[self.matches_ebay[0]][1]
        except IndexError:
            self.opt_title.set('Product not found')

    def search(self):
        if len(self.looktable):
            ebay_get = self.variable_ebay.get()
            self.opt_title.set(ebay_get)
            product = self.opt_title.get()
            price, self.product_link = self.looktable[product][0], self.looktable[product][1]
            self.var_ebay.set(price + '.00')
        else:
            self.opt_title.set('Product not found')
        
        if len(self.looktable_flip):
            flip_get = self.variable_flip.get()
            flip_price, self.link_flip = self.looktable_flip[flip_get][0], self.looktable_flip[flip_get][1]
            self.var_flipkart.set(flip_price + '.00')
        else:
            self.opt_title.set('Product not found')

    def visit_ebay(self):
        webbrowser.open(self.product_link)

    def visit_flip(self):
        webbrowser.open(self.link_flip)

if __name__ == "__main__":
    c = Price_compare(root)
    root.title('Price Comparison Engine')
    root.mainloop()