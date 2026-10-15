<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JamisonThorne/template_project">
    <img src="images/exalted.ico" alt="exalted" width="64" height="64">
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

Descartes' kissing circles, also known as the Descartes Circle Theorem, describes the relationship between four mutually tangent circles. This elegant mathematical concept, formulated by René Descartes in 1643, provides a formula to calculate the ***curvature*** of a fourth circle when three mutually tangent circles are known.

### $$(k_1 + k_2 + k_3 + k_4)^2 = 2(k_1^2 + k_2^2 + k_3^2 + k_4^2)$$ $\\Rightarrow$ $$k_4 = k_1 + k_2 + k_3 \pm 2\sqrt{k_1 k_2 + k_2 k_3 + k_1 k_3}$$

### Complex Decartes Circle Theorem
Finds the ***center*** of the aforementioned fourth circles radius

Calculates the center of the tangential circle:

# $$z_4 = \frac{z_1 k_1 + z_2 k_2 + z_3 k_3 \pm 2\sqrt{k_1 k_2 z_1 z_2 + k_2 k_3 z_2 z_3 + k_1 k_3 z_1 z_3}}{k_4}$$

z is the complex number of x,y (center coordinates or circle) where z = x + iy  

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/JamisonThorne/apollonian_gaskets.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin JamisonThorne/apollonian_gaskets
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

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

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - jamison.e.thorne@gmail.com

Project Link: [https://github.com/JamisonThorne/apollonian_gaskets](https://github.com/JamisonThorne/apollonian_gaskets)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

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
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
