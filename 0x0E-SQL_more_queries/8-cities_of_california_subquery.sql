-- This is a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- This list is also ordered in ascending order
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
