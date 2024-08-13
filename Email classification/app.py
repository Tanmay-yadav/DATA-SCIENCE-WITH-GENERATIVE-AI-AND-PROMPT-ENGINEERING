from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model and vectorizer
mnb = joblib.load('./models/multinomialnaivebayes.lb')
bow_obj = joblib.load('./models/countvectorizer.lb')

@app.route('templates\home.html', methods=['POST'])
def classify():
    email_message = request.form['email_message']
    # Transform the input message
    X = bow_obj.transform([email_message])
    prediction = mnb.predict(X)
    result = 'spam' if prediction[0] == 1 else 'ham'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
