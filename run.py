from product_app import app

app.config.from_object('configuration.DevelopmentConfig')
app.run(debug=True)