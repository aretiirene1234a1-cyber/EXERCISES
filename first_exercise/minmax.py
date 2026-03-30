#Δίνει ο χρήστης τον αριθμό
num=int(input("Give number"))

#Δημιουργεί μια κενή λίστα 
digit=[]
# Όσο ο υπάρχουν ψηφία του αριθμού (διάφορα του μηδενός) συμπληρώνει τα στοιχεια στην λίστα 
while num != 0: 
     last_digit = num % 10
     num //= 10
     digit.append(last_digit)

# υπολογιζει το ελάχιστο και το μέγιστο και τα εμφανίζει 
Min_digit=min(digit)
Max_digit=max(digit)
print(f"Min is:{Min_digit}")
print(f"Max is:{Max_digit}")