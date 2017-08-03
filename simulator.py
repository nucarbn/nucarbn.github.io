"""import datetime
now=datetime.datetime.now()
app(now)
"""
"""from flask import Flask,request
from flask import jsonify
app = Flask(__name__)
@app.route('/checking')
def test1():
    print 'in the test1 function'
    x = json.dumps({'abcd': 1234})
    requests.post('http://127.0.0.1:5000/sending', data = x)
    return 'checking done'

@app.route('/sending', methods= ['POST'])
def test2():
    print 'receiving data'
    request.data
    y = json.loads(request.data)
    print y
    return

if __name__ == '__main__':
    app.run(debug= True,host='0.0.0.0', port = 5000)"""
"""@app.route('/checking')
def test1():
    x = json.dumps({'abcd':'1234'})
    return redirect(url_for('test2', data=x))

@app.route('/sending/<data>')
def test2(data):
    print('receiving data')
    print(json.loads(data))
    return render_template('sending.html', data=data)"""


import random
from flask import Flask,requests
while(1):
    data=random.randint(1,100)
    #@app.route('http://127.0.0.1:5000/star/',x=data,methods=['POST'])
    return redirect('http://127.0.0.1:5000/star/',x=data)
