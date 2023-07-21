users = ['admin', 'andrii', 'erick', 'barbara', 'chuck', 'joe']

if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user.title() + ", would you like to see a status report?")
        else:
            print("\tHello " + user.title())
else:
    print("Empty list")