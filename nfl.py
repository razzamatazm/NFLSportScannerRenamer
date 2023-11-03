import re
import os
import pandas as pd
from collections import defaultdict
from team_mapping import get_team_mapping

#Here are the folders for you to set. folder_to_search is your misnamed files while move_to_folder is where you want your renamed files to go. 

# Folder to search for files to rename
folder_to_search = '/volume2/Synology2/Media/TV/Test/'

# Folder to move the renamed files to
move_to_folder = '/volume2/Synology2/Media/TV/NFL/2023/'


# Load the DataFrame from the CSV file
df = pd.read_csv('NFLScheduleFinal.csv')

# Mapping of team abbreviations and variations to their formal names
team_mapping = get_team_mapping()

# Function to rename NFL game videos
def rename_nfl_files(week_number):
    # Filter the DataFrame by the given week
    filtered_games = df[df['Week'] == week_number]

    # List all files in the folder
    all_files = os.listdir(folder_to_search)
    
    # Prepare regex patterns
    pattern1 = re.compile(r'[-_]*([A-Za-z0-9]{2,15})[@]([A-Za-z0-9]{2,15})[-_]*')
    pattern2 = re.compile(r'NFL\.\d{4}-\d{2}-\d{2}\.(.*?)\.vs\.(.*?)\.[mkv|ts|mp4]')
    pattern3 = re.compile(r'(.*?) at (.*?) \d{2}\.\d{2}\.\d{2}')
    pattern4 = re.compile(r'\d{4}\.\d{2}\.\d{2}\.([a-zA-Z0-9]+)\.vs\.([a-zA-Z0-9]+)')

    # Prepare dictionary to hold original and new filenames
    rename_dict = defaultdict(str)
    
    # Loop through all files in the folder
    for file_name in all_files:
        matched = False

        for idx, row in filtered_games.iterrows():
            away_team_formatted = row['Away Team'].replace(' ', '.')
            home_team_formatted = row['Home Team'].replace(' ', '.')
            game_day = pd.to_datetime(row['Game Day']).strftime('%Y-%m-%d')

            # Try the first pattern
            match = pattern1.search(file_name)
            
            # If no match, try the second pattern
            if not match:
                match = pattern2.search(file_name)
                
            # If still no match, try the third pattern
            if not match:
                match = pattern3.search(file_name)

            # If still no match, try the third pattern
            if not match:
                match = pattern4.search(file_name)
           
            if match:
                away_match_str, home_match_str = match.groups()
                away_match = team_mapping.get(away_match_str, away_match_str.replace(" ", "."))
                home_match = team_mapping.get(home_match_str, home_match_str.replace(" ", "."))

                # Directly use the found match
                away_team_to_use = away_match
                home_team_to_use = home_match

                if away_team_to_use == away_team_formatted and home_team_to_use == home_team_formatted:
                    # Extract file extension
                    file_ext = file_name.split('.')[-1]
                    # Generate new name
                    new_name = f'NFL.{game_day}.{home_team_formatted}.vs.{away_team_formatted}.{file_ext}'
                    rename_dict[file_name] = new_name
                    matched = True
                    break
                
        if not matched:
#            print(f"Unmatched file: {file_name}")

            # Swapping home and away teams
            for idx, row in filtered_games.iterrows():
                away_team_formatted = row['Home Team'].replace(' ', '.')
                home_team_formatted = row['Away Team'].replace(' ', '.')
                game_day = pd.to_datetime(row['Game Day']).strftime('%Y-%m-%d')

                match = pattern1.search(file_name)
                if not match:
                    match = pattern2.search(file_name)
                if not match:
                    match = pattern3.search(file_name)
                if not match:
                    match = pattern4.search(file_name)                

                if match:
                    away_match_str, home_match_str = match.groups()
                    away_match = team_mapping.get(away_match_str, away_match_str.replace(" ", "."))
                    home_match = team_mapping.get(home_match_str, home_match_str.replace(" ", "."))

                    if away_match == away_team_formatted and home_match == home_team_formatted:
                        file_ext = file_name.split('.')[-1]
                        new_name = f'NFL.{game_day}.{away_team_formatted}.vs.{home_team_formatted}.{file_ext}'
                        rename_dict[file_name] = new_name
                        matched = True
                        break

            if not matched:
                print(f"Unmatched Files: {file_name}")


    # Print and confirm the renaming
    print("Files to be renamed:")
    for original, new in rename_dict.items():
        print(f"{original} -> {new}")

    confirm = input("Do you want to proceed with renaming? (y/n): ")
    if confirm.lower() == 'y':
        for original, new in rename_dict.items():
            os.rename(os.path.join(folder_to_search, original), os.path.join(move_to_folder, new))
        print("Files renamed successfully.")
    else:
        print("Renaming cancelled.")

# Get the week number from the user
week_number = int(input("Enter the NFL week number: "))
rename_nfl_files(week_number)
