FP ="todos.txt"
def get_todos(filepath=FP):
    """Read a text file and return the list of to-do items."""

    with open(filepath, 'r') as file_local:
        Todos_local = file_local.readlines()
    return Todos_local

def write_todos(Todos_arg, filepath=FP ):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
         file.writelines(Todos_arg)