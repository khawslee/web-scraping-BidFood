<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Bidfood Web Scraping</h3>

  <p align="center">
    <a href="https://github.com/khawslee/web-scraping-BidFood">View Demo</a>
    ·
    <a href="https://github.com/khawslee/web-scraping-BidFood/issues">Report Bug</a>
    ·
    <a href="https://github.com/khawslee/web-scraping-BidFood/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project utilizes the Python BeautifulSoup library to scrape the HTML DOM of BidFood and extract information such as the title, description, and nutrient values. 

Disclaimer: this project is intended for educational purposes only. Author will not be held responsible for any damages that may result from the use or misuse of the code.

<p align="right">(<a href="#top">back to top</a>)</p>

### Python library

List of python's library used in the project,

* [requests](https://pypi.org/project/requests/), [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), [argparse](https://docs.python.org/3/library/argparse.html), [json](https://docs.python.org/3/library/json.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.


### Prerequisites

You are required to install required library before running the python script.

```sh
  pip install -r requirements.txt
```

## Usage

```properties
python main.py -p <Product name> -i <Product Id> -o <Output filename>
```
-o is optional

Example:
https://www.bidfood.nl/webshop/product/oude-kaas-salade-50-gr-per-cupje-tray-12-cupjes/_/A-productId-009567TR?singleResult=true

```properties
python main.py -p oude-kaas-salade-50-gr-per-cupje-tray-12-cupjes -i 009567TR -o 009567TR.json
```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the Apache License Version 2.0. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - Siang Lee, Khaw - khawslee@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/khawslee/web-scraping-BidFood.svg?style=for-the-badge
[contributors-url]: https://github.com/khawslee/web-scraping-BidFood/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/khawslee/web-scraping-BidFood.svg?style=for-the-badge
[forks-url]: https://github.com/khawslee/web-scraping-BidFood/network/members
[stars-shield]: https://img.shields.io/github/stars/khawslee/web-scraping-BidFood.svg?style=for-the-badge
[stars-url]: https://github.com/khawslee/web-scraping-BidFood/stargazers
[issues-shield]: https://img.shields.io/github/issues/khawslee/web-scraping-BidFood.svg?style=for-the-badge
[issues-url]: https://github.com/khawslee/web-scraping-BidFood/issues
[license-shield]: https://img.shields.io/github/license/khawslee/web-scraping-BidFood.svg?style=for-the-badge
[license-url]: https://github.com/khawslee/web-scraping-BidFood/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/khawslee
