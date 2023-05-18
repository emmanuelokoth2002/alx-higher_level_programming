-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
USE hbtn_0d_tvshows;
SET @dexter_genre_id = (
  SELECT tv_show_genres.genre_id
  FROM tv_shows
  JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  WHERE tv_shows.title = 'Dexter'
  LIMIT 1
);
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
  SELECT genre_id
  FROM tv_show_genres
  WHERE show_id = @dexter_genre_id
)
ORDER BY tv_genres.name ASC;
