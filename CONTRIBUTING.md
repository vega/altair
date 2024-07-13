# Feedback and Contribution

We welcome any input, feedback, bug reports, and contributions via [Altair's
GitHub Repository](http://github.com/vega/altair/). In particular, we
welcome companion efforts from other visualization libraries to render the
Vega-Lite specifications output by Altair. We see this portion of the effort
as much bigger than Altair itself: the Vega and Vega-Lite specifications are
perhaps the best existing candidates for a principled *lingua franca* of data
visualization.

We are also seeking contributions of additional Jupyter notebook-based examples
in our separate GitHub repository: https://github.com/altair-viz/altair_notebooks.

All contributions, suggestions, and feedback you submitted are accepted under the [Project's license](./LICENSE). You represent that if you do not own copyright in the code that you have the authority to submit it under the [Project's license](./LICENSE). All feedback, suggestions, or contributions are not confidential. The Project abides by the Vega Organization's [code of conduct](https://github.com/vega/.github/blob/main/CODE_OF_CONDUCT.md) and [governance](https://github.com/vega/.github/blob/main/project-docs/GOVERNANCE.md).

## How To Contribute Code to Vega-Altair

### Setting Up Your Environment

Fork the Altair repository on GitHub and then clone the fork to you local
machine. For more details on forking see the [GitHub
Documentation](https://help.github.com/en/articles/fork-a-repo).

```cmd
git clone https://github.com/YOUR-USERNAME/altair.git
```

To keep your fork up to date with changes in this repo,
you can [use the fetch upstream button on GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).

Now you can install the latest version of Altair locally using `pip`.
The `-e` flag indicates that your local changes will be reflected
every time you open a new Python interpreter
(instead of having to reinstall the package each time).

```cmd
cd altair/ 
python -m pip install -e ".[all, dev]"
```

'[all, dev]' indicates that pip should also install the optional and development requirements
which you can find in `pyproject.toml` (`[project.optional-dependencies]/all` and `[project.optional-dependencies]/dev`)

### Creating a Branch

Once your local environment is up-to-date, you can create a new git branch
which will contain your contribution
(always create a new branch instead of making changes to the main branch):

```cmd
git switch -c <your-branch-name>
```

With this branch checked-out, make the desired changes to the package.

A large part of Altair's code base is automatically generated.
After you have made your manual changes,
make sure to run the following to see if there are any changes
to the automatically generated files: 

```bash
hatch run generate-schema-wrapper
```

For information on how to update the Vega-Lite version that Altair uses,
please read [the maintainers' notes](NOTES_FOR_MAINTAINERS.md).

### Testing your Changes

Before submitting your changes to the main Altair repository,
it is recommended that you run the Altair test suite,
which includes a number of tests to validate the correctness of your code:

```bash
hatch test
```


This also runs the [`ruff`](https://ruff.rs/) linter and formatter as well as [`mypy`](https://mypy-lang.org/) as type checker.


Study the output of any failed tests and try to fix the issues
before proceeding to the next section.

#### Failures on specific python version(s)
By default, `hatch test` will run the test suite against the currently active python version.
Two useful variants for debugging failures that only appear *after* you've submitted your PR:

```bash
# Test against all python version(s) in the matrix
hatch test --all
# Test against a specific python version
hatch test --python 3.8
```

See [hatch test](https://hatch.pypa.io/latest/cli/reference/#hatch-test) docs for other options.

#### Changes to `__all__`
If `test_completeness_of__all__` fails, you may need to run:

```bash
hatch run update-init-file
```
However, this test usually indicates *unintentional* addition(s) to the top-level `alt.` namespace that will need resolving first.

### Creating a Pull Request

When you are happy with your changes, you can commit them to your branch by running

```cmd
git add <modified-file>
git commit -m "Some descriptive message about your change"
git push origin <your-branch-name>
```

You will then need to submit a pull request (PR) on GitHub asking to merge
your example branch into the main Altair repository. For details on creating a PR see GitHub
documentation [Creating a pull
request](https://help.github.com/en/articles/creating-a-pull-request). You can
add more details about your example in the PR such as motivation for the
example or why you thought it would be a good addition.  You will get feed back
in the PR discussion if anything needs to be changed. To make changes continue
to push commits made in your local example branch to origin and they will be
automatically shown in the PR. 

Hopefully your PR will be answered in a timely manner and your contribution will
help others in the future.

## How To Contribute Documentation to Vega-Altair

Altair documentation is written in [reStructuredText](http://docutils.sourceforge.net/rst.html)
and compiled into html pages using [Sphinx](http://www.sphinx-doc.org/en/master/).
Contributing to the documentation requires some extra dependencies and 
we have some conventions and plugins that are used to help navigate the docs and 
generate great Altair visualizations. 

Note that the [Altair website](https://altair-viz.github.io/)
is only updated when a new version is released so your contribution might not show
up for a while.

### Adding Examples

We are always interested in new examples contributed from the community. These
could be everything from simple one-panel scatter and line plots, to more
complicated layered or stacked plots, to more advanced interactive features.
Before submitting a new example check the [Altair Example
Gallery](https://altair-viz.github.io/gallery/index.html) to make sure that
your idea has not already been implemented. 

Once you have an example you would like to add there are a few guide lines to follow.
Every example should:
- have a `arguments_syntax` and `methods_syntax` implementation. Each implementation 
  must be saved as a stand alone script in the `tests/examples_arguments_syntax` 
  and `tests/examples_methods_syntax` directories.
- have a descriptive docstring, which will eventually be extracted for the
  documentation website.
- contain a category tag.
- define a chart variable with the main chart object (This will be used both in
  the unit tests to confirm that the example executes properly, and also
  eventually used to display the visualization on the documentation website).
- not make any external calls to download data within the script (i.e. don't
  use urllib). You can define your data directly within the example file,
  generate your data using pandas and numpy, or you can use data
  available in the `vega_datasets` package.

The easiest way to get started would be to adapt examples from the [Vega-Lite
example gallery](https://vega.github.io/vega-lite/examples/) which are missing
in the Altair gallery. Or you can feel free to be creative and build your own
visualizations.

Often it is convenient to draft an example outside of the main repository, such
as [Google Colab](https://colab.research.google.com/), to avoid difficulties
when working with git. Once you have an example you would like to add, follow the
same contribution procedure outlined above.

Some additional notes:

- The format and style of new contributions should generally match that of existing examples.
- The file docstring will be rendered into HTML via
  [reStructuredText](http://docutils.sourceforge.net/rst.html), so use that
  format for any hyperlinks or text styling. In particular, be sure you include
  a title in the docstring underlined with `---`, and be sure that the size of
  the underline exactly matches the size of the title text.
- If your example fits into a chart type but involves significant configuration
  it should be in the `Case Studies` category.
- For consistency all data used for a visualization should be assigned to the
  variable `source`. Then `source` is passed to the `alt.Chart` object.
  If the example requires multiple dataframes then this does not apply. See
  other examples for guidance. 
- Example code should not require downloading external datasets. We suggest
  using the `vega_datasets` package if possible.
  If you are using the `vega_datasets` package there are multiple ways to refer
  to a data source. If the dataset you would like to use is included in local
  installation (`vega_datasets.local_data.list_datasets()`) then the data can
  be referenced directly, such as `source = data.iris()`. If the data is not
  included then it should be referenced by URL, such as `source =
  data.movies.url`. This is to ensure that Altair's automated test suite does
  not depend on availability of external HTTP resources.
- If VlConvert does not support PNG export of the chart (e.g. in the case of emoji),
  then add the name of the example to the `SVG_EXAMPLES` set in 
  `tests/examples_arguments_syntax/__init__.py` and `tests/examples_methods_syntax/__init__.py`

### Building the Documentation Locally

The process to build the documentation locally consists of three steps:

1. Clean any previously generated files to ensure a clean build.
2. Generate the documentation in HTML format.
3. View the generated documentation using a local Python testing server.

The specific commands for each step depend on your operating system.
Make sure you execute the following commands from the root dir of altair and have [`hatch`](https://hatch.pypa.io/) installed in your local environment.

- For MacOS and Linux, run the following commands in your terminal:
```bash
hatch run doc:clean-all
hatch run doc:build-html
hatch run doc:serve
```

- For Windows, use these commands instead:
```cmd
hatch run doc:clean-all-win
hatch run doc:build-html-win
hatch run doc:serve
```

To view the documentation, open your browser and go to `http://localhost:8000`. To stop the server, use `^C` (control+c) in the terminal.

---

Part of MVG-0.1-beta.
Made with love by GitHub. Licensed under the [CC-BY 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).
