import mysql.connector

# creating the copy command

def sql_connector(filename):

    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ravi1997"
    )

    mycursor = my_db.cursor(dictionary=True)

    mycursor.execute("USE LEARNING_DB")
    mycursor.execute('SELECT * FROM EDP_INGRESS_PARM WHERE SOURCE_FILENAME ="{0}"'.format(filename))

    myresult = mycursor.fetchone()

    return myresult
