import psycopg2 
from tkinter import *
import tkinter.messagebox 
import random
from tkinter import simpledialog

root = Tk()
root.geometry("830x1080")
root.title("Hotel DB")
passw = simpledialog.askstring(title="Password",
                                  prompt="What's your pgadmin password:")
# passw = input('Your pgadmin password: ') 
# Database connection details 
conn = psycopg2.connect( 
   database="Hotel", user='postgres', password=passw, 
host='localhost', port= '5432' 
) 
 
cur = conn.cursor() 
 
def read_guest(guestname): 
    cur.execute("SELECT guestname,roomid,checkindate,checkoutdate,paymentstatus,guestpaymentmethod FROM booking join guest on guest.guestid=booking.guestid WHERE guestname = %s", (guestname,)) 
    row = cur.fetchone() 
    Output.delete(1.0, END)
    if row: 
        
        return f'\nName:{row[0]}\nRoom: {row[1]}\nCheckin: {row[2]}\nCheckout: {row[3]}\nPayment Status: {row[4]} + {row[5]}'
        
 
    else: 
        return "No guest found"
 
def list_guests():
     cur.execute("SELECT guestname,roomid,checkindate,checkoutdate,paymentstatus,guestpaymentmethod FROM booking join guest on guest.guestid=booking.guestid")
     record = cur.fetchall()
     i=1
     Output.delete(1.0, END)
     for row in record:
        # return f'{i}.' 
        
        Output.insert(END, f'\nName:{row[0]}\nRoom: {row[1]}\nCheckin: {row[2]}\nCheckout: {row[3]}\nPayment Status: {row[4]} + {row[5]}\n')
        i=i+1

     
def insert_guest(): 
    name = inputname.get("1.0", "end-1c")
    contact = inputContactInfo.get("1.0", "end-1c")
    payment = inputPaymethod.get("1.0", "end-1c")
    id = random.randint(1,10000)
    bookingid = random.randint(1,10000)
    room = inputRoom.get("1.0", "end-1c")
    pay = inputPaymentStatus.get("1.0", "end-1c")
    checkin = inputCheckin.get("1.0", "end-1c")
    checkout = inputCheckout.get("1.0", "end-1c")
    cur.execute("SELECT * FROM guest WHERE guestid = %s", (id,)) 
    if cur.fetchone(): 
        print("Guest ID already exists. Please re-enter.") 
 
    else: 
        cur.execute("INSERT INTO guest VALUES (%s, %s, %s, %s)", 
(id, name, contact, payment)) 
        cur.execute("INSERT INTO booking VALUES (%s, %s, %s, %s, %s, %s)", 
(bookingid, id, room, checkin ,checkout, pay)) 
        cur.execute("update room set roomstatus='False' where roomid = %s",(room,))
        conn.commit() 
        tkinter.messagebox.showinfo("Hotel",  "Guest inserted successfully!") 


def list_rooms():
     cur.execute("SELECT * FROM room")
     record = cur.fetchall()
     i=1
     Output.delete(1.0, END)
     for row in record:
        # return f'{i}.' 
        
        Output.insert(END, f'\nRoom Number :{row[0]}\nType: {row[1]}\nStatus: {row[2]}\nPrice: {row[3]} e\n')
        i=i+1




def show_service():
    roomService = inputRoomService.get("1.0", "end-1c")
    cur.execute("SELECT servicename,datetime,paymentstatus FROM servicebooking join service on service.serviceid= servicebooking.serviceid where roomid =  %s", (roomService,))
    recordService = cur.fetchall()
    Output.delete(1.0, END)
    for row in recordService:
         
        
        Output.insert(END, f'\nService Name: {row[0]}\nDate: {row[1]}\nPayment Status: {row[2]}\n')
def Take_input():
    
    INPUT = inputtxt.get(1.0, "end-1c")
    Output.delete(1.0, END)
    Output.insert(END, read_guest(INPUT))


def list_service():
     servicename = inputService.get("1.0", "end-1c")
     cur.execute("SELECT servicename,staffrole,staffcontactinfo FROM service")
     record = cur.fetchall()
    
     Output.delete(1.0, END)
     for row in record:
         
        
        Output.insert(END, f'\nService Name: {row[0]}\nStaff Role: {row[1]}\nStaff Contacts: {row[2]}\n')


def remove_guest():
    guest_name = inputnameDel.get("1.0", "end-1c").strip()
    
    if not guest_name:
        Output.delete(1.0, END)
        Output.insert(END, 'Please provide a valid Guest Name')
        return

    try:
        with conn.cursor() as cur:
            # Fetch the guestid and roomid using the guest name
            cur.execute("""
                SELECT guest.guestid, booking.roomid 
                FROM guest 
                JOIN booking ON guest.guestid = booking.guestid 
                WHERE guest.guestname = %s
            """, (guest_name,))
            guest_info = cur.fetchone()
        
        if guest_info is None:
            Output.delete(1.0, END)
            Output.insert(END, 'Guest not found')
            return

        guestid, roomid = guest_info

        # Start a transaction block
        with conn:
            with conn.cursor() as cur:
                # Delete from the servicebooking table linked to the room
                cur.execute("DELETE FROM servicebooking WHERE roomid = %s", (roomid,))
                
                # Delete from the booking table first to avoid foreign key constraint issues
                cur.execute("DELETE FROM booking WHERE guestid = %s", (guestid,))
                
                # Then delete from the guest table
                cur.execute("DELETE FROM guest WHERE guestid = %s", (guestid,))
                
                # Update the room status to free (True)
                cur.execute("UPDATE room SET roomstatus = 'True' WHERE roomid = %s", (roomid,))
                
        tkinter.messagebox.showinfo("Hotel",  "Deleted successfully, room freed, and services removed") 
        Output.delete(1.0, END)
    
    except Exception as e:
        Output.delete(1.0, END)
        Output.insert(END, f'Error: {e}')


       





        
def add_service():
    servicename = inputService2.get("1.0", "end-1c")
    roomService = inputRoomService.get("1.0", "end-1c")
    paymentStatusService = inputServicePayment.get("1.0", "end-1c")
    
    dateofService = inputServiceDate.get("1.0", "end-1c")
    servicebookingid = random.randint(1,10000)
    cur.execute("SELECT serviceid FROM service where servicename =  %s", (servicename,))
    recordService = cur.fetchone()
    cur.execute("INSERT INTO servicebooking VALUES (%s, %s, %s, %s, %s)", 
(servicebookingid, roomService, recordService[0],dateofService,paymentStatusService)) 
    conn.commit() 
    tkinter.messagebox.showinfo("Welcome to GFG.",  "Service Added successfully") 

l = Label(text = "Name of the Guest")
addGuestText = Label(text = "---------------\nAdd guest\n---------------")

inputtxt = Text(root, height = 2,
                width = 30,
                bg = "light yellow")
 
 
Output = Text(root, height = 15, 
              width = 40, 
              bg = "#ADD8E6")
 
Display = Button(root, height = 2,
                 width = 20, 
                 text ="Show Guest",
                 command = lambda:Take_input())
 
DisplayAll = Button(root, height = 2,
                 width = 20, 
                 text ="Show All Guests",
                 command = lambda:list_guests())

DisplayAllRooms = Button(root, height = 2,
                 width = 20, 
                 text ="Show All Rooms",
                 command = lambda:list_rooms())

AddGuest = Button(root, height = 2,
                 width = 20, 
                 text ="Add Guest",
                 command = lambda:[insert_guest()])

removeGuest = Button(root, height = 2,
                 width = 20, 
                 text ="Remove Guest",
                 command = lambda:[remove_guest()])
seeServiceOfRoom = Button(root, height = 2,
                 width = 20, 
                 text ="Show Service of the room",
                 command = lambda:[show_service()])
delete = Button(root, height = 2,
                 width = 20, 
                 text ="Delete Guest",
                 command = lambda:[remove_guest()])

nameTxt = Label(text = "Name of the Guest")

deleteGuestTxt = Label(text = '-------------\nName of the Guest to be deleted\n-------------')

inputnameDel = Text(root, height = 2,
                width = 30,
                bg = "light yellow")
inputname = Text(root, height = 2,
                width = 30,
                bg = "light yellow")
contactTxt = Label(text = "Contact of the Guest")

inputContactInfo = Text(root, height = 2,
                width = 30,
                bg = "light yellow")
paymentTxt = Label(text = "Payment of the Guest")
searchGuest = Label(text = "-------------\nSearch for a guest\n-------------")

searchService = Label(text = "-------------\nSearch for a service\n-------------")

bookService = Label(text = "-------------\nBook a service\n-------------")

serviceTxt = Label(text = "Name of the Service")
serviceTxt2 = Label(text = "Name of the Service")
roomAsignedTxt = Label(text = "Room of the guest")
paymentService = Label(text = "Payment Status of the Service")
dateService = Label(text = "Date of the Service (YYYY-MM-DD)")
inputServiceDate= Text(root, height = 2,
                width = 30,
                bg = "light yellow")
inputServicePayment = Text(root, height = 2,
                width = 30,
                bg = "light yellow")
inputRoomService = Text(root, height = 2,
                width = 30,
                bg = "light yellow")
inputService = Text(root, height = 2,
                width = 30,
                bg = "light yellow")
inputService2 = Text(root, height = 2,
                width = 30,
                bg = "light yellow")
DisplayService = Button(root, height = 2,
                 width = 20, 
                 text ="Show All Services",
                 command = lambda:list_service())
addService = Button(root, height = 2,
                 width = 20, 
                 text ="Add Service",
                 command = lambda:add_service())

inputPaymethod = Text(root, height = 2,
                width = 30,
                bg = "light yellow")
roomTxt = Label(text = "Room of the Guest")
inputRoom = Text(root, height = 2,
                width = 30,
                bg = "light yellow")

checkin = Label(text = "Check in date (YYYY-MM-DD)")
inputCheckin= Text(root, height = 2,
                width = 30,
                bg = "light yellow")

checkout = Label(text = "Check out date (YYYY-MM-DD)")
inputCheckout= Text(root, height = 2,
                width = 30,
                bg = "light yellow")

paymentStatus = Label(text = "PaymentStatus")
inputPaymentStatus = Text(root, height = 2,
                width = 30,
                bg = "light yellow")

#Arrange

Output.grid(row=23,column=2)
addGuestText.grid(row=1,column=1)
nameTxt.grid(row=2,column=1)

inputname.grid(row=3,column=1)


contactTxt.grid(row=4,column=1)
inputContactInfo.grid(row=5,column=1)
paymentTxt.grid(row=6,column=1)
inputPaymethod.grid(row=7,column=1)
roomTxt.grid(row=8,column=1)
inputRoom.grid(row=9,column=1)
checkin.grid(row=10,column=1)
inputCheckin.grid(row=11,column=1)
checkout.grid(row=12,column=1)
inputCheckout.grid(row=13,column=1)
paymentStatus.grid(row=14,column=1)
inputPaymentStatus.grid(row=15,column=1)
AddGuest.grid(row=16,column=1)

searchGuest.grid(row=1,column=2)
l.grid(row=2,column=2)

inputtxt.grid(row=3,column=2)
Display.grid(row=4,column=2)


DisplayAll.grid(row=5,column=2)
DisplayAllRooms.grid(row=6,column=2)
deleteGuestTxt.grid(row=7,column=2)
inputnameDel.grid(row=8,column=2)
delete.grid(row=9,column=2)
# searchService.grid(row=1,column=3)
# serviceTxt.grid(row=2,column=3)
# inputService.grid(row=3,column=3)
DisplayService.grid(row=1,column=3)
bookService.grid(row=2,column=3)
serviceTxt2.grid(row=3,column=3)
inputService2.grid(row=4,column=3)

roomAsignedTxt.grid(row=5,column=3)
inputRoomService.grid(row=6,column=3)

paymentService.grid(row=7,column=3)
inputServicePayment.grid(row=8,column=3)
addService.grid(row=11,column=3)
dateService.grid(row=9,column=3)
inputServiceDate.grid(row=10,column=3)
seeServiceOfRoom.grid(row=12,column=3)


mainloop()
conn.close() 
