# Health Message Framing A/B Test Analysis

## Import Libraries


import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.proportion import proportion_confint


## Load Data


df = pd.read_excel(
    "/file address/health_message_framing_experiment_v2.xlsx")


## Funnel Analysis

summary = df.groupby('Message_Type').agg(
    Users=('User_ID', 'count'),
    Opens=('Opened_Message', 'sum'),
    Clicks=('Clicked_Learn_More', 'sum'),
    Subscriptions=('Subscribed', 'sum')
)

summary['Open_Rate'] = (
    summary['Opens'] /
    summary['Users']
)

summary['Click_Rate'] = (
    summary['Clicks'] /
    summary['Opens']
)

summary['Subscription_Rate'] = (
    summary['Subscriptions'] /
    summary['Clicks']
)

summary['Conversion_Rate'] = (
    summary['Subscriptions'] /
    summary['Users']
)

summary.round(4)

## Conversion Rate Comparison


summary[['Conversion_Rate']]


## Absolute Lift


absolute_lift = (
    summary.loc['Positive', 'Conversion_Rate']
    -
    summary.loc['Negative', 'Conversion_Rate']
)

print(f"Absolute Lift: {absolute_lift:.2%}")


## Create Groups


positive = df[
    df['Message_Type'] == 'Positive'
]

negative = df[
    df['Message_Type'] == 'Negative'
]


## Confidence Intervals

pos_ci = proportion_confint(
    count=positive['Subscribed'].sum(),
    nobs=len(positive),
    alpha=0.05
)

neg_ci = proportion_confint(
    count=negative['Subscribed'].sum(),
    nobs=len(negative),
    alpha=0.05
)

print(
    f"Positive CI: {pos_ci[0]:.2%} to {pos_ci[1]:.2%}"
)

print(
    f"Negative CI: {neg_ci[0]:.2%} to {neg_ci[1]:.2%}"
)


## Z-Test


successes = [
    positive['Subscribed'].sum(),
    negative['Subscribed'].sum()
]

observations = [
    len(positive),
    len(negative)
]

z_stat, p_value = proportions_ztest(
    successes,
    observations
)

print("Z-score:", round(z_stat, 3))
print("P-value:", round(p_value, 5))


## Age Group Analysis


age_analysis = pd.crosstab(
    df['Age_Group'],
    df['Message_Type'],
    values=df['Subscribed'],
    aggfunc='mean'
) * 100

age_analysis.round(2)


## Personalization Recommendation


recommendation = age_analysis.idxmax(
    axis=1
)

print(recommendation)


## Export for Tableau


summary.to_csv("summary.csv")

age_analysis.to_csv("age_analysis.csv")



kpi_df = pd.DataFrame({
    'Metric':['Absolute Lift','Z Score','P Value'],
    'Value':[absolute_lift*100,z_stat,p_value]
})

kpi_df.to_csv('kpi_metrics.csv',index=False)


funnel_df = pd.DataFrame({
    'Stage': ['Users','Opens','Clicks','Subscriptions'] * 2,
    'Message_Type': ['Positive'] * 4 + ['Negative'] * 4,
    'Count': [
        summary.loc['Positive','Users'],
        summary.loc['Positive','Opens'],
        summary.loc['Positive','Clicks'],
        summary.loc['Positive','Subscriptions'],
        summary.loc['Negative','Users'],
        summary.loc['Negative','Opens'],
        summary.loc['Negative','Clicks'],
        summary.loc['Negative','Subscriptions']
    ]
})

funnel_df

funnel_df.to_csv(
    "funnel_data.csv",
    index=False
)
