# from flask import Flask, redirect, url_for
# app = Flask(__name__)

# @app.route('/admin/')
# def hello_admin():
#    return 'Hello Admin'

# @app.route('/guest/<guest>/')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest

# @app.route('/user/<name>/')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))

# if __name__ == '__main__':
#    app.run(debug = True)

# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)

# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))

# if __name__ == '__main__':
#    app.run(debug = True)

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#    return '<html><body><h1>Hello World</h1></body></html>'

# if __name__ == '__main__':
#    app.run(debug = True)



'''
However, generating HTML content from Python code is cumbersome, 
especially when variable data and Python language elements like 
conditionals or loops need to be put. This would require frequent 
escaping from HTML.

This is where one can take advantage of Jinja2 template engine, 
on which Flask is based. Instead of returning hardcode HTML 
from the function, a HTML file can be rendered by the render_template() function.



Flask will try to find the HTML file in the templates folder, in the same folder in which this script is present.

-Application folder
   -Hello.py
   -templates
      -hello.html
'''


# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/hello/<user>/')
# def hello_name(user):
#    return render_template('hello.html', name = user)

# if __name__ == '__main__':
#    app.run(debug = True)




###############
# <!doctype html>
# <html>
#    <body>
#       {% if marks>50 %}
#          <h1> Your result is pass!</h1>
#       {% else %}
#          <h1>Your result is fail</h1>
#       {% endif %}
#    </body>
# </html>
# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/hello/<int:score>/')
# def hello_name(score):
#    return render_template('hello.html', marks = score)

# if __name__ == '__main__':
#    app.run(debug = True)




########################################
# <!doctype html>
# <html>
#    <body>
#       <table border = 1>
#          {% for key, value in result.items() %}
#             <tr>
#                <th> {{ key }} </th>
#                <td> {{ value }} </td>
#             </tr>
#          {% endfor %}
#       </table>
#    </body>
# </html>



# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/result/')
# def result():
#    dict = {'phy':50,'che':60,'maths':70}
#    return render_template('result.html', result = dict)

# if __name__ == '__main__':
#    app.run(debug = True)

# Here, again the Python statements corresponding to the For loop
# are enclosed in {%..%} whereas, the expressions key and value 
# are put inside {{ }}.





########################################
# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def index():
#    return render_template("index.html")

# if __name__ == '__main__':
#    app.run(debug = True)



from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)