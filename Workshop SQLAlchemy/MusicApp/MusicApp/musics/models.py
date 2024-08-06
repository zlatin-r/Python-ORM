from django.db import models
from sqlalchemy import Column, Integer, String, Float, relationship, ForeignKey

from MusicApp.settings import Base


# Create your models here.

class Album(Base):
    __tablename__ = 'albums'

    id = Column(
        Integer,
        primary_key=True
    )
    album_name = Column(
        String(30),
        nullable=False,
        unique=True
    )
    image_url = Column(
        String(255),
        nullable=False
    )
    price = Column(
        Float,
        nullable=False
    )
    songs = relationship(
        "Song",
        back_populates="album",
        cascade="all, delete-orphan"
    )


class Song(Base):
    __tablename__ = 'songs'

    id = Column(
        Integer,
        primary_key=True
    )
    song_name = Column(
        String(100),
        nullable=False,
    )
    album_id = Column(
        ForeignKey('albums.id'),
        Integer,
        nullable=False
    )
    album = relationship(
        "Album",
        back_populates="songs",
    )
