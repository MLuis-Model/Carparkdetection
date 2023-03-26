# Free Park Spot Detection API

This API demonstrates how YOLO's Object Detection can be used to detect vehicles and their type ('car', 'motorcycle', 'truck', etc.) in an image. A simple front-end is provided for users to test it out.


## Requirements

To run this project, you will need Python ~= 3.7.4


## Run Locally


### Clone the project

```bash
  git clone https://github.com/chandanraj19/Detection-API.git
```

### Go to the project directory

```bash
  cd Detection-API
```

### Create a virtual environment

#### Windows:
```cmd
pip install virtualenv
```
```cmd
virtualenv <virtualenv_name>
```
```cmd
<virtualenv_name>\Scripts\activate
```

#### Linux:
```bash
pip install virtualenv
```
```bash
virtualenv <virtualenv_name>
```
```bash
source <virtualenv_name>/bin/activate
```

#### Install dependencies

```bash
  python -r requirements.txt
```

### Start the server

```bash
  flask --app main.py run
```
**Server starts at** `http://localhost:5000`


## Tech Stack

**Client:** HTML, JS, CSS

**Server:** Python Flask


## Screenshots

![Demo](https://github.com/MLuis-Model/FreeParkSpotDetection/blob/de9036dadb2f43b72223d1908417a1adeb0b87c7/Vehicle%20Detection/Screenshots/outsidenagarrooffice.png)

