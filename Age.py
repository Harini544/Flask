from flask import Flask

app=Flask(__name__)

@app.route('/home/<int:age>')
def home(age):
    return "My age is: %d"%age;

if __name__=='__main__':
    app.run(debug=True,port=2024)