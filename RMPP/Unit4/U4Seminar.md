[Back to Unit overview](./Unit4.md)

# Brief

Please read the case below and answer the questions. You need to determine the ethical issues involved with this case.

### The Case

Ricardo works for the records department of his local government as a computer records clerk, where he has access to files of property tax records. For a scientific study, a researcher, Beth, has been granted access to the numerical portion “but not the corresponding names” of some records.

Beth finds some information that she would like to use, but she needs the names and addresses corresponding with certain properties. Beth asks Ricardo to retrieve these names and addresses, so she can contact these people for more information and for permission to do further study.

Now consider, what are the ethical issues involved in deciding which of these options to pursue?

- If Ricardo is not responsible for determining allowable access, should he release the names and addresses?
- Suppose Ricardo were responsible for determining allowable access to the files. What ethical issues would be involved in his deciding whether to grant access to Beth?
- Should Beth be allowed to contact the individuals involved? That is, should the Records department release individuals' names to a researcher? What are the ethical issues for the Records department to consider?
- Suppose Beth contacts the individuals to ask their permission, and one-third of them respond giving permission, one-third respond denying permission, and one-third do not respond. Beth claims that at least one-half of the individuals are needed to make a valid study. What options are available to Beth?

## Reflection

### 1. If Ricardo is not responsible for determining allowable access, should he release the names and addresses?
Ethical issues and judgement:

- **Unauthorized disclosure / breach of confidentiality:** Releasing identifiers without authorization violates duties of confidentiality and role-based access controls. This is explicitly discouraged by professional codes that require respecting privacy and following organisational rules (ACM, 2018; BCS, 2021).
- **Legal/data-protection risk:** Personal identifiers are subject to GDPR principles (lawfulness, purpose limitation, minimisation); releasing them without a lawful basis or safeguards risks non-compliance. (GDPR, 2016)
- **Professional integrity / accountability:** Professional codes require members to follow policies and escalate requests outside their remit rather than acting unilaterally. (BCS, 2021)

**Conclusion:** Ricardo should not release names/addresses — he must refuse and refer Beth to the proper data-access procedure.

### 2. Suppose Ricardo were responsible for determining allowable access. What ethical issues would be involved in his deciding whether to grant access to Beth?
Ethical issues:

- **Balancing public interest vs individual privacy:** ACM and BCS emphasise protecting the public good while respecting individuals’ rights; Ricardo should weigh research value against privacy intrusion. (ACM, 2018; BCS, 2021)
Lawful basis & safeguards under GDPR: Granting access must satisfy GDPR (or UK GDPR) rules — identify a lawful basis, apply purpose limitation, data minimisation, and appropriate safeguards (pseudonymisation/anonymisation; DPIA where needed). ICO research guidance is directly relevant here.(Information Commissioner’s Office, 2025)
- **Re-identification risk & proportionality:** Even “pseudonymised” datasets may allow re-identification (particularly small/local samples); Ricardo must assess risk and refuse access if re-identification or harms are likely.(Information Commissioner’s Office, 2025)
- **Transparency & fairness:** Decisions should be documented, transparent, and consistent with departmental policy and professional standards. (ACM/BCS stress accountability and transparent decision-making.) (ACM, 2018; BCS, 2021)

**Practical requirement:** If access is considered, require a written data-sharing agreement, minimum data disclosure, data security measures, and REC/DPO sign-off.

### 3. Should Beth be allowed to contact the individuals involved? Should the Records department release individuals’ names to a researcher?
Ethical issues:

- **Informed consent & autonomy:** Contacting people for research involvement requires clear, voluntary informed consent; the Records dept should not hand over names lightly. (ACM/BCS stress respect for persons and consent in data use.) (ACM, 2018; BCS, 2021)
- **Purpose limitation & institutional duty:** Tax records were collected for administration — repurposing them for research triggers GDPR rules and institutional obligations to protect data subjects. The ICO’s research provisions explain safeguards and when secondary use is permissible. (Information Commissioner’s Office, 2025)
- **HIPAA note (if health data implicated):** If any property records contain health information or are linked to health datasets, HIPAA requires strict protections and limits on disclosure of protected health information (PHI). Even indirect health inferences would need careful HIPAA/legal review. (U.S. Department of Health and Human Services, 2008)

**Recommended practice:** The Records dept should either (a) refuse direct release of identifiers, or (b) act as an intermediary (send vetted invitation letters on Beth’s behalf) and ensure any contact includes a clear privacy notice, opt-in consent, and secure handling of replies.

### 4. Suppose Beth contacts the individuals and 1/3 consent, 1/3 refuse, 1/3 don’t respond — she claims she needs ≥50% for validity. What options are available?
Ethical issues:

- **Non-response ≠ consent; refusals must be respected:** Respect for autonomy and GDPR requirements mean only explicit consenters can be included. Professional codes mandate respecting individuals’ choices. (ACM, 2018)
- **Scientific needs vs ethics:** Methodological desires (need for ≥50%) don’t override ethical/legal duties (consent, privacy). Treating non-respondents as consent would be unethical and likely unlawful. (GDPR, 2016)

**Ethically acceptable options for Beth:**

- **Proceed only with consenting participants.** Document limitations and discuss impacts on validity.
- **Re-contact non-respondents** with clearer information / second invitation (non-coercive), extending deadline — while logging attempts and respecting opt-outs.
- **Modify study design** — adjust power calculations, use alternative measures, or rely on anonymised/aggregate administrative data that do not require re-contact (if lawful). (Information Commissioner’s Office, 2025)
- **Seek Ethics Committee / DPO review** to explore acceptable pathways (e.g., wider lawful basis for specific secondary-use research, or approved anonymised linkage).(Information Commissioner’s Office, 2025)
- **Abandon or redesign** if valid results cannot be achieved without ethical compromise.

## Mapping to the professional & legal texts 

- **ACM Code of Ethics & Professional Conduct** — duties to protect privacy, avoid harm, act with honesty and fairness, and follow institutional rules. Useful for assessing individual/professional responsibilities (Ricardo, Beth). (ACM, 2018)
- **BCS Code of Conduct** — emphasises public interest, legal compliance, and professional integrity; supports the requirement to follow access procedures and protect data subjects. (BCS, 2021)
- **GDPR / UK GDPR (ICO research provisions)** — legal principles of lawfulness, purpose limitation, data minimisation, safeguards (pseudonymisation, DPIA), and how research uses of administrative data may be lawful if safeguards are met. See ICO research guidance and the GDPR text. (Information Commissioner’s Office, 2025)
- **HIPAA (HHS / HHS OCR guidance)** — if the dataset contains or is linkable to health information, HIPAA’s Privacy & Security Rules impose strict constraints on disclosure and require administrative, physical, and technical safeguards. (U.S. Department of Health and Human Services, 2008)

## References
ACM (2018) _ACM Code of Ethics and Professional Conduct_. Available at: [https://www.acm.org/code-of-ethics](https://www.acm.org/code-of-ethics) (Accessed: 24 October 2025).

BCS (2021) _BCS Code of Conduct for members - Ethics for IT professionals | BCS_. Available at: [https://www.bcs.org/membership-and-registrations/become-a-member/bcs-code-of-conduct](https://www.bcs.org/membership-and-registrations/become-a-member/bcs-code-of-conduct) (Accessed: 20 October 2025).

GDPR (2016) _General Data Protection Regulation (GDPR) – Legal Text_, _General Data Protection Regulation (GDPR)_. Available at: [https://gdpr-info.eu/](https://gdpr-info.eu/) (Accessed: 20 November 2025).

Information Commissioner’s Office (2025) _What are the research provisions?_ ICO. Available at: [https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/what-are-the-research-provisions/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/what-are-the-research-provisions/) (Accessed: 20 November 2025).

U.S. Department of Health and Human Services (2008) _Summary of the HIPAA Privacy Rule | HHS.gov_. Available at: [https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html) (Accessed: 20 November 2025).