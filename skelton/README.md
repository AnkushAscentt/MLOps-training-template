# tdspds-mlops-sagemaker-training-sample

This guide outlines best practices and a recommended structure for organizing Python projects to ensure readability, maintainability, and consistency in your codebase.

## Project Structure

├───.github                        
│   └───workflows&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# CICD callable workflows</br>
├───conf</br>
│      └───tdspds-config.yml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Variables configuration 1 </br>
│      └───pipelines-config.yml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Variables configuration 2 </br>
│   └── ...</br>
├───data&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Local dataset files</br>
├───docs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Documents</br>
├───example&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# sample scripts </br>
├───logs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# logging details</br>
├───notebooks&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                      # sample notebooks</br>
├───scripts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                        # Command-line scripts (if any)</br>
├── src&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Main Python Code</br>
│       ├── train.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # training script </br>
│   └───tests&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                      # Unit tests</br>
│&nbsp;&nbsp;&nbsp;&nbsp;       ├── test1.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # unit test module1</br>
│&nbsp;&nbsp;&nbsp;&nbsp;       ├── test2.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # unit test module2</br>
│&nbsp;&nbsp;&nbsp;&nbsp;        └── ...</br>
└───utilities&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Reuseable modules</br>
│   ├── module1.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # resuable module1</br>
│   ├── module2.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # resuable module2</br>
│   └── ...</br>


## Code Structure

- **PEP 8 Style Guide**: Follow PEP 8 for code formatting.
- **Modularization**: Organize code into modules and packages.
- **Descriptive Naming**: Use clear, descriptive variable and function names.
- **Import Organization**: Organize imports at the top of your files.

## Documentation

- **Docstrings**: Use docstrings to document modules, classes, and functions.
- **Example File**: Include a file with project information, usage, and examples.

## Dependency Management

- **requirements.txt**: List project dependencies.
- **Poetry**: Use Poetry for managing and installing dependencies.

## Version Control

- **GitHub**: Use GitHub for version control.
- **.gitignore**: Exclude unnecessary files from version control.

## Testing

- **Unit Tests**: Write unit tests using frameworks like unittest, pytest, or nose.
- **Test Organization**: Store tests in a separate directory following a naming convention.

## Logging

- Use the Python logging module for debugging and monitoring.

## Command-Line Interface (CLI)

- Use argparse or click for creating a user-friendly CLI.

## Packaging and Distribution

- **setup.py**: For TMNA CI/CD.
- **Poetry**: Use Poetry for building, packaging, and distributing the project.
- **PyPI**: Publish your project on the Python Package Index if needed.

## Error Handling

- Implement proper error and exception handling.

## Code Comments

- Use comments sparingly, explaining complex sections or non-obvious decisions.

## Code Review

- Encourage code reviews for quality and best practice adherence.

## Features in this Repository

#### A. Launch a Sagemaker training job.

#### B. Log experiment and store trained model in WandB Model registry.

#### C. Sagemaker Traning Job Aler.

#### Requirements

- Terraform 
- AWS CLI configured with necessary permissions

#### Setup

- update conf : The following parameters needs to be updated in conf/tdspds-config.yml

  - sns-topic - (True / False) A boolean value indicating weather to enable the usage of an SNS (Simple Notification Service) topic for notifications.

  - service - Model name ( Basically defines servise name )

  - email-addresses - Provides a list of email addresses to receive notifications.

  - transform-fail-enabled - (True / False) Enables notifications for failures during the batch transformation process.

#### Action

- The Following Resources to be created

   1) SNS Topic 
   2) SNS Subscription
   3) CloudWatch Event Rule 
   4) CloudWatch Event Target 

#### Post Deploy 
   
   - When resources has deployed using terraform. It will applied for all Sagemaker transformm jobs. Whenever Sagemaker transform job state changes or failed that will notify using email notification with all job details.
    
     ![image](https://github.com/Toyota-Motor-North-America/tdspds-mlops-sagemaker-batch-inference-sample/assets/147443118/c5fdc6ad-a540-424f-9f54-8ac131ad1336)

## Continuous Integration (CI)

- Set up CI/CD pipelines for automatic tests and checks.

## Documentation Generation

- Use tools like Sphinx to generate documentation from docstrings.

## Licensing

- Include a license file (e.g., LICENSE.txt) to specify usage terms.

Remember to adapt to evolving best practices and utilize tools like linters and static analysis (e.g., flake8, pylint) to maintain code quality and compliance with standards.
=======
# tdspds-mlops-sagemaker-training-sample

This guide outlines best practices and a recommended structure for organizing Python projects to ensure readability, maintainability, and consistency in your codebase.

## Project Structure

├───.github                        
│   └───workflows&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# CICD callable workflows</br>
├───conf</br>
│      └───config_1.yml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Variables configuration 1 </br>
│      └───config_1.yml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Variables configuration 2 </br>
│   └── ...</br>
├───data&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Local dataset files</br>
├───docs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Documents</br>
├───example&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# sample scripts </br>
├───logs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# logging details</br>
├───notebooks&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                      # sample notebooks</br>
├───scripts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                        # Command-line scripts (if any)</br>
├── src&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Main Python Code</br>
│       ├── train.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # training script </br>
│   └───tests&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                      # Unit tests</br>
│&nbsp;&nbsp;&nbsp;&nbsp;       ├── test1.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # unit test module1</br>
│&nbsp;&nbsp;&nbsp;&nbsp;       ├── test2.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # unit test module2</br>
│&nbsp;&nbsp;&nbsp;&nbsp;        └── ...</br>
└───utilities&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Reuseable modules</br>
│   ├── module1.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # resuable module1</br>
│   ├── module2.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    # resuable module2</br>
│   └── ...</br>


## Code Structure

- **PEP 8 Style Guide**: Follow PEP 8 for code formatting.
- **Modularization**: Organize code into modules and packages.
- **Descriptive Naming**: Use clear, descriptive variable and function names.
- **Import Organization**: Organize imports at the top of your files.

## Documentation

- **Docstrings**: Use docstrings to document modules, classes, and functions.
- **Example File**: Include a file with project information, usage, and examples.

## Dependency Management

- **requirements.txt**: List project dependencies.
- **Poetry**: Use Poetry for managing and installing dependencies.

## Version Control

- **GitHub**: Use GitHub for version control.
- **.gitignore**: Exclude unnecessary files from version control.

## Testing

- **Unit Tests**: Write unit tests using frameworks like unittest, pytest, or nose.
- **Test Organization**: Store tests in a separate directory following a naming convention.

## Logging

- Use the Python logging module for debugging and monitoring.

## Command-Line Interface (CLI)

- Use argparse or click for creating a user-friendly CLI.

## Packaging and Distribution

- **setup.py**: For TMNA CI/CD.
- **Poetry**: Use Poetry for building, packaging, and distributing the project.
- **PyPI**: Publish your project on the Python Package Index if needed.

## Error Handling

- Implement proper error and exception handling.

## Code Comments

- Use comments sparingly, explaining complex sections or non-obvious decisions.

## Code Review

- Encourage code reviews for quality and best practice adherence.

## Continuous Integration (CI)

- Set up CI/CD pipelines for automatic tests and checks.

## Documentation Generation

- Use tools like Sphinx to generate documentation from docstrings.

## Licensing

- Include a license file (e.g., LICENSE.txt) to specify usage terms.

Remember to adapt to evolving best practices and utilize tools like linters and static analysis (e.g., flake8, pylint) to maintain code quality and compliance with standards.

