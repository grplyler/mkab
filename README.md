
<h1 align="center">
  mkab
</h1>

<h3 align="center">Add some sanity to your reading workload. Make neural network sythesized audiobooks from text files.</h3>

![](carbon.png)

<p align="center">
  <a href="#key-features" style="color: red; padding-left: 10px; padding-right: 10px; padding-top: 5px; padding-bottom: 5px; border-radius: 3px; background-color: white; box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.75);">Key Features</a> •
  <a href="#install">Install</a> •
  <a href="#develop">Develop</a> •
  <a href="#examples">Examples</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#Todo">Todo</a> •
  <a href="#license">License</a>
</p>


## Key Features
* **AWS Polly and Google Text to Speech Support**
  * Note: AWS Polly support coming soon
* **Simple command line interface**
  * `mkab synth reading.txt -o reading.ogg`
* **Fast! Uses concurrent requests to sythesize audio**
  * Note: Feature under construction


## Requirements

* Python 3
* Google Cloud API Key
* AWS API Key (client_id and secret)

## Install

*Install from source*

The following commands install adds `mkab` to your `$PATH`

```
git clone https://github.com/grplyler/mkab.git
cd mkab
python setup.py install
```

## Develop


```
git clone https://github.com/grplyler/nginup.git
cd nginup
python setup.py develop
```

## Examples


**Coming soon**


## Rationale

I created this tools to handle the ridiculous amount of reading I had in college. As a pretty good auditory learner with pretty bad dyslexia, it really helped! And in most cases, I felt like my comprehension was much better.


## Contributing

If you like this project, here are some ways you can contribute!

* Feature Requests
* Bug Reports
* Platform Testing

## Todo

* [] Add support for AWS Polly
* [] Add more convient way to manage API config
* [] Add additional features to the command line interface
* [] Create a web interface
* [] Deploy as a service there users can buy tokens that let them generate audiobooks instead of having to have an AWS or GCP API key

## License

MIT


