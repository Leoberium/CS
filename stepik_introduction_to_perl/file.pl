#!/usr/bin/perl
use strict;
use warnings;

my %uniq = ();
while (my $line = <>) {
    chomp $line;
    $uniq{$line}++;
}
open(my $fn, '>>', '/tmp/uniq.txt');
print $fn "$uniq{$_} ", length, " $_\n" for sort keys %uniq;
close($fn);
