# Description of task is no longer available

def song_decoder(song):
    step = 3
    song = str(song)
    for i in range(len(song)):
        if song[i:step] == "WUB":
            song = song.replace(song[i:step], " ")
        step += 1
    song.strip()
    return " ".join(song.split())
