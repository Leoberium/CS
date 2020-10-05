from archive.main import Messenger

m = Messenger()
m.send_message("1", "N")
m.send_message("1", "N")
m.send_message("1", "N")

print(m.get_messages())

m2 = Messenger()
m.send_message("1", "N")
m.send_message("1", "N")
m.send_message("1", "N")

print(m2.get_messages())