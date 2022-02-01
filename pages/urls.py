from django.urls import path
from .views import homePageView, HomePageView, AboutPageView


# url patter consist of:
# 1. a python regular expression. For empty string ""
# 2. a reference to the view, in our case called homePageView
# 3. an optional named URL pattern, in our case called home
# in other words if user requests the homepage represented by empty string ""
# django should use the view called homePageView


urlpatterns = [
    #path("", homePageView, name="home")
    path("", HomePageView.as_view(), name="home"),
    path("about/",AboutPageView.as_view(), name="about"),
]

