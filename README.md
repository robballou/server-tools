# Server Tools

This contains some various server tools that I have found useful on multiple
servers. Many of these need a bit of work to be applicable to ever server, but
they may prove useful for others.

## Fabric

I have added some [Fabric](http://fabfile.org) commands to this repo that I use
almost daily. They currently include some generic server, git and mysql commands.

To install this, I recommend adding it as a symlink in your site-packages directory:

    pushd `python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`
    sudo ln -s /path/to/server-tools/fabfile server_tools_fabfile
    popd

You will then be able to add these commands via an import in your own fabfile.