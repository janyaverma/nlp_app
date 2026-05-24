from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):
        
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#037ffc')
        
        self.dbo = Database()
        self.apio = API()
        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text = 'NLPApp', bg = '#037ffc')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root, text = 'Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root, width = 30)
        self.email_input.pack(pady=(5,10),ipady = 4)

        label2 = Label(self.root, text = 'Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root, width = 30, show='*')
        self.password_input.pack(pady=(5,10),ipady = 4)

        login_btn = Button(self.root, text='Login', width=30, height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root, text='Register Now',command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text = 'NLPApp', bg = '#037ffc')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root, text = 'Enter Name')
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root, width = 30)
        self.name_input.pack(pady=(5,10),ipady = 4)

        label1 = Label(self.root, text = 'Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root, width = 30)
        self.email_input.pack(pady=(5,10),ipady = 4)

        label2 = Label(self.root, text = 'Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root, width = 30, show='*')
        self.password_input.pack(pady=(5,10),ipady = 4)

        register_btn = Button(self.root, text='Register', width=30, height=2, 
                              command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root, text='Login Now',command=self.login_gui)
        redirect_btn.pack(pady=(10,10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
       name = self.name_input.get()
       email = self.email_input.get()
       password = self.password_input.get()

       response = self.dbo.add_data(name,email,password)

       if response:
           messagebox.showinfo('Success','Registration successful, you can login now')
       else:
           messagebox.showerror('Error','Email already exists')
    
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email/password')
    
    def home_gui(self):
        self.clear()
        heading = Label(self.root, text = 'NLPApp', bg = '#037ffc')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=2, 
                              command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))
        
        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=2, 
                              command=self.ner_gui)
        ner_btn.pack(pady=(10,10))
        
        intent_btn = Button(self.root, text='Intent Analysis', width=30, height=2, 
                              command=self.intent_gui)
        intent_btn.pack(pady=(10,10))

        logout_btn = Button(self.root, text='Logout',command=self.login_gui)
        logout_btn.pack(pady=(10,10))

    def intent_gui(self):
        self.clear()
        heading = Label(self.root, text = 'NLPApp', bg = '#037ffc')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        heading2 = Label(self.root, text = 'Intent Analysis', bg = '#037ffc')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana',20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10,10))

        self.intent_input = Entry(self.root, width = 50)
        self.intent_input.pack(pady=(5,10),ipady = 4)

        intent_btn = Button(self.root, text='Analyze',command=self.do_intent_analysis)
        intent_btn.pack(pady=(10,10))

        self.intent_result = Label(self.root, text='', bg='#037ffc', fg='white')
        self.intent_result.pack(pady=(10,10))
        self.intent_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))
    
    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text = 'NLPApp', bg = '#037ffc')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        heading2 = Label(self.root, text = 'Named Entity Recognition', bg = '#037ffc')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana',20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10,10))

        self.ner_input = Entry(self.root, width = 50)
        self.ner_input.pack(pady=(5,10),ipady = 4)

        label2 = Label(self.root, text='Enter the search term')
        label2.pack(pady=(10,10)) 

        self.ner_st_input = Entry(self.root, width = 50)
        self.ner_st_input.pack(pady=(5,10),ipady = 4)

        ner_btn = Button(self.root, text='Analyze',command=self.do_ner)
        ner_btn.pack(pady=(10,10))

        self.ner_result = Label(self.root, text='', bg='#037ffc', fg='white')
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))
       
    
    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text = 'NLPApp', bg = '#037ffc')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        heading2 = Label(self.root, text = 'Sentiment Analysis', bg = '#037ffc')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana',20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10,10))

        self.sentiment_input = Entry(self.root, width = 50)
        self.sentiment_input.pack(pady=(5,10),ipady = 4)

        sentiment_btn = Button(self.root, text='Analyze',command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result = Label(self.root, text='', bg='#037ffc', fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_intent_analysis(self):
        text = self.intent_input.get()
        result = self.apio.intent_analysis(text)

        self.intent_result['text'] = result        
    
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = result
        for i in result['scored_labels']:
            txt += i['label'] + '->' + str(i['score']) + '\n'

        self.sentiment_result['text'] = txt

    def do_ner(self):
        text = self.ner_input.get()
        search_term = self.ner_st_input.get()
        result = self.apio.ner(text,search_term)

        self.ner_result['text'] = result

nlp = NLPApp()