import kubernetes as k8s

JOB_NAME = 'pi-job'
k8s.config.load_kube_config()
job = k8s.client.V1Job(
    api_version='batch/v1',
    kind='Job',
    metadata=k8s.client.V1ObjectMeta(name=JOB_NAME),
    spec=k8s.client.V1JobSpec(
        backoff_limit=3,
        template=k8s.client.V1PodTemplateSpec(
            metadata=k8s.client.V1ObjectMeta(labels={'app': JOB_NAME}),
            spec=k8s.client.V1PodSpec(
                restart_policy='Never',
                containers=[
                    k8s.client.V1Container(
                        name=JOB_NAME,
                        image='perl',
                        command=['perl', '-Mbignum=bpi', '-wle', 'print bpi(2000)'],
                    )
                ],
            ),
        ),
    ),
)
