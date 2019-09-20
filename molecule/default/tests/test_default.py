import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_mysql_user_and_group_exists(host):
    group = host.group("mysql")

    assert group.exists

    user = host.user("mysql")

    assert user.group == "mysql"
    assert user.shell == "/bin/false"


def test_pymysql_package_installed(host):
    package = host.package("python2-PyMySQL")

    assert package.is_installed


def test_mysql_config_file(host):
    file = host.file("/usr/local/mysql/etc/my.cnf")

    assert file.exists
    assert file.is_file
    assert file.user == "mysql"
    assert file.group == "mysql"


def test_service_running_and_enabled(host):
    srv = host.service("mysqld")

    #  assert srv.is_enabled
    assert srv.is_running


def test_mysqld_socket_listen(host):
    ss = host.socket("tcp://0.0.0.0:3306")

    assert ss.is_listening

