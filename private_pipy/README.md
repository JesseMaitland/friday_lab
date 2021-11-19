# Hosting a private PyPi server. 


## Option 1:
The make file can be used to spin up the simple pypi server locally using ``make up``
Destroy the server by running ``make down``

``make build`` can be used to build a local wheel file, which can be manually uploaded to the running server with twine
``twine upload --repository-url http://localhost:8080 dist/*``

A link with a quick how to can be found here
https://testdriven.io/blog/private-pypi/


## Option 2:

Use S3 static file hosting to serve pre-build python wheels as found on the below linked SO post

https://stackoverflow.com/questions/36022867/if-we-want-use-s3-to-host-python-packages-how-can-we-tell-pip-where-to-find-the

I have created an S3 bucket in the playground account and managed to manually upload a wheel file and install it from s3 locally using pip and the command

```
pip install spam --extra-index-url http://jesse-test-pypi-package-hosting.s3-website.eu-central-1.amazonaws.com --trusted-host jesse-test-pypi-package-hosting.s3-website.eu-central-1.amazonaws.com
```

This S3 bucket method has great promise as there is no need to maintain another server / service EC2 instance. The bucket can be locked down
to only allow access from within AWS vpn. 

The ``index.html`` file is required to tell pip where to find the packages within the directory. 

For this to be production worthy, we must build a tool which can build and upload the python wheel files to s3, preferably from a docker container
an ``index.html`` would also have to be maintained to serve as an index for the versions of the build wheel. This would tool could probably be build in 
a matter of 2-3 days tops. 
