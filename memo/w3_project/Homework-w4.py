from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('w1.html')


## API 역할을 하는 부분
@app.route('/receiver', methods=['POST'])
def write_review():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    phone_receive = request.form['phone_give']
    address_receive = request.form['address_give']

    receive = {
       'name': name_receive,
       'number': number_receive,
       'phone': phone_receive,
       'address': address_receive
    }

    db.receiver.insert_one(receive)
    return jsonify({'result': 'success', 'msg': '성공적으로 작성되었습니다.'})


@app.route('/receiver', methods=['GET'])
def read_reviews():
    receiver = list(db.receiver.find({},{'_id':0}))
    return jsonify({'result': 'success', 'receiver': receiver})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)