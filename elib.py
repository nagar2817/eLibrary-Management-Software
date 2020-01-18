import shutil

# library
class Library:
    def __init__(self,name,address):
        pass


# books
class Book:
    def __init__(self,title,ISBN,genre,author,rack_no):
        self.title=title
        self.ISBN=ISBN
        self.genre=genre
        self.author=author
        self.rack_no=rack_no
        self.list=[self.title,self.ISBN,self.genre,self.author]
    def display_catalog(self):
        return self.list
    def add_book(self):
        f = open(self.title+".txt" , "w+")
        f.write(self.title+"\n"+str(self.ISBN)+"\n"+self.genre+"\n"+self.author+"\n"+self.rack_no)
        f.close()
        # move the file
        shutil.move('C:\\Users\\pratyaksh\\Desktop\\SIH\\%s.txt'%(self.title),'C:\\Users\\pratyaksh\\Desktop\\SIH\\books')

# Book Catalog
# book1=Book("Rich Dad Poor Dad", 9783161484100,"Self help book","Robert T. kiyosaki",'312')
# book2=Book("Core Python Programming", 9783161484100,"Computer","Dr. R. Nageswara Rao",'314')

# Adding a book 
def add(name):       
    try:
        name.add_book()
    except shutil.Error:
        print("File already exists")

# Searching books
class Fetch_book:
    def __init__(self,option,title):
        self.option=input()
        self.title=input()
    def search(self):
        if(self.option.lower()=='title'):
            f = open('%s.txt'%(self.title), "r")
            for x in f:
                print(x)
                # if(x==self.title):
                #     return self.title

c=Fetch_book('title','Rich Dad Poor Dad')
c.search()









# Accounts 
class Account:
    def add_member(self,name,roll_no,contact_no,address,email):
        self.name=name
        self.roll_no=roll_no
        self.contact_no=contact_no
        self.address=address
        self.email=email
        f = open(self.name+".txt" , "w+")
        f.write(self.name+"\n"+self.roll_no+"\n"+str(self.contact_no)+"\n"+self.address+"\n"+self.email)
        f.close()
        # move the file
        shutil.move('C:\\Users\\pratyaksh\\Desktop\\SIH\\%s.txt'%(self.name),'C:\\Users\\pratyaksh\\Desktop\\SIH\\Members')
        
# Members Catalog
# member1=Account()
# member1.add_member('Pratyaksh Tyagi','B19EE067',9352209532,'IIT Jodhpur','tyagi.6@iitj.ac.in')


        