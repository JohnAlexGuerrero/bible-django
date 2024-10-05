from django.urls import path

from Person.views import PersonCreateView, PersonListView, PersonHomeView

urlpatterns = [
    path('', PersonHomeView.as_view(), name='person_home'),
    path('create/', PersonCreateView.as_view(), name='person_create'),
    path('list/', PersonListView.as_view(), name='person_list'),
    path('<str:pk>/update/', PersonListView.as_view(), name='person_update'),
]
