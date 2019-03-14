def getLyricsFromFile(fileName = 'lyrics.txt'):
    with open(fileName) as lyricsFile:
        verses = [line.rstrip('\n') for line in lyricsFile]
    return verses

def recite(start_verse, end_verse):
    start_verse -= 1
    verses = getLyricsFromFile()
    song = []
    for i in range (start_verse, end_verse):
        song.append(verses[i])
    return song
