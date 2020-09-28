#!/usr/bin/perl
use strict;
use warnings;

pipe my $r, my $w;
for (1..10) {
    my $pid = fork;
    die if not defined $pid;
    next if $pid != 0;

    sleep 1;
    print $w $_, "\n";
    exit;
}
close $w;
print <$r>;