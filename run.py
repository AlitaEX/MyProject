from app import app

if __name__ == "__main__":
    # 配置到產品的伺服器中，客戶端的電腦才能夠連接上網站的伺服器
    app.run('0.0.0.0', debug=True)