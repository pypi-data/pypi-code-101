import argparse, os, shlex

from .config import (
	video_cache_key, video_key,
	video_cache_dir, video_dir,
	video_extension_key
)
from .converter import extract_audio, append_audios, set_audio_tracks_lang
from .helpers import setup_checks, get_filenames
from .loader import load_files_from_list
from .m3u.parser import read_playlist

def init_argparser():
	parser = argparse.ArgumentParser(description='Make dual-audio movie')

	# playlists
	parser.add_argument('-a', '--audio-playlists', nargs='*', help='Path(s) to playlist(s) with videos from which extract audio', default=[])
	parser.add_argument('-v', '--video-playlists', nargs='*', help='Path(s) to playlist(s) with videos to add a second audio', default=[])

	# other
	parser.add_argument('-d', '--out-dir', type=str, help='Directory where place audio and video folders', default='.')
	parser.add_argument('--preserve-video', action='store_true', help='Preserving main video')
	parser.add_argument('--args', type=str, help='File with shell arguments')

	# fix audio language metadata
	parser.add_argument('--fix-audio-lang', action='store_true', help='Fix audio tracks language metadata. If specified, downloading and converting will not be performed')
	parser.add_argument('--fix-audio-lang-list', type=str, help='File with list of filenames to fix language')
	parser.add_argument('--first-audio-lang', type=str, help='Language in first audio track (from video file). Language is 3-letter identifier like "eng" or "rus"')
	parser.add_argument('--second-audio-lang', type=str, help='Language in second audio track (from extracted audio)')

	args = parser.parse_args()

	if args.args:
		with open(os.path.abspath(args.args)) as args_file:
			args = parser.parse_args(shlex.split(args_file.read(), comments=True))

	return args

def load_and_process(
	audio_playlists, video_playlists,
	out_dir,
	preserve_video,
):
	abs_out_dir = os.path.abspath(out_dir)

	audio_index, videos_index = [], []

	for p in audio_playlists:
		data = read_playlist(os.path.abspath(p))

		# load videos for audio extracting
		loaded_cache_videos = load_files_from_list(
			data,
			video_cache_key,
			abs_out_dir,
			video_cache_dir,
			video_extension_key,
		)
		audio_index += extract_audio(loaded_cache_videos, video_cache_key, abs_out_dir)

	for p in video_playlists:
		data = read_playlist(os.path.abspath(p))

		# load videos for audio appending
		videos_index += load_files_from_list(
			data,
			video_key,
			abs_out_dir,
			video_dir,
			video_extension_key,
		)

	filenames = get_filenames(audio_index, videos_index)
	append_audios(filenames, abs_out_dir, preserve_video)

def main():
	args = init_argparser()
	setup_checks(args.out_dir)

	if args.fix_audio_lang:
		set_audio_tracks_lang(args.fix_audio_lang_list, args.first_audio_lang, args.second_audio_lang)
		return

	load_and_process(
		args.audio_playlists,
		args.video_playlists,
		args.out_dir,
		args.preserve_video,
	)

	print('Done')

if __name__ == '__main__':
	main()
