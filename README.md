# Health Message Framing A/B Test Analysis

## Overview

This project evaluates the impact of **positive** and **negative** message framing on user subscription behavior using an A/B testing approach.

A synthetic dataset of **10,000 users** was created to simulate a health campaign where users were randomly assigned either a positive or negative health message. Python was used for statistical analysis, while Tableau was used to build an executive dashboard for business stakeholders.

---

# Business Problem

A health and wellness company wants to improve the conversion rate of its email campaigns.

The marketing team is unsure whether users respond better to:

- **Positive framing**
  > "Start today and become healthier and stronger."

or

- **Negative framing**
  > "Ignoring your health today could lead to serious health problems."

The objective is to determine which message framing results in a higher subscription rate and whether campaign performance differs across age groups.

---

# Objectives

- Compare Positive vs Negative message framing
- Calculate campaign funnel metrics
- Measure conversion lift
- Validate results using statistical testing
- Analyze conversion across different age groups
- Build an executive dashboard for business stakeholders

---

# Dataset

**Total Users:** 10,000

Each user contains the following attributes:

- User ID
- Month
- Age Group
- Gender
- Exercise Frequency
- Message Type
- Message Text
- Opened Message
- Clicked Learn More
- Subscribed

---

# Tools Used

- Python
- Pandas
- NumPy
- Statsmodels
- Tableau Public

---

# Statistical Techniques

The following analyses were performed:

- Funnel Analysis
- Conversion Rate Analysis
- Absolute Lift
- 95% Confidence Intervals
- Two-Proportion Z-Test
- Age Group Segmentation

---

# Python Analysis

## Funnel Metrics

Calculated:

- Users
- Opens
- Clicks
- Subscriptions

along with:

- Open Rate
- Click Rate
- Subscription Rate
- Overall Conversion Rate

---

## Conversion Rate

| Message Type | Conversion Rate |
|--------------|----------------:|
| Positive | **6.36%** |
| Negative | **4.90%** |

---

## Absolute Lift

Positive framing improved conversions by:

**1.46 percentage points**

---

## Statistical Validation

A **Two-Proportion Z-Test** was conducted using **Statsmodels**.

Results:

| Metric | Value |
|---------|-------|
| Z-Score | **3.167** |
| P-Value | **0.00154** |

### Interpretation

Since:

```
P-value < 0.05
```

the null hypothesis was rejected.

The improvement observed with positive framing is **statistically significant** and unlikely to have occurred due to random chance.

---

## Age Group Analysis

| Age Group | Negative | Positive |
|------------|----------|----------|
| 18–25 | 4.18% | 7.04% |
| 26–40 | 4.89% | 6.31% |
| 40+ | 6.32% | 5.08% |

### Insight

- Positive framing performs better for users aged **18–25** and **26–40**.
- Negative framing performs better for users aged **40+**.

This suggests that **personalized messaging based on age** could further improve campaign performance.

---

# Tableau Dashboard

The dashboard includes:

- KPI Cards
  - Positive Conversion Rate
  - Negative Conversion Rate
  - Absolute Lift
  - P-Value

- Conversion Funnel by Message Type

- Conversion Rate by Age Group

---

# Key Business Insights

- Positive framing achieved a **6.36%** conversion rate compared to **4.90%** for negative framing.

- Positive messaging generated an **absolute lift of 1.46 percentage points**.

- Statistical testing confirmed that the difference is significant (**p = 0.00154**).

- Users below 40 years responded more positively to encouraging messages.

- Users aged 40 and above responded better to negative framing.

---

# Business Recommendation

Instead of using a single campaign for all users:

- Use **Positive Framing** for users aged **18–40**
- Use **Negative Framing** for users aged **40+**

Personalizing campaign messaging by age has the potential to improve overall conversion rates.

---

# Project Structure

```
Health-Message-Framing-AB-Test
│
├── README.md
├── health_message_framing_analysis.py
├── health_message_framing_experiment_v2.xlsx
├── summary.csv
├── age_analysis.csv
├── funnel_data.csv
├── kpi_metrics.csv
├── dashboard.twbx
└── dashboard.png
```

---

# Dashboard Preview

> *(Add a screenshot of your Tableau dashboard here.)*

---

# Skills Demonstrated

- A/B Testing
- Statistical Hypothesis Testing
- Python Data Analysis
- Pandas
- Data Visualization
- Tableau Dashboard Design
- Marketing Analytics
- Business Storytelling
