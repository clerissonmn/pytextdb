import os
import csv

class TextDB:
    def __init__(self, path_to_db):
    
    if not path_to_db.endswith("_db"):
        raise ValueError("Diretorio do bd deve terminar com '_db")
    else:
        path_to_db=self.path_to_db
        
db = TextDB(path_to_db="../tests/teste")
        