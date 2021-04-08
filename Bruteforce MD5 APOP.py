import hashlib
import sys
import time

file = "rockyou.txt"
dig = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"
lemd5 = "4ddd4137b84ff2db7291b568289717f0"

def getMD5(unhashed):
    return hashlib.md5(unhashed.encode('utf-8')).hexdigest()


def rockyoureadline(file):
    with open(file, "r", errors = 'replace') as fp:
        for l in fp:
            conc = dig+l.rstrip()
            print(conc)
            c = getMD5(conc)

            if(c==lemd5):
                return "MDP TROUVÉ :", l.rstrip()

        return "PAS MDP TROUVÉ"




print(rockyoureadline(file))
