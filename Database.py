from tkinter import *
import sqlite3

window = Tk()
window.geometry("400x400")

# create database 
connection = sqlite3.connect('DATA.db')

# create cursor
c = connection.cursor()

# create table
# c.execute("""CREATE TABLE addresses(
#  first_name text,
#  last_name text,
#  address text,
#  city text,
#  state text,
#  zipcode integer)
# """)
# submit function
def submit():
    # create database 
    connection = sqlite3.connect('DATA.db')

    # create cursor
    c = connection.cursor()

    # insert into table
    c.execute(INSERT INTO addresses VALUES (':f_name, l_name', ':address', ':city', ':state', ':zipcode'),
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
            } )
    # commit changes
    connection.commit()

    # close connection
    connection.close()

    # clear text box
    f_name.delete(0, END)
    l_name.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    address.delete(0, END)
    zipcode.delete(0, END)

# create show function
def show():
    # create database 
    connection = sqlite3.connect('DATA.db')

    # create cursor
    c = connection.cursor()

    # show query database
    c.execute("SELECT *,oid FROM addresses")
    record = c.fetchall()
    print(record)
    

    # commit changes
    connection.commit()

    # close connection
    connection.close()


    

# create text box 
f_name = Entry(window, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(window, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(window, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(window, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(window, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(window, width=30)
zipcode.grid(row=5, column=1, padx=20)

# create text box label
f_name = Label(window,text="first name")
f_name.grid(row=0, column=0)

l_name = Label(window, text="last name")
l_name.grid(row=1, column=0)

address = Label(window, text="address")
address.grid(row=2, column=0)

city = Label(window, text="city")
city.grid(row=3, column=0)

state = Label(window, text="state")
state.grid(row=4, column=0)

zipcode = Label(window, text="zipcode")
zipcode.grid(row=5, column=0)

# create submit button
sbmt_btn = Button(window, text="Add data to database",command=submit)
sbmt_btn.grid(row=6,column=0,columnspan=2, pady=10,padx=10,ipadx=100)

# create querry
query_btn = Button(window, text="Show Data", command=show)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


# commit changes
connection.commit()

# close connection
connection.close()


window.mainloop()