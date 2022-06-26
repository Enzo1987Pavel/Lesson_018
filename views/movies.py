from flask import request
from flask_restx import Resource, Namespace

from dao.model.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route("/")  # Показ всех фильмов
class MovieView(Resource):

    def get(self):  # Вывод всех фильмов
        schema = MovieSchema(many=True)

        movies = schema.dump(movie_service.get_movies(**request.args))
        return movies, 200

    def post(self):  # Добавление одного фильма
        new_movie = movie_service.create_movie(request.json)
        return "", 201, {"location": f"{movie_ns.path} / {new_movie.id}"}


@movie_ns.route("/<int:mid>")  # Отображение выбранного фильма по его 'id'
class MoviesView(Resource):
    schema = MovieSchema()

    def get(self, mid):
        return self.schema.dump(movie_service.get_movies(mid)), 200

    def put(self, mid):  # Выводим полные изменения в данных фильма
        return self.schema.dump(movie_service.update_movie(mid, request.json)), 201

    def patch(self, mid):  # Выводим частичные изменения в данных фильма
        return self.schema.dump(movie_service.partial_update(mid, request.json)), 200

    def delete(self, mid):  # Удаление фильма по его 'id'
        movie_service.delete_movie(mid)
        return "", 204
