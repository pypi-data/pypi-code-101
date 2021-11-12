import os


class DockerRunOptionsBuilder(object):
    def __init__(self):
        self.options = set()

    def with_gpu(self) -> 'DockerRunOptionsBuilder':
        self.options.add('--gpus all')
        return self

    def with_privileged(self) -> 'DockerRunOptionsBuilder':
        self.options.add('--privileged')
        return self

    def with_add_devices(self) -> 'DockerRunOptionsBuilder':
        self.options.add('-v /dev:/dev')
        self.with_privileged()
        return self

    def with_display(self, display) -> 'DockerRunOptionsBuilder':
        self.options.add(f'-e DISPLAY={display}')
        self.options.add('-e QT_X11_NO_MITSHM=1')
        self.options.add('-v /tmp/.X11-unix:/tmp/.X11-unix:ro')
        return self

    def with_shared_memory(self) -> 'DockerRunOptionsBuilder':
        self.options.add(f'--ipc=host')
        # self.options.add('--ulimit memlock=-1')
        # self.options.add('--ulimit stack=67108864')
        self.with_add_devices()
        return self

    def with_project_volumes(self, project_workspace) -> 'DockerRunOptionsBuilder':
        project_data = os.path.join(project_workspace, 'data')
        self.options.add(f'-e PROJECT_WORKSPACE={project_workspace}')
        self.options.add(f'-e PROJECT_DATA={project_data}')
        self.options.add(f'-v {project_workspace}:{project_workspace}')
        self.options.add(f'-v {project_data}:{project_data}')
        return self

    def with_jupyter_runtime_volumes(self, workspace) -> 'DockerRunOptionsBuilder':
        project_data = os.path.join(project_workspace, 'data')
        self.options.add(f'-e PROJECT_WORKSPACE={project_workspace}')
        self.options.add(f'-e PROJECT_DATA={project_data}')
        self.options.add(f'-v {project_workspace}:{project_workspace}')
        self.options.add(f'-v {project_data}:{project_data}')
        return self

    def with_tracing(self, tracing_host, tracing_port) -> 'DockerRunOptionsBuilder':
        self.options.add(f'-e OTEL_EXPORTER_JAEGER_AGENT_HOST={tracing_host}')
        self.options.add(f'-e OTEL_EXPORTER_JAEGER_AGENT_PORT={tracing_port}')
        return self

    def with_user(self, uid: int, gid: int) -> 'DockerRunOptionsBuilder':
        self.options.add(f'--user {uid}:{gid}')
        return self

    def build(self):
        return ' '.join(self.options)

