from flask import Flask
from controllers.student_controller import index, add_student

app = Flask(__name__, template_folder='views')

app.add_url_rule('/', 'index', index, methods=['GET'])
app.add_url_rule('/add', 'add_student', add_student, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)
