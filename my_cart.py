import psycopg2

def main():
    db_connection()

    str_login_type = input('Type "USER" for User Login OR "ADMIN" for Admin Login\n')

    if str_login_type.upper() == 'USER':
        db_user_choice()

    elif str_login_type.upper() == 'ADMIN':
        db_admin_choice()



def db_connection():
    global conn, cur
    try:
        conn = psycopg2.connect('dbname={} host={} user={} password={}'.format('db_my_cart', 'localhost', 'postgres', 'postgres'))
        cur = conn.cursor()
    except BaseException as msg:
        print('Exception = ', msg)
        print('connection failed')
        db_connection_close()


def db_user_choice():
    str_register = input('Already Registered Type "YES" OR "NO"\n')

    if str_register.upper() == 'YES':
        db_user_verification()

    elif str_register.upper() == 'NO':
        db_user_insertion()

    else:
        print('Wrong Choice')

def db_admin_choice():
    str_register = input('Already Registered Type "YES" OR "NO"\n')

    if str_register.upper() == 'YES':
        db_admin_verification()

    elif str_register.upper() == 'NO':
        db_admin_insertion()

    else:
        print('Wrong Choice')

    db_connection_close()



def db_product_insertion():
    prod_category = input('Type product category [Computer Accessories | Phone | Computer | Cloth | Footwear] \n')
    prod_brand = input('Type product brand\n')
    prod_name = input('Type product name \n')
    prod_amount = float(input('Type product amount \n'))

    try:
        cur.execute("INSERT INTO \"PRODUCT\"(category, brand, name, amount) VALUES ('{}', '{}', '{}', {})".format(prod_category, prod_brand,prod_name, prod_amount))
        conn.commit()
        insert_prod_choice = input('Insert More type "YES" or "NO"\n')

        if insert_prod_choice.upper() == 'YES':
            db_product_insertion()

        elif insert_prod_choice.upper() == 'NO':
            return
        else:
            print('Wrong Choice')


    except BaseException as msg:
        print('Exception = ', msg)
        db_connection_close()



def db_user_insertion():
    user_name = input('Enter UserName\n')
    user_email = input('Enter UserEmail\n')
    user_password = input('Enter UserPassword\n')

    user_choice = input('Type "YES" to Submit Or "NO" To Cancel\n')

    if user_choice.upper() == 'YES':
        try:
            cur.execute("INSERT INTO \"USER\"(name, email_id, password) VALUES('{}', '{}', '{}')".format(user_name, user_email, user_password))
            conn.commit()

            db_user_verification()

        except BaseException as msg:
            print('exception = ', msg)
            db_connection_close()



    elif user_choice.upper() == 'NO':
        pass

    else:
        print('Wrong Choice')


def db_admin_insertion():
    admin_email = input('Enter AdminEmail\n')
    admin_password = input('Enter AdminPassword\n')

    admin_choice = input('Type "YES" to Submit Or "NO" To Cancel\n')

    if admin_choice.upper() == 'YES':
        try:
            cur.execute("INSERT INTO \"ADMIN\"(email_id, password) VALUES('{}', '{}')".format(admin_email, admin_password))
            conn.commit()

            db_admin_verification()

        except BaseException as msg:
            print('exception = ', msg)
            db_connection_close()

    elif admin_choice.upper() == 'NO':
        pass

    else:
        print('Wrong Choice')

def db_user_verification():
    global user_id

    email_id = input('Enter EmailId\n')
    password = input('Enter Password\n')

    print('email_id = {}, password = {}'.format(email_id, password))

    try:
        cur.execute("SELECT * FROM \"USER\" WHERE email_id = '{}' AND password = '{}'".format(email_id, password))
        rows = cur.fetchall()

        if len(rows) > 0:
            user_id = rows[0][0]
            user_choices()

    except BaseException as msg:
        print('exception = ', msg)
        db_connection_close()

def db_admin_verification():

    email_id = input('Enter EmailId\n')
    password = input('Enter Password\n')

    print('email_id = {}, password = {}'.format(email_id, password))

    try:
        cur.execute("SELECT * FROM \"ADMIN\" WHERE email_id = '{}' AND password = '{}'".format(email_id, password))
        rows = cur.fetchall()

        if len(rows) > 0:
            ##admin verified
            print('Admin credentials verified')
            admin_choices()

        else:
            ##admin not verified
            print('Admin credentials not verified')

    except BaseException as msg:
        print('exception = ', msg)
        db_connection_close()


def admin_choices():
    str_admin_choice = input('Type "INSERT" to insert product, "CART" to view cart or "BILL" to view bill \n')

    if str_admin_choice.upper() == 'INSERT':
        db_product_insertion()
    elif str_admin_choice.upper() == 'CART':
        db_admin_cart()
    elif str_admin_choice.upper() == 'BILL':
        db_admin_bill()

    else:
        print('Wrong Choice')


def user_choices():
    str_view_all_products = input('Type "VIEW" to view all products \n')

    if str_view_all_products.upper() == 'VIEW':
        db_view_all_products()

    else:
        print('Wrong Choice')


def db_view_all_products():

    try:
        cur.execute('SELECT * FROM "PRODUCT" ')
        rows = cur.fetchall()

        categories = ['product_id', 'category', 'brand', 'name', 'amount' ]

        for each_category in categories:
            print(each_category, end=' | ')

        print()
        for each_row in rows:
            for each_elem in each_row:
                print(each_elem, end=' | ')

            print()

        str_filter_flag = input('Filter the product "YES" or "NO" \n')

        if str_filter_flag.upper() == 'YES':
            str_filter_expression = input(
                "filter the product by categories ['category' | 'brand' | 'name' | 'amount'] by writting expression\n")

            print("str_filter_expression = ", str_filter_expression)

            cur.execute("SELECT * FROM \"PRODUCT\" WHERE {}".format(str_filter_expression))
            rows = cur.fetchall()

            for each_category in categories:
                print(each_category, end=' | ')

            print()
            for each_row in rows:
                for each_elem in each_row:
                    print(each_elem, end=' | ')

                print()


        elif str_filter_flag.upper() == 'No':
            pass




        db_insert_to_cart()





    except BaseException as msg:
        print('exception = ', msg)
        db_connection_close()


def db_insert_to_cart():
    input_product_id = input('Type the "product_id" to add it to cart or "CHECKOUT" to checkout \n')

    try:
        cur.execute("SELECT * FROM \"PRODUCT\" WHERE product_id = {}".format(input_product_id))
        rows = cur.fetchone()
    
        cur.execute("INSERT INTO \"CART\"(user_id, product_id, product_cost)VALUES({}, {}, {})".format(user_id, rows[0], rows[4]))
        conn.commit()
    
        if len(rows) > 0:
            input_yes_no = input('Add other product to cart "YES" or "NO" \n')
    
            if input_yes_no.upper() == 'YES':
                db_insert_to_cart()
            elif input_yes_no.upper() == 'NO':
                user_checkout()
    
            else:
                print('Wrong Choice')
                
    except BaseException as msg:
        print('Exception = ', msg)
        db_connection_close()

def user_checkout():
    input_yes_no = input('For checkout type "YES" \n')
    
    try:
        if input_yes_no.upper() == 'YES':
            cur.execute("SELECT * FROM \"CART\" WHERE user_id = {} ".format(user_id))
            rows = cur.fetchall()
    
            total_cost = 0
            for each in rows:
                total_cost += each[3]
    
            cur.execute("DELETE FROM \"CART\" WHERE user_id = {}".format(user_id))
            conn.commit()
    
            if total_cost >= 10000.00:
                discount_cost = 500.00
    
    
            else:
                discount_cost = 0.00
    
            final_cost = float(total_cost) - discount_cost
    
    
            print('Amount Payable is-')
            print('Actual Amount = ', total_cost)
            print('discounted_amount = ', discount_cost)
            print('Final Amount = ', final_cost)
    
    
            cur.execute("INSERT INTO \"BILL\" (user_id, actual_amount, discounted_amount, final_amount) VALUES ({}, {}, {}, {})".format(user_id, total_cost, discount_cost, final_cost))
            conn.commit()
    
    
        else:
            pass

    except BaseException as msg:
        print('Exception = ', msg)
        db_connection_close()




def db_admin_cart():
    try:
        cur.execute("SELECT * FROM \"CART\" ")
        rows = cur.fetchall()
        categories = ['id', 'user_id', 'product_id', 'product_cost']
    
        for each_category in categories:
            print(each_category, end=' | ')
    
        print()
        for each_row in rows:
            for each_elem in each_row:
                print(each_elem, end=' | ')
    
            print()
            
    except BaseException as msg:
        print('Exception = ', msg)
        db_connection_close()


def db_admin_bill():
    try:
        cur.execute("SELECT * FROM \"BILL\" ")
    
        rows = cur.fetchall()
        categories = ['id', 'user_id', 'actual_amount', 'discounted_amount', 'final_amount']
    
        for each_category in categories:
            print(each_category, end=' | ')
    
        print()
        for each_row in rows:
            for each_elem in each_row:
                print(each_elem, end=' | ')
    
            print()


    except BaseException as msg:
        print('Exception = ', msg)

    db_connection_close()

def db_connection_close():
    conn.close()

if __name__ == '__main__':
    main()


