# hydra-flock-central-controller
The Central Controller component for the [simulation](https://github.com/HTTP-APIs/hydra-flock-demo)

This is part of the `hydra-flock-simulation` test-bed. Check the `hydra-flock-demo` for cloud deployment of the full test-bed.

Running tests:
* Create and activate a new virtualenv
* Upgrade pip and setuptools
* Check if `python3-dev` is installed
* Run `pip install -r requirements.txt`
* Start the controller server using `python -m flock_controller.main`
* In another teminal instance run `python -m flock_controller.tests.test_central_controller_endpoints`

**NOTE :-** For design principles and other details please read the Simulation [Wiki](https://github.com/HTTP-APIs/hydra-flock-demo/wiki)
