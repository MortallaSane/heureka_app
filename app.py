from flask import Flask, render_template
import urllib3 as url
import peewee as pw

app = Flask(__name__)
myDB = pw.MySQLDatabase("sql2319791", host="sql2.freemysqlhosting.net", port=3306, user="sql2319791", passwd="zA7!hG7%")


@app.route("/")
@app.route("/index")
def show_index():
    """
    main site, generating sections
    """
    title = "Homepage"
    
    sql_query = 'SELECT categoryId, title FROM category'
    output = myDB.execute_sql(sql_query)

    sections = dict(output)
    
    return render_template("index.html", title=title,sections = sections)


@app.route("/categories/<sectionNumber>")
def show_section(sectionNumber):  
    """
    view all products product with <sectionNumber>
    """
    
    sql_query = 'SELECT productId, title FROM product WHERE categoryId={}'.format(sectionNumber)
    sql_output = myDB.execute_sql(sql_query)

    items = dict(sql_output)

    sql_query = 'SELECT categoryId, title FROM category'
    output = myDB.execute_sql(sql_query)

    sections = dict(output)

    return render_template("categories.html", title="Homepage", items = items, sections = sections)


@app.route("/products/<productId>")
def show_product(productId):  
    sql_query = 'SELECT categoryId, title FROM category'
    output = myDB.execute_sql(sql_query)

    sections = dict(output)   
    return render_template("product.html", productId = productId, sections = sections)


@app.before_request
def before_request():
    myDB.connect()

@app.after_request
def after_request(response):
    myDB.close()
    return response