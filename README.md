# octomongodb
A simple agent to stream Octoprint information from 3d printing process to MongoDB Atlas

# install
### Clone this repo
Open a terminal window and run the following commands from a convenient directory on your machine:

```
git clone git@github.com:kgorman/octomongodb.git
cd octomongodb
```

### Create an environment file
In the same terminal window and directory, create an .env file

```
echo "SOURCE_BASE_URL=http://<octoprint IP>/api/printer?exclude=sd"  > env.txt
echo "SOURCE_KEY=<api key defined in octoprint>" >> env.txt
echo "TARGET_BASE_URL=https://data.mongodb-api.com/app/<endpoint_id>/endpoint/data/beta/ action/insertOne" >> env.txt
echo "TARGET_KEY=<api key from MongoDB Atlas" >> env.txt
echo "TARGET_NAME=<your cluster name>" >> env.txt
```

## run it
```
docker build . -t octomongodb
docker run -it --env-file env.txt octomongodb
```