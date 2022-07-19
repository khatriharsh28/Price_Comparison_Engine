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

# canvas = Canvas(root, width = 500, height = 500)
# canvas.pack()
# #GIF in my_image variable
# #Give the entire file address along with the file name and gif extension
# #Use \\ in the address
# #The image given by me is C:\\UserAdmin\\Device\\Desktop2\\canyon.gif
# my_image = PhotoImage(file='intro.gif')
# canvas.create_image(0, 0, anchor = NW, image=my_image)


img = PhotoImage(file="1.png")
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
        fps=40    #Change the fps to make the animation faster/slower
        shift()

        #Image
        # image = Image.open("LOGO.png")
        # photo = ImageTk.PhotoImage(image)

        
        # label1 = Label(root, image = photo)
        # label1.image = photo
        # # label.grid(row=1)

        # # img=Image.open(name="IMG", file="LOGO.png")
        # # photo = ImageTk.PhotoImage(img)
        # # label1=Label(root, image=img, bd=5, height=450, width=650)
        # label1.grid(row=0, column=0, padx=20, pady=10)
        # click_btn= PhotoImage(file='Continue.png')
        # img_label= Label(image=click_btn)
        # button= Button(root, image=click_btn,command= self.page1)
        # button.pack(pady=30)
        b_continue = Button(master, text = 'Click Me >>',command= self.page1)
        # b_continue = Button(root, text = 'Click Me !', image = click_btn).pack(side = TOP)
        b_continue.place(x = 280, y = 415, width=90,height=35)
        
    def page1(self):
        self.var = StringVar()
        self.pg1 = Toplevel(root)
        self.pg1.geometry("654x487+450+150")
        self.pg1.title('Price Comparison Engine')

        # frame = Frame(self.pg1, width=654, height=487)
        # frame.pack() 
        # frame.place(anchor='center', relx=0.5, rely=0.5)
        # # Label
        # # img1 = PhotoImage(file="LOGO1.png")
        # # labelimg = Label(self.pg1, image=img1)
        # # labelimg.place(x=0, y=0, width=654,height=487)

        # img = ImageTk.PhotoImage(Image.open("LOGO1.png"))

        # # Create a Label Widget to display the text or Image
        # label = Label(frame, image = img)
        # label.pack()

        label = Label(self.pg1, text='Enter the product :-' , font=("Comic Sans MS", 15))
        #label.grid(row=3, column=4,padx=(130,10),pady=30)
        label.place(x = 100, y = 80, width=200,height=40)
        entry = Entry(self.pg1, textvariable=self.var, font=("Comic Sans MS", 15))
        #entry.grid(row=3, column=5)
        entry.place(x = 330, y = 80, width=250,height=40)
        
        button_find = Button(self.pg1, text='Find',font=("Comic Sans MS", 15), command=self.find)
        # button_find.grid(row=4, column=5, sticky=W, pady=8)
        button_find.place(x = 280, y = 150, width=90,height=35)
        

    def find(self):
        #page1.destroy()
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
        self.pg1.destroy()

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
        
        button_search = Button(self.window, text='Search', command=self.search, bd=4)
        button_search.grid(row=3, column=3, sticky=E, padx=30, pady=40)

        button_ebay_visit = Button(self.window, text='Visit Site', command=self.visit_ebay, bd=4)
        button_ebay_visit.grid(row=7, column=2, sticky=W)

        button_flip_visit = Button(self.window, text='Visit Site', command=self.visit_flip, bd=4)
        button_flip_visit.grid(row=2, column=2, sticky=W)

    def price_flipkart(self, key):
        # print(str(key))
        url_flip = 'https://www.flipkart.com/search?q=' + str(key) + '&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
        map = defaultdict(list)

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        source_code = requests.get(url_flip, headers=self.headers)
        soup = BeautifulSoup(source_code.text, "html.parser")
        #print(source_code.text)
        #print(soup)
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
            # for i in block.find_all('img', {'class': '_396cs4_2amPTt_3qGmMb_3exPp9'}):
            #     #disp= i.get('src')
            #     print( i.get('src'))
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
                    
        # Faking the visit from a browser
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }
        html = requests.get('https://www.ebay.com/sch/i.html?_nkw='+str(key), headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        # print(html)
        
        map = defaultdict(list)
        home = 'https://www.ebay.com'
        # source_code = requests.get(url_ebay, headers=headers)
        # plain_text = source_code.text
        self.opt_title = StringVar()
        # self.soup = BeautifulSoup(plain_text, "html.parser")
        # print(source_code)
        #print(self.soup)
        for item in soup.select('.s-item__wrapper.clearfix'):
            title, price, link = None, 'Currently Unavailable', None
            title = item.select_one('.s-item__title').text
            price =  item.select_one('.s-item__price').text
            link = item.select_one('.s-item__link')['href']
            # print(title,link,price)
            if title!= 'Shop on eBay' and link :
                map[title] = [price, link]
        # for html in self.soup.find_all('div', {'class': 's-item__wrapper.clearfix'}):
        #     title, link = None, None
        #     for heading in html.find_all('span', {'class': 's-item__title'}):
        #         title = heading.text
        #     for p in html.find_all('span', {'class': 's-item__price'}):
        #         price = p.text[1:]
        #     for l in html.find_all('a', {'class': 's-item__link'}):
        #         link = home + l.get('href')
        #     print(title,link,price)
        #     if title and link:
        #         map[title] = [price, link]
        
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