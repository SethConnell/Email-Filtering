import re
import json
gmail = 0
yahoo = 0
comcast = 0
aol = 0
att = 0
with open('notusedemails.csv') as f:
    lines = f.readlines()
    isps = {}
    for email in lines:
        email = email.lower()
        if "gmail" in email and gmail < 300:
            gmail = gmail + 1
            print(email)

        if "yahoo" in email and yahoo < 300:
            yahoo = yahoo + 1
            print(email)

        if "comcast" in email and comcast < 300:
            comcast = comcast + 1
            print(email)

        if "hotmail" in email or "live.com" in email or "outlook.com" in email or "msn.com" in email or "passport.com" in email or "passport.net" in email:
            pass

        if "ameritech.net" in email or "att.net" in email or "bellsouth.net" in email or "currently.com" in email or "flash.net" in email or "nvbell.net" in email or "pacbell.net" in email or "prodigy.net" in email or "sbcglobal.net" in email or "snet.net" in email or "swbell.net" in email or "wans.net" in email:
            att = att + 1
            if att < 100:
                print(email)
            
        if "verizon" in email:
            pass

        if "aol" in email and aol < 300:
            aol = aol + 1
            print(email)

        if "verizon" not in email and "ameritech.net" not in email and "att.net" in email and "bellsouth.net" not in email and "currently.com" not in email and "flash.net" not in email and "nvbell.net" not in email and "pacbell.net" not in email and "prodigy.net" not in email and "sbcglobal.net" not in email and "snet.net" not in email and "swbell.net" not in email and "wans.net" not in email and "aol" not in email and "hotmail" not in email and "outlook.com" not in email and "msn.com" not in email and "live.com" not in email and "passport.com" not in email and "passport.net" not in email and "comcast" not in email and "yahoo" not in email and "gmail" not in email and "msn.com" not in email:
            print(email)
