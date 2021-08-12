

1. #          Column           Non-Null Count  Data type      Description                                             Example
###  0   CustomerID         4687 non-null    object       Unique no for each customer.                             5196-WPYOW	
###  1   Count              4691 non-null   float64       No. of account with one id                               1.0
###  2   Country            4708 non-null   object        Country where Customer lives                             United States
###  3   State              4715 non-null   object        State where Customer lives                               California	
###  4   City               4688 non-null   object        City where Customer lives.                               Los Angeles
###  5   Zip Code           4698 non-null   float64       Zip-code of Customer place                               93446.0	
###  6   Lat Long           4713 non-null   object        Geographical coordinates of Customer place               35.634222, -120.728341
###  7   Latitude           4695 non-null   float64       Geographical coordinates of Customer place in Y-axis     35.634222
###  8   Longitude          4685 non-null   float64       Geographical coordinates of Customer place in X-axis     -120.728341
###  9   Gender             4698 non-null   object        Customer Gender                                          Male
###  10  Senior Citizen     4711 non-null   object        Whether customer is a senior citizen                     Yes
###  11  Partner            4678 non-null   object        Is customer Partner using it or not                      Yes
###  12  Dependents         4672 non-null   object        Is customer dependents using it or not                   No
###  13  Tenure Months      4704 non-null   float64       For how long customer is using the services(months)      15
###  14  Phone Service      4692 non-null   object        Phone services included or not                           Yes
###  15  Multiple Lines     4696 non-null   object        Using multiple line or single line                       Single
###  16  Internet Service   4692 non-null   object        Is Net services included and way of providing net        Fiber optic
###  17  Online Security    4674 non-null   object        Customer is protected against online threat or not       Yes
###  18  Online Backup      4714 non-null   object        Online Backup is provided to customer or not             No
###  19  Device Protection  4711 non-null   object        Device Protection is covered for customer or not         Yes
###  20  Tech Support       4695 non-null   object        Tech support is provided to customer or not              Yes
###  21  Streaming TV       4686 non-null   object        Whether TV Subscription included or not                  No
###  22  Streaming Movies   4688 non-null   object        Whether Movies Subscription included or not.             Yes
###  23  Contract           4672 non-null   object        Validity of Plan taken by customer.                      1 month
###  24  Paperless Billing  4694 non-null   object        Whether mode of payment was paperless or not.            No
###  25  Payment Method     4717 non-null   object        Payment method used by customer.                         Credit Card
###  26  Monthly Charges    4714 non-null   float64       Monthly charges customer is paying.                      70.
###  27  Total Charges      4704 non-null   object        Total Payment made by customer from starting till date.  4350
###  28  CLTV               4692 non-null   float64       Average Revenue generated from customer of entire life.  6580
###  29  Churn Reason       1261 non-null   object        Reason for continuing or disconnecting the services.     Limited range of services
###  30  Churn Value        4693 non-null   float64       Whether customer will continue or not                    1.0
