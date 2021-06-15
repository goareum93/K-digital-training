use tip;

-- # python_db.ipynb와 비교하는 것
-- SELECT total_bill FROM tip.tips where tip >= 7

-- SELECT * FROM tips;

-- SELECT total_bill, tip, smoker, time
-- FROM tips
-- LIMIT 5;

-- SELECT *, tip/total_bill as tip_rate
-- FROM tips
-- LIMIT 5;

-- SELECT *
-- FROM tips
-- WHERE time = 'Dinner'
-- LIMIT 5;

-- # tips of more than $5.00 at Dinner meals
-- SELECT *
-- FROM tips
-- WHERE time = 'Dinner' AND tip > 5.00;

-- # tips by parties of at least 5 diners OR bill total was more than $45
-- SELECT *
-- FROM tips
-- WHERE size >= 5 OR total_bill > 45;

-- # GROUP BY
-- SELECT sex, count(*)
-- FROM tips
-- GROUP BY sex;

-- SELECT day, AVG(tip), COUNT(*)
-- FROM tips
-- GROUP BY day

-- SELECT smoker, day, COUNT(*), AVG(tip)
-- FROM tips
-- GROUP BY smoker, day;
-- # GROUP BY smoker, day order by smoker; # ORDER BY 변수 -> 변수에 따라 sorting 시켜줌