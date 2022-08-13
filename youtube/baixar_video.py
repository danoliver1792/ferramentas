from pytube import YouTube, streams

url = input(str('url para download: '))

video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download(output_path='C:/Users/User/Documents/videos')

print('Download concluído!')
