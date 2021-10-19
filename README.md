# Ask Ernie

Ask Ernie is an application that fills out masked queries using [distillbert](https://huggingface.co/transformers/model_doc/distilbert.html).

If you ask Ernie:

    "Hello, This is Farmer Ernie. You might wonder why a city kid like me is doing out here in the [MASK]?"

You'll receive a range of responses like:

    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the woods?
    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the desert?
    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the rain?
    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the city?
    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the dark?

Where Ernie has predicted the word that replaces the `[MASK]` symbol.

## Running ernie

### Create a new virtual env and install dependencies

```shell
python3 -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

Running Flask:

``` shell
FLASK_ENV=development FLASK_APP=ernie:app flask run
```

## Take-home assignment

Ask Ernie™ has grown to be quite a popular service.

In order to scale up our model, we would like you to modify ernie so that requests
to the server are queued using [NATS](https://nats.io/), and serviced by a pool
of workers that are run in a separate Python process from the Flask application.

Each worker should listen for messages published on NATS, and respond with the
output from the model that is currently in `ernie/ernie.py`, which should
be returned as a response to the client.

You should be able to start multiple worker processes so that messages on the
queue are divided up among a number of workers.

### Running NATS

NATS can be run as a standalone Docker container using the following invocation

``` shell
docker run -p 4222:4222 nats
```

### NATS Python

NATS has several Python clients that can be used for this exercise.


- [nats-python](https://github.com/Gr1N/nats-python)
- [nats.py](https://github.com/nats-io/nats.py)

While the "official" nats.py client may be attractive at first, it makes
use of `asyncio`, which Flask does not.

A solution with either library is perfectly acceptable. We found it a little
simpler to use the `nats-python` library.


### Criteria for the assignment

The intent of this exercise is for us to see how you approach a problem,
how you like to structure your code, and to get a sense of the code that
you typically write.

We've attempted to scope this exercise to be respectful of your time.
Completing the assignment should take no longer than two hours.

If you find that you didn't have time to do include things you would have liked,
feel free to include them in your PR description instead of spending the
extra time to complete them.
