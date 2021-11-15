import json
from datetime import datetime

from google.protobuf.json_format import Parse, MessageToJson

import fit_fill_pb2 as pb
import fit_fill_pb2_grpc as pb_rpc
import locapip


def _pass(*args, **kwargs):
    pass


async def _apass(*args, **kwargs):
    return None, None


if locapip.server is not None:
    mesh_reset = {'DynamicBody': _apass, 'StaticBody': _apass}
    mesh_build = {'DynamicBody': _pass, 'StaticBody': _pass}
    server_resolved_path = locapip.module['explorer'].server_resolved_path


    def new_stage(message):
        return '{}'


    async def simulate(message):
        return '{}'


    class Service(pb_rpc.FitFillServicer):
        async def new_stage(self, request, context):
            return Parse(new_stage(MessageToJson(request, True, True)), pb.Setting())

        async def import_mesh(self, request, context):
            name = request.name
            server_path = request.server_path
            server_path = server_resolved_path(server_path)
            point_num, face_num = await mesh_reset[name](str(server_path))
            mesh_build[name]()
            return pb.MeshInfo(name=name, point_num=point_num, face_num=face_num)

        async def simulate(self, request, context):
            request.capture_path = str(server_resolved_path(request.capture_path))
            return Parse(await simulate(MessageToJson(request, True, True)), pb.SimulateResult())


    pb_rpc.add_FitFillServicer_to_server(Service(), locapip.server)

else:
    async def upload_mesh_request(cpp_request, get_point, get_face):
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
        'import_mesh': pb.Mesh,
        'simulate': pb.Simulate,
    }

    locapip.py_response[__name__] = {}


    def _request(prefix, message):
        def foo(_):
            print(prefix, message)
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


    def new_stage(url: str, message):
        if message is str:
            message = json.loads(message)

        locapip.run_rpc(url, 'fit_fill', 'new_stage', [_request('new_stage', {})], [_response])


    def upload_mesh(url: str, message):
        if message is str:
            message = json.loads(message)

        name = message['name']
        path = message['path']

        server_path = f'cache/fit_fill/{name}.stl'

        locapip.module['explorer'].copy(url, {
            'copy_type': 'upload',
            'client_path': path,
            'server_path': server_path})

        locapip.run_rpc(url, 'fit_fill', 'import_mesh',
                        _request('import_mesh', {'name': name, 'server_path': server_path}),
                        _response)


    def simulate(url: str, message):
        if message is str:
            message = json.loads(message)

        transform = None

        def response(_):
            nonlocal transform
            t = json.loads(_)
            transform = [_['values'] for _ in [t['matrix'][_] for _ in t['matrix']][0]]
            return str()

        capture = 'cache/fit_fill/capture/Capture'
        locapip.run_rpc(url, 'fit_fill', 'simulate', [_request('simulate', {'capture_path': capture})], [response])
        return transform
