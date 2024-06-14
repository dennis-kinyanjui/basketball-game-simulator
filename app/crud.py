from sqlalchemy.orm import Session
from .models import Team, Player, Game
from random import randint


def delete_game(db: Session, game_id: int):
    game = db.query(Game).filter(Game.id == game_id).first()
    if game:
        db.delete(game)
        db.commit()
    return game

# Team CRUD
def create_team(db: Session, name: str, city: str):
    team = Team(name=name, city=city)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def get_teams(db: Session):
    return db.query(Team).all()

def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()

def delete_team(db: Session, team_id: int):
    team = db.query(Team).filter(Team.id == team_id).first()
    if team:
        db.delete(team)
        db.commit()
    return team

# Player CRUD
def create_player(db: Session, name: str, position: str, team_id: int):
    player = Player(name=name, position=position, team_id=team_id)
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def get_players(db: Session):
    return db.query(Player).all()

def get_player(db: Session, player_id: int):
    return db.query(Player).filter(Player.id == player_id).first()

def delete_player(db: Session, player_id: int):
    player = db.query(Player).filter(Player.id == player_id).first()
    if player:
        db.delete(player)
        db.commit()
    return player

# Game CRUD
def create_game(db: Session, team1_id: int, team2_id: int):
    team1_score = randint(80, 120)
    team2_score = randint(80, 120)
    winner = team1_id if team1_score > team2_score else team2_id

    game = Game(
        team1_id=team1_id,
        team2_id=team2_id,
        team1_score=team1_score,
        team2_score=team2_score,
        winner=winner
    )
    db.add(game)
    db.commit()
    db.refresh(game)
    return game

def get_games(db: Session):
    return db.query(Game).all()
