from flask import Flask, render_template #bring in a website creator called flask
import flask

app = Flask(__name__) #create an instance of it to use. Always in a flask app. 

@app.route('/') #add after url
def home():
    return render_template('index.html')

@app.route('/contact')
def contact_me():
    return render_template('contact.html')

@app.route('/story')
def dance():
    return render_template('story.html')

@app.route('/features')
def photography():
    return render_template('features.html')

@app.route('/result', methods=['POST','GET'])
def result():
    '''Gets prediction using the HTML form'''
    return render_template('result.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/tips')
def shop():
    return render_template('tips.html')

@app.route('/video')
def video():
    return render_template('video.html')
   
if __name__ == '__main__':
    app.run(debug=True)

