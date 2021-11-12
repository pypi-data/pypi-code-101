import json
import locale
from datetime import datetime
from pathlib import Path

from google.protobuf.json_format import Parse, MessageToJson

import fit_fill_pb2 as pb
import fit_fill_pb2_grpc as pb_rpc
import locapip


def _pass(*args, **kwargs):
    pass


if locapip.server is not None:
    mesh_reset = {'DynamicBody': _pass, 'StaticBody': _pass}
    mesh_add_point = {'DynamicBody': _pass, 'StaticBody': _pass}
    mesh_add_face = {'DynamicBody': _pass, 'StaticBody': _pass}
    mesh_build = {'DynamicBody': _pass, 'StaticBody': _pass}


    def new_stage(message):
        return '{}'


    async def simulate(message):
        return '{}'


    class Service(pb_rpc.FitFillServicer):
        async def new_stage(self, request, context):
            return Parse(new_stage(MessageToJson(request, True, True)), pb.Setting())

        async def upload_mesh(self, request_iterator, context):
            name = ''
            point_num = 0
            face_num = 0
            async for request in request_iterator:
                if request.WhichOneof('type') == 'name':
                    name = request.name
                    mesh_reset[name]()
                elif request.WhichOneof('type') == 'points':
                    for point in request.points.points:
                        if len(point.values) >= 3:
                            point_num += 1
                            mesh_add_point[name](tuple(point.values[:3]))
                elif request.WhichOneof('type') == 'faces':
                    for face in request.faces.faces:
                        if len(face.values) >= 3:
                            face_num += 1
                            mesh_add_face[name](tuple(face.values))
            mesh_build[name]()
            return pb.MeshInfo(name=name, point_num=point_num, face_num=face_num)

        async def simulate(self, request, context):
            return Parse(await simulate(MessageToJson(request, True, True)), pb.SimulateResult())


    pb_rpc.add_FitFillServicer_to_server(Service(), locapip.server)

else:
    async def upload_mesh(cpp_request, get_point, get_face):
        request_dict = json.loads(cpp_request(str()))
        name = request_dict['name']
        point_num = request_dict['point_num']
        face_num = request_dict['face_num']

        yield pb.Mesh(name=name)

        mesh = pb.Mesh()
        t = datetime.now()

        for i in range(point_num):
            values = json.loads(get_point(json.dumps({'id': i})))['point']
            mesh.points.points.append(pb.Vector(values=values))

            if len(mesh.points.points) > 37450 or i == point_num - 1:
                yield mesh
                network_speed = mesh.ByteSize() / (datetime.now() - t).total_seconds() / 1024 / 1024
                print(f'upload {name} {0.5 * (i + 1) / point_num:>7.2%} {network_speed:>5.2f} MiB/s')
                t = datetime.now()
                mesh = pb.Mesh()

        for i in range(face_num):
            values = json.loads(get_face(json.dumps({'id': i})))['face']
            mesh.faces.faces.append(pb.Indices(values=values))

            if len(mesh.faces.faces) > 80660 or i == face_num - 1:
                yield mesh
                network_speed = mesh.ByteSize() / (datetime.now() - t).total_seconds() / 1024 / 1024
                print(f'upload {name} {0.5 + 0.5 * (i + 1) / face_num:>7.2%} {network_speed:>5.2f} MiB/s')
                t = datetime.now()
                mesh = pb.Mesh()


    locapip.pb[__name__] = pb
    locapip.stub[__name__] = pb_rpc.FitFillStub

    locapip.py_request[__name__] = {
        'new_stage': pb.Setting,
        'upload_mesh': upload_mesh,
        'simulate': pb.Simulate,
    }

    locapip.py_response[__name__] = {}


    def _request(message):
        def foo(unused):
            print('request', message)
            return json.dumps(message)

        return foo


    def _response(message):
        print('response', message)
        return str()


    def _get_point(poly):
        def foo(message):
            i = json.loads(message)['id']
            point = list(poly.GetPoint(i))
            return json.dumps({'point': point})

        return foo


    def _get_face(poly):
        def foo(message):
            i = json.loads(message)['id']
            ids = poly.GetCell(i).GetPointIds()
            face = [ids.GetId(_) for _ in range(ids.GetNumberOfIds())]
            return json.dumps({'face': face})

        return foo


    def new_stage(url: str):
        locapip.run_rpc(url, 'fit_fill', 'new_stage', [_request({})], [_response])


    def upload_mesh(url: str, name: str, poly):
        if type(poly) in [str, Path]:
            from vtkmodules.vtkIOGeometry import vtkSTLReader
            reader = vtkSTLReader()

            locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')
            reader.SetFileName(str(poly))
            reader.Update(None)
            poly = reader.GetOutput()

        locapip.run_rpc(url, 'fit_fill', 'upload_mesh',
                        [_request({'name': name,
                                   'point_num': poly.GetNumberOfPoints(),
                                   'face_num': poly.GetNumberOfCells()}),
                         _get_point(poly),
                         _get_face(poly)],
                        [_response])


    def simulate(url: str, capture_file_name: str):
        transform = None

        def response(message):
            nonlocal transform
            t = json.loads(message)
            transform = [_['values'] for _ in [t['matrix'][_] for _ in t['matrix']][0]]
            return str()

        locapip.run_rpc(url, 'fit_fill', 'simulate', [_request({'capture_file_name': capture_file_name})], [response])
        return transform
