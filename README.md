# Modo de trabajo

Aqui esta el comienzo de como trabajar con las cohortes que recien comienzan:

Abrir git bash como administrador en el ordenador de escritorio, los comandos seran los siguientes:

```sh
cd tecnicatura
git init
git branch -M main
git branch Tecnicatura-git
mkdir Python
mkdir Javascript
mkdir Java
mkdir class-git
touch README.md
cd Python
mkdir Leccion01
mkdir Leccion02
mkdir Leccion03
mkdir Leccion04
cd Leccion01
touch clase1.py
cd ..
cd ..
git add
git commit
# Agregar el comentario desde VIM (o cualquier editor de texto de Git)
escape
:wq! + enter
# Generar todos los archivos de las lecciones en todas las carpetas de los diferentes lenguajes
# Pasar al repositorio en la nube desde GitHub Desktop
```