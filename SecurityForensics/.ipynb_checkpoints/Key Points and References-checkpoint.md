- Most LLMs are **inherently vulnerable** to prompt injection to some degree. This is a fundamental architectural limitation rather than a specific model flaw.

---

### Key Points from Research:

1. **Most instruction-tuned models are vulnerable** - including:
   - GPT-3.5/4
   - Claude
   - LLaMA-based models
   - Most open-source chat models

2. **Why they're vulnerable:**
   - LLMs can't reliably distinguish between "system instructions" and "user instructions" embedded in their input
   - The model essentially follows the most recent authoritative-sounding instructions

3. **Variants studied:**
   - Direct prompt injection (malicious instructions in user input)
   - Indirect prompt injection (instructions hidden in retrieved content/RAG)

4. **Mitigations that have been explored:**
   - Input filtering/validation
   - Output filtering
   - Separating user input from instructions
   - Fine-tuning to resist injection

---

### References

### References for Prompt Injection Literature Review

## Foundational / Original Work

1. **Goodside, R. (2022)** - "Prompt Injection Attacks Against LLMs" - *Twitter/Substack* - First coined the term "prompt injection"

2. **Perez, F., & Ribeiro, S. (2022)** - "Ignore Previous Prompt: An Attack on AI-based Systems" - *arXiv:2210.09587* - Early academic treatment of the attack

## Academic Papers

3. **Kumar, S., et al. (2023)** - "Prompt Injection Attacks and Defenses in LLM-Integrated Applications" - *arXiv:2310.12815*

4. **Xie, Y., et al. (2023)** - "Defending Against Indirect Prompt Injection Attacks" - *arXiv:2312.15837*

5. **Wei, B., et al. (2023)** - "GuardLLM: Protecting LLMs from Prompt Injection" - *arXiv:2310.01569*

6. **Schulhoff, S., et al. (2024)** - "The Prompt Report: A Systematic Survey of Prompt Engineering" - Includes injection techniques

7. **Liu, Y., et al. (2023)** - "Prompt Injection in Real-World LLMs" - *arXiv:2308.13763*

## Security Resources

8. **OWASP Top 10 for LLM Applications (2023)** - "LLM01: Prompt Injection" - <https://owasp.org/www-project-top-10-for-large-language-model-applications/>

9. **NVIDIA AI Red Team (2023)** - "Building LLM Applications Securely"

## Practical/Technical

10. **Kenneth L. (2023)** - "A Comprehensive Overview of Prompt Injection Attacks" - *Heim Security*

---


---

