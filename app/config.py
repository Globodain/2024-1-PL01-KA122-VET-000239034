import os
basedir = os.path.abspath(os.path.dirname(__file__))

from redis import Redis
redis_client = Redis(host='localhost', port=6379)

from pymongo import MongoClient

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["microblog"]  # Zastąp 'microblog' nazwą Twojej bazy danych
posts_collection = db["posts"]  # Kolekcja, która przechowuje posty

@app.route('/')
def index():
    posts = posts_collection.find()  # Pobiera dane z MongoDB
    
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    posts_collection.insert_one({"title": title, "content": content})  # Wstaw dane do MongoDB
    return redirect('/')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    POSTS_PER_PAGE = 25
