# Winter Data Analysis Challenge 2026 — Winning Strategies

Link: https://spds.sydney.edu.au/winning-strategies-for-the-winter-data-analysis-challenge/

## Purpose

This guide summarises the advice shared by challenge co-leads **Dr Alistair Senior** and **Dr Shila Ghazanfar** after reviewing three years of Winter Data Analysis Challenge submissions.

The central lesson is clear:

> A winning submission does not rely on one impressive model or one strong visual. It combines a compelling research question, rigorous analysis, critical evaluation, meaningful context, and clear communication.

---

## 1. Start with a Strong Research Question

The strongest submissions were built around a **clear, focused, and compelling research question**.

A strong question:

- gives the project direction;
- helps the audience understand why each analytical step is necessary;
- prevents the analysis from becoming a collection of unrelated graphs or models;
- creates a natural story from exploration to conclusion;
- makes it easier to decide which methods, variables, and external datasets are relevant.

### Important principle

Your first idea is rarely your best idea.

Before committing to a question:

1. Brainstorm several possible questions.
2. Check whether each question can be answered using the available data.
3. Test whether the question is interesting, meaningful, and sufficiently focused.
4. Create a quick prototype or preliminary visualisation.
5. Refine the wording and scope.
6. Only then begin the full analysis.

### Questions to ask when choosing a topic

- Is the question specific enough to investigate in three days?
- Is it meaningful outside the dataset?
- Does it connect to a real social, economic, transport, environmental, or policy issue?
- Can the available data provide convincing evidence?
- Could external information improve the analysis?
- Is the question more interesting than simply describing trends?
- Can the result lead to a clear conclusion or recommendation?

---

## 2. Combine Visual and Statistical Analysis

The best submissions used both:

- **visual analysis** to reveal patterns and communicate findings;
- **statistical analysis** to test whether those patterns were reliable.

Visualisations are valuable for discovering:

- trends;
- differences between groups;
- seasonal effects;
- clusters;
- spatial patterns;
- unusual observations;
- possible relationships between variables.

Statistical methods help assess:

- whether differences are meaningful;
- whether results are robust;
- how uncertain estimates are;
- whether apparent patterns could be due to chance;
- how strongly variables are associated.

### Strong analytical practice

Do not stop after producing an interesting graph.

Follow the graph with questions such as:

- Is this pattern statistically meaningful?
- Does it persist across different time periods or groups?
- Could it be explained by another variable?
- Is it sensitive to outliers or missing values?
- Does the result remain similar under another reasonable method?

---

## 3. Use External Data Purposefully

Great submissions made thoughtful use of additional information and public datasets.

However, external data should not be added simply because it is available.

### Weak use of external data

- adding many variables without a clear reason;
- including a public dataset that does not affect the analysis;
- presenting external information without linking it to the research question;
- merging datasets without explaining assumptions or limitations.

### Strong use of external data

External data should:

- help explain an observed pattern;
- provide wider context;
- test a hypothesis;
- improve measurement;
- control for a possible confounding factor;
- allow comparisons across locations, time periods, or populations.

### Before adding an external dataset, ask

1. What specific question will this data help answer?
2. Which variable or pattern does it help explain?
3. Is the source reliable and appropriately documented?
4. Are the time period, geography, and units compatible?
5. Could the merge introduce missingness, bias, or measurement error?
6. Does the added complexity produce meaningful analytical value?

### Document clearly

For every external source, explain:

- where it came from;
- why it was selected;
- how it was cleaned;
- how it was joined to the challenge data;
- what assumptions were required;
- what limitations it introduced.

---

## 4. Follow Up on Initial Findings

A good submission identifies an interesting result.

A great submission asks:

> What should we investigate next?

The judges valued teams that adapted their analysis after discovering something unexpected.

### Example follow-up process

1. Identify an initial pattern.
2. Ask what could explain it.
3. Form one or more possible hypotheses.
4. Conduct additional analysis.
5. Compare alternative explanations.
6. Assess whether the new evidence strengthens or weakens the original interpretation.
7. Refine the final conclusion.

### Useful follow-up questions

- Does the effect vary by location?
- Does it change over time?
- Is it driven by a particular subgroup?
- Does it remain after controlling for another factor?
- Are there important exceptions?
- Is the pattern concentrated around certain events?
- Could measurement or sampling bias explain it?

This deeper investigation demonstrates:

- curiosity;
- adaptability;
- analytical maturity;
- critical thinking;
- willingness to test rather than merely confirm an idea.

---

## 5. Critically Assess the Evidence

The judges specifically wished more teams had critically evaluated their own findings.

Critical assessment means examining not only what the analysis appears to show, but also:

- how strong the evidence is;
- how sensitive the result is;
- which assumptions were made;
- what alternative explanations remain;
- what conclusions cannot be supported.

---

## 6. Test Robustness and Sensitivity

For statistical models and analyses, ask:

> If the data or method changed slightly, would we reach the same conclusion?

### Possible robustness checks

- repeat the analysis after removing extreme outliers;
- compare alternative model specifications;
- change a threshold or grouping rule;
- evaluate results across several time periods;
- use cross-validation;
- use bootstrapping;
- calculate confidence intervals;
- compare multiple reasonable metrics;
- test different missing-value strategies;
- perturb or resample the data;
- repeat the analysis with and without selected variables;
- compare results using raw and transformed variables.

### What to report

Do not merely say that a result is robust.

Show:

- what was changed;
- why the change was reasonable;
- how much the result changed;
- whether the substantive conclusion remained the same.

---

## 7. Avoid Overstating Causal Conclusions

An association does not automatically prove causation.

For example, observing that two variables move together does not prove that one causes the other.

### Before making a causal claim, consider

- Could a third variable explain both?
- Could the direction of influence be reversed?
- Were the observations randomly assigned?
- Could selection bias affect the relationship?
- Were relevant confounders measured?
- Is the timing consistent with the proposed causal explanation?
- Is there external evidence supporting the mechanism?

### Safer language

Prefer:

- “is associated with”;
- “is linked to”;
- “corresponds with”;
- “is consistent with”;
- “may help explain”;
- “suggests a possible relationship”.

Avoid claiming that one factor caused another unless the study design and evidence genuinely support that conclusion.

---

## 8. State Limitations Clearly

Limitations do not weaken a submission when they are discussed honestly and intelligently.

In fact, thoughtful limitations demonstrate maturity.

### Common limitations

- incomplete or missing data;
- measurement error;
- limited time coverage;
- geographic mismatch;
- unobserved confounding;
- aggregation hiding individual-level differences;
- changing data collection methods;
- small sample size;
- lack of demographic information;
- inability to infer causality;
- external datasets using different definitions or time periods;
- model assumptions that may not hold.

### Strong limitation statements

A useful limitation statement explains:

1. what the limitation is;
2. why it matters;
3. how it may affect the interpretation;
4. how future work could address it.

---

## 9. Build a Clear Analytical Story

Communication and storytelling were described as extremely important.

A strong submission should feel like a guided investigation rather than a notebook containing every analysis attempted.

### Recommended narrative arc

1. **Context**  
   Introduce the real-world issue.

2. **Research question**  
   State exactly what the project investigates.

3. **Motivation**  
   Explain why the question matters.

4. **Data**  
   Introduce the main and external datasets.

5. **Approach**  
   Explain the analytical steps and why they were selected.

6. **Key findings**  
   Present the most important results.

7. **Follow-up analysis**  
   Show how the team investigated unexpected or important patterns.

8. **Critical evaluation**  
   Assess uncertainty, robustness, assumptions, and limitations.

9. **Conclusion**  
   Answer the research question directly.

10. **Wider implications**  
    Explain why the result matters and what could be investigated next.

---

## 10. Tailor the Report and Video to Their Formats

The written report and three-minute video should complement each other.

They should not be identical.

### The reproducible report should provide

- detailed methodology;
- data-cleaning decisions;
- statistical reasoning;
- assumptions;
- reproducible code;
- supporting figures and tables;
- robustness checks;
- limitations;
- citations and data sources.

### The video should provide

- a strong opening;
- a clear research question;
- the most important findings;
- a small number of effective visuals;
- an understandable explanation of the method;
- a concise conclusion;
- a memorable final takeaway.

### Avoid in the video

- reading the report aloud;
- showing dense code;
- using too many charts;
- explaining every minor preprocessing step;
- presenting results without context;
- rushing through an excessive number of methods.

---

## 11. Recommended Three-Minute Video Structure

| Time | Content |
|---|---|
| 0:00–0:20 | Hook, context, and why the issue matters |
| 0:20–0:40 | Research question |
| 0:40–1:05 | Data and analytical approach |
| 1:05–2:05 | Main findings and supporting visuals |
| 2:05–2:30 | Follow-up analysis and critical evaluation |
| 2:30–2:50 | Conclusion and wider implications |
| 2:50–3:00 | Memorable closing statement |

---

## 12. Align the Submission with the Judging Criteria

### Analytical Innovation

Demonstrate:

- an original research question;
- thoughtful method selection;
- creative feature construction;
- meaningful integration of external information;
- useful follow-up analysis;
- an approach that reveals something not immediately obvious.

Innovation does not require using the most complex model.

A simple method applied thoughtfully can be more innovative than an advanced model used without justification.

### Clarity of Communication

Demonstrate:

- a logical narrative;
- readable figures;
- concise explanations;
- definitions of technical terms;
- clear transitions;
- a direct answer to the research question;
- appropriate communication for both report and video.

### Critical Assessment and Evaluation

Demonstrate:

- robustness checks;
- uncertainty estimates;
- comparison of alternative methods;
- awareness of assumptions;
- careful causal language;
- clear limitations;
- evidence-based conclusions.

### Understanding the Wider Context

Demonstrate:

- knowledge of the real-world system represented by the data;
- purposeful use of credible external sources;
- awareness of policy, social, economic, or operational implications;
- discussion of who may be affected;
- understanding of why the result matters beyond the dataset.

---

## 13. A Strong Competition Workflow

### Stage 1 — Ideate

- inspect the dataset;
- brainstorm multiple questions;
- research the domain;
- identify possible external datasets;
- consider what would be genuinely useful or surprising.

### Stage 2 — Prototype

- build quick plots;
- run simple summary statistics;
- check whether the question is answerable;
- test whether the proposed relationship is visible;
- identify data-quality problems.

### Stage 3 — Refine

- narrow the question;
- remove weak or overly broad directions;
- decide which external data is justified;
- define the main analysis and evaluation plan.

### Stage 4 — Analyse

- clean and document the data;
- complete the main visual and statistical analysis;
- perform follow-up analyses;
- assess uncertainty and robustness;
- compare alternative explanations.

### Stage 5 — Communicate

- select only the strongest results;
- build a coherent narrative;
- write the reproducible report;
- design the three-minute video;
- make figures readable and self-contained.

### Stage 6 — Validate

- run the report from beginning to end;
- check all data paths;
- verify tables and calculations;
- confirm all claims are supported;
- check that external sources are cited;
- verify the video duration;
- submit before the deadline.

---

## 14. Final Winning-Strategy Checklist

### Research Question

- [ ] The question is specific and clearly worded.
- [ ] The question matters in a wider context.
- [ ] The analysis directly answers the question.
- [ ] The team considered and rejected weaker alternatives.

### Analysis

- [ ] Visual and statistical evidence are combined.
- [ ] Methods are justified rather than used automatically.
- [ ] External data has a clear purpose.
- [ ] Initial results are followed by deeper investigation.
- [ ] Alternative explanations are considered.

### Critical Evaluation

- [ ] Uncertainty is reported.
- [ ] Robustness or sensitivity checks are included.
- [ ] Causal claims are appropriately cautious.
- [ ] Limitations are explained honestly.
- [ ] Conclusions do not go beyond the evidence.

### Communication

- [ ] The report follows a clear narrative.
- [ ] The video is designed for a three-minute audience.
- [ ] Figures are readable and correctly labelled.
- [ ] The final conclusion answers the research question directly.
- [ ] The main takeaway is memorable.

### Reproducibility

- [ ] The report runs from beginning to end.
- [ ] Random seeds are fixed where relevant.
- [ ] Data sources are documented.
- [ ] Data-cleaning decisions are explained.
- [ ] Software packages and versions are recorded.
- [ ] No essential analysis depends on undocumented manual steps.

---

## Final Principle

> Ideate, prototype, refine, and only then commit to the full analysis.

The winning mindset is not to perform the greatest number of analyses. It is to develop the strongest question, investigate it deeply, challenge your own findings, and communicate the result with precision and creativity.
