from flask import Flask,render_template
zapp=Flask(__name__,template_folder='template')
@zapp.route('/')
def index():
    return render_template('index.html')
if __name__ =='__main__':
    zapp.run(debug=True)
