# Import this module from a running iPython or Jupyter notebook
# to load the magic functions:
#
# %%savefig_dark_light figname
#
# %%savefig_dark figname
#
# %%savefig_light figname

from IPython.core import magic_arguments
from IPython.core.magic import (line_magic, cell_magic, Magics, magics_class)
from sys import stderr
import matplotlib.pyplot as plt


@magics_class
class FigureMagics(Magics):
    
    darkstyle = 'easy-dark'
    lightstyle = 'easy-light'
    darkfigdir = ''
    lightfigdir = ''
    darkappend = '_dark'
    
    @line_magic
    def set_darkstyle(self, line):
        self.darkstyle = line

    @line_magic
    def get_darkstyle(self, line):
        return self.darkstyle
        
    @line_magic
    def set_lightstyle(self, line):
        self.lightstyle = line

    @line_magic
    def get_lightstyle(self, line):
        return self.lightstyle

    @line_magic
    def set_darkfigdir(self, line):
        self.darkfigdir = line

    @line_magic
    def get_darkfigdir(self, line):
        return self.darkfigdir
        
    @line_magic
    def set_lightfigdir(self, line):
        self.lightfigdir = line

    @line_magic
    def get_lightfigdir(self, line):
        return self.lightfigdir

    @line_magic
    def set_darkappend(self, line):
        self.dark_append = line
    
    @line_magic
    def get_darkappend(self, line):
        return self.darkappend
        
    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('figname', help='Base Figure Name to save to')
    def savefig_dark_light(self, line='', cell=None):
        """
        Saves both a light-background and dark-background version of the
        Matplotlib figure generated in the enclosed cell.

        Arguments
        ---------
        figname : name of the figure to save
            Dark/Light figure will be saved in two seperate directories
        """
        args = magic_arguments.parse_argstring(self.savefig_dark_light, line)
        light_figname = self.lightfigdir + args.figname
        if '.' in args.figname:
            pre, _, post = args.figname.rpartition('.')
            dark_figname = self.darkfigdir + pre + self.darkappend + '.' + post
        else:
            dark_figname = self.darkfigdir + args.figname + self.darkappend
        with plt.style.context((self.lightstyle)):
            self.shell.user_ns['is_dark'] = False
            self.shell.ex(cell)
            stderr.write('Saving light figure as %s\n' % (light_figname))
            plt.savefig(light_figname)
        with plt.style.context((self.darkstyle)):
            self.shell.user_ns['is_dark'] = True
            self.shell.ex(cell)
            stderr.write('Saving dark figure as %s\n' % (dark_figname))
            plt.savefig(dark_figname)

    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('figname', help='Base Figure Name to save to')
    def savefig_dark(self, line='', cell=None):
        """
        Saves a dark-background version of the
        Matplotlib figure generated in the enclosed cell.

        Arguments
        ---------
        figname : name of the figure to save
            Will be saved in directory for dark figures
        """
        args = magic_arguments.parse_argstring(self.savefig_dark, line)
        if '.' in args.figname:
            pre, _, post = args.figname.rpartition('.')
            dark_figname = self.darkfigdir + pre + self.darkappend + '.' + post
        else:
            dark_figname = self.darkfigdir + args.figname + self.darkappend
        with plt.style.context((self.darkstyle)):
            self.shell.user_ns['is_dark'] = True
            self.shell.ex(cell)
            stderr.write('Saving dark figure as %s\n' % (dark_figname))
            plt.savefig(dark_figname)
            
    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('figname', help='Base Figure Name to save to')
    def savefig_light(self, line='', cell=None):
        """
        Saves a light-background version of the
        Matplotlib figure generated in the enclosed cell.

        Arguments
        ---------
        figname : name of the figure to save
            Will be saved in directory for light figures
        """
        args = magic_arguments.parse_argstring(self.savefig_light, line)
        light_figname = self.lightfigdir + args.figname
        with plt.style.context((self.lightstyle)):
            self.shell.user_ns['is_dark'] = False
            self.shell.ex(cell)
            stderr.write('Saving light figure as %s\n' % (light_figname))
            plt.savefig(light_figname)

            
# This loads the functions above into your running iPython instance
ip = get_ipython()
ip.register_magics(FigureMagics)
