from flask import Flask
from product_app.module_product.views import product

app=Flask(__name__)

#importar las vistas
app.register_blueprint(product)

def reverse_filter(s):
     return s[::-1]

def mydouble_filter(n:int):
    return n*2

app.jinja_env.filters['mydouble'] = mydouble_filter
app.jinja_env.filters['reverse_filter'] = reverse_filter