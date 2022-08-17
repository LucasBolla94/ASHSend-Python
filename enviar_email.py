import smtplib
import email.message

def enviar_email(sub, end_email, name, total_bills_worth, total_left_bill, bills_name, names, bills_paid, pp, bills_left_pp, minpay):
    corpo_email = """
    <p>Hello, {}</p>
    <p>The full bill is £{:.2f}</p>
    <p>Left Pay: £{}</p>
    <p>All names bills names is bellow :</p>
    <p>{}</p>
    <p>People have paid</p>
    <p>N:{}</p>
    <p>£:{}</p>
    <p>Bill per person is £{:.2f}</p>
    <p>Left you pay £{:.2f}</p>
    <p>Minimum Payment on Thursday 23:59 is £{:.2f}</p>
    <h4>Bank Account</h4>
	<p></p>
	<p></p>
	<p></p>
    """.format(name, total_bills_worth, total_left_bill, bills_name, names, bills_paid, pp, bills_left_pp, minpay)


    msg = email.message.Message()
    msg['Subject'] = sub
    msg['From'] = 'YOUR EMAIL'
    msg['To'] = end_email
    password = 'YOUR PASSWORD'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    #Login Credentials for send email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


