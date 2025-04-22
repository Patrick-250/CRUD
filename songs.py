from fastapi import FastAPI,Body
app=FastAPI()

songs=[

  {"title":"Blessed","artist":"Meddy"},
{"title":"Texas Hold em","artist":"Beyonce"},
{"title":"Till you can't","artist":"Cody Johnson"},
  {"title":"Joylene","artist":"Beyonce"}

]

@app.get("/")
async def see_dashboard():
  return "Hello Rumanzii"
#get all songs
@app.get("/songs")
async def get_songs():
  return songs
#get song by title
@app.get("/songs/{title}")
async def get_song_by_title(title):
  for song in songs:
    if song.get("title")==title:
      return song
#get songs by artist
@app.get("/songs/")
async def get_songs_by_artist(artist):
  songs_of_artist=[]
  for song in songs:
    if song.get("artist").casefold()==artist.casefold():
      songs_of_artist.append(song)
  return songs_of_artist

#add a song to the dictionary
@app.post("/songs/add")
async def add_song(new_song=Body()):
  songs.append(new_song)
# update a song
@app.put("/songs/update")
async def update_song(updated_song=Body()):
  for i,song in enumerate(songs):
    if song.get("title").casefold()==updated_song.get("title").casefold():
      songs[i]=updated_song
      return "songs updated"
  return "failed to update"

#delete a song

@app.delete("/songs/delete/{title}")
async def delete_song(title):
  for i, song in enumerate(songs):
    if song.get("title").casefold()==title.casefold():
      songs.pop(i)
      break







