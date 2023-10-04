# Introducing NFLSportScannerRenamer: A Seamless Way to Rename Your NFL Game Files

Do you love using [SportScanner](https://github.com/mmmmmtasty/SportScanner/tree/master) for its incredible game data scraping capabilities but dread the manual labor involved in naming those NFL game files? Say no more; I've got you covered!

## How Does It Work?

My Python script, aptly named **NFLSportScannerRenamer**, aims to streamline this process significantly. Configure a couple of straightforward variables in the `nfl.py` file—specify the folder where your game files are located and designate the destination folder for the renamed files. That's it for setup!

Once you run the script, it will prompt you for the NFL game week number. The magic happens next: the script will attempt to intelligently match your files with the games from that specific week. After matching, you'll get a neat summary along with a confirmation prompt to proceed with the renaming.

## A Couple of Quick Notes:

1. **Plex Library Sorting**: To ensure SportScanner detects your files, make sure to follow the specific folder structure (`/NFL/2023/FILES...`). The SportScanner GitHub repository has comprehensive guidelines on this.
   
2. **SportScanner Setup**: The initial setup for SportScanner involves manual installation of some scanners. The onus is on you to follow the setup guidelines.

3. **Dependencies**: This script relies on the Python package `pandas`. To get up and running, place all the script files in one directory and execute `pip install pandas`.

## Need Help?

If you encounter any files that aren't getting picked up by the scanner, feel free to reach out. I'm committed to enhancing the script's logic to accommodate as many file formats as possible.

So, ready to make your SportScanner experience even more seamless? Give NFLSportScannerRenamer a try!
