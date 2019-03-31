# Improving Women's Menstrual Health Using Recommender AI

According to medical definition,  menstruation, commonly known as period or bleeding, is the process in a woman of discharging (through the vagina) blood and other materials from the lining of the uterus at about one monthly interval from puberty until menopause (ceasing of regular menstrual cycles), except during pregnancy. This discharging process lasts about 3-5 days.

Menstrual periods are a normal and natural part of a woman’s life. Regular menstrual periods in the years between puberty and menopause are usually a sign that your body is working normally. However, women face irregularites quite often regarding their period. They experience a number of symptoms indicating their irregularities in menstruation such as acne,	backache,	bloating, cramp,	diarrhea,	dizzy,	headache,	mood swing,	nausea,	sore etc.  Therefore, it is very important to track the period and take good care of health during the period. 

PSlove is popular period tracker app that has been helping thousands of women around the world to track their health - during and after the period. 

We have using the app data (Confidential) to find the common irregularities and symptoms women at different age are experiencing based on their given information through the app.

We came up with following observations in short:
1) We found many NaN values in dob columns. It can be explained that users avoid to inputting their personal inforlmation. So dropping this column is better for the exploratory data.
2) We can see some nonsense Max value in period_length_initial column. It is not normal if the period last more than 7 days.
3) There were 2779 missing records that needed to be deleted.
4) There is no NaN values found in Symptom dataset.
5) We know that period length is not valid if it is greater than 7. Let plot 3 group of periods to see how many invalid data.
6) The relation between period length and symptom increased with increase in period lengths.
7) The number of people who record their data are just a little bit more than half of registration. Maybe, they forget to track their activity after creating an account on application. There should be an automatic notification to remind users keeping to record their data.

The data is incomplete in most of the cases making it very difficult to analyze. To make an effective AI to improve app functionality, more informations are important to track. For example the dietry pattern of the  users having similar symptoms can help to understand the irregularities and remedies better.  After having sufficient data, it is possible to apply matrix factorization based recommender system for bringing in realtime health suggestion for the users having irregularities and severe symptoms.

