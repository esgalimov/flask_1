from flask import Flask
from flask import url_for
from flask import request


app = Flask(__name__)


@app.route('/')
def mars():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return 'Человечество вырастает из детства. </br>' \
           ' Человечеству мала одна планета. </br>' \
           ' Мы сделаем обитаемыми безжизненные пока планеты.' \
           ' </br> И начнем с Марса! </br> Присоединяйся!'


@app.route('/image_mars')
def img():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')} alt="Картинка Марса">
                        <p>Вот она какая, красная планета!</p>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def prom_img():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
                            integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />

                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.jpg')}" alt="Картинка Марса">
                            <div class="alert alert-dark" role="alert">
                                Человечество вырастает из детства.
                            </div>
                            <div class="alert alert-success" role="alert">
                                Человечеству мала одна планета.
                            </div>
                            <div class="alert alert-warning" role="alert">
                                Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-info" role="alert">
                                И начнем с Марса!
                            </div>
                            <div class="alert alert-danger" role="alert">
                                Присоединяйся!
                            </div>
                          </body>
                        </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астранавтов</title>
                              </head>
                              <body>
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="surname" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                        <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control email-enter" id="email" placeholder="Введите почту" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас обзазование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Основное общее</option>
                                              <option>Среднее общее</option>
                                              <option>Среднее профессиональное</option>
                                              <option>Высшее образование</option>
                                            </select>
                                         </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules1" name="accept1">
                                            <label class="form-check-label" for="acceptRules1">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept2">
                                            <label class="form-check-label" for="acceptRules">Пилот</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept3">
                                            <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept4">
                                            <label class="form-check-label" for="acceptRules">Врач</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept5">
                                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept6">
                                            <label class="form-check-label" for="acceptRules">Специалист по радиационной защите</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept7">
                                            <label class="form-check-label" for="acceptRules">Киберинженер</label>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему хотите остаться на Марсе?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>

                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="ready">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('file'))
        print(request.form.get('why'))
        print(request.form.get('ready'))
        print(request.form.get('sex'))

        print('Инженер-исследователь', request.form.get('accept1'))
        print('Пилот', request.form.get('accept2'))
        print('Инженер-строитель', request.form.get('accept3'))
        print('Врач', request.form.get('accept4'))
        print('Экзобиолог', request.form.get('accept5'))
        print('Специалист по радиационной защите', request.form.get('accept6'))
        print('Киберинженер', request.form.get('accept7'))

        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-dark" role="alert">
                            <h3>Эта планета близка к Земле;</h3>
                        </div>
                        <div class="alert alert-success" role="alert">
                             <h3>На ней много необходимых ресурсов;</h3>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <h3>На не есть вода и атмосфера;</h3>
                        </div>
                        <div class="alert alert-info" role="alert">
                             <h3>На ней есть небольшое магнитное поле;</h3>
                        </div>
                        <div class="alert alert-danger" role="alert">
                             <h3>Наконец, она просто красива!</h3>
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                           integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                           crossorigin="anonymous">
                            <title>Результаты</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h2>Претендент на участие в миссии {nickname}:</h2>
                            <div class="alert alert-success" role="alert">
                                 <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                            </div>
                            <div class="alert alert-light" role="alert">
                                <h3>составляет {rating}!</h3>
                            </div>
                            <div class="alert alert-warning" role="alert">
                                 <h3>Желаем удачи!</h3>
                            </div>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
