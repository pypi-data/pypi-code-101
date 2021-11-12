import os
import yaml
from dask_kubernetes import KubeCluster
from dask.distributed import Client
from kubernetes import client, config
import socket
from copy import copy

# https://stackoverflow.com/a/46046153
SERVICE_NAMESPACE_FILENAME = "/var/run/secrets/kubernetes.io/serviceaccount/namespace"


def init_dask_cluster(
    max_workers=8, threads=4, memory=8, cpu=1, death_timeout=120, check_interval="5s"
):

    if "_easyai_dask_cluster" in globals():
        return

    # get pod(host) name
    pod_name = socket.gethostname()
    with open(SERVICE_NAMESPACE_FILENAME, "r") as f:
        namespace_name = f.readline().strip()

    # get the y about the current pod
    config.load_incluster_config()
    k8s_v1_api = client.CoreV1Api()
    pod_yaml = k8s_v1_api.read_namespaced_pod(namespace=namespace_name, name=pod_name)
    volumes = pod_yaml.spec.volumes
    volume_mounts = pod_yaml.spec.containers[0].volume_mounts

    # parse pvc and hadoop source(keytab) infos
    pvc_name_list = []
    hadoop_source_name = ""
    mount_name_list = []
    mount_path_name_dict = {}  # one pvc may mount on multi path, so use path as key
    for _volume in volumes:
        if _volume.persistent_volume_claim:
            pvc_name_list.append(_volume.persistent_volume_claim.claim_name)
        elif _volume.config_map:
            hadoop_source_name = _volume.config_map.name

    mount_name_list.extend(pvc_name_list)
    mount_name_list.append(hadoop_source_name)

    for _mnt_vol in volume_mounts:
        if _mnt_vol.name in mount_name_list:
            mount_path_name_dict[_mnt_vol.mount_path] = _mnt_vol.name

    # read raw dask worker pod yaml
    template_worker_pod_yaml_path = os.path.join(
        os.path.dirname(__file__), "template/worker.yaml"
    )
    with open(template_worker_pod_yaml_path, "r") as yaml_reader:
        dask_worker_yaml = yaml.safe_load(yaml_reader)

    # generate pod yaml

    # set args
    dask_worker_yaml["spec"]["containers"][0]["args"] = [
        "dask-worker",
        "--nthreads",
        f"{threads}",
        "--no-dashboard",
        "--memory-limit",
        f"{memory}GiB",
        "--death-timeout",
        f"{death_timeout}",
    ]

    # add pvc
    dask_worker_yaml["spec"]["volumes"] = []
    _yaml_volumes_list = dask_worker_yaml["spec"]["volumes"]
    for _pvc_name in pvc_name_list:
        _dict = {}
        _dict["name"] = _pvc_name
        _dict["persistentVolumeClaim"] = {"claimName": _pvc_name}
        _yaml_volumes_list.append(_dict)

    # add keytab
    _dict = {}
    _dict["configMap"] = {"defaultMode": 420, "name": hadoop_source_name}
    _dict["name"] = hadoop_source_name
    _yaml_volumes_list.append(_dict)

    # add mount path
    _dict = {}
    dask_worker_yaml["spec"]["containers"][0]["volumeMounts"] = []
    _yaml_volume_mounts_list = dask_worker_yaml["spec"]["containers"][0]["volumeMounts"]
    for _mnt_path, _mnt_name in mount_path_name_dict.items():
        _dict = {}
        _dict["mountPath"] = _mnt_path
        _dict["name"] = _mnt_name
        _yaml_volume_mounts_list.append(_dict)

    # set resources
    _yaml_resource_dict = dask_worker_yaml["spec"]["containers"][0]["resources"]
    cpu_memory_dict = {"cpu": cpu, "memory": f"{memory}G"}
    _yaml_resource_dict["limits"] = cpu_memory_dict
    # copy() to ignore anchor
    _yaml_resource_dict["requests"] = copy(cpu_memory_dict)

    global _easyai_dask_cluster, _easyai_dask_client

    _easyai_dask_cluster = KubeCluster(
        dask_worker_yaml, name=f"easydata-{pod_name}-dask-worker", deploy_mode="local"
    )
    _easyai_dask_cluster.adapt(minimum=0, maximum=max_workers, interval=check_interval)
    _easyai_dask_client = Client(_easyai_dask_cluster)
