# Δεύτερος τρόπος λύσης

# Δίνει ο χρήστης τον αριθμό
num=int(input("Give number"))
# Δημιουργεί κενή λίστα 
lst_digit=[]

# Υπολογίζει το κάθε ψηφίο ξεχωριστά
first_digit=num // 1000
second_digit=(num // 100) % 10
third_digit=(num // 10) % 10
last_digit=num %10 

# Προσθέτει στην λίστα τα στοιχεία. (Συμπληρώνει το τελευταίο στοιχείο στο πρώτο Index της λίστα και αντίστοιχα για το τελευταίο)
lst_digit.append(last_digit)
lst_digit.append(second_digit)
lst_digit.append(third_digit)
lst_digit.append(first_digit)

# Εκτυπώνει τα στοιχεία της λίστας
print(lst_digit)

    

