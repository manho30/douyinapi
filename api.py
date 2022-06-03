from flask import Flask, request, jsonify, make_response
from helper import findUrl
import configparser
from scraper import Douyin
import os

douyin = Douyin()

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
config = config['api']

@app.route("/", methods=["POST", "GET"])
def index():
    index_info = {
    'ok': True,
        'status': '200',
        'message': {
            'runing': True,
            'version': '1.0.0',
            'author': 'manho',
            'time': '2020/06/03',
            'msg': 'ads free, open source and free to use.'
        }
    }
    return jsonify(index_info)
    
@app.route("/api", methods=["POST", "GET"])
def api():
    if config['use_api'] == 'True':
        url = request.args.get('url')
        if url:
            vid_url = findUrl.find_url(url)[0]
            if url:
                try:
                    return jsonify(douyin.douyin(vid_url))
                except Exception as e:
                    return jsonify({
                        'ok': False,
                        'status': '500',
                        'message': f'Internal server error. {e}'
                    })
            else:
                return jsonify({
                    'ok': False,
                    'status': '400',
                    'message': 'url is not valid.'
                })
        else:
            return jsonify({
                'ok': False,
                'status': '400',
                'message': 'url is required.'
            })
    else:
        return jsonify({
            'ok': False,
            'status': '403',
            'message': 'api is disabled.'
        })
        
if __name__ == '__main__':
    # 开启WebAPI
    if os.environ.get('PORT'):
        port = int(os.environ.get('PORT'))
    else:
        # 默认端口
        port = config['port']
    app.run(host='0.0.0.0', port=port)