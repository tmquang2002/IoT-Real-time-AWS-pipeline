# IoT Device Monitoring & Analytics System (AWS Serverless)

<img src="https://www.rrms.com/wp-content/uploads/2022/03/shutterstock_1716092806-altered-FLAT-1-scaled.jpg" alt="IoT Architecture" width="800"/>

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [Setup Instructions](#setup-instructions)
- [Visualizations](#visualizations)
- [Conclusion](#conclusion)
- [Future Direction](#future-direction)

## Introduction
The **IoT Device Monitoring & Analytics System** is a serverless solution for real-time monitoring, alerting, and analytics of IoT device data.  
It supports real-time alert notifications when sensor values exceed thresholds, while also storing historical data for analysis and visualization.  
The system is built entirely on AWS managed services, ensuring scalability, low operational overhead, and cost efficiency.

## Technologies Used
- **AWS API Gateway** – Receives data from IoT devices via HTTP endpoints.
- **AWS Lambda** – Processes real-time data and routes it to the appropriate storage or alert system.
- **Amazon DynamoDB** – Stores the latest state of device readings for quick access.
- **Amazon SNS** – Sends instant alert notifications via email.
- **Amazon S3** – Stores historical IoT data in raw format for analytics.
- **AWS Glue Data Catalog** – Manages metadata for Athena queries.
- **Amazon Athena** – Queries IoT data stored in S3 using SQL.
- **Amazon QuickSight** – Creates interactive dashboards for data visualization.
- **Amazon CloudWatch** – Monitors metrics and logs for system health and performance.

## System Architecture
<img src="https://i.ibb.co/rKgcyNfM/diagram.png" alt="IoT Architecture" width="1000"/>

### 1. Data Ingestion
- **IoT Devices** (e.g., temperature, humidity, vibration sensors) send data to the system via **API Gateway**.
- API Gateway triggers **Lambda functions** to process incoming sensor readings.

### 2. Real-Time Processing & Alerting
- The first Lambda function:
  - Saves the latest sensor data to **DynamoDB**.
  - Checks for threshold breaches.
  - If a threshold is exceeded, **Amazon SNS** sends an alert email.
- **CloudWatch** collects logs and metrics for monitoring.

### 3. Historical Data Storage & Analytics
- A second Lambda function:
  - Saves incoming data in **Amazon S3** with a time-partitioned directory structure (e.g., `year=2025/month=08/day=08/hour=10`).
- **AWS Glue Crawler** updates the **Glue Data Catalog** with new partitions.
- **Amazon Athena** queries historical IoT data directly from S3.
- **Amazon QuickSight** visualizes aggregated and filtered data.

## Setup Instructions

### 1. Deploy API Gateway & Lambda Functions
- Create an **HTTP API Gateway** endpoint for device data submission.

<img src="https://i.ibb.co/gFR20syN/api.png" alt="IoT Architecture" width="500"/>

- Deploy **Lambda functions** for Real-time processing & alerting.

<img src="https://i.ibb.co/5g7zzDT7/lambda-3.png" alt="IoT Architecture" width="500"/>

- Deploy **Lambda functions** for Historical data storage to S3.

<img src="https://i.ibb.co/jvyQrHtb/lambda-2.png" alt="IoT Architecture" width="500"/>


### 2. Configure DynamoDB & SNS
- Create a **DynamoDB** table to store the latest device states.

<img src="https://i.ibb.co/847nNdGz/dynamodb.png" alt="IoT Architecture" width="500"/>

- Set up an **SNS topic** for email alerts and subscribe recipients.

<img src="https://i.ibb.co/PshtPV4c/SNS.png" alt="IoT Architecture" width="500"/>


### 3. Configure S3 & Glue
- Create an **S3 bucket** for historical data.


<img src="https://i.ibb.co/WWRvvDxb/s3.png" alt="IoT Architecture" width="500"/>

- Set up an **AWS Glue Crawler** to detect new data partitions.

<img src="https://i.ibb.co/G4hwwPJ9/glue2.png" alt="IoT Architecture" width="500"/>

### 4. Set Up Analytics & Visualization
- Use **Athena** to query S3 data.

<img src="https://i.ibb.co/jkL6C9Py/athena.png" alt="IoT Architecture" width="500"/>

- Connect **QuickSight** to Athena for dashboard creation.

<img src="https://i.ibb.co/MDyNn4qS/quicksight.png" alt="IoT Architecture" width="500"/>


## Visualizations
**QuickSight Dashboards** may include:
- **Real-time alerts table** – List of recent threshold breaches.
- **Historical trends** – Temperature/humidity changes over time.
- **Device status heatmap** – Geographic or categorical view of device states.
- **Aggregated statistics** – Average, min, max sensor values by day/week.

## Conclusion
This project provides a fully serverless IoT monitoring system with real-time alerts and historical analytics. It leverages AWS managed services to achieve scalability, flexibility, and cost efficiency.

## Future Direction
- Integrate AWS IoT Core for MQTT-based device communication.
- Add anomaly detection with Amazon SageMaker.
- Enable multi-region deployment for higher availability.
- Expand alerting channels (SMS, Slack, etc.).

## Contact
For any questions or feedback, please reach out to [tmquang120202@example.com](mailto:tmquang120202@example.com).
