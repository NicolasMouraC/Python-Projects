from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os.path

#-------------------- Information --------------------#
__author__ = 'Nicolas de Moura Carvalho'
__date__ = '06/23/2022'
__github__ = 'https://github.com/NicolasMouraC'

#-------------------- Server configuration --------------------#
# Flask an SQL database setup
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///Shows.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


# Edit form
class EditForm(FlaskForm):
    rating = StringField(label='Your rating out of 10', validators=[DataRequired()])
    review = StringField(label='Your review', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


# Add form
class AddForm(FlaskForm):
    show = StringField(label='Show', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


# Database class
class Shows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), unique=False, nullable=False)
    description = db.Column(db.String(350), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=True, default=0.0)
    ranking = db.Column(db.Integer, unique=False, nullable=True, default=0)
    review = db.Column(db.String(250), unique=False, nullable=True, default='')
    img_url = db.Column(db.String(250), unique=False, nullable=False)


# If the database don't exist, then it creates a new database
if not (os.path.exists('Shows.db')):
    db.create_all()
    new_show = Shows(
        title="Clannad",
        year=2007,
        description="Tomoya Okazaki is a third year high school student resentful of his life. His mother passed away from a car accident when he was younger, causing his father to resort to alcohol and cigarettes. This results in fights between the two until Tomoya's shoulder is injured in a fight. Since then, Tomoya has had distant relationships with his father, causing him to become a delinquent over time. While on a walk to school, he meets a strange girl named Nagisa Furukawa who is a year older, but is repeating due to illness. Due to this, she is often alone as most of her friends have moved on. The two begin hanging out and slowly, as time goes by, Tomoya finds his life shifting in a new direction. Anime based on a popular visual novel game.",
        rating=10,
        ranking=1,
        review='Author personal choice',
        img_url="https://www.themoviedb.org/t/p/original/bmugfsOLi5Q01nTsFkNwO0V4xgg.jpg"
    )
    db.session.add(new_show)
    db.session.commit()


#-------------------- Actual server --------------------#
# Home route
@app.route("/", methods=['POST', 'GET'])
def home():
    shows = db.session.query(Shows).order_by(Shows.rating).all()
    for i in range(len(shows)):
        shows[i].ranking = len(shows) - i
    return render_template("index.html", shows=shows)


# Edit route
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    show_id = request.args.get('id')
    show = Shows.query.get(show_id)
    if form.validate_on_submit():
        show.rating = form.rating.data
        show.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", show=show, form=form)


# Delete route
@app.route('/delete')
def delete():
    show_id = request.args.get('id')
    movie = Shows.query.get(show_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


# Add route
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        query = form.show.data
        api_parameters = {'api_key': 'af43112c88c6937884dff0ac22bbaee7',
                          'query': query,
                          'language': 'pt-BR',
                          'include_adult': 'true'}
        response = requests.get(url='https://api.themoviedb.org/3/search/tv', params=api_parameters)
        data = response.json()['results']
        return render_template('select.html', shows=data)
    return render_template('add.html', form=form)


# Select route
@app.route('/select', methods=['GET', 'POST'])
def select():
    new_show = Shows(
        title=request.args.get('name'),
        year=request.args.get('date'),
        description=request.args.get('description'),
        img_url=request.args.get('img')
    )
    db.session.add(new_show)
    db.session.commit()
    show_list = Shows.query.all()
    return redirect(url_for('edit', id=show_list[-1].id))


if __name__ == '__main__':
    app.run(debug=True)
