violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
new_playlist = []
time = 0
count = int(input('Сколько песен выбрать? '))

for i_song in range(3):
    print('Название', i_song + 1,'песни: ',end='')
    name_song = input()
    new_playlist.append(name_song)

for i_name_song in violator_songs:
    if i_name_song[0] in new_playlist:
        time += i_name_song[1]
print('Общее время звучания песен: ', round(time,2),'минуты.')

