FILEPATH="todo_auto.txt"
def get_act(filepath=FILEPATH):
    """this function reads the data from a text file
    located at a specified filepath"""
    with open(filepath, "r") as file_loc:
        actions_loc = file_loc.readlines()
        return actions_loc

def set_act(actions_loc, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(actions_loc)