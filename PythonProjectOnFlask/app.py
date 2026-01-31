from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/autorize')

def autorize(): # это авторизация, здесь блог регистации/авторизации
    return render_template('autorize.html')

@app.route('/autorize/registration')

def reg():  # это регистрация
    return render_template('registration.html')

@app.route('/popular') # популярное
@app.route('/')

def popular():
    return render_template('popular.html')
@app.route('/menu')

def menu(): # это меню, и блок с учениками
    return render_template('menu.html')

@app.route('/orders') # это заказы

def orders():
    return render_template('orders.html')

@app.route('/orders/purchase') # это заказы, часть 2 с оплатой заказа

def orders2():
    return render_template('orders2.html')

@app.route('/orders/purchase/success') # это заказы, часть 2 с оплатой заказа

def orders3():
    return render_template('orders3.html')

@app.route('/grades') # это оценка блюд

def grades():
    return render_template('grades.html')

@app.route('/money') # это баланс

def money():
    return render_template('money.html')

@app.route('/recommendations') # это рекоммендации

def recomm():
    return render_template('recomm.html')

@app.route('/change') # это смена класса взаимодействия, не нужно редактировать в html, это временная мера
def change():
    return render_template('change.html')

@app.route('/chef/dishcheck') # здесь начинается раздел поваров, это учёт выданных завтраков и обедов

def dishuct_check():
    return render_template('dish_check.html')

@app.route('/chef/checkstocks') # это контроль остатков блюд и продуктов

def check_stocks():
    return render_template('check_stocks.html')

@app.route('/chef/procurement') # это закупки продуктов

def procurement():
    return render_template('procurement.html')

@app.route('/administrator/stats') # здесь начинается раздел админов, это просмотр статиски, оплат и посещаемости

def stats():
    return render_template('stats.html')

@app.route('/administrator/procurementapprove') # это согласование заявок на закупки

def procurement_approve():
    return render_template('procurement_approve.html')

@app.route('/administrator/report') # это формирование отчётов

def report():
    return render_template('report.html')

@app.route('/administrator/add') # это назначение поваров и админинов

def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)