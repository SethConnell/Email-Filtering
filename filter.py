def Clearfile():
    f = open("results/unusedemails.txt", "w")
    f.write("")
    f.close()

def addEmail(x):
    f = open("results/unusedemails.txt", "a")
    f.write(str(x))
    f.close()

def CheckFile(x):
    with open('subsandunsubs.txt', "r") as subsandunsubs:
        if str(x) not in subsandunsubs.read():
            addEmail(str(x))
            return
Clearfile()
with open('totalemails.csv') as f:
    lines = f.readlines()
    for email in lines:
        fixedemail = email.lower()
        CheckFile(fixedemail)
