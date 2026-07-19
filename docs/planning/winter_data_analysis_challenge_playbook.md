# Winter Data Analysis Challenge Playbook

*A detailed, practical, and easy-to-follow plan for producing a strong submission in three days.*

---

## 1. Understand the Challenge

**Objective**

Before analysing the data, make sure the team understands what success looks like.

**Confirm**

- Challenge opening and submission deadlines
- Required deliverables
- Video length
- Reproducibility requirements
- Judging criteria
- Team responsibilities
- Available support, mentoring, and information sessions

**Judging Criteria**

The work should demonstrate:

1. **Analytical innovation**
2. **Clarity of communication**
3. **Critical assessment and evaluation**
4. **Understanding of the wider context**

**Team Output**

Create a short shared plan containing:

- team roles;
- communication channel;
- file-sharing or Git workflow;
- meeting times;
- internal deadlines;
- final reviewer;
- person responsible for submission.

---

## 2. Inspect and Understand the Dataset

**Objective**

Understand what the dataset represents before deciding what to analyse.

**First Checks**

- Number of rows and columns
- Variable names and meanings
- Data types
- Units
- Time range
- Geographic coverage
- Unique identifiers
- Missing values
- Duplicate records
- Outliers or impossible values
- Data source and collection method
- Possible sampling or measurement bias
- Potential data leakage

**Questions to Ask**

- Who collected this data?
- Why was it collected?
- What does one row represent?
- What information is missing?
- Are variables measured consistently?
- Could some values be inaccurate or incomplete?
- Are there important time, location, or group effects?
- What real-world system does the data describe?

**Deliverables**

- Short dataset summary
- Basic data dictionary
- Initial data-quality notes
- List of possible limitations

---

## 3. Generate and Refine Research Questions

**Objective**

Develop one focused, meaningful, and answerable research question.

This is one of the most important stages. A strong question gives the entire analysis direction.

**Process**

1. Explore the dataset briefly.
2. Brainstorm several possible questions.
3. Identify which questions are meaningful.
4. Check whether the data can answer them.
5. Create quick prototype plots or summaries.
6. Refine the strongest question.
7. Commit only after comparing alternatives.

**A Strong Question Should Be**

- specific;
- meaningful;
- answerable within three days;
- connected to a wider real-world issue;
- supported by the available data;
- capable of producing a clear conclusion;
- interesting enough to communicate in a three-minute video.

**Questions to Ask**

- Why does this question matter?
- Who would care about the answer?
- Is the question too broad?
- Is it only descriptive, or does it investigate something deeper?
- Can external data improve the analysis?
- What evidence would support or challenge the idea?
- Could the answer have policy, social, economic, environmental, or operational value?

**Deliverable**

Write one clear sentence:

> **Research question:** ...

Then add:

> **Why it matters:** ...

---

## 4. Perform Focused Exploratory Data Analysis

**Objective**

Use exploration to generate hypotheses and identify the strongest analytical direction.

Do not create plots only because they are common. Every plot should answer a question.

**Useful Exploration**

**Numerical Data**

- Summary statistics
- Histograms
- Boxplots
- Scatterplots
- Correlation analysis
- Outlier inspection

**Categorical Data**

- Counts
- Proportions
- Group comparisons
- Cross-tabulations

**Time Data**

- Trends
- Seasonality
- Peaks and declines
- Before-and-after comparisons
- Rolling averages
- Change points

**Spatial Data**

- Maps
- Regional comparisons
- Distance-based features
- Geographic clustering

**High-Dimensional Data**

- PCA
- Clustering
- Feature importance
- Embeddings, where appropriate

**Questions to Ask**

- What is surprising?
- Which patterns are strongest?
- What differences exist between groups?
- Are there important exceptions?
- Are apparent relationships driven by time or location?
- What findings deserve deeper investigation?
- What might explain the observed patterns?

**Deliverables**

- A small set of useful exploratory figures
- Initial hypotheses
- Short list of promising research directions

---

## 5. Research the Wider Context

**Objective**

Understand the real-world system behind the data and identify relevant external information.

**Possible Sources**

- Government open data
- Census data
- Policy documents
- Industry reports
- Academic papers
- Credible news sources
- Weather data
- Geographic data
- Economic indicators
- Public infrastructure records

**Use External Data Purposefully**

External data should:

- explain an observed pattern;
- test a hypothesis;
- add necessary context;
- improve measurement;
- control for a possible confounder;
- support comparisons across time or location.

Do not add external datasets simply because they are available.

**Before Adding External Data, Ask**

1. What exact question will this data help answer?
2. Is the source reliable?
3. Are the time period, geography, and units compatible?
4. How will the datasets be joined?
5. Could the merge introduce missingness or bias?
6. Does the additional complexity provide real analytical value?

**Document**

For each external source, record:

- source;
- purpose;
- variables used;
- cleaning steps;
- join method;
- assumptions;
- limitations.

---

## 6. Clean and Prepare the Data

**Objective**

Create a reliable analysis dataset while preserving reproducibility.

**Common Tasks**

- Remove or resolve duplicates
- Fix incorrect data types
- Handle missing values
- Detect impossible values
- Investigate outliers
- Standardise units
- Encode categorical variables
- Scale or normalise features
- Parse dates and times
- Create consistent geographic identifiers
- Address class imbalance
- Apply data augmentation only when appropriate

**Important Principle**

Every cleaning decision should be documented.

For each major decision, explain:

- what was changed;
- why it was changed;
- how many observations were affected;
- whether the decision could influence the conclusion.

**Avoid**

- deleting large amounts of data without explanation;
- filling missing values automatically;
- removing outliers only because they reduce model performance;
- using future information in feature creation;
- cleaning data manually without reproducible code.

**Deliverables**

- Reproducible cleaning pipeline
- Final analysis dataset
- Data-quality summary
- Record of assumptions and decisions

---

## 7. Engineer Meaningful Features

**Objective**

Create variables that better represent the real-world process being studied.

**Possible Features**

**Numerical**

- Ratios
- Differences
- Rates
- Log transformations
- Interaction terms
- Polynomial features
- Group-level aggregates

**Time**

- Hour
- Day of week
- Month
- Season
- Holiday indicator
- Lag features
- Rolling averages
- Time since an event
- Before-and-after indicators

**Spatial**

- Distance
- Density
- Region type
- Accessibility
- Proximity to services
- Geographic clusters

**Text**

- Keyword counts
- TF-IDF
- Sentiment
- Topic features
- Embeddings

**Requirements**

Each engineered feature should have:

- a clear meaning;
- a reason for inclusion;
- no leakage;
- a reproducible calculation.

**Deliverables**

- Feature list
- Justification for important features
- Comparison before and after feature engineering, where relevant

---

## 8. Choose Appropriate Analytical Methods

**Objective**

Select methods that answer the research question, not simply the most complex techniques.

**Possible Statistical Methods**

- Descriptive statistics
- Confidence intervals
- Correlation
- Hypothesis testing
- Linear regression
- Logistic regression
- ANOVA
- Time-series analysis
- Spatial analysis

**Possible Machine Learning Methods**

- Decision trees
- Random Forest
- Gradient boosting
- XGBoost
- LightGBM
- CatBoost
- Clustering
- Dimensionality reduction
- Neural networks, where justified

**Start with a Baseline**

A baseline may be:

- mean or median prediction;
- majority-class prediction;
- simple linear or logistic model;
- basic decision tree;
- simple descriptive comparison.

A baseline helps show whether additional complexity is useful.

**Always Explain**

- Why is this method appropriate?
- What assumptions does it make?
- What does it contribute to the research question?
- Why is it better than a simpler alternative?

**Avoid**

- trying many models without purpose;
- selecting a model only because it has the highest score;
- using advanced methods that cannot be explained;
- changing methods until a preferred result appears.

---

## 9. Design a Rigorous Validation Strategy

**Objective**

Estimate how reliable the results are and avoid misleading conclusions.

**Common Validation Methods**

- Train/validation/test split
- k-fold cross-validation
- Stratified k-fold
- Grouped cross-validation
- Time-series split
- Nested cross-validation
- Bootstrapping

**Choose Based on the Data**

**Use stratification when**

- classes are imbalanced;
- each fold should preserve group proportions.

**Use grouped validation when**

- multiple rows belong to the same person, station, location, organisation, or entity;
- related observations must not appear in both training and validation sets.

**Use time-based validation when**

- future observations are predicted from past observations;
- random splitting would leak future information.

**Avoid**

- tuning on the test set;
- random splitting of time-series data;
- leakage between related groups;
- reporting only one favourable split.

---

## 10. Evaluate Beyond a Single Metric

**Objective**

Assess performance, uncertainty, robustness, and practical meaning.

**Classification Metrics**

- Accuracy
- Precision
- Recall
- F1 score
- Macro-F1
- ROC-AUC
- PR-AUC
- Log loss
- Calibration

**Regression Metrics**

- MAE
- RMSE
- R²
- MAPE, when appropriate

**Clustering Metrics**

- Silhouette score
- Davies–Bouldin index
- Cluster stability
- Practical interpretability

**Also Evaluate**

- variation across folds;
- confidence intervals;
- subgroup performance;
- calibration;
- practical significance;
- statistical significance;
- whether the result is useful in context.

**Deliverables**

- Main metric with justification
- Supporting metrics
- Uncertainty estimates
- Clear comparison table
- Interpretation in plain language

---

## 11. Perform Robustness and Sensitivity Checks

**Objective**

Test whether the conclusion remains similar under reasonable changes.

Ask:

> If the data or method changed slightly, would we still make the same conclusion?

**Possible Checks**

- Remove extreme outliers
- Change thresholds or grouping rules
- Use alternative missing-value strategies
- Compare multiple model specifications
- Analyse different time periods
- Repeat with and without selected variables
- Use bootstrapping
- Perturb or resample the data
- Compare raw and transformed variables
- Test different evaluation metrics
- Examine important subgroups separately

**Report**

- what was changed;
- why it was reasonable;
- how much the result changed;
- whether the main conclusion remained the same.

---

## 12. Conduct Error and Exception Analysis

**Objective**

Understand where the method fails and what those failures reveal.

**Investigate**

- Worst-performing cases
- Misclassified groups
- Geographic concentrations of error
- Time periods with weaker performance
- Rare or unusual observations
- Overconfident predictions
- Systematic subgroup differences
- Cases that contradict the main pattern

**Questions to Ask**

- Why did the method fail here?
- Is the failure caused by poor data quality?
- Is an important variable missing?
- Does the model perform differently across groups?
- Are some observations fundamentally harder?
- Do exceptions reveal a better research question?

Error analysis often produces stronger insights than a small improvement in a headline metric.

---

## 13. Assess Causality Carefully

**Objective**

Avoid making claims stronger than the evidence supports.

An association does not prove causation.

**Before Making a Causal Claim, Ask**

- Could another variable explain both factors?
- Could the direction of influence be reversed?
- Was there random assignment?
- Could selection bias be present?
- Are relevant confounders measured?
- Does the timing support the proposed direction?
- Is there an established mechanism?

**Safer Language**

Use:

- “is associated with”;
- “is linked to”;
- “corresponds with”;
- “is consistent with”;
- “may help explain”;
- “suggests a possible relationship”.

Only claim causation when the design and evidence justify it.

---

## 14. Interpret Results in Context

**Objective**

Turn outputs into meaningful conclusions.

Move beyond statements such as:

> Model accuracy was 91%.

Instead explain:

- what the result means;
- why the pattern may exist;
- who is affected;
- whether the effect is large enough to matter;
- how the finding relates to external evidence;
- what decision or policy it could inform.

**Questions to Ask**

- What did we learn that was not obvious?
- Why does this finding matter?
- Is the result practically important?
- Who could use this information?
- What decisions could it influence?
- What should be investigated next?

---

## 15. State Limitations Clearly

**Objective**

Show that the team understands what the analysis can and cannot prove.

**Common Limitations**

- Missing or incomplete data
- Measurement error
- Limited time coverage
- Geographic mismatch
- Small sample size
- Unobserved confounding
- Aggregated data
- Changing collection methods
- Incompatible external sources
- Model assumptions
- Lack of causal identification

**Strong Limitation Format**

For each major limitation, explain:

1. what it is;
2. why it matters;
3. how it could affect the result;
4. how future work could address it.

Thoughtful limitations strengthen credibility.

---

## 16. Build a Clear Story

**Objective**

Present the analysis as a logical investigation.

**Recommended Narrative**

1. **Context**  
   What real-world issue are you studying?

2. **Research question**  
   What exactly are you trying to learn?

3. **Motivation**  
   Why does the question matter?

4. **Data**  
   What data did you use and why?

5. **Method**  
   How did you investigate the question?

6. **Key finding**  
   What is the most important result?

7. **Follow-up analysis**  
   How did you investigate the result further?

8. **Critical evaluation**  
   How reliable is the evidence?

9. **Limitations**  
   What can you not conclude?

10. **Conclusion and impact**  
    What is the answer, and why should anyone care?

**Important Principle**

Do not include every analysis attempted.

Include the analyses that best support the story.

---

## 17. Prepare the Reproducible Report

**The Report Should Include**

- Title
- Team members and SIDs
- Research question
- Motivation
- Data sources
- Data cleaning
- Exploratory analysis
- Methods
- Results
- Follow-up analysis
- Robustness checks
- Limitations
- Conclusion
- References
- Reproducibility information

**Reproducibility Checklist**

- Notebook or report runs from beginning to end
- File paths are portable
- Random seeds are fixed
- Package requirements are listed
- External data sources are linked and cited
- Manual steps are avoided or documented
- Figures and tables regenerate correctly
- No unnecessary cells or debugging output remain

---

## 18. Prepare the Three-Minute Video

**Recommended Structure**

| Time | Content |
|---|---|
| 0:00–0:20 | Hook and real-world context |
| 0:20–0:40 | Research question |
| 0:40–1:05 | Data and approach |
| 1:05–2:05 | Main findings and visuals |
| 2:05–2:30 | Follow-up analysis and critical evaluation |
| 2:30–2:50 | Conclusion and wider implications |
| 2:50–3:00 | Memorable closing statement |

**Video Guidelines**

- Use only the strongest visuals.
- Keep text minimal.
- Explain technical ideas simply.
- Make the research question explicit.
- State the conclusion clearly.
- Rehearse to remain under three minutes.
- Ensure narration and visuals support each other.

**Avoid**

- reading the report aloud;
- showing dense code;
- using too many graphs;
- describing every cleaning step;
- rushing through many methods;
- ending without answering the research question.

---

## 19. Suggested Three-Day Timeline

**Day 1 — Understand, Explore, and Choose**

**Morning**

- Attend the information session
- Understand the dataset
- Check quality and structure
- Brainstorm research questions

**Afternoon**

- Perform focused EDA
- Research wider context
- Test several possible questions
- Identify useful external data

**Evening**

- Finalise the research question
- Clean the data
- Build baseline analysis
- Divide follow-up tasks

**Day 2 — Analyse, Evaluate, and Refine**

**Morning**

- Complete feature engineering
- Run main statistical or machine learning analysis
- Establish validation strategy

**Afternoon**

- Perform follow-up analysis
- Add external data where justified
- Run robustness checks
- Conduct error analysis

**Evening**

- Decide final findings
- Create final figures
- Draft report sections
- Outline video narrative

**Day 3 — Communicate, Verify, and Submit**

**Morning**

- Complete report
- Refine explanations
- Add limitations and context
- Run notebook from start to finish

**Afternoon**

- Create and rehearse video
- Record final version
- Review report and visuals

**Evening**

- Final reproducibility check
- Verify names and SIDs
- Confirm video duration
- Check submission files
- Submit before the deadline

---

## 20. Team Roles

For a team of three, a useful structure is:

**Person 1 — Data and Engineering**

- Cleaning
- Wrangling
- Data integration
- Reproducibility
- Repository organisation

**Person 2 — Analysis and Evaluation**

- Statistical analysis
- Modelling
- Validation
- Robustness checks
- Error analysis

**Person 3 — Context and Communication**

- External research
- Visualisation
- Report editing
- Storytelling
- Video preparation

All members should still understand the full project.

---

## 21. Final Submission Checklist

**Research Question**

- [ ] The question is specific and meaningful.
- [ ] The question is answerable using the available data.
- [ ] The wider importance is clear.
- [ ] The conclusion directly answers the question.

**Analysis**

- [ ] The team used visual and statistical evidence.
- [ ] Methods are justified.
- [ ] External data has a clear purpose.
- [ ] Initial findings were followed up.
- [ ] Alternative explanations were considered.

**Critical Evaluation**

- [ ] Uncertainty is reported.
- [ ] Robustness checks are included.
- [ ] Causal claims are cautious.
- [ ] Limitations are explained.
- [ ] Conclusions do not exceed the evidence.

**Communication**

- [ ] The report has a clear narrative.
- [ ] The video is under three minutes.
- [ ] Figures are readable and labelled.
- [ ] Technical ideas are explained clearly.
- [ ] The main takeaway is memorable.

**Reproducibility**

- [ ] The report runs from start to finish.
- [ ] Random seeds are fixed.
- [ ] Data sources are documented.
- [ ] Cleaning decisions are explained.
- [ ] Packages and versions are recorded.
- [ ] No undocumented manual steps remain.

**Submission**

- [ ] All team names and SIDs are included.
- [ ] Correct files are uploaded.
- [ ] Video opens and plays correctly.
- [ ] Report renders correctly.
- [ ] Submission is completed before the deadline.

---

## Final Strategy

The strongest submission is not the one with the greatest number of models or graphs.

A winning submission should:

1. ask a compelling question;
2. investigate it rigorously;
3. use external information purposefully;
4. follow up on initial findings;
5. challenge its own conclusions;
6. communicate a clear and memorable story.

> **Ideate, prototype, refine, analyse, evaluate, communicate, and verify.**


## 22. Common Mistakes and How to Avoid Them

**1. Choosing a Question Too Quickly**

**Mistake:**
Selecting the first interesting idea without comparing alternatives.

**Risk:**
The question may be too broad, weakly supported, or difficult to explain.

**Better approach:**

* Brainstorm several questions.
* Test each with simple plots and summary statistics.
* Check whether the required data exists.
* Choose the question with the strongest balance of importance, evidence, and feasibility.

---

**2. Performing Random EDA**

**Mistake:**
Creating many plots without a clear purpose.

**Risk:**
The analysis becomes long, disconnected, and difficult to follow.

**Better approach:**
Before creating a figure, ask:

> What question will this figure help answer?

Keep only figures that:

* support the research question;
* reveal an important pattern;
* test an explanation;
* show a limitation;
* strengthen the final story.

---

**3. Starting with Complex Models**

**Mistake:**
Immediately using advanced models or extensive tuning.

**Risk:**
The team may spend too much time improving a metric without gaining meaningful insight.

**Better approach:**

1. Start with descriptive analysis.
2. Build a simple baseline.
3. Use an interpretable model.
4. Add complexity only when it provides clear value.

> Complexity should always have a purpose.

---

**4. Adding External Data Without a Clear Reason**

**Mistake:**
Adding external datasets only to make the project appear more advanced.

**Risk:**
This may introduce incompatible dates, geographic mismatches, missing values, or unnecessary complexity.

**Better approach:**
For every external dataset, complete this sentence:

> We added this dataset because it helps us test or explain...

Remove the dataset when its purpose is unclear.

---

**5. Data Leakage**

**Mistake:**
Allowing validation or test information to influence training.

**Common examples:**

* scaling before splitting the data;
* imputing using the full dataset;
* selecting features using all observations;
* using future data to predict the past;
* placing related records in both training and validation sets;
* repeatedly tuning against the test set.

**Better approach:**

* Fit preprocessing using training data only.
* Use stratified splitting for imbalanced classes.
* Use grouped splitting for related entities.
* Use chronological splitting for time-dependent data.

---

**6. Treating Correlation as Causation**

**Mistake:**
Claiming that one variable causes another because they are associated.

**Better approach:**
Consider:

* confounding variables;
* reverse causality;
* selection bias;
* timing;
* measurement error;
* alternative explanations.

Use cautious wording such as **“associated with”** or **“linked to”** unless causation is properly supported.

---

**7. Reporting Only the Best Result**

**Mistake:**
Showing only the most favourable model, split, or subgroup.

**Risk:**
The result may be unstable or selected by chance.

**Better approach:**
Include:

* baseline results;
* variation across folds or samples;
* confidence intervals where possible;
* alternative methods;
* robustness checks;
* informative unsuccessful results.

---

**8. Using Too Many Metrics**

**Mistake:**
Reporting many metrics without explaining which one matters most.

**Better approach:**

* Choose one primary metric.
* Add one or two supporting metrics.
* Explain why they suit the problem.

For example, **macro-F1** may be more useful than accuracy when all classes should be treated equally.

---

**9. Ignoring Negative or Unexpected Results**

**Mistake:**
Removing results that do not support the original hypothesis.

**Better approach:**
Unexpected findings may lead to the most interesting analysis.

Ask:

* Why was the expected relationship absent?
* Does it appear only in certain groups?
* Is an important variable missing?
* Did another factor dominate the result?
* Does the finding challenge a common assumption?
