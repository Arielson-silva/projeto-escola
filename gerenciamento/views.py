from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Aluno, Curso, Matricula

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {'cursos': cursos})

def lista_matriculas(request):
    matriculas = Matricula.objects.all()
    return render(request, 'lista_matriculas.html', {'matriculas': matriculas})