-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT s.title, SUM(r.rate) AS 'rating'
  FROM tv_shows AS s LEFT JOIN tv_show_ratings AS r
    ON s.id = r.show_id
  GROUP BY s.title
  ORDER BY `rating` DESC;
