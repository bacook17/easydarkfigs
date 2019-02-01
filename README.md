# easydarkfigs - iPython Magic for easy Dark/Light Matplotlib figures

## Installation
`easydarkfigs` can be installed through [pip](https://pip.pypa.io/en/stable) via

```
pip install easydarkfigs
```

## Usage

Within an active iPython or Jupyter environment:

```python
import easydarkfigs
```

Then, at the beginning of a cell where a Matplotlib figure is created:
```python
%%savefig_dark_light figname.ext
# Code
# to
# create
# figure
```
This will save two versions of the created figure, using the `easy-dark` and `easy-light` Matplotlib style files
included with this package.

To customize these default styles, edit them in your [matplotlib directory](https://matplotlib.org/users/style_sheets.html).

To change the default figure save location or styles to use:
```python
%set_darkstyle new-style

%set_darkfigdir my/dir/

%set_lightstyle new-style

%set_lightfigdir my/dir/
```

The code also makes a boolean variable `is_dark` available during execution, the value of which changes depending on which version of the plot is being created.

```python
%%savefig_dark_light figname.ext
if is_dark:
    title = 'This Is A Dark Plot'
else:
    title = 'This Is A Light Plot'
plt.title(title)
```
