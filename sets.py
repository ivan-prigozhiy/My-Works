players = [
    "Steve", "Alex", "Notch", "Steve",
    "Herobrine", "Alex", "Dream", "Notch",
    "Technoblade", "Steve", "Bob", "Lightstar4ik"
]

online_players = [
    "Alex", "Dream", "Steve", "Notch", "Bob", "Lightstar4ik"
]

unique_players, online_players, offline_players = set(players), set(online_players), set(players) - set(online_players)

#STATS
def show_stats(unique_players=unique_players, online_players=online_players, offline_players=offline_players):
    print(f'========== Statistics ==========\nAll players: {len(unique_players)}', ', '.join(unique_players)+'.', sep='  ->  ')
    print(f'Online players {len(online_players)}', ', '.join(online_players)+'.', sep='  ->  ')
    print(f'Offline players {len(offline_players)}', ', '.join(offline_players)+'.', sep='  ->  ', end='\n\n')

#CHECK PLAYER
def check_player():
    player=input('Enter player nick_name: ').strip()
    if player in unique_players:
        return True


show_stats()
print('Player exists! \n') if check_player() else print('Player not exists! \n')
print(f'All players: {offline_players|online_players}')