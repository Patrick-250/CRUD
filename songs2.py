from typing import Optional

import optional
from fastapi import FastAPI, Body,Path,Query,HTTPException
from pydantic import BaseModel,Field
from datetime import date


app=FastAPI()


class Song:
    id:int
    title:str
    artist:str=Field(min_length=1)
    album:str =Field(min_length=1)
    release_date:date

    def __init__(self,id,title,artist,album,release_date):
        self.id=id
        self.title=title
        self.artist=artist
        self.album=album
        self.release_date=release_date

class SongRequest(BaseModel):
    id: Optional[int] =Field(gt=0)
    title: str=Field(min_length=1)
    artist: str=Field(min_length=1)
    album: str =Field(min_length=1)
    release_date: date

    model_config = {

        "json_schema_extra":{
            "example":{
                "title":"a new song",
                "artist":"the artist that made that song",
                "album":"what album is that song on, otherwise single",
                "release_date":'when was the song released'
            }

        }

    }




songs=[
    Song(1,"Blessed","Meddy","single","04-05-2024"),
    Song(2,"Jolene","Beyonce","CowBoy Carter","04-01-2024"),
    Song(3,"Many Things","Zinolysky","single","04-02-2024"),
    Song(4,"abanikanda","Zinolysky","single","05-07-2024"),
    Song(5,"Ungirira ubuntu","Meddy","single","04-05-2011"),

]

#main endpoint for now
@app.get("/")
async def get_home():
    return "lets get to version 2 of this"
#first api to get all the songs
@app.get("/songs")
async def get_songs():
    return songs

#get a song by id
@app.get("/songs/{song_id}")
async def get_song_by_id(song_id:int =Path(gt=0)):
    for song in songs:
        if song.id==song_id:
            return song
    raise HTTPException(status_code=404, detail="song not found")
#get songs by artist name
@app.get("/songs/")
async def get_songs_by_artist(artist:str):
    songs_to_return=[]
    for song in songs:
        if song.artist==artist:
            songs_to_return.append(song)
    return songs_to_return


#update a song
@app.put("/songs/update_song")
async def update_song(song:SongRequest):
    for i in range(len(songs)):
        if songs[i].id==song.id:
            songs[i]=song



#delete a song
@app.delete("/songs/delete")
async def delete(song_id:int=Path(gt=0)):
    for i in range(len(songs)):
        if songs[i].id==song_id:
            songs.pop(i)
            break



#let 's create a song now
@app.post("/songs/add")
async def add_song(song_request:SongRequest):
    new_song=Song(**song_request.model_dump())

    songs.append(assign_song_id(new_song))
def assign_song_id(song:Song):
    if len(songs)>0:
        song.id=songs[-1].id+1
    else:
        song.id=1
    return song


