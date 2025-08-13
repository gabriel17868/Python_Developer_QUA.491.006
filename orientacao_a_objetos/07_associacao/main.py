import Curso
import Aluno

def main():
    # Instancia objetos das classes
    curso1 = Curso.Curso(nome_curso="Python")
    curso2 = Curso.Curso(nome_curso="Java")

    aluno1 = Aluno.Aluno(nome_aluno="Gabriel Maraschin", matricula="1")
    aluno2 = Aluno.Aluno(nome_aluno="Alex Machado", matricula="2")
    aluno3 = Aluno.Aluno(nome_aluno="Paulo Ribeiro", matricula="3")
    aluno4 = Aluno.Aluno(nome_aluno="Amanda Carvalho", matricula="4")
    aluno5 = Aluno.Aluno(nome_aluno="Jessica Arruda", matricula="5")
    aluno6 = Aluno.Aluno(nome_aluno="Geovane Folleto", matricula="6")

    # Inscrevendo alunos no curso 1
    aluno1.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso1)
    aluno3.inscrever_curso(curso1)
    aluno4.inscrever_curso(curso1)

    # Inscrevendo alunos no curso 2
    aluno5.inscrever_curso(curso2)
    aluno6.inscrever_curso(curso2)

    # lista de alunos do curso 1
    print(f"Curso: {curso1.nome_curso}")
    print("Lista de alunos:")
    for aluno in curso1.listar_alunos():
        print(aluno)

    print(f"{'-'*40}")
    # lista de alunos do curso 2
    print(f"Curso: {curso2.nome_curso}")
    print("Lista de alunos:")
    for aluno in curso2.listar_alunos():
        print(aluno)


if __name__ == "__main__":
    main()