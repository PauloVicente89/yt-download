from pytube import YouTube

# pegando url do video a ser baixado
url = input(str("Url do vídeo: "))
video = YouTube(url)

# definindo a maior resoluçao do video
stream = video.streams.get_highest_resolution()

# baixando no diretorio escolhido
stream.download(output_path = 'C:\\Users\\...') # PARA DIRECIONAR DIRETORIOS NO WINDOWS, UTILIZE DUAS BARRAS
