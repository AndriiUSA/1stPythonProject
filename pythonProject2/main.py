users = ['admin', 'andrii', 'erick', 'barbara', 'chuck', 'joe']

for user in users:
    if user == 'admin':
        print("Hello " + user.title() + ", would you like to see a status report?")
    else:
        print()
        print("\tHello " + user.title())