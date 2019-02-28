# -*- coding: utf-8 -*-
import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

print("Quais são os três artigos mais populares de todos os tempos?")
print("-----------------------------------------------")
c.execute("SELECT articles.title, count(*) as num from articles, log where articles.slug = SPLIT_PART(path, '/', 3) group by articles.title order by num desc limit 3;")
top3 = c.fetchall()
for n in top3:
    print("{0} - {1} Views".format(n[0], n[1]))
print("------------------------------------------------")

print("Quem são os autores de artigos mais populares de todos os tempos?")
print("-----------------------------------------------")

c.execute("select authors.name, count(*) as num from authors, articles, log where authors.id = articles.author and articles.slug = SPLIT_PART(path, '/', 3) group by authors.name order by num desc;")
autors = c.fetchall()
for n in autors:
    print("{0} - {1} Views".format(n[0], n[1]))
print("------------------------------------------------")

print("Em quais dias mais de 1% das requisições resultaram em erros?")
c.execute("select to_char(time, 'FMMonth DD, YYYY') as date , ROUND(100*(CAST(SUM(CASE WHEN status='404 NOT FOUND' THEN 1 ELSE 0 END) AS decimal)/count(*)),2) as percentagem from log group by date having ROUND(100*(CAST(SUM(CASE WHEN status='404 NOT FOUND' THEN 1 ELSE 0 END) AS decimal)/count(*)),2) >1;")
erros = c.fetchall()
for n in erros:
    print("{0} - {1}% erros".format(n[0], n[1]))
print("------------------------------------------------")

db.close()