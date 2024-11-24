# Directory Structure

minimal-mistakes   
├── _data                      # data files for customizing the theme   
|  ├── navigation.yml          # main navigation links   
|  └── ui-text.yml             # text used throughout the theme's UI   
├── _includes   
|  ├── analytics-providers     # snippets for analytics (Google and custom)   
|  ├── comments-providers      # snippets for comments   
|  ├── footer   
|  |  └── custom.html          # custom snippets to add to site footer   
|  ├── head   
|  |  └── custom.html          # custom snippets to add to site head   
|  ├── feature_row             # feature row helper   
|  ├── gallery                 # image gallery helper   
|  ├── group-by-array          # group by array helper for archives   
|  ├── nav_list                # navigation list helper   
|  ├── toc                     # table of contents helper   
|  └── ...   
├── _layouts   
|  ├── archive-taxonomy.html   # tag/category archive for Jekyll Archives plugin   
|  ├── archive.html            # archive base   
|  ├── categories.html         # archive listing posts grouped by category   
|  ├── category.html           # archive listing posts grouped by specific category   
|  ├── collection.html         # archive listing documents in a specific collection   
|  ├── compress.html           # compresses HTML in pure Liquid   
|  ├── default.html            # base for all other layouts   
|  ├── home.html               # home page   
|  ├── posts.html              # archive listing posts grouped by year   
|  ├── search.html             # search page   
|  ├── single.html             # single document (post/page/etc)   
|  ├── tag.html                # archive listing posts grouped by specific tag   
|  ├── tags.html               # archive listing posts grouped by tags   
|  └── splash.html             # splash page   
├── _sass                      # SCSS partials   
├── assets   
|  ├── css   
|  |  └── main.scss            # main stylesheet, loads SCSS partials from _sass   
|  ├── images                  # image assets for posts/pages/collections/etc.   
|  ├── js   
|  |  ├── plugins              # jQuery plugins   
|  |  ├── vendor               # vendor scripts   
|  |  ├── _main.js             # plugin settings and other scripts to load after jQuery   
|  |  └── main.min.js          # optimized and concatenated script file loaded before </body>   
├── _config.yml                # site configuration   
├── Gemfile                    # gem file dependencies   
├── index.html                 # paginated home page showing recent posts   
└── package.json               # NPM build scripts


# Two type of installation of gems (plugins)
A. gem-based method
- download gem - remote theme  OR fork minimal mistake-jekyll repo
- install gem-based theme : add gem "......" in Gemfile => from cmd prompt run "bundle" (from cmd)
- set these : add theme: ---------- in _config.yml => bundle update (to update theme run)

B. Remote these method.
- keep only following code in Gemfile 
	source: "https:/rubygems.org 
	gem "github-pages", group: :jekyll-plugin 
	gem "jekyll-include-cache", group: :jekyll-plugin 
- in _config.yml in plugins array add jekyll-inlcude-cache 
- bundle (for fetch and update)
- in _confic.yml add => remote-theme: "mmistakes/minimal-mistakes@4.24" => remove an other theme: or remote-theme 

```
(base) PS D:\github\dasarpai.github.io> bundle
Fetching gem metadata from https://rubygems.org/...........
Resolving dependencies.........................
Using concurrent-ruby 1.1.10
Using public_suffix 4.0.7
Using json 2.6.2
Using racc 1.6.0
Using bundler 2.3.22
Using coffee-script-source 1.11.1
Using execjs 2.8.1
Fetching multi_json 1.15.0
Fetching httpclient 2.8.3
Using colorator 1.1.0
Using unf_ext 0.0.8.2 (x64-mingw-ucrt)
Fetching commonmarker 0.23.6
Using eventmachine 1.2.7
Using http_parser.rb 0.8.0
Using ffi 1.15.5 (x64-mingw-ucrt)
Using faraday-net_http 3.0.0
Using ruby2_keywords 0.0.5
Fetching filesize 0.2.0
Installing filesize 0.2.0
Installing multi_json 1.15.0
Using forwardable-extended 2.6.0
Using gemoji 3.0.1
Using rb-fsevent 0.11.2
Using rexml 3.2.5
Using liquid 4.0.3
Using mercenary 0.3.6
Using rouge 3.26.0
Using safe_yaml 1.0.5
Using jekyll-paginate 1.1.0
Using rubyzip 2.3.2
Using jekyll-swiss 1.0.0
Using unicode-display_width 1.8.0
Fetching progressbar 1.11.0
Installing commonmarker 0.23.6 with native extensions
Installing httpclient 2.8.3
Installing progressbar 1.11.0
Fetching verbal_expressions 0.1.5
Using wdm 0.1.1
Using i18n 0.9.5
Using addressable 2.8.1
Using nokogiri 1.13.8 (x64-mingw-ucrt)
Fetching tzinfo 2.0.5
Installing verbal_expressions 0.1.5
Using coffee-script 2.4.1
Using unf 0.1.4
Using em-websocket 0.5.3
Using ethon 0.15.0
Using rb-inotify 0.10.1
Using faraday 2.5.2
Using pathutil 0.16.2
Using kramdown 2.3.2
Using terminal-table 1.8.0
Fetching activesupport 3.2.22.5
Installing tzinfo 2.0.5
Fetching algolia_html_extractor 2.6.4
Installing algolia_html_extractor 2.6.4
Using jekyll-coffeescript 1.1.1
Using simpleidn 0.2.1
Using typhoeus 1.4.0
Using sass-listen 4.0.0
Using listen 3.7.1
Using sawyer 0.9.2
Using kramdown-parser-gfm 1.1.0
Fetching algoliasearch 1.27.5
Installing activesupport 3.2.22.5
Using dnsruby 1.61.9
Using sass 3.7.4
Using jekyll-watch 2.2.1
Using octokit 4.25.1
Using tzinfo-data 1.2022.3
Using jekyll-sass-converter 1.5.2
Using github-pages-health-check 1.17.9
Using jekyll-gist 1.5.0
Using jekyll 3.9.2
Using jekyll-avatar 0.7.0
Using jekyll-default-layout 0.1.4
Using jekyll-feed 0.15.1
Using jekyll-github-metadata 2.13.0
Using jekyll-include-cache 0.2.1
Using jekyll-optional-front-matter 0.3.2
Using jekyll-readme-index 0.3.0
Using jekyll-redirect-from 0.16.0
Using jekyll-relative-links 0.6.1
Using jekyll-remote-theme 0.4.3
Using jekyll-seo-tag 2.8.0
Using jekyll-sitemap 1.4.0
Using jekyll-titles-from-headings 0.5.3
Using jekyll-theme-architect 0.2.0
Using jekyll-theme-cayman 0.2.0
Using jekyll-theme-dinky 0.2.0
Using jekyll-theme-hacker 0.2.0
Using jekyll-theme-leap-day 0.2.0
Using jekyll-theme-merlot 0.2.0
Using jekyll-theme-midnight 0.2.0
Using jekyll-theme-minimal 0.2.0
Using jekyll-theme-modernist 0.2.0
Using jekyll-theme-primer 0.6.0
Using jekyll-theme-slate 0.2.0
Using jekyll-theme-tactile 0.2.0
Using jekyll-theme-time-machine 0.2.0
Using minima 2.5.1
Installing algoliasearch 1.27.5
Fetching jekyll-algolia 1.7.1
Installing jekyll-algolia 1.7.1
Using html-pipeline 2.14.2
Using jemoji 0.12.0
Using jekyll-mentions 1.6.0
Using jekyll-commonmark 1.4.0
Using jekyll-commonmark-ghpages 0.2.0
Using github-pages 227
Bundle complete! 10 Gemfile dependencies, 99 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
Post-install message from algoliasearch:
A new major version is available for Algolia! Please now use the https://rubygems.org/gems/algolia gem to get the latest features.
```

# New Steps on 10-Feb-24 

10-Feb-24 Build Failed on Netlify. Githubio. For sometime it was working on local machine but it started failing on local machine also.

After investigation, identified that it was theme issue. I am using minimum-mistake theme.
Software required to the website.

Ruby 
Jekyll : Site generator 
Theme: MinimalMistake. 
Plugin: Used by the themes. You can install more based on the need.

## Ruby 
is a dynamic, open source programming language with a focus on simplicity and productivity. Ruby is great for building desktop applications, static websites, data processing services, and even automation tools. It's used for web servers, DevOps, and web scraping and crawling. Designed in 1995 by Yukihiro. Implemented in C. Paradigm: functional, imperative, object-oriented, reflective (Multi-paradigm). Versions of Ruby. https://www.ruby-lang.org/en/. Ruby 3.2.3 has been released on 18-Jan-24

Ruby installed on machine: ruby 3.1.2p20 (2022-04-12 revision 4491bb740a) [x64-mingw-ucrt]

## Jekyll 
is a static site generator written in Ruby by Tom Preston-Werner. It is distributed under the open source MIT license. Jekyll is a blog-aware, site generator written in Ruby. It takes raw text files, runs it through a renderer and produces a publishable static website.


https://jekyllrb.com/resources/
Jekyll Themes: https://github.com/topics/jekyll-theme
- Minimal-Mistake
	- https://github.com/mmistakes/minimal-mistakes
	- The theme uses the jekyll-include-cache plugin which will need to be installed in your Gemfile and must be retained in the plugins array of _config.yml. Otherwise you'll encounter Unknown tag 'include_cached' errors at build.
	
### What is Jekyll 
Jekyll is a static site generator that allows you to create and manage websites with ease. It takes content, typically written in Markdown, and uses templates to generate a complete, static website that can be hosted on various platforms.

Key features of Jekyll include:

Static Site Generator: Jekyll is a static site generator, which means it takes your input files (often written in Markdown, HTML, or other formats) and generates a complete website with HTML, CSS, and JavaScript. The resulting website consists of static files that can be served by any web server.

Markdown Support: Jekyll supports Markdown, a lightweight markup language that is easy to write and read. Markdown allows you to write content in a plain-text format with simple syntax and then convert it into HTML.
Liquid Templating Engine:

Jekyll uses the Liquid templating engine to enable dynamic content in templates. Liquid tags and filters provide a way to insert dynamic content into static pages during the generation process.

Front Matter: Jekyll uses YAML front matter, a section of metadata at the top of a file, to configure settings for a specific page or post. This metadata includes variables that control how the page is processed and displayed.

Layouts and Templates: Jekyll allows you to use layouts and templates to define the structure of your site. This enables you to maintain a consistent design across multiple pages.

Plugins: Jekyll supports plugins that extend its functionality. Plugins can add features, import data, or modify the build process. However, it's important to note that GitHub Pages, a popular hosting platform for Jekyll sites, has some limitations on the use of custom plugins.

GitHub Pages: Jekyll is commonly used with GitHub Pages, a web hosting service provided by GitHub. GitHub Pages supports Jekyll natively, making it easy to deploy and host Jekyll-powered websites directly from a GitHub repository.
Command-Line Interface (CLI):

Jekyll is operated through a command-line interface. Developers use commands to build the site, serve it locally, and make it ready for deployment.

Liquid Templating Engine: Jekyll uses the Liquid templating engine to process and transform your content. Liquid allows you to insert variables, conditionals, and loops into your templates, providing dynamic features in a static site.


Layouts and Themes: Jekyll allows you to define layouts for your site, which helps maintain a consistent structure and design. Additionally, you can use pre-built themes or create your own to give your site a specific look and feel.

Plugins: Jekyll supports plugins that extend its functionality. You can find or create plugins to add features such as SEO optimization, social media integration, and more.

GitHub Pages Integration: Jekyll is the default engine used by GitHub Pages, a platform for hosting static websites directly from your GitHub repositories.

Fast and Secure: Since Jekyll generates static HTML pages, websites built with Jekyll are fast and secure. There is no need for a database or server-side processing, making the sites easy to deploy and host.

To use Jekyll, 
- you typically install it locally on your computer, 
- create a Jekyll project, 
- install theme and plugins
- and then build the site using the command line. 
- The generated static files can be deployed to any web server or hosting platform that supports static content. 

Jekyll is popular among developers, bloggers, and anyone who needs a straightforward way to create and maintain a static website.









  

