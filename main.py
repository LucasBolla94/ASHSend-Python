import enviar_email


#Variables from Register
names = []
emails = []
mobile = []
bills_name = []
bills_value = []
bills_paid = []
bills_paid_total = 0
total_left_bill = 00.00
total_names = 0
total_bills = 0
bill_left_pay = 0
total_bills_worth = 0
bills_pp = 0
minpay = 85
full_left = 0


#Variables E-mail
sub = 'Statement Bills Home (14/08 | 20/08)'


# Function Variables to Register
def register_ipt():
    name_ipt = input('Whats the name ?   ')
    names.append(name_ipt)
    email_ipt = input('Whats the e-mail?  ')
    emails.append(email_ipt)
    print('Please put code of the country.')
    print('Ex +*** ***********')
    mobile_ipt = input('Whats the mobile number :  ')
    mobile.append(mobile_ipt)
    bills_left_ipt = input('This person have paid anythinh ?  £')
    bills_paid.append(bills_left_ipt)


#Don't change can stop work
def register():
    global total_names
    total_names_ipt = input('How many peoples you want register ?  ')
    total_names = int(total_names_ipt)
    for nt in range(0, total_names):
        register_ipt()


#Bills Inputs
def bills_ipt():
    bills_name_ipt = input('Whats this Bill name?  ')
    bills_name.append(bills_name_ipt)
    bills_value_ipt = input('How much worth this bill ?   £')
    bills_value.append(float(bills_value_ipt))


#Calculate All Bills worth
def calculate_total_bills():
    global total_bills_worth
    global bills_value
    len_bills = len(bills_value)
    for nt in range(0, len_bills):
        total_bills_worth = total_bills_worth + bills_value[nt]
        print(total_bills_worth)


#Calculate Each Person Bill
def calculate_bill_pp():
    global total_bills_worth
    global total_names
    global bills_pp
    bills_pp = total_bills_worth / total_names


#Don't change here
def bills():
    global total_bills
    total_bills_ipt = input('How many bills you want register ?  ')
    total_bills = int(total_bills_ipt)
    for nt in range(0, total_bills):
        bills_ipt()

    calculate_total_bills()
    calculate_bill_pp()


#Calculate How Much Paid Total
def calculate_bills_paid_total():
    global bills_paid_total
    global bills_paid
    global bill_left_pay
    lenpaid = len(bills_paid)
    for nt in range(0, lenpaid):
        bills_paid_total = bills_paid_total + bills_paid[nt]
        print(nt)
    bill_left_pay = total_bills_worth - bills_paid_total


#Enviar E-mail
def send_email():
    global total_names
    global sub
    global bills_paid
    global bills_pp
    global bills_paid_total
    for nt in range(0, total_names):
        name = names[nt]
        end_email = emails[nt]
        bill_pp = float(bills_paid[nt])
        bills_left_pp = bills_pp - bill_pp
        print(bills_left_pp)
        enviar_email.enviar_email(sub, end_email, name, total_bills_worth, bill_left_pay, bills_name, names, bills_paid, bills_pp, bills_left_pp,
         minpay)


register()
bills()
calculate_bills_paid_total()
send_email()

