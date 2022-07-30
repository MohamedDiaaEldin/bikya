from database import create_app

app = create_app()

@app.route('/')
def index():
    return 'hi from new app'