In their paper Spring et al. (2021) identify a number of shortcomings with the Common Vulnerability Scoring System (CVSS), namely:

-	Lack of transparency in how the formula used is derived.
-	Lack of context to specific industries.
-	Does not consider material consequences.
-	Inconsistencies in initial scoring.
-	
Additionally, they argue that the output of a risk assessment should be action categories, and not integers, and that it fails as a risk assessment tool because it provides severity score, not risk.

The authors propose an alternative Stakeholder-Specific Vulnerability Categorisation (SSVC) as a solution to many of the failings of CVSS (Spring et al., 2020).
Whilst many of the arguments presented by Spring et al. (2021) are true, and there are flaws to CVSS, it has the potential to be a useful tool when used in the right context. 

From personal experience, an integer score is very useful when presenting risk to top-level management. It is a clear way to show quantitative return on investment for any expense required to resolve the risk. 

When receiving Cyber Alerts which have been issued by manufactures (Juniper Networks, 2021; NHS Digital, 2024), the CVSS score is useful, since it has been calculated by product specialists. An organisation can then apply their own context scoring to assess the impact of this particular vulnerability on their business operations. 
One manufacturer I work closely with applies the following guidelines (Varian, 2021): 

*Varian uses the CVSS (Common Vulnerability Scoring System) to review the latest list of vulnerabilities.  During the assessment:-*

- *CVSS scores 3.9 and below are accepted as is.*
- *CVSS scores 4.0 to 8.9 are reviewed on a quarterly basis and evaluated for applicability.  For example, Varian does not use DHCP/IPv6 and so these vulnerabilities are not applicable. Those vulnerabilities that are applicable are analysed and depending on the risk analysis will confirm the next steps of accepting it or mitigating the risk with a change of configuration or updating the firmware.  Any changes or updates will be documented in the Service Technical Bulletin (STB) process and released once qualified with the medical device.*
- *CVSS scores 9.0 and above trigger an emergency cybersecurity risk assessment, by the product security team.*

References:
- Juniper Networks. (2021). *2021-04 Security Bulletin: Junos OS: Remote code execution vulnerability in overlayd service (CVE-2021-0254)*. Available from: https://supportportal.juniper.net/s/article/2021-04-Security-Bulletin-Junos-OS-Remote-code-execution-vulnerability-in-overlayd-service-CVE-2021-0254?language=en_US [Accessed 9 September 2024]
- NHS Digital. (2024). *Cyber Alerts*. Available from: https://digital.nhs.uk/cyber-alerts [Accessed 9 September 2024]
- Spring, J., Hatleback, E., Householder, A., Manion, A., & Shick, D. (2021) Time to Change the CVSS? *IEEE Security and Privacy*, 19(2): 74–78. DOI: https://doi.org/10.1109/MSEC.2020.3044475
- Spring, J. M., Hatleback, E., Householder, A., Manion, A., & Shick, D. (2020) Prioritizing Vulnerability Response: a Stakeholder-Specific Vulnerability Categorization. *Workshop on the Economics of Information Security* Carnegie Mellon University Software Engineering Institute.
- Varian Medical Systems (2021), Email to Mark Collins, 26 April.
