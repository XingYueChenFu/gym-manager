import os  

basedir = os.path.abspath(os.path.dirname(__file__)) # 绝对路径

# ===== 配置基类 ===== 
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or r'mysql+pymysql://admin:HZtj4oZLe*MiA7y3@101.91.146.59/gym_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭对模型修改的监控
    SECRET_KEY='kdjklfjkd87384hjdhjh' # 用于加密 session 的密钥 可以换为其他字符串
    DEBUG = False
    JSON_AS_ASCII = False
    
    # 自定义参数
    RESET_DATABASE = False # 重置数据库
    HOST_IPV4 = '127.0.0.1'
    PORT = 5000
    

# ===== 开发环境配置 ===== 
class DevelopmentConfig(Config):  # 开发模式
    # RESET_DATABASE = True
    DEBUG = True

# ===== 测试环境配置 ===== 
class TestingConfig(Config):
    pass

# ===== 生产环境配置 ===== 
class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = { # 配置选项字典
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}  

    