import csv

def read_names_from_csv(filename):
    
    names = []
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:  # boş satır yoksa
                names.append(row[0])
    return names
