-- Script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT ts.title, g.genre_id
  FROM tv_shows AS ts LEFT JOIN tv_show_genres AS g
    ON ts.id = g.show_id
  ORDER BY ts.title, g.genre_id;
