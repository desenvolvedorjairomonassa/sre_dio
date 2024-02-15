# sre_dio

desafio DIO - Aceleração Internacional - Working as an SRE in an International Company with Azure
-------------
-------------

Challenge 1 
----------

As part of the responsibilities of Site Reliability Engineers (SREs), it is essential to implement and maintain monitoring systems to detect and respond to issues proactively. Additionally, it is crucial to configure alerts that notify teams when problems occur, enabling a quick and effective response. In this challenge, you will be tasked with developing a monitoring and alert system capable of identifying anomalies in performance metrics and notifying the team when issues are detected.

Input
The input will consist of three integers representing performance metrics collected from different components of a system, namely: the percentage of CPU usage, RAM memory usage, and application response time, respectively.

Output
The output of the system will be an alert notification whenever it detects an anomaly in any of the performance metrics. These notifications will be triggered if CPU consumption reaches or exceeds 80%, if RAM memory usage is equal to or greater than 70%, or if the application response time is greater than 250ms.

For example, if the CPU is operating at 95%, the alert "Alert: High CPU usage detected (95%)" should be generated. Similarly, if the response time is 300ms, the warning to be issued is "Alert: Application response time above the limit (300ms)". If no anomalies are identified, the message "No anomalies detected" should be emitted.
