# lambda-tutorial

This repository is made to get you comfortable with developing code on the backend of the API. It simulates how the actual API works. All the development can happen locally. There is also a test suite to automatically verify your solutions.

## Prerequisites
This tutorial assumes that you have read the onboarding document, and have installed the AWS cli tools, specifially the SAM cli tool. It also assumes that you have downloaded the `requests` python library (this can be accomplished using the command `python3 -m pip install requests`).

## Running the test suite
To run the test suite, call the function `python test.py`. It will tell you which the challenges you have successfully completed. Make sure that the local dev api is running in a seperate terminal window in order for the tests to work.

## Challenges:
1. Get the local dev server running. This can be accomplished using the command `sam local start-api`. Verify that the API is working by calling the /hello endpoint (it can be accessed at 127.0.0.1:3000/hello, using cURL or Postman).
2. Change the output from /hello to say "Hello, World!". You can accomplish this by changing the code in hello_world/app.py. Verify that your changes were successful by calling the /hello endpoint again.
3. Implement the logic for the /customHello endpoint. This endpoint uses [query string parameters](https://en.wikipedia.org/wiki/Query_string) to specify the user's name, and then writes "Hello, <name>!" to the screen. (Hint: look at the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format) to see what information is passed in to the `event` parameter in the function `handler`)
4. Implement the logic for the endpoint `/getNames`. This endpoint is to read all names from the database (`db.get_names()`), sort them alphabetically, and filter out the empty strings (`""`). Then, it will return a JSON object (dictionary) of the form:
```json
{
  "names": [
    "name1",
    "name2",
    ...,
    "nameN"
  ],
  "count": N
}
```
Where `N` is the number of names in the list.
5. Implement the logic for the endpoint `/addName`. This is a POST endpoint that takes a JSON object of the following form: 
```json
{
  "name": "new_name"
}
```
Where `new_name` is the new name to be added. The endpoint will call the database function `db.write_name()` to add the name to the database. If `write_name` is successful (i.e. it returns True), then the output should be "Success". Otherwise, the output should be "Failure".

## Final challenge
Once you have completed challenges 1-5, the final challenge has to do with pushing your changes to GitHub. The goal of this challenge is to create a new branch whose name is your name (e.g. if my name is Logan, I should create a branch called logan), commit your code, and then push it to origin. Once you have completed this challenge, please let your team leader know.