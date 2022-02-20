import stat
import re
from config import Configuration
import pytest

def is_mounted(host, path):
    return host.run(f"mount | grep -E '\\s{path}\\s'").stdout != ""

def assert_is_mounted(host, path):
    assert is_mounted(host, path), \
        f"{path} should be mounted on its own partition"

def is_mounted_with_argument(host, path, argument):
    return host.run(f"mount | grep -E '\\s{path}\\s' | grep -v {argument}").stdout == ""

def assert_is_mounted_with_argument(host, path, argument):
    if not is_mounted(host, path):
        pytest.skip(f"{path} has no separated partition")
    assert is_mounted_with_argument(host, path, argument), \
        f"{path} should be mounted with `{argument}` option"


@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_cramfs_module_loaded(record_property, host):
    record_property("code", "1.1.1.1")
    record_property("title", f"CIS 1.1.1.1: Disable unused filesystem cramfs (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
Ensure mounting of cramfs is disabled.
Solution:
- Add the line `install cramfs /bin/true` to the file `/etc/modprobe.d/cramfs.conf`.
"""
    )
    assert "" == host.run("lsmod | grep cramfs").stdout
    #modprobe = host.run(f"modprobe -n -v cramfs")
    #assert "install /bin/true" == modprobe.stdout

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_freevxfs_module_loaded(record_property, host):
    record_property("code", "1.1.1.2")
    record_property("title", f"CIS 1.1.1.2: Disable unused filesystem freevxfs (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
Ensure mounting of freevxfs is disabled.
Solution:
- Add the line `install freevxfs /bin/true` to the file `/etc/modprobe.d/freevxfs.conf`.
"""
    )
    assert "" == host.run("lsmod | grep freevxfs").stdout
    #modprobe = host.run(f"modprobe -n -v freevxfs")
    #assert "install /bin/true" == modprobe.stdout

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_iffs2_module_loaded(record_property, host):
    record_property("code", "1.1.1.3")
    record_property("title", f"CIS 1.1.1.3: Disable unused filesystem iffs2 (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
Ensure mounting of iffs2 is disabled.
Solution:
- Add the line `install iffs2 /bin/true` to the file `/etc/modprobe.d/iffs2.conf`.
"""
    )
    assert "" == host.run("lsmod | grep iffs2").stdout
    #modprobe = host.run(f"modprobe -n -v iffs2")
    #assert "install /bin/true" == modprobe.stdout

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_hfs_module_loaded(record_property, host):
    record_property("code", "1.1.1.4")
    record_property("title", f"CIS 1.1.1.4: Disable unused filesystem hfs (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
Ensure mounting of hfs is disabled.
Solution:
- Add the line `install hfs /bin/true` to the file `/etc/modprobe.d/hfs.conf`.
"""
    )
    assert "" == host.run("lsmod | grep hfs").stdout
    #modprobe = host.run(f"modprobe -n -v hfs")
    #assert "install /bin/true" == modprobe.stdout

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_hfsplus_module_loaded(record_property, host):
    record_property("code", "1.1.1.5")
    record_property("title", f"CIS 1.1.1.5: Disable unused filesystem hfsplus (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
Ensure mounting of hfsplus is disabled.
Solution:
- Add the line `install hfsplus /bin/true` to the file `/etc/modprobe.d/hfsplus.conf`.
"""
    )
    assert "" == host.run("lsmod | grep hfsplus").stdout
    #modprobe = host.run(f"modprobe -n -v hfsplus")
    #assert "install /bin/true" == modprobe.stdout

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_squashfs_module_loaded(record_property, host):
    record_property("code", "1.1.1.6")
    record_property("title", f"CIS 1.1.1.6: Disable unused filesystem squashfs (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
Ensure mounting of squashfs is disabled.
Solution:
- Add the line `install squashfs /bin/true` to the file
  `/etc/modprobe.d/squashfs.conf`.
"""
    )
    assert "" == host.run("lsmod | grep squashfs").stdout
    #modprobe = host.run(f"modprobe -n -v squashfs")
    #assert "install /bin/true" == modprobe.stdout

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_udf_module_loaded(record_property, host):
    record_property("code", "1.1.1.7")
    record_property("title", f"CIS 1.1.1.7: Disable unused filesystem udf (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
Ensure mounting of udf is disabled.
Solution:
- Add the line `install udf /bin/true` to the file
  `/etc/modprobe.d/udf.conf`.
"""
    )
    assert "" == host.run("lsmod | grep udf").stdout

@pytest.mark.workstation2
@pytest.mark.server2
@pytest.mark.cis
def test_fat_module_loaded(record_property, host):
    record_property("code", "1.1.1.8")
    record_property("title", f"CIS 1.1.1.8: Disable unused filesystem fat (Not Scored)")
    record_property("impact", 0)
    record_property("description", f"""
Ensure mounting of fat is disabled.
Solution:
- Add the line `install fat /bin/true` to the file
  `/etc/modprobe.d/fat.conf`.
"""
    )
    assert "" == host.run("lsmod | grep fat").stdout

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_tmp_configured(record_property, host):
    record_property("code", "1.1.2")
    record_property("title", f"CIS 1.1.2: Ensure /tmp is configured (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The /tmp directory is a world-writable directory used for temporary storage by
all users and some applications.
Solution:
Configure /etc/fstab as appropriate.
example:
```
tmpfs /tmp tmpfs defaults,rw,nosuid,nodev,noexec,relatime 0 0
```
"""
    )
    assert_is_mounted(host, "/tmp")

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_tmp_with_nodev(record_property, host):
    record_property("code", "1.1.3")
    record_property("title", f"CIS 1.1.3: Ensure nodev option set on /tmp partition (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The nodev mount option specifies that the filesystem cannot contain special devices.
Solution:
Edit the /etc/fstab file and add nodev to the fourth field (mounting options) for the /tmp partition.
"""
    )
    assert_is_mounted_with_argument(host, "/tmp", "nodev")

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_tmp_with_nosuid(record_property, host):
    record_property("code", "1.1.4")
    record_property("title", f"CIS 1.1.4: Ensure nosuid option set on /tmp partition (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The nosuid mount option specifies that the filesystem cannot contain setuid
files.
Solution:
Edit the /etc/fstab file and add nosuid to the fourth field (mounting options) for the /tmp partition.
"""
    )
    assert_is_mounted_with_argument(host, "/tmp", "nosuid")

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_tmp_with_noexec(record_property, host):
    record_property("code", "1.1.5")
    record_property("title", f"CIS 1.1.5: Ensure noexec option set on /tmp partition (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The noexec mount option specifies that the filesystem cannot contain executable binaries.
Solution:
Edit the /etc/fstab file and add noexec to the fourth field (mounting options) for the /tmp partition.
"""
    )
    assert_is_mounted_with_argument(host, "/tmp", "noexec")

@pytest.mark.workstation2
@pytest.mark.server2
@pytest.mark.cis
def test_separate_partition_for_var(record_property, host):
    record_property("code", "1.1.6")
    record_property("title", f"CIS 1.1.6: Ensure separate partition exists for /var (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The /var directory is used by daemons and other system services to temporarily store
dynamic data. Some directories created by these processes may be world-writable.
Solution:
Configure /etc/fstab as appropriate.
"""
    )
    assert_is_mounted(host, "/var")

@pytest.mark.workstation2
@pytest.mark.server2
@pytest.mark.cis
def test_separate_partition_for_var_tmp(record_property, host):
    record_property("code", "1.1.7")
    record_property("title", f"CIS 1.1.7: Ensure separate partition exists for /var/tmp (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The /var/tmp directory is a world-writable directory used for temporary storage by all
users and some applications.
Solution:
Configure /etc/fstab as appropriate.
"""
    )
    assert_is_mounted(host, "/var/tmp")

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_nodev_on_var_tmp_if_exists(record_property, host):
    record_property("code", "1.1.8")
    record_property("title", f"CIS 1.1.8: Ensure nodev option set on /var/tmp partition (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The nodev mount option specifies that the filesystem cannot contain special devices.
Solution:
Edit the /etc/fstab file and add nodev to the fourth field (mounting options) for the
/var/tmp partition
"""
    )
    assert_is_mounted_with_argument(host, "/var/tmp", "nodev")

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_nosuid_on_var_tmp_if_exists(record_property, host):
    record_property("code", "1.1.9")
    record_property("title", f"CIS 1.1.9: Ensure nosuid option set on /var/tmp partition (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The nosuid mount option specifies that the filesystem cannot contain setuid files.
Solution:
Edit the /etc/fstab file and add nosuid to the fourth field (mounting options) for the
/var/tmp partition
"""
    )
    assert_is_mounted_with_argument(host, "/var/tmp", "nosuid")

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_noexec_on_var_tmp_if_exists(record_property, host):
    record_property("code", "1.1.10")
    record_property("title", f"CIS 1.1.10: Ensure noexec option set on /var/tmp partition (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The noexec mount option specifies that the filesystem cannot contain executable binaries.
Solution:
Edit the /etc/fstab file and add noexec to the fourth field (mounting options) for the
/var/tmp partition
"""
    )
    assert_is_mounted_with_argument(host, "/var/tmp", "noexec")

@pytest.mark.workstation2
@pytest.mark.server2
@pytest.mark.cis
def test_separate_partition_for_var_log(record_property, host):
    record_property("code", "1.1.11")
    record_property("title", f"CIS 1.1.11: Ensure separate partition exists for /var/log (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The /var/log directory is used by system services to store log data.
Solution:
Configure /etc/fstab as appropriate.
"""
    )
    assert_is_mounted(host, "/var/log")

@pytest.mark.workstation2
@pytest.mark.server2
@pytest.mark.cis
def test_separate_partition_for_var_log(record_property, host):
    record_property("code", "1.1.12")
    record_property("title", f"CIS 1.1.12: Ensure separate partition exists for /var/log/audit (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The auditing daemon, auditd , stores log data in the /var/log/audit directory.
Solution:
Configure /etc/fstab as appropriate.
"""
    )
    assert_is_mounted(host, "/var/log/audit")

@pytest.mark.workstation2
@pytest.mark.server2
@pytest.mark.cis
def test_separate_partition_for_home(record_property, host):
    record_property("code", "1.1.13")
    record_property("title", f"CIS 1.1.13: Ensure separate partition exists for /home (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The /home directory is used to support disk storage needs of local users.
Solution:
Configure /etc/fstab as appropriate.
"""
    )
    assert_is_mounted(host, "/home")

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_home_with_nodev(record_property, host):
    record_property("code", "1.1.14")
    record_property("title", f"CIS 1.1.14: Ensure nodev option set on /home partition (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The nodev mount option specifies that the filesystem cannot contain special devices.
Solution:
Edit the /etc/fstab file and add nodev to the fourth field (mounting options) for the /home partition.
"""
    )
    assert_is_mounted_with_argument(host, "/home", "nodev")

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_dev_shm_with_nodev(record_property, host):
    record_property("code", "1.1.15")
    record_property("title", f"CIS 1.1.15: Ensure nodev option set on /dev/shm partition (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The nodev mount option specifies that the filesystem cannot contain special devices.
Solution:
Edit the /etc/fstab file and add nodev to the fourth field (mounting options) for the /dev/shm partition.
"""
    )
    assert_is_mounted_with_argument(host, "/dev/shm", "nodev")

@pytest.mark.workstation1
@pytest.mark.server1
@pytest.mark.cis
def test_dev_shm_with_nosuid(record_property, host):
    record_property("code", "1.1.16")
    record_property("title", f"CIS 1.1.16: Ensure nosuid option set on /dev/shm partition (Scored)")
    record_property("impact", 1.0)
    record_property("description", f"""
The nosuid mount option specifies that the filesystem cannot contain setuid files.
Solution:
Edit the /etc/fstab file and add nosuid to the fourth field (mounting options) for the /dev/shm partition.
"""
    )
    assert_is_mounted_with_argument(host, "/dev/shm", "nosuid")



