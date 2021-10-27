cd /pai
./paictl.py service stop -n cluster-configuration hivedscheduler rest-server job-exporter
./paictl.py config push -p /cluster-configuration -m service
./paictl.py service start -n cluster-configuration hivedscheduler rest-server job-exporter
