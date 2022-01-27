import sys
sys.path.insert(0, "")


def main():
    from src.domain.note import NotesRepository, Note
    from src.domain.info import InfoRepository, Info

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="f5-my-notes-app2"))
    print("creando obj")

    nota1_compras = Note(title="Lista de la compra:", text="Pan y Chorizo")
    nota2 = Note(title='Bebidas', text='Vino y agua')
    print("obj creado")

    notes_repository = NotesRepository(database_path)
    print("repositorio notes hecho")
    notes_repository.save(nota1_compras)
    notes_repository.save(nota2)


main()
