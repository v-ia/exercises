/* Task: https://ibb.co/hFRz7CK */

SELECT article.id, article.text
FROM article
LEFT JOIN comment
ON article.id = comment.article_id
GROUP BY article.id
HAVING COUNT(comment.id) = 0
ORDER BY article.id;
