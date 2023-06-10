import mysql.connector # a libray for connect sql to python

print('connecting to database...')
# connect to the your database 
cnx = mysql.connector.connect(host='127.0.0.2',database='get_info',
                              user='root',password='Aa09024193537$')

print('connected to database')
# a code to allow to change the database code
cursor = cnx.cursor()
# for get information from users
email_info = input('type your gmail : ')
pass_info = input('type your password : ')
data_users = (email_info , pass_info)

# for check email form is correct 
if '@' and '.' in email_info:
        add_info ="""INSERT INTO data(email , password)
              VALUES(%s , %s)"""
        cursor.execute(add_info , data_users)

        cnx.commit()

        print('data inserted.')

else:
        print('your gmail incorecct... ')        

# for close from database        
cnx.close()
