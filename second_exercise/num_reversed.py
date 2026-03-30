# Δίνει ο χρήστης τον αριθμό
num=int(input("Give number"))

# Δημιουργεί κενή λίστα 
digit_lst=[]
# Διαβάζει το κείμενο του χρήστη , το μετατρέπει σε ακέραιο και το προσθέτει στο κάθε Index της λίστας
for i in str(num):
    digit_lst.append(int(i))
if len(digit_lst) ==4:
    temp=digit_lst[0]
    digit_lst[0]=digit_lst[3]
    digit_lst[3]=temp
    print(digit_lst)
else:
    print('wrong number')