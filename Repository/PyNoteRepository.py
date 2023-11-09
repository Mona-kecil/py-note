class PyNoteRepository:
    __dir = "client"
    notes = dict()

    def __init__(self, dir = "client"):
        self.__dir = dir
        print(f"PyNoteRepository: {self.__dir} created")

    def __str__(self):
        return f"Directory: {self.__dir}"
    
    # Save note to dir/author/title.txt and to notes Dictionary
    def save(self, note):
        pass

    # Delete note from dir/author/title.txt and from notes Dictionary
    def delete(self, note):
        pass

    # Get all notes title from notes Dictionary
    def getAll(self):
        pass