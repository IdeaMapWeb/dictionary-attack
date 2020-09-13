from attack import dictionaly_attack
import time

user_id = 'leo@mail'
dictionaly_file = "dictionary.txt"
password = 'acb123'
strinf = 'abcdefghijklmnopqrstuvwxyz 0123456789'
start = time.time()
ans = dictionaly_attack(user_id, string, dictionaly_file, 3, password)
elapsed_time = time.time() -start
print ans,password
print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
