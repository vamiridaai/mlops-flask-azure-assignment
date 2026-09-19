# Part 1: Conceptual Questions

## 1. MLOps
MLOps (Machine Learning Operations) combines machine learning development, software engineering, and DevOps practices to make ML systems reproducible, testable, deployable, and maintainable. For a Flask ML application, MLOps includes version control, dependency management, automated testing, CI/CD, cloud deployment, and operational monitoring. The trained model is exposed through a Flask API, while automated pipelines validate and deploy changes consistently.

## 2. Continuous Integration and Delivery (CI/CD)
Continuous Integration automatically validates code changes through dependency installation, linting, and unit testing. Continuous Delivery/Deployment moves validated versions toward or into the production environment. GitHub Actions supports CI/CD through YAML workflows stored in the repository. A push can automatically configure Python, create a virtual environment, install dependencies, lint the code, and execute tests.

## 3. Cloud Service Integration
To connect GitHub to Azure DevOps, create an Azure DevOps project, create a pipeline, select GitHub as the source, authorize repository access, select or create a YAML pipeline, and configure the Azure deployment resources. Cloud integration connects source control, automated validation, deployment infrastructure, and the production environment, making releases repeatable and reducing manual deployment errors.

## 4. ARM Service Connection
An Azure Resource Manager (ARM) service connection is an authenticated connection between Azure DevOps and an Azure subscription or selected Azure resources. It provides the pipeline with an authorized identity that can deploy resources such as an Azure App Service without requiring a developer to authenticate manually during every pipeline run.

## 5. Environment Setup
A Python virtual environment isolates project dependencies from system-wide packages and other projects. This reduces dependency conflicts and improves reproducibility. Machine learning projects often rely on specific versions of numerical and ML libraries, so an isolated environment plus requirements.txt helps local development, CI agents, and cloud deployments use a consistent dependency set.

## 6. Pipeline Triggers
A pipeline trigger defines which event starts an Azure Pipeline. For example, a YAML trigger configured for the main branch causes pushes to main to start the pipeline. Trigger configuration determines which branches initiate automated build, testing, packaging, and deployment operations.

## 7. Stages and Jobs
A stage is a major logical phase of an Azure Pipeline, such as Build, Test, or Deploy. A job is a collection of steps executed by an agent within a stage. Multiple stages and jobs make an ML deployment easier to organize and control. A deployment stage can depend on successful build and test work so that invalid changes do not reach production.

## 8. YAML Configuration for Pipelines
YAML provides a version-controlled and reproducible definition of pipeline behavior. It can be reviewed together with application changes and reused consistently. A Python Azure deployment YAML normally includes triggers, an agent pool, Python version, dependency installation, model/build preparation, linting, unit tests, artifact packaging, an Azure service connection, the App Service name, and a deployment task.
