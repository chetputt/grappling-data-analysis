# grappling-data-analysis
Data analysis of grappling techniques from Brazilian Jiu-Jitsu, wrestling, and judo using Pandas and Matplotlib.

# Background

After watching several YouTube videos comparing different martial arts, I became interested in learning a grappling-based martial art. Many of the videos these videos pit martial arts against each other and rank different arts for certain scenarios. After watching several videos, I decided I wanted to learn a grappling art.


To better understand grappling arts from a data-driven perspective, I analyzed a dataset containing techniques from Brazilian Jiu-Jitsu (BJJ), wrestling, and judo.

# Questions Explored

This project aims to answer the following questions:

1. Which grappling martial art has the most named techniques?

2. How are techniques categorized across grappling martial arts?

3. Based on technique types, which martial art appears most suitable for controlling a fight?

# Dataset
This project uses the “Grappling techniques” (Version 1) dataset from Kaggle. It was contributed by liiucbs and contains a CSV file with information about grappling techniques in Brazilian Jiu-Jitsu (BJJ), wrestling, and judo. 

License: Apache 2.0 

Link: [Dataset Here](https://www.kaggle.com/datasets/liiucbs/grappling-techniques/data)

**Note:** The raw CSV file is not included in this repository. To run the analysis, please download the dataset on Kaggle and place it in the appropriate directory

# Analysis and Results
### 1. Number of Techniques per Martial Art

Based on the dataset, Brazilian Jiu-Jitsu has the highest number of named techniques, followed by wrestling and then judo.

This suggests that BJJ may be more complex in terms of technique variety, which could imply a longer learning curve compared to the other arts. Wrestling falls between BJJ and judo in terms of technique count.

<img width="1240" height="434" alt="technique counts" src="https://github.com/user-attachments/assets/c5b5dea7-b015-4e5d-a20f-48ce23f7aab1" />

<img width="630" height="472" alt="technique distribution" src="https://github.com/user-attachments/assets/dc471af7-6680-4271-8140-93f17f5444ed" />

### 2. Technique Categories

The dataset includes 11 distinct technique categories, such as submissions, takedowns, and control-based techniques.

Submissions are the most common category, which aligns with the strong presence of Brazilian Jiu-Jitsu techniques in the dataset. Takedowns are the second most frequent category, reflecting the emphasis placed on takedowns in wrestling and judo.

<img width="634" height="470" alt="technique types" src="https://github.com/user-attachments/assets/d56cc946-9f5e-4299-97c3-7b549a935f1f" />

### 3. Techniques for Control

To evaluate “control,” this analysis focuses on techniques categorized as dominant or control-oriented.

According to the dataset, Brazilian Jiu-Jitsu contains the highest number of dominant techniques, suggesting it may be well-suited for controlling a fight. Wrestling and BJJ show similar counts for defensive techniques, indicating that either could be effective for defensive-focused grappling.

<img width="630" height="479" alt="dominant vs defensive techniques" src="https://github.com/user-attachments/assets/b53c3ed2-af8f-4f37-9551-7ff88fd30d7b" />

# Summary

Using this dataset, I gained insight into the distribution and categorization of grappling techniques across three major martial arts. Based on the available data, Brazilian Jiu-Jitsu stands out for both technique variety and control-oriented techniques, making it an appealing option for someone interested in a control-focused grappling art.

# Limitations

The dataset is biased toward Brazilian Jiu-Jitsu, while judo appears underrepresented compared to real-world technique catalogs.

The data does not measure effectiveness, frequency of use, or success rate of techniques.

Other important factors, such as cost, availability, injury risk, and competition rules, are not considered.

This analysis focuses solely on technique data and should not be interpreted as a definitive ranking of martial arts.
