#!/usr/bin/perl
use strict;
use warnings;

sub primes_from_interval {
    my ($x, $y) = @_;
    my @a = 0..$y;
    $a[1] = 0;
    for ( my $i = 2; $i**2 <= $y; $i++ ) {
        $a[$_ * $i] = 0 for 2..$y/$i;
    }
    for ($x..$y) {
        if ($a[$_] != 0) {print "$a[$_]\n"}
    }
}


while(<>) {
    primes_from_interval(split / /, $_);
}