[Back to Discussion Details](../ColabDiscus2.md)

# [Peer Response by Gesine Linn Hamburger](https://www.my-course.co.uk/mod/forum/discuss.php?d=253527#p475071)

Hi Mark,

You’ve made some great points about the practical use of the Common Vulnerability Scoring System (CVSS), especially when presenting risks to top-level management. I agree that the simplicity of an integer score can be incredibly effective for communicating complex technical risks to non-technical stakeholders. It provides a clear, quantifiable metric that helps decision-makers see the value of risk mitigation efforts, which aligns well with established risk management frameworks (NIST, 2018).

However, I think Spring et al. (2021) are right in pointing out that CVSS has significant limitations, particularly the lack of context and consideration of material consequences. While you’ve illustrated how organizations like Varian adjust CVSS to their own environments, this requires a level of customization that smaller organizations or less experienced teams may not have the resources to perform. The issue with relying too heavily on CVSS alone is that it can lead to oversimplification of risks, which may not always capture the full impact on a specific business sector.

I also agree with Spring et al.’s (2020) argument that risk assessment should focus on actionable categories rather than just severity scores. While CVSS does a good job of highlighting the "what" (i.e., the severity of the vulnerability), it doesn't always address the "how" and "what next" in terms of specific actions organizations should take. This is where something like SSVC could add value by providing clearer guidance on prioritization.

So, while CVSS is useful, especially when combined with internal context, it could benefit from being part of a broader, more flexible framework like SSVC to avoid oversights.

Word count: 261

References:

* NIST (2018) *Framework for Improving Critical Infrastructure Cybersecurity*(Version 1.1) [DOI: https://doi.org/10.6028/NIST.CSWP.04162018](https://doi.org/10.6028/NIST.CSWP.04162018)

* Spring, J., Hatleback, E., Householder, A. (2020) *A Stakeholder-Specific Vulnerability Categorization*. [Podcast]. Available from: [https://insights.sei.cmu.edu/library/a-stakeholder-specific-vulnerability-categorization/](https://insights.sei.cmu.edu/library/a-stakeholder-specific-vulnerability-categorization/) [Accessed 22 September 2024]

* Spring, J., Hatleback, E., Householder, A., Manion, A., & Shick, D. (2021) Time to Change the CVSS? *IEEE Security and Privacy* 19(2): 74–78. [DOI: https://doi.org/10.1109/MSEC.2020.3044475](https://doi.org/10.1109/MSEC.2020.3044475)

# [Summary Post](https://www.my-course.co.uk/mod/forum/discuss.php?d=253527#p476580)

Hi Gesine,

Thank you for your comments.

There is no doubt that there are flaws with CVSS as outlined by Spring et al., (2021), however we should be careful not to dismiss it entirely. It is one of the most widely used scoring systems, and Wunder et al., (2024) listed six alternatives, each of which will have its advantages over CVSS, but will also have flaws.

Wunder et al., (2024) found that attitudes towards CVSS in industry is that it is both problematic and useful. They cited several opinions, ranging from “veneer of objectivity used to justify whatever subjective opinion the scorer brings with them” to “for certain vulnerability types, CVSS is a good scoring system. However, there are so many aspects of security that CVSS is not suitable for scoring, yet clients still request CVSS to be used as it’s “known”, even where it is not suitable” (Wunder et al., 2024).

The example I have used prior when experiencing CVSS relates to a remote execution on a firewall (Juniper Networks, 2021). This vulnerability was given a score of 9.8 by the manufacturer, which given firewalls are used to protect against threats, this is understandable. If an organisation were to implement this firewall as their main firewall, then they would be exposed to considerable risk. However, our implementation of this firewall was internal, and used only to isolate medical equipment from the wider network. Our network has multiple levels of security, adopting a Swiss-cheese approach (Wiegmann et al., 2022) to reducing risk. As such, we were able to apply our organisation specific context and continue with daily operations and schedule a firmware update when convenient.

The main issue with CVSS is that without considering the specific implementation of a system, the severity is going to vary widely, and no tool can do this accurately. CVSS is a useful tool for communicating vulnerabilities across organisations and industries, however it is important for those responsible for implementing said systems to understand how a particular vulnerability affects the implemented solution.

Word Count: 355

References

* Juniper Networks. (2021) *2021-04 Security Bulletin: Junos OS: Remote code execution vulnerability in overlayd service (CVE-2021-0254)*. [https://supportportal.juniper.net/s/article/2021-04-Security-Bulletin-Junos-OS-Remote-code-execution-vulnerability-in-overlayd-service-CVE-2021-0254?language=en_US](https://supportportal.juniper.net/s/article/2021-04-Security-Bulletin-Junos-OS-Remote-code-execution-vulnerability-in-overlayd-service-CVE-2021-0254?language=en_US)

* Spring, J., Hatleback, E., Householder, A., Manion, A., & Shick, D. (2021) Time to Change the CVSS? *IEEE Security and Privacy*, 19(2): 74–78. [DOI: https://doi.org/10.1109/MSEC.2020.3044475](https://doi.org/10.1109/MSEC.2020.3044475)

* Wiegmann, D. A., Wood, L. J., Cohen, T. N., & Shappell, S. A. (2022) Understanding the “swiss Cheese Model” and Its Application to Patient Safety. *Journal of Patient Safety*, 18(2): 119–123. [DOI: https://doi.org/10.1097/PTS.0000000000000810](https://doi.org/10.1097/PTS.0000000000000810)

* Wunder, J., Kurtz, A., Eichenmüller, C., Gassmann, F., & Benenson, Z. (2024) Shedding Light on CVSS Scoring Inconsistencies: A User-Centric Study on Evaluating Widespread Security Vulnerabilities. *2024 IEEE Symposium on Security and Privacy (SP)*, 1102–1121. [DOI: https://doi.org/10.1109/sp54263.2024.00058](https://doi.org/10.1109/sp54263.2024.00058)