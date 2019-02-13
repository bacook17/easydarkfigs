# easydarkfigs - iPython Magic for easy Dark/Light Matplotlib figures

## Installation
`easydarkfigs` can be installed through [pip](https://pip.pypa.io/en/stable) via

```
pip install easydarkfigs
```

### Important Installation Note

`easydarkfigs` comes packaged with two custom `matplotlib` style files. The first time you import `easydarkfigs`, it will copy those files over to your local `matplotlib` style library, but you __must then restart your notebook kernel__ or `matplotlib` will not recognize they are there. This is only a one-time issue.

If anyone knows a good way of solving this issue (such that the files are copied over on `pip install`) please see the Issues list to this Repo.

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
