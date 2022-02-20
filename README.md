# About sectests

[sectests](https://github.com/magmax/sectests) is a python/pytest test suite for
infrastructure.

# Usage

It can be used to check the CIS Distribution Independent Linux Benchmark v2.0.0
with:

```
pytest test_cis_dil_benchmark.py
```

showing an useful report like:
```
----------------------------------- Security Report -----------------------------------
1.1.11: CIS 1.1.11: Ensure separate partition exists for /var/log (Scored) (impact: 1.0)

The /var/log directory is used by system services to store log data.
Solution:
Configure /etc/fstab as appropriate.
--
1.1.12: CIS 1.1.12: Ensure separate partition exists for /var/log/audit (Scored) (impact: 1.0)

The auditing daemon, auditd , stores log data in the /var/log/audit directory.
Solution:
Configure /etc/fstab as appropriate.
--
Score: 6.0
============================== short test summary info ================================
SKIPPED [3] test_cis_dil_benchmark.py:18: /tmp has no separated partition
SKIPPED [3] test_cis_dil_benchmark.py:18: /var/tmp has no separated partition
SKIPPED [1] test_cis_dil_benchmark.py:521: Not implemented yet
SKIPPED [1] test_cis_dil_benchmark.py:540: Not implemented yet
FAILED test_cis_dil_benchmark.py::test_separate_partition_for_var_log[local] - AssertionError: /var/log should be mounted on its own partition
FAILED test_cis_dil_benchmark.py::test_separate_partition_for_var_log_audit[local] - AssertionError: /var/log/audit should be mounted on its own partition
```


## Running it remotely

Thanks to [pytest-testinfra](https://testinfra.readthedocs.io/en/latest/) it can
be run remotely with ssh:

```
pytest test_cis_dil_benchmark.py --hosts ssh://hostname
```

or using ansible connections:
```
pytest test_cis_dil_benchmark.py --hosts ansible://all
```

or inside a docker instance:

```
pytest test_cis_dil_benchmark.py --hosts docker://docker-uid
```

or inside a kubernetes Pod instance:
```
pytest test_cis_dil_benchmark.py --hosts kubectl://somepod-2536ab?container=nginx&namespace=web
```

Please, check the [pytest-testinfra backends
documentation](https://testinfra.readthedocs.io/en/latest/backends.html) for
more connectivity information.


# Current status:

CIS Distribution indenpendent Linux Benchmark:
| type | status |
| --- | --- |
| Filesystem configuration | incomplete |
| Services | not started yet |
| Network configuration | not started yet |
| Logging and Auditing | not started yet |
| Access, authentication and authorization | not started yet |
| System Maintenance | not started yet |
