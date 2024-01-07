# Blood Donation System

## Overview

Blood Donation System is a web application built with Flask to manage blood donation activities. It includes features for adding blood donors, managing blood donations, and handling blood requests.

## Features

- Add Blood Donor
- Add Blood to Bank
- Request Blood

## Folder Structure

- **templates:** HTML templates for the web pages.
- **static:** Static files (CSS, images, etc.).
- **app.py:** The main Flask application file.

## Assumptions

- Assuming when adding blood to bank, there is already a donor created in Donors table

## Deployment

- **Storage:** Azure SQL Server
- **Frontend:** Azure App Service
- **Backend:** Azure App Service
- **Gateway:** Azure API Management
- **Queue:** Azure Message Queue
- **PhotoStorage:** Azure Blob Storage
- **Scheduler:** Azure App Service + Azure Function App

## Encountered Issues

1. Gateway Integration
    Resolution: [Microsoft Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts)

## Deployment Urls

1. **UI Layer Deployed at:**
    `https://sefrontend.azurewebsites.net/`
2. **Donor Service Deployed at:**
    `https://sebackend.azurewebsites.net/`
3. **Scheduler Service Deployed at:**
    `https://bloodserviceschedule.azurewebsites.net/`