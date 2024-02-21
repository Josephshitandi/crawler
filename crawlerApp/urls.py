from django.urls import path
from crawlerApp.views import scrape, news_list
urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', news_list, name="home"),
]