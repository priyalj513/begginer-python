email = input("enter your email : ")  # g@g.in
k = j = d = 0

if len(email) >= 6:
    if email[0].isalpha():  # first character must be a letter
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):
                for ch in email:
                    if ch.isspace():
                        k = 1
                    elif ch.isalpha():
                        if ch == ch.upper():
                            j = 1
                    elif ch.isdigit():
                        continue
                    elif ch in ("_", ".", "@"):
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("wrong email 5")
                else:
                    print("valid email")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")