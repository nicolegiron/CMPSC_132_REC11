# Recitation Activity #11

# Enter your SQL query in the multiline string sqlStatement
# Do NOT modify the return statement

def answer():

    sqlStatement = '''
                    SELECT SKU, Pname, Price
                    FROM Product, Company
                    WHERE price < 200
                    AND CName = Manufacturer
                    AND Country = "Japan";
                   '''
    return sqlStatement
