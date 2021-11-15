#from fabric import Connection


def run_command_on_host(host, password, cmd):

    connection = Connection(host, connect_kwargs={"password": password})
    result = connection.run(cmd, hide=True)

    #for result doc : https: // docs.fabfile.org / en / 2.5 / getting - started.html
    return result


def launch_student_command(host, password, cmd, working_dir):


    # maybe useless
    run_command_on_host(host, password)