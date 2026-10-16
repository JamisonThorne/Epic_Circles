<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--

<!-- PROJECT SHIELDS -->
<!--
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![project_license][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JamisonThorne/template_project">
    <img src="images/icon.ico" alt="icon" width="64" height="64">
  </a>

<h3 align="center">Apollonian Gaskets</h3>

  <p align="center">
    Generates apollonian gaskets with only the outer circle radius and number of inner circles as input.
    <br />
    <a href="https://github.com/JamisonThorne/apollonian_gaskets"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JamisonThorne/apollonian_gaskets">View Demo</a>
    &middot;
    <a href="https://github.com/JamisonThorne/apollonian_gaskets/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/JamisonThorne/apollonian_gaskets/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#Descartes-Circle-Theorem">Descartes Circle Theorem</a></li>
      </ul>
      <ul>
        <li><a href="#Complex-Decartes-Circle-Theorem">Complex Decartes Circle Theorem</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Rene Decartes (1596 - 1650)](images/decartes.jpg "Rene Decartes")

I discovered apollonian gaskets from the youtube channel Numberphile featuring Simon Pampena. An apollonian gasket starts with three tangent circles and through a series of equations a fourth circle whose curvature is tangent to all three is found. This process could repeat indefinitely and results in an infinite fractal generated image.

### Descartes Circle Theorem

Descartes' kissing circles, also known as the Descartes Circle Theorem, describes the relationship between four mutually tangent circles. This elegant mathematical concept, formulated by René Descartes in 1643, provides a formula to calculate the curvature ($k$) of a fourth circle when three mutually tangent circles are known.

##### $$(k_1 + k_2 + k_3 + k_4)^2 = 2(k_1^2 + k_2^2 + k_3^2 + k_4^2)$$  

##### $$k_4 = k_1 + k_2 + k_3 \pm 2\sqrt{k_1 k_2 + k_2 k_3 + k_1 k_3}$$

### Complex Decartes Circle Theorem
Calculates the center of a tangential circle with radius $k_4$:

##### $$z_4 = \frac{z_1 k_1 + z_2 k_2 + z_3 k_3 \pm 2\sqrt{k_1 k_2 z_1 z_2 + k_2 k_3 z_2 z_3 + k_1 k_3 z_1 z_3}}{k_4}$$

$z$ is the complex number of $x$,$y$ (center coordinates or circle) where $z = x + iy$  

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python-badge]][Python-url]
* [![uv][uv-badge]][uv-url]
* [![TOML][TOML-badge]][TOML-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

To install uv:

```sh
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installation

1. Clone the repo
```sh
   git clone https://github.com/JamisonThorne/apollonian_gaskets.git
   cd apollonian_gaskets
```
2. Install the dependencies (Matplotlib and NumPy)
```sh
   uv sync
```
   Or, if you prefer pip:
```sh
   python -m venv .venv
   source .venv/bin/activate    # Windows: .venv\Scripts\activate
   pip install -e .
```
3. Run it
```sh
   uv run run.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Edit the following lines in run.py to adjust output accordingly
```
R = 1000 # select any given starting radius 
number_of_starting_inner_circles = 5 # selecting desired number of inner circles
```

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] ***v1.0*** - Initial release with core features
- [ ] ***v1.1*** - Add unit tests
- [ ] ***v1.2*** - Add command line arguments
- [ ] ***v1.3*** - Speed improvements for number of circles > 6
- [ ] ***v1.4*** - Look into automation of changelog if possible

See the [open issues](https://github.com/JamisonThorne/apollonian_gaskets/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/JamisonThorne/apollonian_gaskets/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=JamisonThorne/apollonian_gaskets" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the Unlicense

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jamison Thorne - jamison.e.thorne@gmail.com

Project Link: [https://github.com/JamisonThorne/apollonian_gaskets](https://github.com/JamisonThorne/apollonian_gaskets)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Numberphile Video](https://www.youtube.com/watch?v=sG_6nlMZ8f4)
* [Paper by Jeffrey Lagarias, Colin Mallows and Allan Wilks](https://arxiv.org/pdf/math/0101066)
* [Apollonian Gaskets Wiki](https://en.wikipedia.org/wiki/Apollonian_gasket)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JamisonThorne/apollonian_gaskets.svg?style=for-the-badge
[contributors-url]: https://github.com/JamisonThorne/apollonian_gaskets/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JamisonThorne/apollonian_gaskets.svg?style=for-the-badge
[forks-url]: https://github.com/JamisonThorne/apollonian_gaskets/network/members
[stars-shield]: https://img.shields.io/github/stars/JamisonThorne/apollonian_gaskets.svg?style=for-the-badge
[stars-url]: https://github.com/JamisonThorne/apollonian_gaskets/stargazers
[issues-shield]: https://img.shields.io/github/issues/JamisonThorne/apollonian_gaskets.svg?style=for-the-badge
[issues-url]: https://github.com/JamisonThorne/apollonian_gaskets/issues
[license-shield]: https://img.shields.io/github/license/JamisonThorne/apollonian_gaskets.svg?style=for-the-badge
[license-url]: https://github.com/JamisonThorne/apollonian_gaskets/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jamison-thorne/
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[uv-badge]: https://img.shields.io/badge/uv-DE5FE9?style=for-the-badge&logo=uv&logoColor=white
[uv-url]: https://docs.astral.sh/uv/
[TOML-badge]: https://img.shields.io/badge/TOML-9C4221?style=for-the-badge&logo=toml&logoColor=white
[TOML-url]: https://toml.io/