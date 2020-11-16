# my_cart
## Python CLI

***

### Workflow
User Flow
 1. Add User
 2. User Authentication
 3. View all products
 4. Filter the product Single, Multiple Category
 5. Adding the  single/multiple product to cart by product_id.
 6. User Checkout
 7. Bil generation

Admin Flow
 1. Admin Authentication
 2. Insert a product
 3. View Cart
 4. View Bill

***

### Run

1. Run the code in any python IDE.<br />
2. Type "User" for User Login OR "Admin" for Admin Login.<br />
3. For Admin<br />
   1. Enter email_id and password for login.<br />
   2. Type "Insert" to insert product by-<br />
    * Typing the category from the given categories.
    * Typing the product brand.
    * Typing the product.
    * Typing the product cost.
   3. Type "Cart" to view the cart of different users.<br />
   4. Type "Bill" to view the bill of different users.<br />
4. For User<br />
   1. Registering the user for unregistered user.<br />
   2. Enter email_id and password for login.<br />
   3. Type "View" to view all products.<br />
   4. Filter by Single/Multiple categories by writting SQL WHERE clause Note-For '(single quote) escape the charater.<br />
   5. Adding Single/Multiple product to cart by typing corresponding product_id.<br />
   6. Checkout the cart.<br />
   7. Bill generation and removing of the product from user cart.<br />
   8. If Bill >= 10000.00 discoount of 500.00 is given   <br />
 
*** 
### DB
1. PostgreSQL used as a backend.<br />
2. DB credentials-<br />
  1. dbname - db_my_cart<br />
  2. host - localhost<br />
  3. user - postgres<br />
  4. password - postgres<br />
3. Schema - public<br />
4. Table-<br />
    1. "ADMIN"<br /><br />
       1. admin_id serial NOT NULL,
       2. email_id character varying(100),
       3. password character varying(50)
       
    2. "BILL"<br />
        1. id serial NOT NULL,
        2. user_id integer NOT NULL,
        3. actual_amount numeric(9,2) DEFAULT 0.0,
        4. discounted_amount numeric(9,2) DEFAULT 0.0,
        5. final_amount numeric(9,2) DEFAULT 0.0

    3. "CART"<br />
       1. id serial NOT NULL,
       2. user_id integer NOT NULL,
       3. product_id integer NOT NULL,
       4. product_cost numeric(9,2)

    4. "PRODUCT"<br />
       1. product_id serial NOT NULL,
       2. category character varying(50) NOT NULL,
       3. brand character varying(50) NOT NULL,
       4. name character varying(50) NOT NULL,
       5. amount numeric(6,2) NOT NULL

    5. "USER"<br />
       1. user_id serial NOT NULL,
       2. name character varying(50),
       3. email_id character varying(100),
       4. password character varying(50)


 	

