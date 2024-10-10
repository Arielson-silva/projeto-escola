from django.urls import path
from .views import lista_alunos, lista_cursos, lista_matriculas

urlpatterns = [
    path('aluno/', lista_alunos, name='lista_alunos'),
    path('curso/', lista_cursos, name='lista_cursos'),
    path('matriculas/', lista_matriculas, name='lista_matriculas'),
]
