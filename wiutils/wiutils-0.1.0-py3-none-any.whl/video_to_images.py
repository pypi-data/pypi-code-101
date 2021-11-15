import pathlib

from wiutils import convert_video_to_images
from wiutils import reduce_image_size


folder = pathlib.Path("/home/marcelo/Downloads/cam 3 octubre doñana/")
for path in folder.glob("*.JPG"):
    output_folder = pathlib.Path("/home/marcelo/Downloads/fotos_donana")
    reduce_image_size(path, output_folder.joinpath(path.name))


folder = pathlib.Path(
    "/home/marcelo/videos_dct/cjfajardo/VIDEOS MONITOREO OCTUBRE 2021/"
)
for path in folder.glob("*/*.MP4"):
    output_folder = folder.parent.joinpath(f"images/{path.parent.stem}/{path.stem}")
    try:
        convert_video_to_images(path, output_folder, offset=1)
    except:
        print(path)


folder = pathlib.Path("/home/marcelo/videos_dct/jgiraldo")
for path in folder.glob("*.M4V"):
    output_folder = folder.joinpath(f"images/{path.stem}")
    try:
        convert_video_to_images(path, output_folder, offset=1)
    except:
        print(path)


folder = pathlib.Path("/home/marcelo/videos_dct/antawara")
for path in folder.glob("*.AVI"):
    output_folder = folder.parent.joinpath(f"images/{path.stem}")
    try:
        convert_video_to_images(path, output_folder, offset=1)
    except:
        print(path)


folder = pathlib.Path("/home/marcelo/videos_dct/jpcerrato2486/")
for path in folder.rglob("*/*.MP4"):
    output_folder = folder.joinpath(f"images/{path.parent.stem}/{path.stem}")
    try:
        convert_video_to_images(path, output_folder, offset=1)
    except:
        print(path)


folder = pathlib.Path(
    "/home/marcelo/videos_dct/sergiomedellin/Monitoreo Octubre BHM - Terrasos/"
)
for path in folder.glob("*/*.MP4"):
    output_folder = folder.parent.joinpath(f"images/{path.parent.stem}/{path.stem}")
    try:
        convert_video_to_images(path, output_folder, offset=1)
    except:
        print(path)


folder = pathlib.Path("/home/marcelo/videos_dct/daymalzateg/CT/")
for path in folder.glob("*.mp4"):
    output_folder = folder.parent.joinpath(f"images/{path.stem}")
    try:
        convert_video_to_images(path, output_folder, offset=1)
    except:
        print(path)
