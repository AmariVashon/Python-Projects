email_dict = dict()

def email_slicer(email):
    username, domain = email.split("@")
    email_dict.update({username : email})
    print("Username: " + username + "\nDomain: " + domain)

#get_info = str(input("Enter your email: "))
#email_slicer(get_info)
email_slicer('amarivashon@gmail.com')
email_slicer('kalonji_derron@gmail.com')
print(email_dict)
print("\n")
for key in email_dict:
    print(f"Username: {key} and Email: {email_dict[key]}")
