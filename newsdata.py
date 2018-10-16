#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def connect(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    db.close()
    return c.fetchall()
    


query1 = '''select title, count (*) as num from articles
join log on log.path = concat('/article/',articles.slug)
group by title order by
num desc limit 3;'''

query2 = '''select authors.name, count(*) as num from articles
join authors on authors.id = articles.author
join log on log.path = concat('/article/',articles.slug)
group by authors.name order by num desc limit 3;'''

query3 = '''select * from(select date(time) as Date,
round(100*sum(case log.status when '404 NOT FOUND'
then 1 else 0 end)/count(log.status),5)
as error from log  group by date(time)
order by error desc) as errTable where error > 1;'''


def print_query_articles(query):
    results = connect(query)
    print('\n1.The 3 most popular articles of all time are:\n')
    for result in results:
        print(str(result[0]) + ' ==> ' + str(result[1]) + ' views')


def print_query_authors(query):
    results = connect(query)
    print('\n2.The 3 most popular article authors of all time are:\n')
    for result in results:
        print(str(result[0]) + ' ==> ' + str(result[1]) + ' views')


def print_query_onePercent(query):
    results = connect(query)
    print('\n3.On which days did more than 1 percent of the requests lead to errors:\n')
    for result in results:
        print(str(result[0]) + ' ==> ' + str(result[1]) + ' %\n')


print_query_articles(query1)
print_query_authors(query2)
print_query_onePercent(query3)
