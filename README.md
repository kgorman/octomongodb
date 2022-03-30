# octomongodb
A simple agent to stream Octoprint information from 3d printing process to MongoDB Atlas

# configuration

The agent uses os variables for source/dest identification and authentication.

For example:
```
#!/bin/bash

export SOURCE_BASE_URL="http://<octoprint IP>/api/printer?exclude=sd"
export SOURCE_KEY="<api key defined in octoprint>"

export TARGET_BASE_URL="https://data.mongodb-api.com/app/<endpoint_id>/endpoint/data/beta/action/insertOne"
export TARGET_KEY="<api key from MongoDB Atlas"
export TARGET_NAME="<your cluster name>" 
```