-- Script: List Shows by Rating
USE hbtn_0d_tvshows_rate;
SELECT tv_shows.title, SUM(ratings.rating) AS rating_sum
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating_sum DESC;
