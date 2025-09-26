[Back to Module](./README.md)

# Unit 3 Formative Activity

## Formative Discussion: Cloud Design Tools

### Brief
Choose a cloud design tool and explain, with reasons, why you believe it to be a superior tool compared to others.

This should be 300 words (excluding references).

### Post

Two tools used to design and manage Cloud Infrastructure are _Terraform_ from HashiCorp and AWS _CloudFormation_ (Bavadiya, 2021; Spitzenbuerger and Dinu, 2025). Both have their advantages over the other, but also disadvantages. 

### AWS Cloudformation

Amazon Web services is the ideal solution if AWS is the only environment the cloud infrastructure is being deployed. 

It is native to AWS and always supports new AWS features. It uses the widely used JSON and YAML languages, which while difficult to learn, once mastered can be used in a variety of applications. 

When it comes to scaling and enterprise deployment, CloudFormation can use StackSets to deploy to multiple AWS accounts/regions, providing tight governance with Identity Access Management (IAM).

#### Terraform

Terraform uses its own HCL language (HashiCorp Configuration Language), which while being unique to Terraform, is also concise, human readable and modular, making it easy to use and a relatively shallow learning curve. 

Terraform works with multiple cloud providers such as AWS, Azure, and GCP and many more, making this an ideal choice when implementing multi-cloud or hybrid cloud environments. However support for new features often lags when compared to native tools. 

There is a large open source community supporting Terraform, with a significant registry of reusable modules and strong third-party integrations. 

#### Conclusion

Depending on context, both CloudFormation and Terraform are both strong contenders for being superior Cloud Design Tools for deploying Infrastructure as Code (IaC). 

If vendor lock-in is less of a concern, and support for latest features and ease of scaling are important, then AWS CloudFormation is a superior choice if AWS is the only cloud service being used. However, if vendor lock-in is a concern, or due to regulatory requirements a hybrid cloud approach is required, then Terraform is the superior choice. 

### References
Bavadiya, P. (2021) ‘OPTIMIZING CLOUD INFRASTRUCTURE DEPLOYMENTS USING INFRASTRUCTURE AS CODE: A COMPARATIVE STUDY OF TERRAFORM AND CLOUDFORMATION’, _International Journal of Innovation Studies_ [Preprint].

Spitzenbuerger, C. and Dinu, F. (2025) _Terraform vs. AWS CloudFormation - Ultimate Comparison_, _Spacelift_. Available at: [https://spacelift.io/blog/[slug]](https://spacelift.io/blog/[slug]) (Accessed: 20 September 2025).