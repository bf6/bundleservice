# Bundle Service

Simple, fast service for fetching and storing sensor data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

```
$ brew install python3
$ pip3 install virtualenv
```

### Installing

Clone the repository

```
$ git clone https://github.com/bf6/bundleservice.git
```

Create a virtual environment

```
$ virtualenv venv -p `which python3`
$ source venv/bin/activate
```

Install project dependencies

```
$ cd bundleservice
$ pip3 install .
```

Start the service

```
$ python main.py
```

The service is now running at localhost:8080

You can GET /bundles by specifying query parameters in the URL

```
$ curl "localhost:8080/bundles\
?device_uuid=b21ad0676f26439482cc9b1c7e827de4\
&start_time=1510093202\
&end_time=1510993202\
&sensor_type=temperature" | python -m json.tool

[
    {
        "device_uuid": "b21ad0676f26439482cc9b1c7e827de4",
        "sensor_value": 50.0,
        "sensor_reading_time": 1510093202,
        "sensor_type": "temperature"
    },
    {
        "device_uuid": "b21ad0676f26439482cc9b1c7e827de4",
        "sensor_value": 65.4,
        "sensor_reading_time": 1510993202,
        "sensor_type": "temperature"
    }
]
```

You can POST /bundles by including a request body

```
$ curl -X POST -H "Content-type: application/json" \
-d '{"device_uuid": "b21ad0676f26439482cc9b1c7e827de4", "sensor_type": "temperature", "sensor_value": 60.0, "sensor_reading_time": 1510093202 }' \
"localhost:8080/bundles/" | python -m json.tool

{
    "message": "Resource created"
}

```

Invalid requests will return an error message

```
$ curl "localhost:8080/bundles\
?device_uuid=123456\
&start_time=now\
&sensor_type=pressure" | python -m json.tool

{
    "title": "400 Bad Request",
    "description": {
        "device_uuid": [
            "Not a valid UUID."
        ],
        "start_time": [
            "Not a valid integer."
        ],
        "end_time": [
            "Missing data for required field."
        ],
        "sensor_type": [
            "Not a valid choice."
        ]
    }
}
```

## Running the tests

To run tests:

```
python -m pytest
```


## Built With

* [Falcon](https://falconframework.org/) - Unburdening APIs for over 5.11 x 10-2 centuries.
* [gevent](http://www.gevent.org/) - a coroutine-based Python networking library
* [marshmallow](https://marshmallow.readthedocs.io/en/latest/) - simplified object serialization
* [sqlalchemy](https://www.sqlalchemy.org/) - The Python SQL Toolkit and Object Relational Mapper


## Authors

* **Brian Fernandez** - I took this way too seriously.
