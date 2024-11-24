# Install on 06-May-24 

- Link: https://jekyllrb.com/docs/installation/windows/
- Install from: https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.2.4-1/rubyinstaller-devkit-3.2.4-1-x64.exe
- ridk install  (select option 1, 2 and 3) (to setup msys2 and development tool chain). MSYS2 is required to install gems with c extensions.
- ridk enable
- gem update (update your Ruby gems) - THIS TAKES LOT OF TIME
- gem install jekyll bundler (Install Jekyll)
- bundle install 

- bundle exec jekyll serve

# Information
- https://rubyinstaller.org/
- https://groups.google.com/g/rubyinstaller/c/eG6OWJjQ420
- https://github.com/oneclick/rubyinstaller2/wiki

## ridk 
ridk is a helper tool to manage the runtime environment of RubyInstaller-2.4 and up. It can be used in cmd and powershell.

See ridk help for available sub-commands:

  Usage:   
      C:/Ruby24-x64/bin/ridk.cmd [option]

  Option:
      install                   Install MSYS2 and MINGW dev tools   
      exec <command>            Execute a command within MSYS2 context   
      enable                    Set environment variables for MSYS2   
      disable                   Unset environment variables for MSYS2   
      version                   Print RubyInstaller and MSYS2 versions   
      use                       Switch to a different ruby version   
	  
