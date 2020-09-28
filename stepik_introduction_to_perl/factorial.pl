#!/usr/bin/perl
use strict;
use warnings;

sub fac {
    my ($n) = @_;
    my $x = 1;
    $x *= $_ for 2 .. $n;
    print "$x\n";
}

while (<>) {
    fac($_);
}
