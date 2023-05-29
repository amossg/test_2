from flask import Flask
from flask import render_template
from flask_restful import Api, Resource, reqparse
import json, subprocess, random, time

app = Flask(__name__)
api = Api()

somedata  = list(range(999))

io = open("/flask_sr/base/base.json", "r+")
string = io.read()
somedata = json.loads(string)
randomlist = []
parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("otherdata", type=int)


class Main(Resource):
    def get(self, somedata_id):
        if somedata_id == 0:
            io = open("/flask_sr/base/base.json", "r+")
            string = io.read()
            somedata = json.loads(string)
            return somedata
        else:
            io = open("/flask_sr/base/base.json", "r+")
            string = io.read()
            somedata = json.loads(string)
            return somedata[somedata_id]


    def delete(self, somedata_id):
        del somedata[somedata_id]
        with open('/flask_sr/base/base.json', 'w') as outfile:
            json.dump(somedata, outfile)
            return somedata


    def post(self, somedata_id):
        somedata[somedata_id] = parser.parse_args()
        with open('/flask_sr/base/base.json', 'w') as outfile:
            json.dump(somedata, outfile)
            return somedata


    def put(self, somedata_id):
        somedata[somedata_id] = parser.parse_args()
        with open('/flask_sr/base/base.json', 'w') as outfile:
            json.dump(somedata, outfile)
            return somedata

@app.route('/mem')
def mem_test():
    randomlist = []
    for i in range(0,331015543):
        n = random.randint(1,5544545545455463646444422)
        randomlist.append(n)
#time.sleep(10)
    print(randomlist)
#api.add_resource(Main, "/mem")

@app.route('/mem2')
def mem_test2():
    n = 10 ** 9
    alist = [0] * n
    time.sleep(100)


api.add_resource(Main, "/api/somedata/<int:somedata_id>", "/mem", "/mem2")
api.init_app(app)
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")

with open('/flask_sr/base/base.json', 'w') as outfile:
    json.dump(somedata, outfile)

