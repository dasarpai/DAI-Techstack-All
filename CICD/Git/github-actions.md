#myprojects # dasarpai #github.io

# github actions
- It is about building application and deploying application.
- github actions works only for the code kept on githubb.- 

# Trigger
- There are several trigger point when github action can be triggered. Like, forking, checkout, checkin, issue fixing etc.
- There are many aspects of build and deployment. To take care of these aspects code is written in the workflow file in folder 
.github/workflows/
- There are several pre-written actions, you can use and modify them for your work.

# Workflow need to take care of 
- Langauge of the code.
- Dependencies like pip or npm or gem libraries
- os required to build the code 
- checkout latest or particular version for building
- compiling code 
- if build fail then report this with specific details to the people involved.
- run test case.
- if test case fail then report this with specific details to the people involved.
- os required to deploy the code 
- deploy the code 
- notify

