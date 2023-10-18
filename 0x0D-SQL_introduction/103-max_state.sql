-- Script that displays the max temperature of each state (ordered by State name).
SELECT `state`, MAX(`value`)
FROM temperature
GROUP BY `stat`;
