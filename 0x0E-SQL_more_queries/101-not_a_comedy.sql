-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT(s.title)
  FROM tv_shows AS s LEFT JOIN tv_show_genres AS sg
    ON s.id = sg.show_id
  LEFT JOIN tv_genres AS g
    ON g.id = sg.genre_id
  WHERE s.title NOT IN (
    SELECT s.title
      FROM tv_shows AS s INNER JOIN tv_show_genres AS sg
        ON s.id = sg.show_id
      INNER JOIN tv_genres AS g
        ON g.id = sg.genre_id
      WHERE g.name = 'Comedy')
  ORDER BY s.title;

