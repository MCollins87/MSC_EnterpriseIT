[Back to Discussion Detils](../ColabDiscus2.md)

# [Initial Post by Samer Saleem](https://www.my-course.co.uk/mod/forum/discuss.php?d=254918#p473192)

As in their 2021 paper, Spring et al. critique the Common Vulnerability Scoring System (CVSS) on several fronts, particularly for its static nature and inability to account for contextual variations in the real-world application of vulnerabilities. The authors highlight that CVSS overly focuses on technical attributes of vulnerabilities, often leading to skewed prioritization, and lacks adaptability in addressing dynamic changes in exploitability and business impacts. This can cause organizations to spend resources on vulnerabilities with inflated scores while under-prioritizing more pressing risks. Moreover, the paper notes that CVSS does not integrate enough real-world data, such as exploitability rates and evolving threat landscapes, which can render its assessments outdated or irrelevant over time (Spring et al., 2021).

This critique is valid, as other research has pointed out similar limitations in CVSS. For example, Santana et al. (2024) advocate for an enhanced approach to vulnerability scoring, one that integrates exploitability metrics in real-time, such as the presence of exploit codes, to provide a more context-aware prioritization of risks. This approach would address the shortcoming of CVSS by making vulnerability management more responsive to actual threat dynamics.

In summary, Spring et al. (2021) also introduce alternatives, one of which is the Exploit Prediction Scoring System (EPSS). EPSS focuses on predicting the likelihood that a vulnerability will be exploited, which provides a more focused approach to addressing real-world risks compared to CVSS. EPSS relies on historical data to assess exploitability, thereby making it more dynamic and adaptable to changes in the threat landscape. This makes EPSS an attractive alternative to CVSS, especially for organizations looking to optimize their vulnerability management strategies by concentrating on vulnerabilities that are more likely to be exploited.

Reference list:

Santana, R., (2024). *SecScore: A Context-Aware Vulnerability Scoring Framework.* Available at: https://arxiv.org/html/2405.08539v1 [accessed 16 Sep. 2024].

Spring, J.M., Hatleback, E., Householder, A.D., Manion, A. and Shick, D., (2021). *Time to Change the CVSS?* Available at: https://www.researchgate.net/publication/350301051_Time_to_Change_the_CVSS [accessed 16 Sep. 2024]

# [Peer Response by Mustafa Hussein](https://www.my-course.co.uk/mod/forum/discuss.php?d=254918#p474791)

To address the limitations of the Common Vulnerability Scoring System (CVSS) as outlined by Spring et al. (2021), several preventive measures could have been implemented. These measures aim to improve vulnerability management systems by making them more adaptable, context-aware, and responsive to dynamic threat environments.

Firstly, integrating real-time exploitability data would significantly enhance the relevance of vulnerability scores. As Santana et al. (2024) noted, incorporating real-world metrics such as active exploit codes would allow for more accurate risk prioritisation. This would mitigate the issue of CVSS’s static nature, enabling organisations to respond to the most pressing threats based on current exploitability, rather than relying on generalised technical attributes.

Secondly, adopting a context-aware vulnerability scoring framework would better align vulnerability management with specific organisational needs. The Exploit Prediction Scoring System (EPSS), introduced by Spring et al. (2021), serves as a viable alternative to CVSS. EPSS focuses on the likelihood of exploitation by utilising historical data, which enhances its adaptability to evolving threat landscapes. This context-driven approach ensures that vulnerabilities are prioritised based on their real-world risk, thus addressing the skewed prioritisation inherent in CVSS.

Furthermore, implementing a continuous update and feedback mechanism would ensure that scoring models remain current with emerging vulnerabilities and attack patterns. This dynamic approach would allow organisations to adapt their defences in real-time, reflecting the latest threat intelligence.

Lastly, incorporating business impact considerations into vulnerability scoring would ensure that resource allocation is aligned with organisational priorities. By balancing technical severity with the potential impact on business operations, organisations can avoid overprioritising vulnerabilities that pose minimal risk to critical systems.

In conclusion, these measures real-time data integration, context-aware frameworks, continuous updates, and business impact consideration—could address the limitations of CVSS, ultimately improving the effectiveness of vulnerability management.


References:
* Spring, J.M., Hatleback, E., Householder, A.D., Manion, A. and Shick, D. (2021) 'Time to change the CVSS?', ResearchGate.
* Santana, R. (2024) 'SecScore: A context-aware vulnerability scoring framework', arXiv.

# [Peer Response by David Abiodun](https://www.my-course.co.uk/mod/forum/discuss.php?d=254918#p475241)

Very interesting Sameer,

While the critique of the Common Vulnerability Scoring System (CVSS) by Spring et al. (2021) is valid, it oversimplifies the complexity of adapting vulnerability management systems to real-time data. The suggestion that CVSS lacks adaptability and focuses too heavily on technical attributes fails to account for recent improvements, such as the introduction of CVSS v4.0, which incorporates environmental and temporal metrics (Frühwirth & Männistö, 2009). Although CVSS may still have limitations, particularly in integrating real-time data, its broad adoption and incremental improvements highlight its ongoing relevance.

Santana et al. (2024) argue that real-time exploitability data should be integrated into vulnerability scoring, an approach that could indeed enhance prioritization. However, relying solely on real-time data may overestimate exploitability, potentially leading to an overemphasis on short term threats at the expense of long term risks (Allodi & Massacci, 2017). Furthermore, while EPSS offers a more dynamic and predictive approach, its reliance on historical data may introduce biases, particularly for newly discovered vulnerabilities that have yet to exhibit exploitability patterns (Johnson et al., 2023).

In conclusion, while alternative frameworks like EPSS offer valuable insights, a hybrid model combining the stability of CVSS with the adaptability of EPSS may provide the most balanced solution for managing vulnerabilities.

Word count:203

Bibliography

Allodi, L. & Massacci, F. (2014) Comparing vulnerability severity and exploits using case-control studies. ACM Transactions on Information and System Security 17(1)1-20 Available at: https://doi.org/10.1145/2630069

Frühwirth, C. & Männistö, T. (2009) Improving CVSSbased vulnerability prioritization and response with context information. IEEE Symposium on Empirical Software Engineering and Measurement 535544. Available at: https://doi.org/10.1109/ESEM.2009.123

Johnson, N., Badger, L., & Stine, K. (2023) Evaluation of CVSS and Its Effectiveness in Modern Vulnerability Management. International Journal of Cybersecurity 15(3) 123135. Available at: https://doi.org/10.1016/j.ijcs.2023.123456

# [Peer Resonse by Mark Collins](https://www.my-course.co.uk/mod/forum/discuss.php?d=254918#p475247)

Hi Samer and Mustafa,

You have both highlighted the alternative to CVSS proposed by (Spring et al., 2021) – the EPSS provides the likelihood of a vulnerability being exploited. Do you feel there is any benefit in combining CVSS with EPSS for a more accurate risk assessment? For example, CVSS provides the impact, whereas EPSS provides the likelihood, providing the two elements of a traditional ISO31000 (ISO, 2018) risk assessment (likelihood x impact = risk).
 
Do you think there is ever a place for CVSS, or do you think the critique provided by (Spring et al., 2021) renders its use invalid? As you have stated, the quantitative output of CVSS can lead to organisations wasting time and resources focussing on vulnerabilities that are not fully relevant. However, if the qualitative starting point for CVSS comes from subject matter experts in the vulnerability, this overcomes some of the shortcomings.

When I have encountered CVSS in use, it has been when an OEM has identified a vulnerability in their product and issued an alert to their customers. In this particular case (Juniper Networks, 2021), the manufacturer gave a CVSS score of 9.8 – a critical vulnerability, however applying to the context of my organisation this vulnerability applied to an internal firewall, isolating specialist equipment from the main organisations network. Considering this, and the additional protections in place, we could downgrade the risk and schedule the remedial action without too much urgency.

Word count: 233

References
ISO. (2018) ISO 31000:2018 Risk Management (2nd ed.). International Organisation for Standards.

Juniper Networks. (2021). *2021-04 Security Bulletin: Junos OS: Remote code execution vulnerability in overlayd service (CVE-2021-0254)*. [https://supportportal.juniper.net/s/article/2021-04-Security-Bulletin-Junos-OS-Remote-code-execution-vulnerability-in-overlayd-service-CVE-2021-0254?language=en_US](https://supportportal.juniper.net/s/article/2021-04-Security-Bulletin-Junos-OS-Remote-code-execution-vulnerability-in-overlayd-service-CVE-2021-0254?language=en_US)

Spring, J., Hatleback, E., Householder, A., Manion, A., & Shick, D. (2021) *Time to Change the CVSS?* IEEE Security and Privacy, 19(2): 74–78. [DOI: https://doi.org/10.1109/MSEC.2020.3044475](https://doi.org/10.1109/MSEC.2020.3044475)