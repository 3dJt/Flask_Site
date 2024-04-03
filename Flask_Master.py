from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/contacts/")
def contacts():
    developer_name = "Ilon Mask"
    developer_address = "ул. Московская, д.2, кв.103"
    developer_phone = "88005553535"
    developer_email = "devemail@mail.ru"
    return render_template('contacts.html', name = developer_name, phone = developer_phone, address = developer_address, email = developer_email)

@app.route("/projects/")
def projects():
    return render_template('projects.html')

@app.route("/news/")
def news():
    return render_template('news.html')

if __name__ == "__main__":
    app.run(debug= True)