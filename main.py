from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)
    #anytime we make change to python code, going to rerun webserver 
    #turn off when running in production 
    #hi