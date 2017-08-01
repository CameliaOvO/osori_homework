from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.article_table, name='article_table'),
	url(r'^test_board/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
	url(r'^test_board/new/$', views.article_new, name='article_new'),
	url(r'^test_board/(?P<pk>\d+)/edit/$', views.article_edit, name='article_edit'),
	url(r'^test_board/(?P<pk>\d+)/remove/$', views.article_remove, name='article_remove'),
	url(r'^test_board/(?P<pk>\d+)/comment/$', views.add_comment_to_article, name='add_comment_to_article'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]