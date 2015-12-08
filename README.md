# sublime-scripts

Collection of useful scripts to be used with your own Sublime Text packages

## Scripts

### brew-install.py

Install Homebrew dependencies, equivalent to `brew install <package>`.

### chmod.py

Make included scripts executable, equivalent to `chmod +x <file>`.

### git-clone.py

Install Git dependencies, equivalent to `git clone <repository>`. Falls back to `git pull` if cloned repository exists.

### npm-install.py

Install global Node dependencies, equivalent `npm install -g <package>`. Alternatively, you can use this to install dependencies specified in supplied `package.json` (ignores devDependencies!) 

## License

This work is licensed under the [The MIT License](LICENSE).