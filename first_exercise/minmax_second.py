# Δεύτερος τρόπος λύσης

#Δίνει ο χρήστης τον αριθμό
num=int(input("Give number"))

#Δημιουργεί μια κενή λίστα 
Lst_digit=[]
# Διαβάζει το κείμενο που έδωσε ο χρήστης , το μετατρέπει σε ακέραιο και μπαίνει σε κάθε index Της λίστας
for i in str(num):
    Lst_digit.append(int(i))


# Υπολογίζει το ελάχιστο και το μέγιστο και τα εμφανίζει
Min_digit=min(Lst_digit)
Max_digit=max(Lst_digit)

print(f"Min is: {Min_digit}")
print(f"Max is: {Max_digit}")