def validate_team_name(name):
    return len(name) > 0

def validate_city_name(city):
    return len(city) > 0

def validate_player_name(name):
    return len(name) > 0

def validate_position(position):
    return position in ['Guard', 'Forward', 'Center']
