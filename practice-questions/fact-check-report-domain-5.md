# Fact-Check Report: Domain 5 (Generative AI -- Highest Weight)

## Summary
- Items checked: 5
- Issues found: 2
- Items requiring correction: Item 5 (reference URL mismatch), terminology advisory for all items

---

### Item 1: PASS
- **Correct answer verified:** Yes -- DALL-E 3 is confirmed by Microsoft Learn as the Azure OpenAI Service model for text-to-image generation. The transparency note states: "DALL-E 2, DALL-E 3, and GPT-image-1 APIs use natural language prompts to generate new content." The how-to guide at the reference URL confirms `dall-e-3` is a deployable image generation model. (Source: https://learn.microsoft.com/azure/ai-foundry/openai/how-to/dall-e)
- **Terminology current:** Yes -- uses "Azure OpenAI Service," "DALL-E 3," and current model names.
- **Distractors valid:** Yes -- All distractors are plausible but definitively wrong:
  - A (GPT-4o): While GPT-4o can now *orchestrate* image generation via the Responses API by calling `gpt-image-1` as a tool, GPT-4o itself does not generate images. The distractor explanation is accurate for AI-900 level.
  - C (Embeddings): Correctly described as vector representations, not images.
  - D (Whisper): Correctly identified as speech-to-text only.
- **Reference URL verified:** Yes -- resolves to "How to use Azure OpenAI image generation models" on Microsoft Learn. Page is current and covers DALL-E 3.
- **Stem is scenario-based:** Yes -- presents a realistic marketing agency scenario requiring banner image generation.

---

### Item 2: PASS
- **Correct answer verified:** Yes -- Microsoft Learn confirms the system message (also called "metaprompt" or "system prompt") is the mechanism for defining behavioral constraints, persona, tone, and topic boundaries. The System Message Design page states: "A system message is a set of instructions and context you provide to the model to guide its responses. You typically use it to: 1. Define the assistant's role and boundaries. 2. Set tone and communication style. 3. Specify output formats. 4. Add safety and quality constraints." (Source: https://learn.microsoft.com/azure/ai-foundry/openai/concepts/advanced-prompt-engineering)
- **Terminology current:** Yes -- uses "system message," "metaprompt," "Azure OpenAI Service." All current.
- **Distractors valid:** Yes -- All distractors are plausible but definitively wrong:
  - B (Few-shot learning): Correctly noted as useful for demonstrating patterns but not for persistent behavioral constraints.
  - C (Temperature): Correctly identified as randomness control, not behavioral enforcement.
  - D (Embeddings for filtering): Correctly dismissed; content filtering uses Guardrails, not embeddings.
- **Reference URL verified:** Yes -- resolves to "Prompt engineering techniques" on Microsoft Learn. Page is current and comprehensive.
- **Stem is scenario-based:** Yes -- presents a realistic customer service chatbot scenario with specific behavioral requirements.

---

### Item 3: PASS
- **Correct answer verified:** Yes -- Microsoft Learn confirms RAG as the recommended pattern for grounding generative AI in enterprise data. The RAG overview states: "Retrieval-augmented Generation (RAG) is a pattern that extends LLM capabilities by grounding responses in your proprietary content." Azure AI Search is confirmed as the core retrieval component. The customizing LLMs guide states: "RAG helps ground AI output in real-world data and reduces the likelihood of fabrication." (Source: https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview)
- **Terminology current:** Yes -- uses "Azure AI Search" (not deprecated "Cognitive Search"), "RAG," "Azure OpenAI Service."
- **Distractors valid:** Yes -- All distractors are plausible but definitively wrong:
  - A (Fine-tuning): Correctly distinguished from RAG. MS Learn states fine-tuning adjusts model behavior/style, not for injecting frequently changing factual content.
  - B (Increase token limit): Correctly dismissed as infeasible for thousands of documents.
  - D (DALL-E 3): Correctly identified as irrelevant to document Q&A.
- **Reference URL verified:** Yes -- resolves to "Design and develop a RAG solution" on Microsoft Learn. Page is current, comprehensive, and describes the RAG architecture with Azure AI Search.
- **Stem is scenario-based:** Yes -- presents a realistic enterprise scenario with specific document types and hallucination concerns.
- **RAG accuracy:** Verified -- the architecture description (Azure AI Search indexes documents, retrieves relevant content, provides as context to the model) matches Microsoft's current documentation exactly.

---

### Item 4: PASS
- **Correct answer verified:** Yes -- Microsoft Learn's responsible AI overview confirms a layered mitigation approach: (1) model level, (2) safety system level (Guardrails/content filters), (3) application level (metaprompt/system message), and (4) positioning level. The overview states: "Application Level Mitigations: Prompt engineering, including metaprompt tuning, can be an effective mitigation for many different types of harm." Content filters are described as "Safety System Level Mitigations." (Source: https://learn.microsoft.com/azure/ai-foundry/responsible-ai/openai/overview)
- **Terminology current:** Yes -- uses "Azure OpenAI content filters," "Guardrails," and "system message." Note: Microsoft now uses "Guardrails (previously content filters)" throughout their docs, and the practice item uses both terms appropriately.
- **Distractors valid:** Yes -- All distractors are plausible but definitively wrong:
  - B (Older model): Correctly dismissed; all generative models can hallucinate regardless of version.
  - C (Remove system message): Correctly identified as removing a critical mitigation layer, contradicting MS guidance.
  - D (Disable content filtering): Correctly identified as removing safety; MS requires content filtering be enabled.
- **Reference URL verified:** Yes -- resolves to "Overview of responsible AI practices for Azure OpenAI models" on Microsoft Learn. Page is current and comprehensive.
- **Stem is scenario-based:** Yes -- presents a realistic e-commerce chatbot scenario with specific hallucination problem.

---

### Item 5: FAIL (minor -- reference URL mismatch)
- **Correct answer verified:** Yes -- Microsoft Learn confirms the Foundry model catalog enables browsing, comparing, testing, and deploying models from multiple providers. The model catalog overview states: "The model catalog in Foundry portal is the hub to discover and use a wide range of models for building generative AI applications. The model catalog features hundreds of models across model providers such as Azure OpenAI, Mistral, Meta, Cohere, NVIDIA, and Hugging Face." It also confirms: "You can search and discover models... Model catalog also offers the model performance leaderboard and benchmark metrics for select models. You can access them by selecting Browse leaderboard and Compare Models." (Source: https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview)
- **Terminology current:** Yes -- uses "Microsoft Foundry" which aligns with AI-900 exam objectives (last updated May 2, 2025). See advisory note below.
- **Distractors valid:** Yes -- All distractors are plausible but definitively wrong:
  - A (ML designer): Correctly identified as drag-and-drop ML pipeline tool, not a model catalog.
  - C (Azure AI Search): Correctly distinguished as a retrieval/indexing service, not a model catalog.
  - D (Azure AI Language): Correctly identified as a fixed-capability NLP service.
- **Reference URL verified:** FAIL -- The reference URL (https://learn.microsoft.com/azure/ai-foundry/openai/overview) resolves to "What is Azure OpenAI in Microsoft Foundry Models?" which is specifically about Azure OpenAI, not about the Microsoft Foundry model catalog. The correct reference should be the Foundry model catalog page.
- **Stem is scenario-based:** Yes -- presents a realistic team evaluation scenario with specific requirements for browsing, comparing, testing, and deploying models.

---

## Corrections Needed

### Item 5: Reference URL Update
**Issue:** The reference URL points to the Azure OpenAI overview page, but the item tests knowledge of the Microsoft Foundry model catalog (which includes models from many providers, not just OpenAI).

**Current:** `https://learn.microsoft.com/azure/ai-foundry/openai/overview`

**Corrected:** `https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview`

**Citation:** The Foundry Models overview page (https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview) directly describes the model catalog capabilities tested in this item: browsing, comparing, testing, and deploying models from multiple providers.

---

## Terminology Advisory (Informational -- No Correction Required)

As of mid-2025, Microsoft renamed "Microsoft Foundry" to "Microsoft Foundry." The documentation now states: "Microsoft Foundry is now Microsoft Foundry." However, the AI-900 exam objectives (last updated May 2, 2025) still reference "Microsoft Foundry." The practice items correctly use "Microsoft Foundry" to match the current exam objectives. **Monitor for AI-900 exam objective updates** that may adopt the "Microsoft Foundry" naming. When the exam objectives change, all 5 items should be updated accordingly.

---

*Report generated: 2026-02-23*
*Verified against: Microsoft Learn documentation (live pages fetched 2026-02-23)*
