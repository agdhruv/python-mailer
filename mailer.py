import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def main():
  # prepare all the lists
  email_ids = []
  names = []
  user_names = []
  passwords = []

  with open('dummy.csv') as file:
    for line in file:
      values = line.split(',')
      # 1 -> email id 
      # 2 -> Name
      # 3 -> user name
      # 5 -> password
      email_ids.append(values[1].strip())
      names.append(values[2].strip())
      user_names.append(values[3].strip())
      passwords.append(values[5].strip())

  #establish connection to the server
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("SENDER EMAIL ID", "mypassword") #Enter the email ID and the password of the sender here
  sender = "SENDER EMAIL ID" #Enter the email ID of the sender here

  counter = 0
  #go through all the lists now to play the game
  for email_id in email_ids:

    #form the message object
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = email_id
    msg['Subject'] = "SUBJECT OF THE MAIL"
    body = "Hello " + names[counter] + ",\n\nYour message goes here."
    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()
    server.sendmail(sender, email_id, text)
    counter += 1
  
  #disconnect 
  server.quit()

if __name__ == '__main__':
    main()