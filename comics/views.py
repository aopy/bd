# -*- coding: utf-8 -*-
from comics.models import Comics, Genre, Artist, Publisher, Article, Kind
from django.shortcuts import render

#from search import functions


def index(request):

    latest_comics = Comics.objects.order_by('-id')[:4]
    
    random_publishers = Publisher.objects.all().order_by('?')[:6]
    random_artists = Artist.objects.all().order_by('?')[:6]
    random_articles = Article.objects.all().order_by('?')[:6]

    return render(request, 'index.html',
                  {'latest_comics': latest_comics,
                   'random_publishers': random_publishers,
                   'random_artists': random_artists,
                   'random_articles': random_articles})


def comics_detail(request, name):

    name = name.replace('-', ' ')

    comics = Comics.objects.get(name=name)
    comics_name = comics.name

    comics_genre = Genre.objects.filter(comics__name=name)

    comics_info = comics.info

    comics_writer = comics.writer.all()
    comics_artist = comics.artist.all()

    comics_letterer = comics.letterer.all()
    comics_colorist = comics.colorist.all()
    comics_inker = comics.inker.all()
    comics_penciller = comics.penciller.all()
    comics_editor = comics.editor.all()

    comics_pub_date = comics.pub_date
    comics_publisher = comics.publisher

    comics_article = Article.objects.filter(comics__name=name)

    comics_pic = [comics.pic1, comics.pic2, comics.pic3, comics.pic4, comics.pic5]
    comics_link = comics.link

    return render(request, 'comics_detail.html',
                  {'comics_name': comics_name,
                   'comics_genre': comics_genre,
                   'comics_info': comics_info,
                   'comics_writer': comics_writer,
                   'comics_artist': comics_artist,
                   'comics_letterer': comics_letterer,
                   'comics_colorist': comics_colorist,
                   'comics_inker': comics_inker,
                   'comics_penciller': comics_penciller,
                   'comics_editor': comics_editor,
                   'comics_pub_date': comics_pub_date,
                   'comics_publisher': comics_publisher,
                   'comics_article': comics_article,
                   'comics_pic': comics_pic,
                   'comics_link': comics_link})


def artist_detail(request, name):

    name = name.replace('-', ' ')

    artist = Artist.objects.get(name=name)
    artist_name = artist.name
    artist_profession = artist.profession
    artist_bio = artist.bio
    artist_photo = artist.photo
    artist_website = artist.website

    artist_works = Comics.objects.filter(artist__name=name).order_by('-id')[:6]

    return render(request, 'artist_detail.html',
                  {'artist_name': artist_name,
                   'artist_profession': artist_profession,
                   'artist_bio': artist_bio,
                   'artist_photo': artist_photo,
                   'artist_works': artist_works,
                   'artist_website': artist_website})


def publisher_detail(request, name):

    name = name.replace('-', ' ')

    publisher = Publisher.objects.get(name=name)
    publisher_name = publisher.name
    publisher_info = publisher.info
    publisher_logo = publisher.logo
    publisher_website = publisher.website

    publisher_comics = Comics.objects.filter(publisher__name=name).order_by('-id')[:6]

    return render(request, 'publisher_detail.html',
                  {'publisher_name': publisher_name,
                   'publisher_info': publisher_info,
                   'publisher_logo': publisher_logo,
                   'publisher_comics': publisher_comics,
                   'publisher_website': publisher_website})


def article_detail(request, title):

    title = title.replace('-', ' ')

    article = Article.objects.get(title=title)
    article_title = article.title
    article_kind = article.kind
    article_text = article.text
    
    article_writer = Artist.objects.filter(article__title=title)

    article_pic = [article.pic1, article.pic2, article.pic3, article.pic4]
    article_source = article.source


    return render(request, 'article_detail.html',
                  {'article_title': article_title,
                   'article_kind': article_kind,
                   'article_text': article_text,
                   'article_writer': article_writer,
                   'article_pic': article_pic,
                   'article_source': article_source})


def show_news(request):

    try:
        latest_news = Article.objects.filter(kind__name="News").order_by('-id')[:1].get()

    except Article.DoesNotExist:
        latest_news = None  
    

    news_all = Article.objects.filter(kind__name="News").order_by('-id')

    #query_string, found_entries = functions.fts_search(request)

    return render(request, 'news.html',
                  {'latest_news': latest_news,
                   'query_string': query_string,
                   'found_entries': found_entries,
                   'news_all': news_all})


