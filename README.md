# gs2bs

Convert Gradescope text to Brightspace text

* Converts `$$...$$` to `\( ... \)`
* Strips `\displaystyle`
* Adjusts differential spacing from `\ dx` to `\,dx`.
* Replaces commas and spaces inside math expressions with a comma and space outside of math mode
* Various other LaTeX code tweaks

# Usage

## Command line

    virtualenv ~/.local/share/virtualenvs/gs2bs
    . ~/.local/share/virtualenvs/gs2bs/bin/activate
    chmod u+x gs2bs.py
    ./gs2bs.py TEXT

## Mac Automator

Create your own Automator Workflow:

* Create a new "Quick Action" (might also be labeled as "Service").
* At the top, leave the defaults: "Service receives *selected text* in *any application*"
* Select the checkmark "output replaces selected text".
* Add the action "Run Shell Script".
* From dropdown, select to "pass in: as arguments".
* The command is: `/path/to/python /path/to/gs2bs.py $1`. 

# Development

Use a virtual enviroment:

    virtualenv ~/.local/share/virtualenvs/gs2bs
    . ~/.local/share/virtualenvs/gs2bs/bin/activate

Requires the `typer` package.

