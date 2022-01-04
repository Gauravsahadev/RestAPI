# API for conversion of Docx to PDF

The project contains a API implemented with flask to [convert docx file to pdf](https://www.pdfbanao.com/word-to-pdf/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install 
```
cd flask/
```
* Python3
```
sudo apt install python3 python3-pip
```
* Dependencies
```
pip3 install -r requirements.txt
```
* [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)

* [Postman](https://www.postman.com/downloads/)


### Installing

A step by step series of examples that tell you how to get a development env running

Inside flask dir
```
export FLASK_APP=run.py
```

And repeat
```
export FLASK_ENV=development
```
Run Flask app
```
flask run
```
Go to [127.0.0.1:5000](127.0.0.1:5000), You will see API Running

Now, Build the container
```
sudo docker-compose build
```
And Run it
```
sudo docker-compose up
```
Go to [127.0.0.1:80](127.0.0.1:80)


## To test the API

1. Open Postman
2. Make a post request to [127.0.0.1:80/docxtopdf](127.0.0.1:80/docxtopdf)
3. Go to body and then form-data, In key select 'file' and value shoul be the path of file.
4. Click on Send and Download


## Deployment


## Built With

* [Flask](https://g.co/kgs/bDNDHj) - The web framework used

<!-- ## Contributing

Please read for details on our code of conduct, and the process for submitting pull requests to us. -->
 

## Authors

* **Gaurav Sahadev** - *Initial work* - [Gaurav Sahadev](https://github.com/Gauravsahadev)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Gauravsahadev/RestAPI/blob/master/LICENSE) file for details


