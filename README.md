# Table of contents

- [Table of contents](#table-of-contents)
  - [Information Server / Datastage Health Check Role](#information-server--datastage-health-check-role)
    - [Deliverables](#deliverables)
    - [Issues and Enhancements](#issues-and-enhancements)
  - [Requirements](#requirements)
  - [Role Workflow](#role-workflow)
  - [Running a Report](#running-a-report)
    - [From Tower or AWX](#from-tower-or-awx)
    - [From a Local Clone](#from-a-local-clone)
  - [Updating to Future Releases of ISALite](#updating-to-future-releases-of-isalite)
  - [Author Information](#author-information)
  - [Miscellaneous](#miscellaneous)

## Information Server / Datastage Health Check Role

The function of this report is to provide an overall health check on an Infosphere host.  The health check is performed using the [ISALite](https://www.ibm.com/support/knowledgecenter/SSZJPZ_11.7.0/com.ibm.swg.im.iis.productization.iisinfsv.install.doc/topics/wsisinst_install_verif_troublshtng.html) utility which is a tool developed to perform health checks and other actions required to support the product on customer and internal infrastructure.  

The version of ISALite packaged with this automation will support all versions of Information Server up to 11.7.1.1.  

This role can be run without any interruption in service as it does not make any changes to the running applications.  The ISALite application, which is installed as part of the initial deployment, will be upgraded to the version packaged with this role if it is an older release.

### Deliverables
After the health check runs successfully, it will produce a compressed archive in the reports path that contains two html reports.  To view examples of the reports, right click one of the links and save to your file system.  You can then open them in your browser.
- [SuiteHealthChecker.html](SampleFiles/SuiteHealthChecker.html)
  - This file is a comprehensive report of the system configuration and results of all health check operations
- [SuiteHealthChecker-Failures.html](SampleFiles/SuiteHealthChecker-Failures.html)
  - This is a subset of the primary report which only contains warnings and failures.  



## Requirements

This automation was built and tested to run on RedHat 7 implementations only.

In order to execute an ISALite health check, the services and database tier must be running.  The role will do a precheck to ensure a service call reaches the database.

If the isadmin credentials were changed post install, the role will fail until some manual steps are taken to populate authentication and response files with the appropriate encrypted credentials.

## Role Workflow

This role will attempt to execute the following steps:

1.  Verify the target host is running IBM Information Server.  If no install path can be identified in /etc/services for dsrpc (Datastage), the job will exit.
2.  Compare the installed version of ISALite on the target host with the one in this package.  If lower, replace the version on the target.
3.  Create directories under the ansible user's home directory for storing reports and configurations, if they don't already exist.
4.  Generate a host specific response file and store in the config directory
5.  Create auth file to allow encrypted credential calls to automation (***no plain text passwords anywhere***)
6.  Run precheck to verify system is up with basic connectivity/
7.  Execute ISALite healthcheck

The compressed files from the health check will be stored in the:
>/home/( ansible_user )/IISDS_Healthcheck/reports path

## Running a Report

### From Tower or AWX

Execute the template "ansible-iisds-healthcheck" and enter the target host(s) in the limit field.

### From a Local Clone

CLI playbook syntax example.  Run from local clone directory:

>ansible-playbook -i ~/inventory -l hostname* createReport.yml

## Miscellaneous

