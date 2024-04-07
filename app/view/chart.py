import os
import calendar
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
# import matplotlib.ticker as ticker
from flask import current_app
from sqlalchemy import func
from app.models import db, Product, Link, Dates

range = 10

def getChartAll():
    for x in ['web','ig','fb']:
        links = db.session.query(Dates.date, func.count().label('link_count')).filter(Dates.platform == x).group_by(Dates.date).all()
        indexX = [link.date for link in links]
        indexY = [link.link_count for link in links]
        plt.bar(indexX,indexY)
        # plt.plot(indexX,indexY, marker='o')
        plt.gca().set_ylim(0, range)
        plt.xlabel('date')
        plt.ylabel('count')
        plt.title(f'jumlah click {x}')
        filepath = os.path.join(current_app.config['CHART_FOLDER'], f'{x}_chart.png')
        plt.savefig(filepath)
        plt.clf()

def getChartCustomAll(date1, date2, title):
    date1f = datetime.strptime(date1, '%Y-%m-%d')
    date2f = datetime.strptime(date2, '%Y-%m-%d')
    fDate1 = date1f.strftime('%d-%m-%Y')
    fDate2 = date2f.strftime('%d-%m-%Y')
    for x in ['web','ig','fb']:
        links = db.session.query(Dates.date, func.count().label('link_count')).filter(Dates.platform == x, Dates.date.between(fDate1,fDate2)).group_by(Dates.date).all()
        indexX = [link.date for link in links]
        indexY = [link.link_count for link in links]
        plt.bar(indexX,indexY)
        # plt.plot(indexX,indexY, marker='o')
        plt.gca().set_ylim(0, range)
        plt.xlabel('date')
        plt.ylabel('count')
        if title is not None:
            plt.title(f'jumlah click {x} antara {title}')
        else:
            plt.title(f'jumlah click {x} antara {fDate1} dan {fDate2}')
        filepath = os.path.join(current_app.config['CHART_FOLDER'], f'{x}_chart.png')
        plt.savefig(filepath)
        plt.clf()

def getChartWeekAll():
    today = datetime.now().date()
    daysAgo = today + timedelta(days=-7)
    daysAgoStr = daysAgo.strftime('%Y-%m-%d')
    todayStr = today.strftime('%Y-%m-%d')
    getChartCustomAll(date1=todayStr,date2=daysAgoStr,title='seminggu lalu')

def getChartMonthAll():
    date = getMonthDate()
    todayStr = date[0]
    daysAgoStr = date[1]
    getChartCustomAll(date1=todayStr,date2=daysAgoStr,title='sebulan lalu')

def getChartYearAll():
    today = datetime.now().date()
    daysAgo = today + timedelta(days=-365)
    daysAgoStr = daysAgo.strftime('%Y-%m-%d')
    todayStr = today.strftime('%Y-%m-%d')
    getChartCustomAll(date1=todayStr,date2=daysAgoStr,title='setahun lalu')

def getChartProduct(id):
    product = Product.query.filter_by(id=int(id)).first()
    for x in ['web','ig','fb']:
        links = db.session.query(Dates.date, Product.id, func.count().label('link_count')).\
            join(Link, Dates.id_link == Link.id).\
            join(Product, Link.id_product == Product.id).\
            filter(Dates.platform == x, Product.id == int(id)).\
            group_by(Dates.date).all()
        indexX = [link.date for link in links]
        indexY = [link.link_count for link in links]
        plt.bar(indexX,indexY)
        # plt.plot(indexX,indexY, marker='o')
        plt.gca().set_ylim(0, range)
        plt.xlabel('date')
        plt.ylabel('count')
        plt.title(f'jumlah click {x} {product.title}') 
        filepath = os.path.join(current_app.config['CHART_FOLDER'], f'{x}_chart.png')
        plt.savefig(filepath)
        plt.clf()

def getChartCustom(date1, date2, title, id):
    product = Product.query.filter_by(id=int(id)).first()
    date1f = datetime.strptime(date1, '%Y-%m-%d')
    date2f = datetime.strptime(date2, '%Y-%m-%d')
    fDate1 = date1f.strftime('%d-%m-%Y')
    fDate2 = date2f.strftime('%d-%m-%Y')
    for x in ['web','ig','fb']:
        links = db.session.query(Dates.date, Product.id, func.count().label('link_count')).\
            join(Link, Dates.id_link == Link.id).\
            join(Product, Link.id_product == Product.id).\
            filter(Dates.platform == x, Product.id == int(id), Dates.date.between(fDate1,fDate2)).\
            group_by(Dates.date).all()
        indexX = [link.date for link in links]
        indexY = [link.link_count for link in links]
        plt.bar(indexX,indexY)
        # plt.plot(indexX,indexY, marker='o')
        plt.gca().set_ylim(0, range)
        plt.xlabel('date')
        plt.ylabel('count')
        if title is not None:
            plt.title(f'jumlah click {x} {product.title} antara {title}')
        else:
            plt.title(f'jumlah click {x} {product.title} antara {fDate1} dan {fDate2}')
        filepath = os.path.join(current_app.config['CHART_FOLDER'], f'{x}_chart.png')
        plt.savefig(filepath)
        plt.clf()

def getChartWeek(id):
    today = datetime.now().date()
    daysAgo = today + timedelta(days=-7)
    daysAgoStr = daysAgo.strftime('%Y-%m-%d')
    todayStr = today.strftime('%Y-%m-%d')
    getChartCustom(date1=todayStr,date2=daysAgoStr,title='seminggu lalu', id=id)

def getChartMonth(id):
    date = getMonthDate()
    todayStr = date[0]
    daysAgoStr = date[1]
    print(daysAgoStr)
    print(todayStr)
    getChartCustom(date1=todayStr,date2=daysAgoStr,title='sebulan lalu',id=id)

def getChartYear(id):
    today = datetime.now().date()
    daysAgo = today + timedelta(days=-365)
    daysAgoStr = daysAgo.strftime('%Y-%m-%d')
    todayStr = today.strftime('%Y-%m-%d')
    getChartCustom(date1=todayStr,date2=daysAgoStr,title='setahun lalu', id=id)

def getMonthDate():
    today = datetime.now().date()
    month = today.month - 1 
    year = today.year
    last = calendar.monthrange(year, month)[1]
    return [f'{year}-{month:02d}-01',f'{year}-{month:02d}-{last}']