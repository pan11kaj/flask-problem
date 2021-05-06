from flask import Flask,jsonify
import csv,pandas;

all_movies = []
with open("movies.csv") as f:
    reader_data = csv.reader(f)
    data   = list(reader_data)
    all_movies = data[1:]
like_movies = []
dislike_movies = []
not_watched_movies = []

app = Flask(__name__)
@app.route('/get-movie')

def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":'success'
    })
@app.route("/liked-movie",methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    like_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unliked-movie",methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    dislike_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did-not-watch",methods = ["POST"])
def did_not_watch_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_watch_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()