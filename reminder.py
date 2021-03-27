import csv
import pandas as pd

def writer_csv_file():
    with open("reminder_csv.csv", 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(['column1','column2','column3'])
        csv_writer.writerow(['row 1 col 1','row 1 col 2','row 1 col 3'])
        csv_writer.writerow(['row 2 col 1','row 2 col 2','row 2 col 3'])
        csv_writer.writerow(['row 3 col 1','row 3 col 2','row 3 col 3'])
        csv_writer.writerow(['row 4 col 1','row 4 col 2','row 4 col 3'])
        csv_writer.writerow(['row 5 col 1','row 5 col 2','row 5 col 3'])
        csv_writer.writerow(['row 6 col 1','row 6 col 2','row 6 col 3'])
def reader_csv_file():  
    with open("reminder.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            print(line['column1'],'| ',line['column2'])

def reader_csv_pandas():
    df = pd.read_csv(r'C:\Users\Rikky\telegram_bot\reminder_bot\reminder_csv.csv',header=0)
    print(df.iloc[1][1])
    print(df['column1'][1])

if __name__ =='__main__':
    reader_csv_pandas()
