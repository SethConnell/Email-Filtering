def CheckFile(x):
    with open('subsandunsubs.txt', "r") as subsandunsubs:
        if str(x) not in subsandunsubs.read():
            print(str(x))
            return

with open('totalemails.csv') as f:
    lines = f.readlines()
    for email in lines:
        fixedemail = email.lower()
        CheckFile(fixedemail)
