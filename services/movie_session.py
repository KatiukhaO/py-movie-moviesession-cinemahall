from datetime import datetime

from db.models import MovieSession


def create_movie_session(movie_show_time: str, movie_id: int,
                         cinema_hall_id: int):
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date: str = None):
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None):
    movie_session = MovieSession.objects.filter(id=session_id)

    if show_time:
        movie_session.update(show_time=show_time)
    if movie_id:
        movie_session.update(movie=movie_id)
    if cinema_hall_id:
        movie_session.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int):
    get_movie_session_by_id(session_id).delete()
