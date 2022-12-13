from app import app

if __name__ == "__main__":
    # 配置到產品的伺服器中，客戶端的電腦才能夠連接上網站的伺服器('0.0.0.0', debug=True)
    app.run(debug=True)
    # 要將應用程式部署到生產環境，一種選擇是使用 Waitress，即生產 WSGI 伺服器。
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)