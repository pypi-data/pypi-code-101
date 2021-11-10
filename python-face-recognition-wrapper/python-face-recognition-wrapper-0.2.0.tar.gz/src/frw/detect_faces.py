import argparse
import face_recognition


parser = argparse.ArgumentParser()


parser.add_argument(
    '--image', '-img', type=str,
    help="path of image"
)
parser.add_argument(
    '--output', '-o', type=str,
    help="path to write results"
)


class DetectFace:
    def __init__(self, image_path=None, result_file_path=None):
        self.image_path = image_path
        self.results = None
        self.result_file_path = result_file_path

    def get_result(self):
        image = face_recognition.load_image_file(self.image_path)
        self.results = face_recognition.face_locations(image)
        return self.results

    def save(self):
        if self.results is None:
            self.get_result()

        with open(self.result_file_path, "w") as _file:
            _file.write(f'{self.results}\r\n')


if __name__ == "__main__":
    args = parser.parse_args()

    output = args.output

    kw = dict(image_path=args.image)

    if output:
        kw['result_file_path'] = output
        DetectFace(**kw).save()
    else:
        print(DetectFace(**kw).get_result())
