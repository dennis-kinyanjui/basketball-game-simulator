from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    score = Column(Integer, default=0)
    players = relationship("Player", back_populates="team")
    games1 = relationship("Game", back_populates="team1", foreign_keys='Game.team1_id')
    games2 = relationship("Game", back_populates="team2", foreign_keys='Game.team2_id')

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    position = Column(String, index=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="players")

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, index=True)
    team1_id = Column(Integer, ForeignKey('teams.id'))
    team2_id = Column(Integer, ForeignKey('teams.id'))
    team1_score = Column(Integer)
    team2_score = Column(Integer)
    winner = Column(Integer, ForeignKey('teams.id'))

    team1 = relationship("Team", foreign_keys=[team1_id], back_populates="games1")
    team2 = relationship("Team", foreign_keys=[team2_id], back_populates="games2")
