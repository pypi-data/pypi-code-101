import m3u8

playlist = m3u8.load('http://videoserver.com/playlist.m3u8')  # this could also be an absolute filename
print(playlist.segments)
print(playlist.target_duration)

# if you already have the content as string, use

playlist = m3u8.loads('#EXTM3U8 ... etc ... ')
print(playlist)
