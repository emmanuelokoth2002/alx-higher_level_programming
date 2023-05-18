-- Script: List Shows Without Comedy Genre
USE hbtn_0d_tvshows;
SET @comedy_genre_id = (
  SELECT id
  FROM tv_genres
  WHERE name = 'Comedy'
  LIMIT 1
);
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
  SELECT show_id
  FROM tv_show_genres
  WHERE genre_id = @comedy_genre_id
)
ORDER BY tv_shows.title ASC;
