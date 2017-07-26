![alt text](http://i.imgur.com/2wToUmP.png "CIRCA Logo")
> CIRCA | Centralized IP-Based Reboot Center Application.

This application is designed to make a post request to multiple VOIP devices to run a reboot cgi script if the TTL is surpassed.

## Installation

Only Windows is supported at this time.
Windows:

In the 'build' directory there is an 'app.exe' file that will start a local server.
```sh
|--build
  |-- app.py
```

## Usage example

This project was written in Flask, a microframework for Python. The project was compiled into a Windows executable utilizing cx\_Freeze. All files and dependencies needed to run _Circa_ are in the build directory. Simply scroll to _'app.exe'_ and it will start a server on your localhost. Navigate to your localhost:5000 (127.0.0.1:5000) in your web browser to use the application. 

> _Note:_ Severe performance degradation when using IE10 or below.

## Release History

* v1.2(rel: 25-07-2017)
    1. Officially named _Circa_ (Centralized IP-Based Reboot Center Application),
    2. Added error handling,
    3. Added flash messaging,
    4. Added cool logo,
    5. Broke buildings into tabs for easier navigation
  
* v1.0(rel: 21-07-2017)
    1. Dubbed CRC for 'Consolidated Reboot Center'
    2. Shaky, but functioning.

## Who is Circa

Designed, coded and maintained by Corey M. Russell (coreymrussell@gmail.com)

## Contributing

Special shout out to Shayn S. and his help in getting my mind in the right place to code this.
I'd also like to mention _ThiefMaster_ and _Doobeh_ from the #pocoo IRC who helped a great deal.
