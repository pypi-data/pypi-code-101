import qualys_etl.etld_lib.etld_lib_config as etld_lib_config
import qualys_etl.etld_lib.etld_lib_spawn_etl as etld_lib_spawn_etl
import qualys_etl.etld_host_list_detection.etld_01_workflow_manager_host_list_detection as etl_host_list_detection

global vm_workflow
global asset_inventory_workflow
global was_workflow
global host_list_workflow
global kb_workflow


def workflows(workflow_list :list):
    global vm_workflow
    global asset_inventory_workflow
    global was_workflow
    global host_list_workflow
    global kb_workflow
    vm_workflow = False
    asset_inventory_workflow = False
    was_workflow = False
    host_list_workflow = False
    kb_workflow = False

    if workflow_list.__contains__('host_list_etl_workflow'):
        host_list_workflow = True
    if workflow_list.__contains__('kb_etl_workflow'):
        kb_workflow = True
    if workflow_list.__contains__('host_list_detection_etl_workflow'):
        vm_workflow = True
        # Ensure kb and hostlist are run through vm_workflow and not independently
        host_list_workflow = False
        kb_workflow = False

    if workflow_list.__contains__('asset_inventory_etl_workflow'):
        asset_inventory_workflow = True


def main():
    etld_lib_config.set_path_qetl_user_home_dir()
    etld_lib_spawn_etl.log_dir = etld_lib_config.qetl_user_log_dir
    etld_lib_spawn_etl.log_file_path = etld_lib_config.host_list_detection_log_file
    etld_lib_spawn_etl.log_file_rotate_path = etld_lib_config.host_list_detection_log_rotate_file
    etld_lib_spawn_etl.lock_file = etld_lib_config.host_list_detection_lock_file
    etld_lib_spawn_etl.log_file_max_size = (1024 * 100000)          # 1024 * size = Max Meg Size
    etld_lib_spawn_etl.spawned_process_max_run_time = (60*120)       # (seconds * minutes), then terminate as there is an issue.
    etld_lib_spawn_etl.spawned_process_sleep_time = 5               # check every n seconds for spawned_process.is_alive()
    etld_lib_spawn_etl.spawned_process_count_to_status_update = 11  # Every n checks print status spawned_process.is_alive()

    etld_lib_spawn_etl.etl_dir_to_monitor = etld_lib_config.qetl_user_data_dir
    etld_lib_spawn_etl.etl_files_max_time_between_changes = 300

    etld_lib_spawn_etl.target_module_to_run = etl_host_list_detection.host_list_detection_etl_workflow
    etld_lib_spawn_etl.target_method_in_module_to_run = "host_list_detection_etl_workflow"
    etld_lib_spawn_etl.etl_main()


if __name__ == '__main__':
    main()
