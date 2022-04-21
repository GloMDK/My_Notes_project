from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesListView.as_view(), name='home1'),
    path('add_note/', views.NotesCreateView.as_view(), name='add_note'),
    path('update_note/<pk>', views.NoteUpdateView.as_view(), name='upd_note'),
    path('delete_note/<pk>', views.NoteDeleteView.as_view(), name='del_note'),
]
