<link rel="stylesheet" href="../style.css">

# Ruby and Jekyll Installation.

## Ruby Installation (final).
- https://rubyinstaller.org/downloads/
> https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.1.2-1/rubyinstaller-devkit-3.1.2-1-x64.exe
- it automatically runs ridk install 
- gem update (it takes lots of time)
- gem install jekyll bundler (intall two gems 1. jekyll framework, 2. bundler)
- gem install webrick (There was issue so Installed this also)
- jekyll -v 
- bundle exec jekyll serve (Ruby and Jekyll is intalled so run on the local machine. This will help building and testing Jekyll site locally)

# Ignore all below.

# ruby installation 

(base) PS D:\> choco install ruby

Chocolatey v1.1.0
Chocolatey detected you are not running from an elevated command shell
 (cmd/powershell).

 You may experience errors - many functions/packages
 require admin rights. Only advanced users should run choco w/out an
 elevated shell. When you open the command shell, you should ensure
 that you do so with "Run as Administrator" selected. If you are
 attempting to use Chocolatey in a non-administrator setting, you
 must select a different location other than the default install
 location. See
 https://docs.chocolatey.org/en-us/choco/setup#non-administrative-install
 for details.


 Do you want to continue?([Y]es/[N]o): y

Installing the following packages:
ruby
By installing, you accept licenses for the packages.
Progress: Downloading ruby.install 3.1.2.1... 100%
Progress: Downloading ruby 3.1.2.1... 100%

ruby.install v3.1.2.1 [Approved]
ruby.install package files install completed. Performing other installation steps.
The package ruby.install wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint): y

Ruby is going to be installed in 'C:\tools\ruby31'
Installing 64-bit ruby.install...
ruby.install has been installed.
  ruby.install can be automatically uninstalled.
Environment Vars (like PATH) have changed. Close/reopen your shell to
 see the changes (or in powershell/cmd.exe just type `refreshenv`).
 The install of ruby.install was successful.
  Software installed to 'C:\tools\ruby31\'

ruby v3.1.2.1 [Approved]
ruby package files install completed. Performing other installation steps.
 The install of ruby was successful.
  Software installed to 'd:\ProgramData\chocolatey\lib\ruby'

Chocolatey installed 2/2 packages.
 See the log for details (d:\ProgramData\chocolatey\logs\chocolatey.log).
 
 
# Jekyll on Windows:  
> https://jekyllrb.com/docs/installation/windows/
## Installing Ruby and JekyllPermalink
> Installation via RubyInstallerPermalink : The easiest way to install Ruby and Jekyll is by using the RubyInstaller for Windows.
- Download and install a Ruby+Devkit version from RubyInstaller Downloads. 
- Run the ridk install
- Open a new command prompt window from the start menu, so that changes to the PATH environment variable becomes effective. Install Jekyll and Bundler using gem install jekyll bundler
- Check if Jekyll has been installed properly: jekyll -v
 
## Installation via Bash on Windows 10 : 
> If you are using Windows 10 version 1607 or later, another option to run Jekyll is by installing the Windows Subsystem for Linux.
> You must have Windows Subsystem for Linux enabled.
- Open a new Command Prompt or PowerShell window and type bash
- sudo apt-get update -y && sudo apt-get upgrade -y

> Next, install Ruby. To do this, let’s use a repository from BrightBox, which hosts optimized versions of Ruby for Ubuntu.
- sudo apt-add-repository ppa:brightbox/ruby-ng
- sudo apt-get update
- sudo apt-get install ruby2.5 ruby2.5-dev build-essential dh-autoreconf
> update your Ruby gems:
- gem update 
> Install Jekyll:
- gem install jekyll bundler
- jekyll -v

# Installing Ruby
> https://www.ruby-lang.org/en/documentation/installation/
> Here are available installation methods:
- Package Management Systems
	- Debian, Ubuntu
	- CentOS, Fedora, RHEL
	- Snap
	- Gentoo
	- Arch Linux
	- macOS
	- FreeBSD
	- OpenBSD
	- OpenIndiana
	- Windows Package Manager
	- Chocolatey package manager for Windows
	- Other Distributions
- Installers
	- ruby-build
	- ruby-install
	- RubyInstaller (Windows)
	- Ruby Stack
Managers
	- asdf-vm
	- chruby
	- rbenv
	- RVM
	- uru
- Building from source

# Install Linux on Windows with WSL
> https://docs.microsoft.com/en-us/windows/wsl/install
- Prerequisites: You must be running Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11.
- powershell (admin)
- wsl --install

> Change the default Linux distribution installed
- wsl --install -d <Distribution Name>

> Check which version of WSL you are running
- wsl -l -v

> Upgrade version from WSL 1 to WSL 2
- wsl --set-version <distro name> 2

> Ways to run multiple Linux distributions with WSL
- wsl --help
- wsl -l 






# Ruby
- Ruby is a server-side scripting language, so it is very much similar to Python and PERL. Ruby language can be used to write Common Gateway Interface (CGI) scripts. It has a similar syntax to that of many programming languages like Perl and C++.
- https://guides.rubygems.org/make-your-own-gem/
- Ruby on Rail is Frontend Devlopment framework.
- Ruby is a programming language, while Ruby on Rails is a framework that is built in Ruby. In developer circles “Ruby on Rails” is usually just referred to as “Rails”.
- Ruby on Rail is MVC framework
- The MVC, or model-view-controller, framework is an architectural pattern used to create web and desktop applications. Many other web frameworks use this pattern, such as AngularJS (JavaScript), Django (Python) and CakePHP (PHP). It structures code by separating the logic of the application into three interconnected parts.
- The Model represents the logic of the application, the data objects, and high-level classes associated with them. 
- The View is essentially the visual representation of the data (the template files, in other words). 
- The Controller is the piece which connects the other two, responding to user input and gathering data from the Model to render in the View.
- Just a few well-known startups built in Ruby on Rails: Basecamp, Bleacher Report, Scribd, Groupon, Gumroad, Hulu, Kickstarter, Pitchfork, Sendgrid, Soundcloud, Square, Yammer, Crunchbase, Slideshare, Zendesk, GitHub, Shopify
 
 
 
Migrating wordpress to jekyll.

creating CNAME on github (both the branches main, gh-pages )
Creating ANAME on godaddy (domain name provider)
https://www.youtube.com/watch?v=hUChaN-VRIc


nodejs/reactjs site on github pages.
npm (nodejs)
npx (react js)
https://www.youtube.com/watch?v=SKXkC4SqtRk