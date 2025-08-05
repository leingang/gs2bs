#!/usr/bin/perl

use strict;
use warnings;

# This script reads from standard input, converts LaTeX expressions
# from `$$...$$` or `$...$` to `\(...\)`, and adds a thin space `\,`
# before differential terms like `dx`, `dy`, etc. for proper formatting.

# The `add_thin_space_to_diffs` subroutine is a helper function that
# takes a string (the LaTeX content) and performs a substitution to
# insert the thin space.
sub add_thin_space_to_diffs {
    my ($content) = @_;
    
    # We use a substitution with a lookahead and lookbehind to
    # find `dx`, `dy`, `dz`, or `dt` that isn't already preceded by
    # a `\,` and isn't part of a word.
    $content =~ s/(?<![\\,])\s*(d[xyz]|d[tT])/\, $1/g;

    # A second pass to handle cases like `e^x dx` becoming `e^x\, dx`
    # and to clean up any extra spaces before the comma.
    $content =~ s/(\S)\s*\,\s*d([xyz]|d[tT])/\$1\, d$2/g;

    return $content;
}

# The main loop reads each line from standard input (`STDIN`).
while (<STDIN>) {
    # The `s///e` command with the /e (evaluate) modifier is used here.
    # It allows us to execute Perl code (our subroutine) on the captured
    # content of the regex match.

    # 1. First, remove non-breaking spaces (HTML entity or Unicode).
    s/\x{A0}|&nbsp;/ /g;

    # 2. Handle the `$$...$$` display math delimiter.
    # The regex `\$\$(.*?)\$\$` captures the content between `$$`.
    # We pass this content to our subroutine to format the differential,
    # then wrap the result in `\(` and `\)` for the new delimiter.
    s/\$\$(.*?)\$\$/'\\('. add_thin_space_to_diffs($1) . '\\)'/ge;

    # 3. Handle the `$..$` inline math delimiter.
    # This must be done after the `$$` conversion to prevent the single
    # `$` from matching inside a `$$` block.
    s/\$(.*?)\$/'\\('. add_thin_space_to_diffs($1) . '\\)'/ge;
    
    # Print the modified line to standard output.
    print;
}
