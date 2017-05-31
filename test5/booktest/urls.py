from django.conf.urls import url
import views
urlpatterns=[
    url('^$',views.index ),
    url('^area1/$',views.area1),
    url('^area2/$', views.sheng),
    url('^area3/$',views.shi),
    url('^pic_upload/$',views.pic_upload),
    url('^pic_handle/$',views.pic_handle),
    url('^pic_show/$',views.pic_show),
    url(r'^page(?P<pIndex>[0-9]*)/$', views.page_test),
    url('^rich/$',views.rich),
    url('^rich_handle/$',views.rich_handle),
    url('^rich_show/$',views.rich_show),
    url('^query/$', views.query),
    url('^mail_test/$',views.mail_test),
    url('^sayhello/$', views.sayhello),

]
