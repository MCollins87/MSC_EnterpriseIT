[Back to Discussion Detils](../ColabDiscus2.md)

# [Initial Post by Nelson Akaffou](https://www.my-course.co.uk/mod/forum/discuss.php?d=254758#p472809)

In the article by Spring et al. (2021), several critical aspects of the Common Vulnerability Scoring System (CVSS) are scrutinised. The authors argue that the CVSS scoring formula lacks empirical and theoretical justification. Specifically, CVSS converts ordinal data into a numerical scale, but this transformation assumes interval properties not supported by the data’s inherent nature. This misuse of ordinal data, as discussed by Jamieson (2004), can lead to inaccuracies in risk assessment. Additionally, CVSS fails to account for contextual factors such as the interaction of vulnerabilities and their real-world implications, which can lead to an incomplete understanding of a vulnerability’s impact (Spring et al., 2021).

 

I concur with these critiques. Empirical studies have demonstrated that CVSS scores often do not correlate well with actual exploitation likelihood or impact (Allodi & Massacci, 2012). The lack of contextual consideration in CVSS assessments can result in misleading prioritization, as vulnerabilities in shared libraries or those chained together may be severely underrepresented.

 

Among the alternatives discussed, the Stakeholder-Specific Vulnerability Categorization (SSVC) stands out as a viable replacement for CVSS. SSVC offers a more tailored approach by incorporating contextual and material consequence factors into its risk assessments. This method allows for a more nuanced evaluation that reflects the specific needs and threat environment of an organization, potentially leading to more actionable and accurate risk management strategies (Spring et al., 2020). The adaptability and context-awareness of SSVC make it a compelling alternative to the limitations of CVSS.

Words Count: 241 words

References:

 - Allodi, L., & Massacci, F. (2012). A preliminary analysis of vulnerability scores for attacks in the wild: The EKITS and SYM datasets. In *Proceedings of the Workshop on Building Analytic Datasets Gathering Experience Returns Security* (pp. 17-24).

 - Jamieson, S. (2004). Likert scales: How to (ab)use them. *Medical Education*, 38(12), 1217-1218. doi:10.1111/j.1365-2929.2004.02012.x.

 - Spring, J. M., Hatleback, E., Householder, A. D., Manion, A., & Shick, D. (2021). Time to Change the CVSS? *IEEE Security & Privacy*, 19(2), 74-83. doi:10.1109/MSEC.2021.3060561.

 - Spring, J. M., et al. (2020). Prioritizing vulnerability response: A stakeholder-specific vulnerability categorization. *Proceedings of the Workshop on Economics of Information Security*, Brussels, Belgium

 # [Peer Response by Samer Saleem](https://www.my-course.co.uk/mod/forum/discuss.php?d=254758#p473202)

 Hi Nelson,
Nicely written post, I agree with the critique presented by Spring et al. (2021) regarding the limitations of the Common Vulnerability Scoring System (CVSS), particularly concerning the misuse of ordinal data. As argued by Jamieson (2004), converting ordinal data to a numerical scale without interval properties can lead to erroneous conclusions. This criticism aligns with empirical findings by Allodi and Massacci (2012), who demonstrated that CVSS scores often fail to reflect the true likelihood or impact of vulnerability exploitation. By neglecting contextual factors such as the real-world implications of vulnerabilities, CVSS can lead to ineffective prioritization, where significant risks are underemphasized.

In contrast, the Stakeholder-Specific Vulnerability Categorization (SSVC) offers a more robust alternative, as it incorporates contextual elements like business relevance and threat environment into its assessment. By doing so, SSVC allows for more tailored and actionable risk management strategies, making it highly adaptive to the specific needs of an organization. This context-aware approach improves upon the static nature of CVSS, providing a clearer understanding of the true risk posed by vulnerabilities. Given the dynamic nature of cyber threats, SSVC’s flexibility makes it a compelling alternative for improving vulnerability management.

References

- Allodi, L., & Massacci, F. (2012). *Security Events and Vulnerability Data: The Incident of Heartbleed*. Available at: https://www.semanticscholar.org/paper/Security-Events-and-Vulnerability-Data-for-Risk-Allodi-Massacci/71229970927ce817c4df68acbf6e4b1b2f464fe7 [accessed 16 Sep. 2024]

- Jamieson, S. (2004). Likert Scales: *How to (Ab)use Them*. Available at: https://eprints.gla.ac.uk/59552/1/59552.pdf [accessed 16 Sep. 2024].

- Spring, J.M., Hatleback, E., Householder, A.D., Manion, A., & Shick, D. (2021). *Time to Change the CVSS?* IEEE Security & Privacy available at: https://ieeexplore.ieee.org/document/9382369 [accessed 16 Sep. 2024]#

# [Peer Respnse by Mark Collins](https://www.my-course.co.uk/mod/forum/discuss.php?d=254758#p475681)

Hi Nelson and Samer,

Thank you for your posts.

I agree that there are many flaws to CVSS, however its wide use, do you feel it is practical to replace its use in industry, or should we be focussing on improving it?

Walkowski et al. (2021) has developed an automatic CVSS-based prioritisation method that applies context to a given CVSS score released with a Common Vulnerabilities and Exposure (CVE). This allows for a vulnerability to be identified and have a CVSS score applied by those responsible for the release of the product.

Despite the starting point for CVSS being qualitative, if the score is calculated by the manufacturer/developer, then it is fairly accurate in terms of product vulnerability. It is then the responsibility of the end user to apply context, such as the method proposed by Walkowski et al. (2021) to prioritise the threat to the individual organisation.

If we consider a specific threat – that of a firewall that has the potential to allow remote code execution. This would naturally be scored as a high threat. If this make/model of firewall was the main firewall to the network, or the same make/model was used across the entire organisation, then the score would be a legitimate high score. However if the firewall was only one of many brands, and was used to isolate certain segments of the network, then the “Swiss Cheese” approach to risk mitigation (Wiegmann et al., 2022) would lower the score.

**Word count: 243**

 

- Walkowski, M., Krakowiak, M., Jaroszewski, M., Oko, J., & Sujecki, S. (2021) Automatic CVSS-based Vulnerability Prioritization and Response with Context Information. *2021 International Conference on Software, Telecommunications and Computer Networks (SoftCOM 2021)*, 1–6. [DOI: https://doi.org/10.23919/softcom52868.2021.9559094](https://doi.org/10.23919/softcom52868.2021.9559094)

- Wiegmann, D. A., Wood, L. J., Cohen, T. N., & Shappell, S. A. (2022) Understanding the “swiss Cheese Model” and Its Application to Patient Safety. *Journal of Patient Safety*, 18(2): 119–123. [DOI: https://doi.org/10.1097/PTS.0000000000000810](https://doi.org/10.1097/PTS.0000000000000810)