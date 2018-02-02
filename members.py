import pandas as pd
import sys

def etf(in_directory):
    df = pd.read_csv(in_directory) 
    df = df.loc[df['Confirmed'] == 'Yes']
    #df = df.drop(columns=['StudentID', 'ClubMemberID','Confirmed', 'Type', 'Active'])
    df = df[['Phone','First Name']]

    return df


def main(in_directory, out_directory):
    df = etf(in_directory)
    #print(df)
    df.to_csv(out_directory,  index = False)

if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)
