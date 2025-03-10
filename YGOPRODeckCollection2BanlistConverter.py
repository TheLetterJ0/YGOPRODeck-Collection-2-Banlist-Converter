import sys
import argparse
from pathlib import Path
import re

def main():
    args = sys.argv[1:]
    path = args[0]
    
    parser = argparse.ArgumentParser(description="A tool to convert a YGOPRODeck .csv collection file to a banlist file for EDOPro/YGO Omega.")
    parser.add_argument("path", help="The path to the collection.csv file to convert.")
    args = parser.parse_args()
    
    p = Path(args.path)
    newlist = Path(Path.cwd(), 'YGOPRODeckCollection.conf')
    
    if p.is_file():
        newfile = "!YGOPRODeck Collection\n$whitelist\n"
        with open(p) as file:
            for line in file:
                if "cardname,cardq" not in line:
                    id = int(line.split(',')[-2])
                    l = re.sub(r'^(.+?),(\d+),.*$', str(id) + r' \2 -- \1', line).replace('""','"')
                    newfile += l
        with open(newlist, 'w') as file:
            file.write(newfile)
    else:
        print("Could not find file", p)

if __name__=="__main__": 
    main() 