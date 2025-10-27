from utils.file_utils import read_names_from_csv
from utils.openspace import Openspace

def main():
 
    input_filepath = "new_colleagues.csv"
    
    names = read_names_from_csv(input_filepath)

    open_space = Openspace(number_of_tables=6)

    open_space.organize(names)

    
    open_space.store("output.csv")

   
    open_space.display()

if __name__ == "__main__":
    main()
