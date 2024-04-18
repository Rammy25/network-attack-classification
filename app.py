from flask import Flask, request, render_template
from markupsafe import escape
import numpy as np
import pickle
model = pickle.load(open("model.pkl",'rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        """
        to_predict_list = request.form.to_dict()
        print(to_predict_list
              )
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))

        print(to_predict_list)
        to_predict = np.array(to_predict_list).reshape(1, 26)
        """
        inputs = []
        for i in range(1, 27):  # Assuming you have 26 inputs
            input_value = request.form.get(f'input{i}', type=int)
            print("input",input_value)
            if input_value is None:
                return "Error: All fields are required.", 400
            inputs.append(input_value)

        to_predict = np.array(inputs).reshape(1, -1)
        predict = model.predict(to_predict)
        print("prediction:",predict)[0]
        return render_template("prediction.html", prediction_text = "network is -> {}".format(predict))
    else:
        return render_template("prediction.html")
    return


if __name__ == '__main__':
    app.run(debug=True)