-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT ts.title, g.genre_id
  FROM tv_shows AS ts INNER JOIN tv_show_genres AS g
    ON ts.id = g.show_id
  ORDER BY ts.title, g.genre_id;
