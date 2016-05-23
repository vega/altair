"""
This script will fetch all example specs from the vegalite respository and
save them as json files in ``altair/examples/json``.
The automated testing tools there are then used to validate that Altair is
working correctly.
"""
import os
import json


DESTINATION = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           '..', 'altair', 'examples', 'json'))
DATA_URL = 'http://vega.github.io/vega-lite/'




def copy_all_examples(vegalite_repo,
                      destination=DESTINATION,
                      data_url=DATA_URL):
    source_dir = os.path.join(vegalite_repo, 'examples', 'specs')
    print("Reading from {0}".format(source_dir))
    if not os.path.exists(source_dir):
        raise ValueError("{0} does not exist".format(source_dir))

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination, filename)

        print(filename)
        with open(source_file) as f:
            spec = json.load(f)

        # Adjust to use absolute URLs
        try:
            url = spec['data']['url']
            if url.startswith('data/'):
                spec['data']['url'] = DATA_URL + url
        except KeyError:
            continue

        print(" -> {0}".format(destination_file))
        with open(destination_file, 'w') as f:
            json.dump(spec, f, indent=4, sort_keys=True)


if __name__ == '__main__':
    vegalite_repo = os.path.join(os.path.dirname(__file__),
                                 '..', '..', '..', 'vega', 'vega-lite')
    vegalite_repo = os.path.abspath(vegalite_repo)
    copy_all_examples(vegalite_repo)
