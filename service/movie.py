from dao.movie import MovieDAO


class MovieService:
	def __init__(self, movie_dao: MovieDAO):
		self.movie_dao = movie_dao

	# Вывод фильма всех или при наличии 'id' - фильма с указанным 'id'
	def get_movies(self, mid=None, **kwargs):
		return self.movie_dao.get(mid, **kwargs)

	def create_movie(self, data):
		return self.movie_dao.create(data)

	def update_movie(self, mid, data):  # Выводим полные изменения в данных фильма
		edit_all_movie = self.get_movies(mid)

		edit_all_movie.title = data["title"]
		edit_all_movie.description = data["description"]
		edit_all_movie.trailer = data["trailer"]
		edit_all_movie.year = data["year"]
		edit_all_movie.rating = data["rating"]
		edit_all_movie.genre_id = data["genre_id"]
		edit_all_movie.director_id = data["director_id"]
		self.movie_dao.update(edit_all_movie)

		return edit_all_movie

	def partial_update(self, mid, data):
		movie = self.get_movies(mid)

		if "title" in data:
			movie.title = data["title"]
		elif "description" in data:
			movie.description = data["description"]
		elif "trailer" in data:
			movie.trailer = data["trailer"]
		elif "year" in data:
			movie.year = data["year"]
		elif "rating" in data:
			movie.rating = data["rating"]
		elif "genre_id" in data:
			movie.genre_id = data["genre_id"]
		elif "director_id" in data:
			movie.director_id = data["director_id"]

		self.movie_dao.update(movie)  # обновляем данные фильма

		return movie

	def delete_movie(self, mid):
		self.movie_dao.delete(mid)

	def filter(self, **filter_param):
		pass
