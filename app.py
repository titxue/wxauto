from flask import Flask

app = Flask(__name__)




@app.route('/',methods=['POST','GET'])
def wechat():
    return render_template('ss')


@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了哈哈哈'

@app.errorhandler(404)
def internal_server_error(e):
    return '瞎请求什么路径呢'

if __name__ == '__main__':
    app.run(debug=False,port=5500,host="0.0.0.0")
