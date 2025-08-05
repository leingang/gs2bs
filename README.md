# gs2bs

Convert Gradescope text to Brightspace text

* Converts `$$...$$` to `\( ... \)`
* Strips `\displaystyle`
* Adjusts differential spacing from `\ dx` to `\,dx`.

# Usage

## Mac Automator

Create your own Automator Workflow:

* Create a new "Quick Action" (might also be labeled as "Service").
* At the top, leave the defaults: "Service receives *selected text* in *any application*"
* Select the checkmark "output replaces selected text".
* Add the action "Run Shell Script".
* From dropdown, select to "pass in: as arguments".
* The command is: `/path/to/python /path/to/gs2bs.py $1`. 


# Development

    virtualenv ~/.local/share/virtualenvs/gs2bs
    . ~/.local/share/virtualenvs/gs2bs/bin/activate

