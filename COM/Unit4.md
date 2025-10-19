[Back to Module](./README.md)

# Unit 4 Formative Activity

## Brief
 *Develop and execute a Bash script to automate the provisioning of cloud resources on an OpenStack cloud platform. The script should create a new instance, configure it, and run basic commands automatically.*

For this activity, I had to first provision a Virtual Machine (VM) on OCI. I then attempted to install both OpenStack and Devstack. However I encountered numerous issues which required allot of debugging and troubleshooting. More than the formative nature of the activity warranted. There were times when deploying DevStack would run without issue, but when I attempted to incorporate into a bash script, it would fail. Even a simple script that called the `./stack.sh` script would produce errors.

Eventually, I decided to approach the exercise differently, and write a bash script to run in the Oracle Command line Interface (CLI) to provision an instance on OCI. For this, I made extensive use of the `oci -i` command, which provided interactive support with options for commands.

The first section of the script defined the variables. Documentation (Oracle, 2025) suggested I could create dynamic variables, where I could read the existing Compartment ID, Sub Net ID, and find an appropriate Image and Shape, I decided to simplify the process and use methodology I have in the past - do the process manually first, and record all the relevant information for use in future automation scripts. I therefore created an instance manually and used the OCID values for Compartment, Sub net, Image and Shape.

I also included an if statement as part of my troubleshooting process while I was attempting to dynamically find an the latest available version of my chosen image. Although, on reflection, if I were to be doing this on an enterprise scale, and using scripting to deploy cloud instances, I would most likely have a custom image with required software and services preinstalled, so using a fixed OCID in this case would be appropriate.

The next section was simply the deploy instance command with all the relevant options required. This is where the `oci -i` command/environment came into its own, helping provide the correct syntax for the launch instance command.

Once the instance was running, the script obtains the public IP to allow `ssh` to the new instance, before running simple Ubuntu/Debian update and upgrade commands.

#### Learning outcomes
This was an interesting unit, where it helped understand the concept of Infrastructure as Code (IaC). I could see the benefit of scripting the deployment of instances to allow expansion as demand increased. The simple commands run via `ssh` can be expanded to configure the compute instance to run required services, or for new Block Storage instances to automatically mount to certain locations. Of course, enterprise deployments would use more sophisticated tools such as *Terraform* for cross-platform deployment(Bavadiya, 2021; Spitzenbuerger and Dinu, 2025).

If I were to approach this task again, I would probably take advantage of the OCI developer interface, providing a built-in IDE within the cloud environment. Instead I scripted everything using `vim`, although there is something quite nostalgic at using tools that many consider outdated (Oliveira and Zuchi, 2020).

[**Developed Script**](./Unit4/OCI_prov.sh)

## References

Bavadiya, P. (2021) ‘OPTIMIZING CLOUD INFRASTRUCTURE DEPLOYMENTS USING INFRASTRUCTURE AS CODE: A COMPARATIVE STUDY OF TERRAFORM AND CLOUDFORMATION’, _International Journal of Innovation Studies_, 5(1).

Oracle (2025) _Oracle Cloud Infrastructure Documentation_. Available at: [https://docs.oracle.com/en-us/iaas/Content/home.htm](https://docs.oracle.com/en-us/iaas/Content/home.htm) (Accessed: 18 October 2025).

Spitzenbuerger, C. and Dinu, F. (2025) _Terraform vs. AWS CloudFormation - Ultimate Comparison_, _Spacelift_. Available at: [https://spacelift.io/blog/[slug]](https://spacelift.io/blog/[slug]) (Accessed: 20 September 2025).