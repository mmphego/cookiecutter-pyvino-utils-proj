# {{cookiecutter.project_name}}

| Details            |              |
|-----------------------|---------------|{% if cookiecutter.add_python_version_badge == 'y' %}
| Programming Language: |  [![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/) |{% endif %}{% if cookiecutter.add_licence_badge == 'y' %}
| License: |  [![license](https://img.shields.io/github/license/{{ cookiecutter.github_username}}/{{ cookiecutter.repo_name }}.svg)](LICENSE) |{% endif %}{% if cookiecutter.add_openvino_version_badge == 'y' %}
| Intel OpenVINO ToolKit: |[![OpenVINO 2020.2](https://img.shields.io/badge/openvino-2020.2-blue.svg)](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit/choose-download.html)|{% endif %}{% if cookiecutter.add_docker_image_badge == 'y' %}
| Docker (Ubuntu OpenVINO pre-installed): | [mmphego/intel-openvino](https://hub.docker.com/r/mmphego/intel-openvino)|{% endif %}{% if cookiecutter.add_hardware_used_badge == 'y' %}
| Hardware Used: | Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz |{% endif %}{% if cookiecutter.add_device_used_badge == 'y' %}
| Device: | CPU |
{% endif %}

{{cookiecutter.project_short_description}}

## Installation

*NONE*, as everything runs in a container.

## Prerequisites

- PC/Laptop with minimum `Intel Generation 6 CPU` and WebCam. (Preferably running **Linux**)
- `docker`

This examples runs inside a docker container that comes pre-installed with Intel OpenVINO Toolkit and other tools.

See: [Docker docs for installation.](https://docs.docker.com/engine/install/)

## Application Usage

```bash
make run-bootstrap
```

The command above does the following:

- Builds a docker image based on the user and current working directory. 
    eg: `{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}`
- Downloads the models that OpenVINO uses for inference.
- Adds current hostname/username to the list allowed to make connections to the X/graphical server.
- Runs the application inside the pre-built docker image.

### Models

Add list of models you would like to use in your application into: `./models.lst`
See list of available models from [Open Model Zoo](https://github.com/openvinotoolkit/open_model_zoo#repository-components)

### Demo

*Screenshots or gif* 
 
## Credits
This package was created with Cookiecutter and the [mmphego/cookiecutter-pyvino-utils](mmphego/cookiecutter-pyvino-utils) project template.
