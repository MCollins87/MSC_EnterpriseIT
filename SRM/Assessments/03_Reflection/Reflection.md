[Back to Module](../README.md)
# Reflection of Module *Security and Risk Management*

**Word Count**: 858

## Personal Reflections
Whilst the content of this module has been interesting, my ability to study for it has been challenged, mainly by the time of year. This is the first year my son has had a summer holiday from school, meaning I needed to try to balance work, university studies, and childcare/family activities. Traditionally, resources are stretched at work for similar reasons; colleagues also have family commitments during August and September, so there is increased annual leave and cross-cover to consider, so work pressures rise. 

Overall, I think my ability to balance competing demands has been successful. However, when I was able to take leave from work, the rest obtained on family holidays was countered by the stress of catching up with work and University; there have been many late nights preparing assignments for submission.

Moving forward, time management will need to be improved. Better communication with my family over what my other commitments are, and how best to plan activities together, while still doing what is required for both University and Work. 

## Security and Risk Management Reflections

Whilst I have significant experience in risk management from my years working in Medical Physics, this module has provided me with a fresh perspective. 

Previously, my focus has been on risk reduction, ensuring *Administrative* controls are adequate and easy to follow, and where possible, implementing *Engineering* Controls, as defined in the Hierarchy of Controls (de Castro, 2003). This module has allowed me to gain a fresh perspective on the additional levels of control, such as *Transference* of risk and aiming for an inherently safe design (*Elimination*). 

![Hierarchy of Risk, adapted from de Castro (2003)](./Assets/RiskHierachy.svg)

While this course has been running, I have been nominated by my employer to act as a Clinical Safety Officer (CSO), as defined by DCB0129 and DCB0160 (NHS Digital, 2024). This required industry-specific training in cyber security and risk management which has aided my studies for this module, and the module has helped with the CSO training. Something that was covered in the NHS-provided training that drew my interest, was the use of *Bowtie diagrams* in the identification of hazards and mitigations. (de Ruijter & Guldenmund, 2016). 

![An example of a Bow-tie diagram](./Assets/BowTie.svg)

Initially, these *Bowtie* diagrams look to be an extension of *Attack trees* covered in the module. On closer examination, *Attack trees* can be combined with *Bowtie* diagrams to provide a fuller picture of risk and its impacts. Further reflection and examination of the similarities and differences of the two methods of visualising and identifying risk, it can be seen where some of the shortcomings of CVSS arise, and how they can be resolved. 

Other than CVSS not being objectively Quantitative, since the starting point is Qualitative, the other main issue with CVSS is the lack of context. (Spring et al., 2021). A common use of CVSS is the communication of risk between industries through CVE alerts. Given the wide range of industries using IT systems (software and hardware), it is arguably both essential and impossible to accurately communicate risk scores when a vulnerability has been identified. This is where shared responsibility for risk needs to be clearly identified. 

An *Attack tree* can be used, either wholly or in part, as the left-hand side of the *bowtie* diagram. A CVE alert will identify vulnerabilities in the left-hand side of the *Bowtie* diagram, while a CVSS score will provide an indication of the severity and likelihood of the vulnerability being exploited, but not the impact on an organisation using the IT system. This is where the right-hand side of the *Bowtie* can be used. 

As a Clinical Safety Officer, defined under DCB0160, I am required to create and administer a *Clinical Safety File* for all applications I am responsible for. Part of this is an identification of risks and hazards, using tools such as the *Bowtie* diagram. When a CVE alert is issued for one of the products we use, the alert along with the corresponding CVSS score can be applied to the left-hand side, and then we can assess the right-hand side along with the mitigations already in place to inform any actions required to further mitigate the risk. 

The use of diagrams, such as *Attack trees* and *Bowtie* diagrams, go a long way to addressing the area of *Presentation* identified by (Aven, 2016) as they are a clear way of visualising risk, attack vectors, and consequences, and are tools I will use in future when assessing and communicating risk. 

In conclusion, addressing the additional layers in the Hierarchy of Controls aids in the *Hard Problems* in cyber security, identified by the NSA (Scala et al., 2019) by addressing the human behaviour problem. That is by moving to a more effective level, we move away from human error. Secondly, an organisation using a well-designed *Bowtie* diagram, addresses the second hard problem, that of collaboration. It is a lot easier to communicate the effects of the causes of a hazard when communicating between organisations and industries, but not the impact. An organisation can use their *Bowtie* diagram to assess the risk posed by a CVE alert and determine the true level of risk.

# References

* Aven, T. (2016) Risk assessment and risk management: Review of recent advances on their foundation. European Journal of Operational Research, 253(1), 1–13. DOI: https://doi.org/10.1016/j.ejor.2015.12.023
* de Castro, A. B. (2003) “Hierarchy of Controls” Providing a framework for addressing workplace hazards. AJN, American Journal of Nursing, 103(12).
* de Ruijter, A., & Guldenmund, F. (2016) The bowtie method: A review. Safety Science, 88, 211–218. DOI: https://doi.org/10.1016/j.ssci.2016.03.001
* NHS Digital. (2024). Digital Clinical Informatics Safety Team. Available from:  https://digital.nhs.uk/services/clinical-safety [Accessed 19 October 2024]
* Scala, N. M., Reilly, A. C., Goethals, P. L., & Cukier, M. (2019) Risk and the Five Hard Problems of Cybersecurity. Risk Analysis, 39(10), 2119–2126. DOI: https://doi.org/10.1111/risa.13309
* Spring, J., Hatleback, E., Householder, A., Manion, A., & Shick, D. (2021) Time to Change the CVSS? IEEE Security and Privacy, 19(2), 74–78. DOI: https://doi.org/10.1109/MSEC.2020.3044475

