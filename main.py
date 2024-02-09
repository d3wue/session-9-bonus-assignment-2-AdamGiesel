import requests
import bs4

userAgent = { 
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

while True:
    print("Press 1 to show all football teams from the Bundesliga")
    print("Press 2 to select a team to show high level information on the team")
    print("Press 3 to select a team to show all players from the team and their market value")
    print("Press 4 to stop the program")
    
    choice = int(input("Choice: "))

    if choice == 1:
        print("All teams from the Bundesliga: ")
        
        url = "https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"

        r = requests.get(url, headers=userAgent)
        htmlText = r.text
        htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') 

        teams = htmlDocument.find_all("td", {"class": "hauptlink no-border-links"})

        for index, team in enumerate(teams, 1):
            text = team.get_text()
            print(f"{index}. {text}")
            print()
            
    
    elif choice == 2:
        print("All teams from the Bundesliga: ")
            
        url = "https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"

        r = requests.get(url, headers=userAgent)
        htmlText = r.text
        htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') 

        teams = htmlDocument.find_all("td", {"class": "hauptlink no-border-links"})

    
        for index, team in enumerate(teams, 1):
            text = team.get_text()
            print(f"{index}. {text}")
            print()

    
        team_number = int(input("Enter the number of the team you want to print: "))
        print()

        if 1 <= team_number <= len(teams):
            selected_team = teams[team_number - 1]
            team_name = selected_team.get_text()
            print(f"The selected team is: {team_name}\n")

        
            squad_size = selected_team.find_next_sibling("td", {"class": "zentriert"}).get_text(strip=True)
            print(f"Squad size of {team_name}: {squad_size}")
            print()

            average_value = selected_team.find_next_sibling("td", {"class": "rechts"}).get_text(strip=True)
            print(f"Average value of a player {team_name}: {average_value}")
            print()
        else:
            print("Invalid team number. Please enter a number within the range.")

    
    elif choice == 3:
        print("All teams from the Bundesliga: ")
            
        url = "https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"

        r = requests.get(url, headers=userAgent)
        htmlText = r.text
        htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') 

        teams = htmlDocument.find_all("td", {"class": "hauptlink no-border-links"})

    
        for index, team in enumerate(teams, 1):
            text = team.get_text()
            print(f"{index}. {text}")
            print()

    
        team_number = int(input("Enter the number of the team you want to see the players of: "))

        if 1 <= team_number <= len(teams):
            selected_team = teams[team_number - 1]
            team_name = selected_team.get_text()
            print(f"The selected team is: {team_name}")

        
            team_link = selected_team.find('a')['href']
            team_url = "https://www.transfermarkt.com" + team_link

        
            team_response = requests.get(team_url, headers=userAgent)
            team_html = team_response.text
            team_soup = bs4.BeautifulSoup(team_html, 'html.parser')

            players_table = team_soup.find("table", class_="items")
            
            players = players_table.find_all("td", class_="hauptlink")
            print("Players:")
            
            for player in players:
                player_name = player.get_text(strip=True)
                print(player_name)
                
    

    elif choice == 4:
        print("The program has stopped!")
        break