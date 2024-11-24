# jekyll #github

You can configure RubyGems to publish a package to GitHub Packages and to use packages stored on GitHub Packages as dependencies in a Ruby project with Bundler.

Prerequisites
You must have RubyGems 2.4.1 or higher. To find your RubyGems version:

$ gem --version
You must have bundler 1.6.4 or higher. To find your Bundler version:

$ bundle --version
Bundler version 1.13.7
Install keycutter to manage multiple credentials. To install keycutter:

$ gem install keycutter

You must use a personal access token with the appropriate scopes to publish and install packages in GitHub Packages. 



You need an access token to publish, install, and delete private, internal, and public packages.

You can use a personal access token (classic) to authenticate to GitHub Packages or the GitHub API. When you create a personal access token (classic), you can assign the token different scopes depending on your needs.

GitHub currently supports two types of personal access tokens: fine-grained personal access tokens and personal access tokens (classic).

GitHub recommends that you use fine-grained personal access tokens instead of personal access tokens (classic) whenever possible. Fine-grained personal access tokens have several security advantages over personal access tokens (classic)