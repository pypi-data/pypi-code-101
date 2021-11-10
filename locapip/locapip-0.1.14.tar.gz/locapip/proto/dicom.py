import locale

import itk

import dicom_pb2 as pb
import dicom_pb2_grpc as pb_rpc
import locapip
from explorer import server_resolved_path

locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')
itk.ProcessObject.SetGlobalWarningDisplay(False)

if locapip.server is not None:
    class Service(pb_rpc.DicomServicer):
        async def parse_series(self, request: pb.Path, context):
            path = server_resolved_path(request.path)

            io = itk.GDCMImageIO.New()

            if path.is_file() and io.CanReadFile(path):
                io.SetFileName(path)
                io.ReadImageInformation()
                meta = io.GetMetaDataDictionary()
                meta = [(tag, io.GetLabelFromTag(tag, '')[1], meta[tag]) for tag in meta.GetKeys()]
                meta_label = {io.GetLabelFromTag(tag): meta[tag] for tag in meta.GetKeys()}

                yield [str(path)]
            elif path.is_dir():
                filenames = itk.GDCMSeriesFileNames.New()
                filenames.SetDirectory(str(path))
                filenames.SetUseSeriesDetails(True)
                filenames.SetRecursive(True)
                uids = filenames.GetSeriesUIDs()

                for uid in uids:
                    seriesIdentifier = uid
                    fileNames = [path for path in filenames.GetFileNames(seriesIdentifier)]

                uids = filenames.GetSeriesUIDs()

            dcmdir = str(pathlib.Path(dcmdir))
            filenames_list = []

            roots = [dcmdir]
            if recursive:
                roots = [root for root, *_ in os.walk(dcmdir)]
                roots.sort()
            for root in roots:
                with tempfile.TemporaryDirectory() as p:
                    if vmi.contains_zh_CN(root):
                        for f in os.listdir(root):
                            f = os.path.join(root, f)
                            if os.path.isfile(f):
                                shutil.copy2(f, p)
                        directory = p
                    else:
                        directory = root

                    for i in sitk.ImageSeriesReader.GetGDCMSeriesIDs(directory):
                        filenames = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(directory, i)
                        filenames = [str(pathlib.Path(root) / pathlib.Path(f).name) for f in filenames]
                        filenames_list.append(filenames)
                        print('sortFilenames {}'.format(len(filenames_list)))
            yield pb.Filenames(filenames=filenames)


    pb_rpc.add_DicomServicer_to_server(Service(), locapip.server)

else:
    locapip.pb[__name__] = pb
    locapip.stub[__name__] = pb_rpc.DicomStub

    locapip.py_request[__name__] = {
        'parse_series': pb.Path,
    }

    locapip.py_response[__name__] = {
    }
