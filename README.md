# sublime-scripts

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/github/release/idleberg/sublime-developer-scripts.svg?style=flat-square)](https://github.com/idleberg/sublime-developer-scripts/releases)

Collection of useful scripts to be used with your own Sublime Text packages

## Dependency Installation

Automatically install dependencies required by your package

### brew-install.py

Install Homebrew dependencies, equivalent to `brew install <package>`.

### git-clone.py

Install Git dependencies, equivalent to `git clone <repository>`. Falls back to `git pull` if cloned repository exists.

### npm-install.py

Install global Node dependencies, equivalent `npm install -g <package>`. Alternatively, you can use this to install dependencies specified in supplied `package.json` (ignores devDependencies!)

### pip-install.py

Install Python packages, equivalent to `pip install <package>`.

## File Operations

### chmod.py

Make included scripts executable, equivalent to `chmod +x <file>`.

## License

This work is licensed under the [The MIT License](LICENSE).

## Donate

You are welcome support this project using [Flattr](https://flattr.com/submit/auto?user_id=idleberg&url=https://github.com/idleberg/sublime-developer-scripts) or Bitcoin `17CXJuPsmhuTzFV2k4RKYwpEHVjskJktRd`