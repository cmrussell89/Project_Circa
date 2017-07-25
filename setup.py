from cx_Freeze import setup, Executable

include_files = ['templates/',
                 'static/', ]

include = ['jinja2', 'jinja2.ext', ]

setup(name='Consolidated Reboot Center',
      version='1.3',
      description='Reboot center for IP based devices',
      options={
            'build_exe':{
                  'include_files': include_files,
                  'includes': include,
                  'build_exe': "build"
            }
      },
      executables=[Executable("app.py")])
