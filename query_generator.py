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

  print("LOL CATS")

  counter = 0
  query = "INSERT INTO `users` (`username`, `lvl`, `name`, `tlc`) VALUES "
  entries = [query]
  #go through all the lists now to play the game
  for password in passwords:
    this_entry = "('" + user_names[counter] + "', '0', " + "'" + names[counter] + "', '0000-00-00 00:00:00.000000'), "
    entries.append(this_entry)
    counter += 1
  s = ''.join(entries)
  print s;

if __name__ == '__main__':
    main()