from lab_assistant_utils.kernel_cli import lab_start_kernel_image
project_name = ''
project_version = ''
project_path = ''
def lab_start_kernel(ctx, connection, image_name_prefix):
    image_name_prefix.append(project_name)
    kernel_image = f"{'/'.join(image_name_prefix)}:{project_version}"
    lab_start_kernel_image(ctx, connection, kernel_image, project_name, project_path)
