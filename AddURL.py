from flask import Flask
app=Flask(__name__)


#add_url_rule(<url rule>, <endpoint>, <view function>)  

def about():
    return 'It is add URL'
app.add_url_rule('/about','about',about) #add /about in web browser after copying url

if __name__=='__main__':
    app.run(debug=True,port=2023)
