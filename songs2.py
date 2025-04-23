from fastapi import FastAPI, Body
from datetime import date


app=FastAPI()


class Song:
    id:int
    title:str
    artist:str
    album:str
    release_date:date

    def __init__(self,id,title,artist,album,release_date):
        self.id=id
        self.title=title
        self.artist=artist
        self.album=album
        self.release_date=release_date





songs=[
    Song(1,"Blessed","Meddy","single","04-05-2024"),
    Song(2,"Jolene","Beyonce","CowBoy Carter","04-01-2024"),
    Song(3,"Many Things","Zinolysky","single","04-02-2024"),
    Song(4,"abanikanda","Zinolysky","single","05-07-2024")

]

#main endpoint for now
@app.get("/")
async def get_home():
    return "lets get to version 2 of this"
#first api to get all the songs
@app.get("/songs")
async def get_songs():
    return songs
#let 's create a song now
@app.post("/songs/add")
async def add_song(new_song=Body()):
    songs.append(new_song)

