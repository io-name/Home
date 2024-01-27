# -*- coding: utf-8 -*-
# рабочий цикл flask-а

import pages
from flask import Flask
from flask import render_template
from flask import request
# from flask import url_for

app = Flask(__name__, "/static")
    
# Сборка страниц
main = pages.Index()
login = pages.Login()
help = pages.Help()

@app.route("/",)
def index_():
    # main.update() #обновление данных в элементе класса
    return render_template(main.template,
                           title = main.title,
                           info = main.info,
                           temp = main.temp)
    
@app.route("/login")
def login_():
    # if request.method == "POST":
    #     username = request.form['username']
    #     password = request.form['password']
    #     return "Вы вошли в систему"
    # else:
    return render_template(login.template,
                            title = login.title,
                            info = login.info)
        
        
@app.route("/help")
def help_():
    return render_template(help.template,
                           title = help.title,
                           info = help.info)

@app.route("/temperature_deploy", methods=["GET", "POST"])
def temperature_deploy():
    temp = request.args.get("temp")
    main.temp = temp
    return temp

if __name__ == "__main__":
    app.run(debug=False, host="192.168.88.50", port="80")