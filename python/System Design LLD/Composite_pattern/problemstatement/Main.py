from Directory import Directory
from File import File

if __name__ == "__main__":
    movie_directory = Directory("Movie")

    border = File("Border")
    movie_directory.add(border)

    comedy_movie_directory = Directory("ComedyMovie")
    hulchul = File("Hulchul")
    comedy_movie_directory.add(hulchul)
    movie_directory.add(comedy_movie_directory)

    movie_directory.ls()
