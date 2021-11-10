import json
import os
import time
import zipfile

import tqdm

try:
    from pet_core_aws.s3 import upload_file
except ImportError:
    pass


def update_deploy_id_resource_api_gateway(path_template):
    deploy_name = "DeployApi"
    with open(path_template, 'r') as _template:
        template = json.load(_template)
    resource_data = template['Resources'].pop(deploy_name)
    resource_name = f"DeployApi{int(time.time())}"
    template['Resources'][resource_name] = resource_data
    template['Resources']['ApiStage']['Properties']["DeploymentId"]['Ref'] = resource_name
    depends_on = template['Resources']['ApiKey']['DependsOn']
    depends_on[depends_on.index(deploy_name)] = resource_name
    template['Resources']['ApiKey']['DependsOn'] = depends_on
    with open(path_template, 'w') as _template:
        _template.write(json.dumps(template, indent=2))


def _create_layer_zip(*, layers_zips, layer, layer_path, bucket):
    zip_path_file = os.path.join(layers_zips, f'{layer}.zip')
    with zipfile.ZipFile(zip_path_file, 'w') as my_zip:
        for _sub_dir in os.listdir(layer_path):
            sub_path = os.path.join(layer_path, _sub_dir)
            for file in os.listdir(sub_path) if os.path.isdir(sub_path) else []:
                my_zip.write(os.path.join(sub_path, file), os.path.join('python', _sub_dir, file))
    if not upload_file(file_name=zip_path_file, bucket=bucket):
        print(f"Error to try save the layer zip in s3 {bucket}")


def build_layers(*, layers_path, bucket=None, use_zip=False):
    layers_zips = 'layers_zips'
    if not os.path.exists(layers_zips):
        os.mkdir(layers_zips)

    for layer in tqdm.tqdm(os.listdir(layers_path)):
        layer_path = os.path.join(layers_path, layer)

        layer_path = os.path.join(layer_path, 'python')
        try:
            print('runing command', f'pip install -r {os.path.join(layer_path, "requirements.txt")} -t {layer_path}')
            os.system(f'pip install -r {os.path.join(layer_path, "requirements.txt")} -t {layer_path}')
        except Exception as e:
            print("WARNING: ", str(e))
        if use_zip:
            _create_layer_zip(layers_zips=layers_zips, layer=layer, layer_path=layer_path, bucket=bucket)


def build_all_lambdas(*, lambdas_path, path_cfn_template, path_swagger_template, bucket):
    with open(path_cfn_template, 'r') as f:
        cfn_template = json.load(f)

    with open(path_swagger_template, 'r') as f:
        swagger_template = json.load(f)

    for path in os.listdir(lambdas_path):
        name = path
        path = os.path.join(lambdas_path, path)
        if (path == lambdas_path) or not (os.path.isdir(path)):
            continue

        with open(os.path.join(path, 'configuration.json'), 'r') as f:
            configuration = json.load(f)
        cfn_template['Resources'][name] = configuration['cfn']
        for k, v in configuration['swagger'].items():
            if k not in swagger_template['paths']:
                swagger_template['paths'].update(configuration['swagger'])
            else:
                for vk, vv in v.items():
                    if vk not in swagger_template['paths'][k]:
                        swagger_template['paths'][k].update({vk: vv})

    with open(path_cfn_template, 'w') as f:
        f.write(json.dumps(cfn_template))

    with open(path_swagger_template, 'w') as f:
        f.write(json.dumps(swagger_template))

    # upload_file(file_name=path_swagger_template, bucket=bucket)
