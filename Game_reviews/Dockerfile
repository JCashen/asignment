FROM python:3.7
WORKDIR /application
RUN pip install Flask Flask-SQLAlchemy Flask-WTF PyMySQL WTForms gunicorn
copy . .
ENV 'DATABASE_URI'='mysql+pymysql://root:Bungle_11@35.242.174.199/game_review' 
ENV 'SECRET_KEY'='SECRET_KEY'
RUN python create.py
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
