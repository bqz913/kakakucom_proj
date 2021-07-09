from flask import Flask, request, render_template, jsonify
from model import pc_spec

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:id>')
def catch_int(id):
    # request.args.get(クエリパラメータ、[デフォルト値]、[値の型])
    cpu = request.args.get('cpu', 0, type=int)
    gpu = request.args.get('gpu', 0, type=int)
    memory = request.args.get('memory', 0, type=int)
    disk = request.args.get('disk', 'ssd', type=str)
    disk_capacity = request.args.get('disk_capacity', 0, type=int)

    # jsonify({key:value}): 引数に与えられた辞書形式データをJsonに変換する。
    # またその際にheaderの"content-type"を'application/json'に変換してくれる。
    return jsonify({'result': cpu+gpu+memory})

@app.route('/<string:name>')
def catch_int(name):
    print(jsonify({request.args.get(name, 0, type=int)}))
    return jsonify({request.args.get(name, 0, type=int)})

@app.route('/<string:name>')
def catch_str(name):
    print(jsonify({request.args.get(name, '', type=str)}))
    return jsonify({request.args.get(name, '', type=str)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)