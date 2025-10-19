[Back to Module](./README.md)

## Introduction
The module *Cloud Operations Management* has revealed a number of learning points. My approach to the module was initially theoretical. There were many exercises involving OpenStack, which while as a software is Free and Open Source Software (FOSS), there are hardware requirements, where it is recommended the host exceeds 4 cores, and 8GB RAM (Openstack, 2025). Unfortunately my home system only just met those specs. Also, for the best experience, a fresh Linux install is recommended, and I was unwilling to loose existing configuration.

During the closing weeks of the module, I decided to begin a free trial on a cloud infrastructure environment - Oracle Cloud Infrastructure (OCI) (Oracle, 2025). Within this environment, I revisited a number of practical formative activities, which are discussed here.

## [Unit 4 - Bash Script for Provisioning Cloud Platform](./Unit4.md)
**Brief:** *Develop and execute a Bash script to automate the provisioning of cloud resources on an OpenStack cloud platform. The script should create a new instance, configure it, and run basic commands automatically.*

For this activity, I had to first provision a Virtual Machine (VM) on OCI. I then attempted to install both OpenStack and Devstack. However I encountered numerous issues which required allot of debugging and troubleshooting. More than the formative nature of the activity warranted. There were times when deploying DevStack would run without issue, but when I attempted to incorporate into a bash script, it would fail. Even a simple script that called the `./stack.sh` script would produce errors.

Eventually, I decided to approach the exercise differently, and write a bash script to run in the Oracle Command line Interface (CLI) to provision an instance on OCI. For this, I made extensive use of the `oci -i` command, which provided interactive support with options for commands.

The first section of the script defined the variables. Documentation (Oracle, 2025) suggested I could create dynamic variables, where I could read the existing Compartment ID, Sub Net ID, and find an appropriate Image and Shape, I decided to simplify the process and use methodology I have in the past - do the process manually first, and record all the relevant information for use in future automation scripts. I therefore created an instance manually and used the OCID values for Compartment, Sub net, Image and Shape.

I also included an if statement as part of my troubleshooting process while I was attempting to dynamically find an the latest available version of my chosen image. Although, on reflection, if I were to be doing this on an enterprise scale, and using scripting to deploy cloud instances, I would most likely have a custom image with required software and services preinstalled, so using a fixed OCID in this case would be appropriate.

The next section was simply the deploy instance command with all the relevant options required. This is where the `oci -i` command/environment came into its own, helping provide the correct syntax for the launch instance command.

Once the instance was running, the script obtains the public IP to allow `ssh` to the new instance, before running simple Ubuntu/Debian update and upgrade commands.

#### Learning outcomes
This was an interesting unit, where it helped understand the concept of Infrastructure as Code (IaC). I could see the benefit of scripting the deployment of instances to allow expansion as demand increased. The simple commands run via `ssh` can be expanded to configure the compute instance to run required services, or for new Block Storage instances to automatically mount to certain locations. Of course, enterprise deployments would use more sophisticated tools such as *Terraform* for cross-platform deployment(Bavadiya, 2021; Spitzenbuerger and Dinu, 2025).

If I were to approach this task again, I would probably take advantage of the OCI developer interface, providing a built-in IDE within the cloud environment. Instead I scripted everything using `vim`, although there is something quite nostalgic at using tools that many consider outdated (Oliveira and Zuchi, 2020).

## [Unit 5 - Deploy a 12-Factor App using Docker and Manage it through Kubertetes](./Unit5.md)
**Brief:** *Deploy a 12-Factor App using Docker and manage it through Kubernetes. Set up a local Kubernetes cluster using Minikube and deploy a containerised application following the 12-Factor methodology.*

For this activity, I was able to perform on my local machine. I was able to build a simple python app adhering to the 12-Factor principles (Wiggins, 2017).

The use of Docker and Kubernetes helps in adhering to 12-factor principles. Breaking down by each principle:

1. **Codebase**:
    - Docker helps encapsulate the codebase into containers, ensuring consistency across environments.
    - Kubernetes can manage multiple services (microservices) that share the same codebase or are part of the same system.
2. Dependencies:
    - Docker images explicitly declare dependencies in Dockerfile, isolating them from the host system.
    - This supports the principle of dependency declaration and isolation.
3. Config:
    - Kubernetes uses ConfigMaps and Secrets to manage configuration separately from code.
    - This aligns with the principle of storing config in the environment.
4. Backing Services:
    - Kubernetes treats backing services (like databases, caches) as attached resources, which can be dynamically bound and replaced.
    - Docker can link containers to services, but Kubernetes makes this more dynamic and scalable.
5. Build, Release, Run:
    - Docker separates build (image creation) from run (container execution).
    - Kubernetes supports CI/CD pipelines and separates deployment stages clearly.
6. Processes:
    - Docker containers run as stateless processes.
    - Kubernetes manages these processes, ensuring they are ephemeral and scalable.
7. Port Binding:
    - Docker exposes services via ports.
    - Kubernetes uses Services and Ingress to manage port binding and routing.
8. Concurrency:
    - Kubernetes scales apps horizontally by running multiple container instances (pods).
    - This supports concurrency through process model scaling.
9. Disposability
    - Docker containers can be started and stopped quickly.
    - Kubernetes handles container lifecycle, restarts failed containers, and supports graceful shutdowns.
10. Dev/Prod Parity
    - Docker ensures environment parity between development, staging, and production.
    - Kubernetes can replicate production-like environments locally using tools like Minikube or Kind.
11. Logs
    - Docker outputs logs to stdout/stderr.
    - Kubernetes aggregates logs and integrates with logging systems like Fluentd, ELK, or Prometheus.
12. Admin Processes
    - Admin tasks can be run in one-off Docker containers.
    - Kubernetes supports Jobs and CronJobs for running admin or maintenance tasks.

This activity helped me understand Kubernetes and Docker in more detail. Prior to this, they were concepts that I didn't really have much of a grasp on, but troubleshooting this activity, and in particular creating a Dockerfile, allowed the concept of containerisation to finally make sense.

## [Unit 8 - Disaster Recovery using Duplicity](./Unit8.md)
**Brief:** *Design and implement a Disaster Recovery (DR) plan for a cloud-based infrastructure on OpenStack. Simulate a failure scenario and perform a recovery operation using open-source backup tools such as Bacula or Duplicity.*

Again for this activity, I did not use an Open stack environment, but a Ubuntu 24.04 running on Oracle Cloud Infrastructure.

For the proof of concept, I set the back-up location to be locally on the same machine, however if deploying to production, I would use a remote location (e.g. `oci://bucket@namespace`).

The use of automation, for example using `crontab`, can be used to achieve the RPO and RTO required for the particular scenario.

Additional improvements to simply backing up data, is to create some scripts that automate the testing of the back-up process (Ganesan, 2024). Also, depending on the RPO/RTO the frequency of back-ups may mean the storage becomes full. Scripting can be used to remove some of the older back-ups. A policy I have personally implemented has been to perform incremental back-ups during the week, and then full back-ups at the weekend, when the systems I am responsible are not in use (reducing computing burden). I then remove older back-ups, once the need to retrieve the state at that time is no longer required.

## [Unit 9 - Restore SQL](./Unit9.md)
**Brief:** *Migrate a database from a local machine to an OpenStack cloud environment using MySQL and Percona XtraBackup (open-source tools). Demonstrate data consistency and minimal downtime during migration.*

Again the migration was to an OCI environment (the same compute instance used previously).

This activity took advantage of the *Hot Back-up* feature of Percona XtraBackup (Percona LLC, 2025). The advantage of Hot Back-ups is that incremental back-ups can be performed while the database is live and the MySQL services are running. This allows for users to continue using the original database while the new location is prepared.

Within a production environment, I would most likely follow the following steps:

1. Perform full back-up with:
2. Prepare the remote / new environment (Unit 4).
3. Transfer full back-up to new location.
4. Restore full back-up in new location.
5. Test migration
6. Place original database into Lock state.
7. Perform incremental back-up.
8. Transfer to new location.
9. Restore incremental back-up, adding the changes since full back-up.
10. Point any services relying on database to new location and restart MySQL services.

The advantage to running a migration this way is that it results in minimal downtime. By performing the Full back-up while the Database is still running, allows for no downtime while the longest task takes place. In theory, within a production environment, this database could be many GB or even TB resulting in allot of time to perform back-up, transfer and restore in new location.

Once the new location is fully prepared and tested, the existing production database can be stopped to prevent any data loss, an incremental back-up can be performed to capture any changes and then this much smaller dataset can be transferred and restored before pointing any services that use the database to the new location.

Additionally, if the preparation of the new environment, including the transfer and restore takes a long time, and the database has many transactions, additional hot incremental backups can be performed and restored during operational with the final back-up and restore and configuration occurring out of hours, further mitigating risk of data loss or service downtime.

## [Unit 11 - Deploy an AI model](./Unit11.md)
**Brief:** *Using TensorFlow and Keras (both open-source AI tools), build and deploy a simple AI model for image recognition on OpenStack/OCI.*

This activity was a really good activity to finish off with, as it took advantage of earlier learning regarding Docker and Kubernetes.

I was able to build and train a model using TensorFlow and the CIFAR-10 dataset (Aslam and Nassif, 2023).

I was then able to wrap the model and "dockerise" using the learning from [Unit 5](./Unit5.md), before pushing to a cluster on the Oracle Kubernetes Engine (OKE).

Once pushed, I was able to deploy the model and and implement a load balancer using simple `yaml` files. I then produced a small python script to generate a random image array and request a response.

This activity felt as if it was pulling together all the previous learning from the module and applying it in a way that is directly related to the future of cloud computing. The use of AI in the cloud has many applications:

1. Intelligent Resource Management.
2. Anomaly Detection and Predictive Maintenance.
3. Smart Scheduling and Orchestration.
4. Security Compliance Automation.
5. DevOps Acceleration.

This formative activity demonstrates how AI models can be effectively deployed and evaluated in a cloud-native environment using OCI and Kubernetes. Beyond application-level benefits, AI has the potential to transform cloud infrastructure itself — making it more intelligent, adaptive, and efficient.

## Conclusion and final reflections
This module has been a steep learning curve for me. I had very little prior knowledge or experience with cloud infrastructure. In my day job, I manage applications that are hosted on a private cloud, but have very little input to the infrastructure management, other than knowing how to ask for horizontal expansion for our Citrix VDA's.

The greatest learning experience was practically building on a public cloud, in this case Oracle Cloud Infrastructure. I really struggled getting anything related to OpenStack to work on the hardware I had available to me, and waited until the end of the module to begin a free trial on OCI. I think this module would greatly benefit from the University provisioning some sort of bare metal infrastructure, and providing step by step guides to deploy OpenStack the students could use as test labs for the formative activities.

One surprising reflection from this module was how I used popular Large Language Models such as ChatGPT and Copilot to help with troubleshooting (France, 2024). When errors occurred, the ability to copy and paste the command line output and have the error identified, along with a suggested fix sped the process significantly, compared to analysing line by line, looking for key words with tired eyes. Of course it is not perfect, and on occasion I encountered cyclical errors i.e. ChatGPT would suggest a fix that didn't work, and the subsequent suggested fix produced the original error.

Overall this module has been valuable in teaching new concepts that are becoming more essential in the field of Enterprise IT Management.

## References

Aslam, S. and Nassif, A.B. (2023) ‘Deep learning based CIFAR-10 classification’, in _2023 Advances in Science and Engineering Technology International Conferences (ASET)_, pp. 01–04. Available at: [https://doi.org/10.1109/ASET56582.2023.10180767](https://doi.org/10.1109/ASET56582.2023.10180767).

Bavadiya, P. (2021) ‘OPTIMIZING CLOUD INFRASTRUCTURE DEPLOYMENTS USING INFRASTRUCTURE AS CODE: A COMPARATIVE STUDY OF TERRAFORM AND CLOUDFORMATION’, _International Journal of Innovation Studies_, 5(1).

France, S.L. (2024) ‘Navigating software development in the ChatGPT and GitHub Copilot era’, _Business Horizons_, 67(5), pp. 649–661. Available at: [https://doi.org/10.1016/j.bushor.2024.05.009](https://doi.org/10.1016/j.bushor.2024.05.009).

Ganesan, P. (2024) ‘Cloud-Based Disaster Recovery: Reducing Risk and Improving Continuity’, _Journal of Artificial Intelligence & Cloud Computing_, pp. 3–1. Available at: [https://doi.org/10.47363/JAICC/2024(3)E162](https://doi.org/10.47363/JAICC/2024\(3\)E162).

Oliveira, B.C. de and Zuchi, J.D. (2020) ‘EFFICIENCY IN WRITING SOFTWARE WITH VIM’, _Revista Interface Tecnológica_, 17(2), pp. 386–397. Available at: [https://doi.org/10.31510/infa.v17i2.1066](https://doi.org/10.31510/infa.v17i2.1066).

Openstack (2025) _Overview — Installation Guide documentation_. Available at: [https://docs.openstack.org/install-guide/overview.html#figure-hwreqs](https://docs.openstack.org/install-guide/overview.html#figure-hwreqs) (Accessed: 18 October 2025).

Oracle (2025) _Oracle Cloud Infrastructure Documentation_. Available at: [https://docs.oracle.com/en-us/iaas/Content/home.htm](https://docs.oracle.com/en-us/iaas/Content/home.htm) (Accessed: 18 October 2025).

Percona LLC (2025) _Percona XtraBackup_. Available at: [https://docs.percona.com/percona-xtrabackup/](https://docs.percona.com/percona-xtrabackup/) (Accessed: 19 October 2025).

Spitzenbuerger, C. and Dinu, F. (2025) _Terraform vs. AWS CloudFormation - Ultimate Comparison_, _Spacelift_. Available at: [https://spacelift.io/blog/[slug]](https://spacelift.io/blog/[slug]) (Accessed: 20 September 2025).

Wiggins, A. (2017) _The Twelve-Factor App_. Available at: [https://12factor.net/](https://12factor.net/) (Accessed: 18 October 2025).