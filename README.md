# Task Management Web App

This repository contains the code for a simple Task Management web application built with HTML, CSS, Python and JavaScript, utilizing AWS Amplify, AWS Lambda, AWS IAM, AWS API and AWS DynamoDB.

<img width="1180" alt="Screen Shot 2023-06-25 at 02 43 21" src="https://github.com/holycabbage/Task_Management_Web_App-AWS-/assets/90731193/7f06c8e8-7a1d-4fd4-8420-b2c58c7a719a">

## Overview

The Task Management Web App allows users to create and view tasks. Each task has an ID, description, creation date, completion date, and status.
And the task will be saved in the database.

## Step-by-step guide to replicate this project

### Step 1: Prepare the frontend
1. I started by creating the frontend of the application using HTML, CSS, and JavaScript. The frontend consists of a simple form that takes user inputs for task details.
   Script: (index.html)   

### Step 2: Set up AWS Amplify
1. I set up an AWS Amplify application.
2. I used the drag and drop option in AWS Amplify console to upload my index.html file.
   <img width="1405" alt="Screen Shot 2023-06-25 at 01 49 59" src="https://github.com/holycabbage/Task_Management_Web_App-AWS-/assets/90731193/f3884a83-65aa-4a8c-b4d4-1b4157aed359">


### Step 3: Set up DynamoDB
1. Next, I created a new DynamoDB table with the name 'Task_Management_Table' and set 'ID' as the primary key.

### Step 4: Create AWS Lambda Function
1. I created a new AWS Lambda function to handle the backend logic.
2. I wrote the Lambda function in Python to handle CRUD operations on the DynamoDB table.
3. I ensured that the Lambda function had the correct permissions to access DynamoDB.
Script:(TM_lambda_py)

### Step 5: Set IAM Policies
1. I navigated to AWS Identity and Access Management (IAM).
2. I created a new policy(inline policy) with the necessary permissions for the Lambda function to access the DynamoDB table, then attached this policy to the Lambda function.
Script:(Execution Role Policy JSON.txt)

### Step 6: Connect with API Gateway
1. I set up an API Gateway that acts as an interface between the frontend and the backend.
2. I connected my AWS Lambda function with the API Gateway.
   <img width="899" alt="Screen Shot 2023-06-25 at 01 49 50" src="https://github.com/holycabbage/Task_Management_Web_App-AWS-/assets/90731193/1e798739-a44c-42a8-b25f-a51b256bf540">

    <img width="1419" alt="Screen Shot 2023-06-25 at 01 49 23" src="https://github.com/holycabbage/Task_Management_Web_App-AWS-/assets/90731193/30d25395-2254-4aba-b6a1-884373c73fd1">

### Step 7: Connect Frontend and Backend
1. I replaced the `API_URL` in the JavaScript part of `index.html` with my API Gateway URL.

### Step 8: Deploy with AWS Amplify
1. After committing and pushing my changes to the GitHub repository, AWS Amplify automatically detected the changes and deployed my application.
<img width="1405" alt="Screen Shot 2023-06-25 at 01 49 59" src="https://github.com/holycabbage/Task_Management_Web_App-AWS-/assets/90731193/5496bd21-b0a8-4350-b5d3-88ad7ce9813f">



## How To Use

Simply input the details of your task in the relevant fields, then click "Add Task". The task will be sent to the backend and stored in the database.
<img width="1440" alt="Screen Shot 2023-06-25 at 01 52 35" src="https://github.com/holycabbage/Task_Management_Web_App-AWS-/assets/90731193/6e98b75c-6d45-4f7e-86d2-9895d24f32d5">

## Output
show "Success!" and task has been saved in database
<img width="1440" alt="Screen Shot 2023-06-25 at 01 48 27" src="https://github.com/holycabbage/Task_Management_Web_App-AWS-/assets/90731193/629acafd-87a3-4c44-87f2-4778e8ea0f67">

<img width="1386" alt="Screen Shot 2023-06-25 at 01 48 50" src="https://github.com/holycabbage/Task_Management_Web_App-AWS-/assets/90731193/607ccf11-8d3d-4b2c-9990-80f07414c314">


## Reference
This project was developed following the guide on [YouTube](https://www.youtube.com/watch?v=7m_q1ldzw0U). (https://www.youtube.com/watch?v=7m_q1ldzw0U)
