# YGOPRODeck-Collection-2-Banlist-Converter
A tool to convert a YGOPRODeck .csv collection file to a banlist file for EDOPro/YGO Omega.

## How to Use
1. Download your collection as a .csv file from YGOPRODeck.
2. Run `python .\YGOPRODeckCollection2BanlistConverter.py .\collection.csv`, replacing `.\collection.csv` with the path to your downloaded collection.
3. A new file, `YGOPRODeckCollection.conf` will be created in the location where the script was run. Move it to the banlist folder of your application. (`ProjectIgnis\lflists` for EDOPro, `Duelists Unite\YGO Omega\YGO Omega_Data\Files\Banlists` for YGO Omega.)
