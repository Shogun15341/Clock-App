#CLOCK PROGRAM///////////////////////////////////////////////
 from tkinter import *
 from time import *

 def update():
     time_string = strftime("%I:%M:%S %p")
     time_label.config(text = time_string)

     day_string = strftime("%A")
     day_label.config(text = day_string)

     date_string = strftime("%B %d, %Y")
     date_label.config(text = date_string)

     window.after(1000, update)
 window = Tk()

 time_label = Label(window, font = ("Arial", 50), fg = "#85c997", bg = "black")
 time_label.pack()

 day_label = Label(window, font = ("Arial", 30, "bold"))
 day_label.pack()

 date_label = Label(window, font = ("Arial", 35, "bold"))
 date_label.pack()
 update()

 window.mainloop()

 import smtplib

 sender = "BLABLALBA@gmail.com"
 receiver = "BLABLABLA@gmail.com"
 password = "PASSWORD" #APP PASSWORD NOT GMAIL PASSWORD
 subject = "Test from Python"
 body = "This is Email"

 message = f"""From: Sho 1{sender}
 To:Sho 2{receiver}
 Subject: {subject}\n
 {body}
 """

 server = smtplib.SMTP("smtp.gmail.com", 587)
 server.starttls()

 try:
     server.login(sender,password)
     print("Logged in...")
     server.sendmail(sender, receiver, message)
     print("Email has been sent!")

 except smtplib.SMTPAuthenticationError:
     print("Unable to sign in")