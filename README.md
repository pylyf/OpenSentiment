
<br />
<p align="center">


  <h3 align="center">OpenSentiment</h3>

  <p align="center">
    Get sentimend rating of finance news articles using OpenAI API and Yahoo Finance
    <br />
    <a href="https://github.com/pylyf/OpenSentiment"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/pylyf/OpenSentiment/issues">Report Bug</a>
    ·
    <a href="https://github.com/pylyf/OpenSentiment/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

![example screenshot](https://github.com/pylyf/OpenSentiment/blob/main/screenshots/screenshot.PNG)

A simple script that scrapes Yahoo Finance articles for a specific stock and then passes them into the OpenAI API to rate their sentiment
<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Clone the repository on your machine.
```
git clone https://github.com/pylyf/OpenSentiment.git
```

### Installation
 
Install all required libraries in order to execute the script.
```
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage
```
python main.py
```

The script will ask you to enter the ticker of the stock (ie. AAPL for the apple company).
It will then rate the sentiment of the news articles and print them out in a table format

<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Filip Komarek - pylyf.kom@gmail.com

Project Link: [https://github.com/pylyf/OpenSentiment](https://github.com/pylyf/OpenSentiment)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
