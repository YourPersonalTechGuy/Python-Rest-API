# Python-Rest-API
A simple Rest API in python

when using docker dev environment use the following commands

```shell
apt-get update
apt-get install python3-pip
pip install fastapi
pip install requests
pip install uvicorn
```

To get this running use the following command
```shell
uvicorn {filename}:{fastapi_var_name}
```

To enable hot reload use the following command
```shell
uvicorn {filename}:{fastapi_var_name} --reload
```