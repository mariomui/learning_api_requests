# Poetry workflow

* Make a directory name:
  * `mkdir foo_app`
* Set a local python version for poetry to hook into:
  * `pyenv local [3.7.9]`
* Scaffold:
  * poetry new --src [app_name]
* Go into newly scaffolded folder
* Create a local python version for poetry just for people that don't have auto poetry detection bash script
  * `pyenv local [3.7.9]
    * confirm that a .python-version file is created with the version number
* Enter into working mode:
  * poetry shell
  * poetry add [dependencies]
    * confirmations:
      * check if your pip is pointing to your poetry virtualenv
        * `which pip`
        * mine looks like: `$HOME/Library/Caches/pypoetry/virtualenvs/api-requests-eAXd-DUU-py3.7/bin/pip`
      * console.log your dependencies
        * `pip freeze | xargs -I {} echo {}`
        * looks exactly like .toml file

---

* Result
  * Note:
    ```md
      This allows a firmest way to at least get all the dependencies correct.
    ```
