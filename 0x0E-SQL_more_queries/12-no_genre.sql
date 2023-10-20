-- Script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT ts.title, g.genre_id
  FROM tv_shows AS ts LEFT JOIN tv_show_genres AS g
    ON ts.id = g.show_id
  WHERE g.show_id IS NULL
  ORDER BY ts.title, g.genre_id;
