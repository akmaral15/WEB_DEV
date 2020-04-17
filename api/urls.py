from django.urls import path


from api.views.views_generic import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView,\
    CompanyWithVacanciesListAPIView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [

    path('login/', obtain_jwt_token),

    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),

    path('companies/<int:pk>/vacancies/', CompanyWithVacanciesListAPIView.as_view()),

    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),
    # path('vacancies/top_ten/', TopVacanciesListAPIView.as_view())
]