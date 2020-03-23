import pandas as pd
class file_reader (object):
    
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.read_excel(filename)
        self.products = self.df[self.df.columns[0:1]]





def main():
    fr = file_reader("hussmann.com.xlsx")
    print(fr.filename)
    first_col = fr.df[fr.df.columns[0:1]]

    
if __name__ == "__main__":
    main()

