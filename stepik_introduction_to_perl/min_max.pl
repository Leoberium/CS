#!/usr/bin/perl
use strict;
use warnings;

sub min_and_max {
    my @res = sort {$a <=> $b} @_;
    print join ', ', @res[0, 2];
}

while (my $line = <>) {
    min_and_max(split / /, $line);
}