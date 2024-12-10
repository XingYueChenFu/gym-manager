import os
from gym_manager import create_app
from flask import render_template, jsonify, g
from config import config

used_config = config['default']

# 创建应用
app = create_app(used_config)

# 捕获所有404并处理
@app.errorhandler(404)
def page_not_found(error):
    # 前端可以自行在得到状态码后，渲染404页面。而不是直接使用我返回的html页面
    return render_template('errors/404.html'), 404

app.run(debug=True, host=used_config.HOST_IPV4, port=used_config.PORT)
